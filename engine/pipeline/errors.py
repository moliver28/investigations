"""Hermes Investigation Pipeline — error taxonomy and structured error emission.

Every stage emits errors through this module. Errors are LOUD and STRUCTURED:
machine-actionable codes + severity + JSON-pointer/line path + a `fix` hint, so
a repair agent (or a `--fix` pass) can pattern-match and auto-correct instead of
a human eyeballing a traceback.

Error code grammar:  `<DOMAIN>.<KIND>`  e.g. `GRAPH.ORPHAN`, `REL.UNCLASSIFIED`.

Severity ladder (drives halt-vs-warn behaviour in the orchestrator):
  FATAL  — pipeline cannot proceed (config missing, file unreadable, schema invalid)
  ERROR  — invalid data; must be fixed before publish (unknown node ref, self-loop)
  WARN   — drift / best-effort (unclassified relationship, empty facts, orphan ref)
  INFO   — benign notice

Emission format: one JSON object per line (JSON-Lines), stable keys:
  {"code","severity","message","path","fix","data"}
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

FATAL = "FATAL"
ERROR = "ERROR"
WARN = "WARN"
INFO = "INFO"

_SEVERITY_ORDER = {FATAL: 0, ERROR: 1, WARN: 2, INFO: 3}


@dataclass
class PipelineError:
    code: str
    severity: str
    message: str
    path: str = ""                      # JSON pointer (e.g. /nodes/0/id) or "file:line"
    fix: str = ""                       # concrete remediation hint for automation
    data: Optional[dict] = None         # machine-usable payload (id, values, counts)

    def to_dict(self) -> dict:
        d = {k: v for k, v in asdict(self).items() if v not in (None, "", {})}
        return d

    def as_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class ErrorCollector:
    """Accumulates structured errors; renders JSON-Lines to a stream."""

    def __init__(self, stream=None):
        self.stream = stream or sys.stderr
        self._errors: list[PipelineError] = []

    def add(self, code, severity, message, path="", fix="", data=None) -> None:
        self._errors.append(PipelineError(code, severity, message, path, fix, data))

    def fatal(self, code, message, path="", fix="", data=None) -> None:
        self.add(code, FATAL, message, path, fix, data)

    def error(self, code, message, path="", fix="", data=None) -> None:
        self.add(code, ERROR, message, path, fix, data)

    def warn(self, code, message, path="", fix="", data=None) -> None:
        self.add(code, WARN, message, path, fix, data)

    def info(self, code, message, path="", fix="", data=None) -> None:
        self.add(code, INFO, message, path, fix, data)

    def extend(self, other: "ErrorCollector") -> None:
        self._errors.extend(other._errors)

    def emit(self) -> None:
        """Write all collected errors as JSON-Lines, sorted by severity then code."""
        ordered = sorted(self._errors, key=lambda e: (_SEVERITY_ORDER[e.severity], e.code))
        for e in ordered:
            self.stream.write(e.as_json() + "\n")
        self.stream.flush()

    @property
    def errors(self) -> list[PipelineError]:
        return list(self._errors)

    def count(self, severity: Optional[str] = None) -> int:
        if severity is None:
            return len(self._errors)
        return sum(1 for e in self._errors if e.severity == severity)

    def worst(self) -> str:
        """Highest-priority severity present (INFO if empty)."""
        if not self._errors:
            return INFO
        return min(self._errors, key=lambda e: _SEVERITY_ORDER[e.severity]).severity

    def has_any(self, *severities: str) -> bool:
        wanted = set(severities)
        return any(e.severity in wanted for e in self._errors)
