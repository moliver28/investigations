/* app.js part 1 of 3 — constants, state, helpers (Task 3.3)
   Concatenated with parts 2 and 3 by build_ui_bundle.py. */
'use strict';

const D = window.PIERCE_DATA;

/* ── Canonical classes ─────────────────────────────────────────────── */
const CLASS_ORDER = ['money','influence','governance','legal','business','media','community'];
const CLASS_COLOR = {};
for (const c of D.classes) { CLASS_COLOR[c.id] = c.color; }

/* ── Tier bands: display constants, verified at build time ─────────── */
const TIER_LABEL = { top: 'Top tier', high: 'High', notable: 'Notable' };
const TIER_RANK_PREFIX = { top: 1, high: 2, notable: 3 };

/* ── Locked UI decisions (plan) ────────────────────────────────────── */
const EGO_DIAGRAM_MIN_DEGREE = 3;   // degree >=3 gets a diagram; <=2 gets cards
const EGO_DIAGRAM_MAX_DEGREE = 40;  // above this, a grouped list replaces the (unreadable) hairball
const MAP_W = 2560, MAP_H = 1440;   // viewBox space (x/y precomputed in data)
/* Radius: ~0.75 exponent separates the visible top stratum. The old sqrt (0.5)
   squeezed a 1.5x power spread into an 11% diameter spread — the big bubbles
   all looked alike (review complaint "the sizes all look the same"). Steeper
   curve spreads the top, R_MAX bumps to keep mid/tier nodes >=24px diameter
   (gate 1); rank numbers burned into the biggest bubbles disambiguate further. */
const R_MIN = 14, R_MAX = 42, R_EXP = 0.75;

/* ── Single source of truth for mission→content wiring (gate 14) ──── */
const MISSION_CONTENT_MAP = {
  m1_rank:    { selectors: ['#dir-table', '#th-rank'],                text: 'Who is most powerful? The directory is sorted by rank — open the top name.' },
  m2_where:   { selectors: ['.money-callout', '.entity-header'],      text: 'Where does their power come from? Open any entity and read the gold callout.' },
  m3_money:   { selectors: ['#money-toggle', '.edge.money-edge'],     text: 'Follow the money. Toggle gold rings on the map.' },
  m4_connect: { selectors: ['.conn-group', '.ego-host'],              text: 'Who are they connected to? Connections are grouped on every entity page.' },
  m5_meaning: { selectors: ['#method-modal', '#method-btn'],          text: 'What does it all mean? Method & Sources explains the ranking.' },
};

/* ── State ─────────────────────────────────────────────────────────── */
const state = {
  sortKey: 'rank', sortDir: 'asc',
  search: '',
  domainFilter: null, tierFilter: null,
  moneyOn: false, userToggledMoney: false,
  currentEntity: null,
  missionsActive: null,   // null = undecided (first run); true/false set below
  missionIndex: 0,
};

const FUNDED = new Set(D.nodes.filter(n => n.moneyFigure).map(n => n.id));
const NODE_BY_ID = Object.fromEntries(D.nodes.map(n => [n.id, n]));
const DEGREE = {};
for (const e of D.edges) {
  DEGREE[e.s] = (DEGREE[e.s] || 0) + 1;
  DEGREE[e.t] = (DEGREE[e.t] || 0) + 1;
}
/* rank ascending is the default view */
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $ = sel => document.querySelector(sel);

/* Money-source strings are "evidence/<file> L<nn>; https://<primary-url>".
   Render the evidence reference and the primary URL as SEPARATE anchors
   (the whole-string-as-href bug made the modal links dead). */
function sourceHtml(src) {
  if (!src) return '';
  const parts = String(src).split(';').map(x => x.trim()).filter(Boolean);
  const out = [];
  for (const p of parts) {
    const mref = p.match(/^evidence\/([^ ]+)(.*)$/);
    if (mref) {
      out.push(`<a href="../${esc(mref[1])}">evidence/${esc(mref[1])}</a>${esc(mref[2])}`);
    } else if (/^https?:\/\//.test(p)) {
      out.push(`<a href="${esc(p)}">${esc(p.replace(/^https?:\/\//, ''))}</a>`);
    } else {
      out.push(esc(p));
    }
  }
  return out.join(' · ');
}

/* ── localStorage helpers ──────────────────────────────────────────── */
const store = {
  get(k, dflt) { try { const v = localStorage.getItem(k); return v === null ? dflt : JSON.parse(v); } catch { return dflt; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* file:// may block; ignore */ } },
};

function initMissionState() {
  const seen = store.get('pierceV3Intro', null);
  state.missionsActive = seen === null ? true : !store.get('pierceV3MissionsDismissed', false);
  state.missionIndex = store.get('pierceV3MissionIndex', 0);
}

/* ── Sorting / filtering ───────────────────────────────────────────── */
function currentRows() {
  let rows = D.nodes.slice();
  if (state.search) {
    const q = state.search.toLowerCase();
    rows = rows.filter(n => n.label.toLowerCase().includes(q) || n.id.includes(q));
  }
  if (state.domainFilter) rows = rows.filter(n => n.domain === state.domainFilter);
  if (state.tierFilter) rows = rows.filter(n => n.tier === state.tierFilter);
  const dir = state.sortDir === 'asc' ? 1 : -1;
  const key = state.sortKey;
  rows.sort((a, b) => {
    let va = a[key], vb = b[key];
    if (key === 'tier') { va = TIER_RANK_PREFIX[a.tier]; vb = TIER_RANK_PREFIX[b.tier]; }
    if (typeof va === 'string') return va.localeCompare(vb) * dir;
    return (va - vb) * dir;
  });
  return rows;
}

/* ── Mission machinery (lowest priority; strip-only; real detection) ── */
function missionDone(m) {
  switch (m) {
    case 'm1_rank':    return store.get('pierceV3OpenedTop', false) || store.get('pierceV3ClickedRankHeader', false);
    case 'm2_where':   return store.get('pierceV3SeenCallout', false);
    case 'm3_money':   return state.userToggledMoney && state.moneyOn;
    case 'm4_connect': return store.get('pierceV3FollowedConnection', false);
    case 'm5_meaning': return store.get('pierceV3OpenedMethod', false);
    default: return false;
  }
}
function advanceMissions() {
  const keys = Object.keys(MISSION_CONTENT_MAP);
  while (state.missionIndex < keys.length && missionDone(keys[state.missionIndex])) {
    state.missionIndex++;
    store.set('pierceV3MissionIndex', state.missionIndex);
  }
  renderMissionStrip();
}
function renderMissionStrip() {
  const strip = $('#mission-strip');
  if (!state.missionsActive) { strip.hidden = true; return; }
  strip.hidden = false;   /* visibility is the [hidden] attribute; CSS never forces display:none */
  const keys = Object.keys(MISSION_CONTENT_MAP);
  if (state.missionIndex >= keys.length) {
    strip.innerHTML = 'All missions complete · <button class="dismiss-btn" id="mission-replay">Replay</button>';
    const rp = $('#mission-replay');
    if (rp) rp.addEventListener('click', () => {
      state.missionIndex = 0; store.set('pierceV3MissionIndex', 0);
      renderMissionStrip();
    });
    return;
  }
  const m = MISSION_CONTENT_MAP[keys[state.missionIndex]];
  strip.innerHTML = `Mission ${state.missionIndex + 1}/5 · ${esc(m.text)} <button class="dismiss-btn" id="mission-dismiss">Dismiss</button>`;
  const db = $('#mission-dismiss');
  if (db) {
    db.setAttribute('aria-label', 'Dismiss missions');
    db.addEventListener('click', () => {
      state.missionsActive = false;
      store.set('pierceV3MissionsDismissed', true);
      renderMissionStrip();
    });
  }
}
/* app.js part 2 of 3 — directory + map (Task 3.3) */

/* ── Directory rendering ───────────────────────────────────────────── */
function renderDirectory() {
  const rows = currentRows();
  const tbody = $('#dir-body');
  tbody.innerHTML = rows.map(n => {
    const fund = n.moneyFigure
      ? `<span class="fund-dot" role="img" title="Sourced money figure: ${esc(n.moneyFigure)}" aria-label="Sourced money figure: ${esc(n.moneyFigure)}">$</span>`
      : '';
    return `<tr tabindex="0" data-id="${esc(n.id)}" aria-label="${esc(n.label)}, rank ${n.rank}, ${TIER_LABEL[n.tier]}, ${esc(n.domain)}">
      <td class="rank-cell">${n.rank}</td>
      <td class="name-cell">${esc(n.label)}${fund}</td>
      <td><span class="tier-pill">${TIER_LABEL[n.tier]}</span></td>
      <td class="domain-cell">${esc(n.domain)}</td>
    </tr>`;
  }).join('');
  for (const tr of tbody.querySelectorAll('tr')) {
    tr.addEventListener('click', () => openEntity(tr.dataset.id, tr));
    tr.addEventListener('keydown', ev => {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); openEntity(tr.dataset.id, tr); }
    });
  }
  announceSort();
}

function announceSort() {
  const el = $('#sort-status');
  if (!el) return;
  const flt = state.domainFilter || state.tierFilter || state.search;
  el.textContent = `Sorted by ${state.sortKey}, ${state.sortDir === 'asc' ? 'ascending' : 'descending'}; ${currentRows().length} entities shown`
    + (flt ? '. Filters apply to this directory only — the map still shows all 163.' : '');
}

function wireSorters() {
  const ths = [['th-rank','rank'], ['th-name','label'], ['th-tier','tier'], ['th-domain','domain']];
  for (const [id, key] of ths) {
    const th = document.getElementById(id);
    /* keyboard-operable: the th holds a real <button> (WCAG 2.1.1) */
    const trigger = th.querySelector('button') || th;
    trigger.addEventListener('click', () => {
      if (key === 'rank') store.set('pierceV3ClickedRankHeader', true);
      if (state.sortKey === key) {
        state.sortDir = state.sortDir === 'asc' ? 'desc' : 'asc';
      } else {
        state.sortKey = key;
        state.sortDir = key === 'rank' || key === 'label' ? 'asc' : 'asc';
      }
      for (const [tid] of ths) document.getElementById(tid).removeAttribute('aria-sort');
      th.setAttribute('aria-sort', state.sortDir === 'asc' ? 'ascending' : 'descending');
      renderDirectory();
    });
  }
}

function wireFilters() {
  const dchips = $('#domain-chips');
  const domains = [...new Set(D.nodes.map(n => n.domain))].sort();
  dchips.innerHTML = domains.map(d =>
    `<button class="chip" aria-pressed="false" data-domain="${esc(d)}">${esc(d)}</button>`).join('');
  for (const b of dchips.querySelectorAll('button')) {
    b.addEventListener('click', () => {
      const on = b.getAttribute('aria-pressed') === 'true';
      for (const x of dchips.querySelectorAll('button')) x.setAttribute('aria-pressed', 'false');
      if (!on) { b.setAttribute('aria-pressed', 'true'); state.domainFilter = b.dataset.domain; }
      else state.domainFilter = null;
      renderDirectory();
    });
  }
  const tchips = $('#tier-chips');
  tchips.innerHTML = ['top','high','notable'].map(t =>
    `<button class="chip" aria-pressed="false" data-tier="${t}">${TIER_LABEL[t]}</button>`).join('');
  for (const b of tchips.querySelectorAll('button')) {
    b.addEventListener('click', () => {
      const on = b.getAttribute('aria-pressed') === 'true';
      for (const x of tchips.querySelectorAll('button')) x.setAttribute('aria-pressed', 'false');
      if (!on) { b.setAttribute('aria-pressed', 'true'); state.tierFilter = b.dataset.tier; }
      else state.tierFilter = null;
      renderDirectory();
    });
  }
  $('#dir-search').addEventListener('input', e => {
    state.search = e.target.value.trim();
    renderDirectory();
  });
}

/* ── Map: inline SVG (role="img"; nodes pointer-only per plan) ─────── */
const pmax = Math.max(...D.nodes.map(n => n.power));
function nodeR(p) { return R_MIN + (R_MAX - R_MIN) * Math.pow(p / pmax, R_EXP); }

function renderLegend() {
  const doms = [...new Set(D.nodes.map(n => n.domain))].sort();
  const shape = { government: '&#9632;', economic: '&#9679;', institutional: '&#9650;',
                  political: '&#9670;', legal: '&#11022;', media: '&#11021;' };
  $('#map-legend').innerHTML = doms.map(d =>
    `<span class="key"><span aria-hidden="true" style="color:${domainColor(d)}">${shape[d] || '&#9679;'}</span>${esc(d)}</span>`).join('')
    + `<span class="key">·</span><span class="key"><span aria-hidden="true" style="color:${CLASS_COLOR.money}">#</span> money links</span>`;
}

function domainColor(d) {
  const hexes = { government: '#1f77b4', economic: '#b84a00', institutional: '#1e7d32',
                  political: '#b71c1c', legal: '#6a1b9a', media: '#5d4037' };
  return hexes[d] || '#555555';
}

function renderMap() {
  const host = $('#svg-host');
  const pane = $('#map-pane');
  /* TRUE 1:1 rendering (plan: "viewBox == pane, no downscaling"): map the
     2560x1440 data space onto the pane's PIXEL size, so an r=14 node is 14px
     on screen — rendered diameter >=28px at EVERY viewport (gate 1). */
  const pw = Math.max(pane.clientWidth, 300);
  const ph = Math.max(pane.clientHeight, 300);
  const sx = pw / MAP_W, sy = ph / MAP_H;
  const X = x => x * sx, Y = y => y * sy;

  const top10 = D.nodes.slice().sort((a, b) => a.rank - b.rank).slice(0, 10)
    .map(n => n.label).join(', ');
  let edgeEls = '';
  for (const e of D.edges) {
    const a = NODE_BY_ID[e.s], b = NODE_BY_ID[e.t];
    if (!a || !b) continue;
    edgeEls += `<line class="edge${e.relClass === 'money' ? ' money-edge' : ''}" data-s="${esc(e.s)}" data-t="${esc(e.t)}" x1="${X(a.x).toFixed(1)}" y1="${Y(a.y).toFixed(1)}" x2="${X(b.x).toFixed(1)}" y2="${Y(b.y).toFixed(1)}"/>`;
  }
  let nodeEls = '';
  for (const n of D.nodes) {
    const dom = domainColor(n.domain);
    const r = nodeR(n.power).toFixed(1);
    /* rank number burned into the largest bubbles (review: sizes indistinguishable):
       a 13px two-digit rank sits clean once the diameter clears ~34px. */
    const rankTxt = n.rank <= 12 ? `<text class="node-rank" x="${X(n.x).toFixed(1)}" y="${Y(n.y).toFixed(1)}" dy="0.35em" text-anchor="middle">${n.rank}</text>` : '';
    nodeEls += `<circle class="node" data-id="${esc(n.id)}" cx="${X(n.x).toFixed(1)}" cy="${Y(n.y).toFixed(1)}" r="${r}" fill="${dom}" fill-opacity="1" stroke="#ffffff" stroke-width="1.5"><title>${esc(n.label)} — rank ${n.rank}, power ${n.power.toFixed(3)}</title></circle>${rankTxt}`;
  }
  host.innerHTML = `<svg width="${pw}" height="${ph}" viewBox="0 0 ${pw} ${ph}" role="img" aria-label="Pierce County power network. Most powerful: ${esc(top10)}. Each circle is one entity; size shows relative power. The entity directory lists all 163.">${edgeEls}${nodeEls}</svg>`;

  /* labels: HTML overlays in PANE pixel space (top-ranked only, no overlap) */
  const labelled = D.nodes.slice().sort((a, b) => a.rank - b.rank).slice(0, 12);
  const placed = [];
  let labelEls = '';
  for (const n of labelled) {
    const cx = X(n.x), cy = Y(n.y);
    const w = n.label.length * 7.2;
    /* collision rect mirrors RENDERED geometry: labels are centred on the node
       (transform: translate(-50%,-50%)), 13px font ≈ 16px line box. The old
       phantom rect above the node never matched what was drawn (audit finding). */
    const rect = { x: cx - w / 2, y: cy - 8, w, h: 16 };
    if (placed.some(r2 => Math.abs(rect.x - r2.x) < (rect.w + r2.w) / 2 + 6 && Math.abs(rect.y - r2.y) < (rect.h + r2.h) / 2 + 6)) continue;
    placed.push(rect);
    labelEls += `<div class="label" data-id="${esc(n.id)}" style="left:${(cx / pw * 100).toFixed(2)}%;top:${(cy / ph * 100).toFixed(2)}%">${esc(n.label)}</div>`;
  }
  const wrap = document.createElement('div');
  wrap.id = 'label-layer';
  wrap.innerHTML = labelEls;
  host.appendChild(wrap);

  /* pointer-only interactions (keyboard path is the directory).
     Labels are clickable and open THEIR OWN entity (no click-through misclicks). */
  for (const c of host.querySelectorAll('.node')) {
    c.addEventListener('click', () => openEntity(c.dataset.id, null));
  }
  for (const l of wrap.querySelectorAll('.label')) {
    l.addEventListener('click', () => openEntity(l.dataset.id, null));
  }

  applyMoney();   /* reserve gold for the ON state (money edges render neutral when off) */
}

function wireMoneyToggle() {
  const t = $('#money-toggle');
  t.addEventListener('click', () => {
    state.moneyOn = !state.moneyOn;
    state.userToggledMoney = true;
    t.setAttribute('aria-checked', state.moneyOn ? 'true' : 'false');
    applyMoney();
    advanceMissions();
  });
}

function applyMoney() {
  const svg = $('#svg-host svg');
  if (!svg) return;
  svg.querySelectorAll('.edge:not(.money-edge)').forEach(el => { el.style.opacity = state.moneyOn ? '0.12' : ''; });
  svg.querySelectorAll('.money-edge').forEach(el => {
    el.style.opacity = state.moneyOn ? '1' : '';
    el.style.stroke = state.moneyOn ? '' : '#C8C8C8';   /* gold is reserved for the ON state */
  });
  svg.querySelectorAll('.node').forEach(el => {
    if (state.moneyOn && FUNDED.has(el.dataset.id)) el.setAttribute('stroke', '#B8860B');
    else el.setAttribute('stroke', '#ffffff');
  });
  if (state.moneyOn) store.set('pierceV3SeenMoneyOn', true);
}
/* app.js part 3 of 3 — entity page, ego-network, modal, routing, init */

/* ── Entity page (full takeover; split view untouched beneath) ─────── */
function connGroups(nid) {
  const groups = {};
  for (const e of D.edges) {
    let other = null, rel = e.rel, dirOut = null;
    if (e.s === nid) { other = e.t; rel = e.rel; dirOut = true; }
    else if (e.t === nid) { other = e.s; rel = e.rel; dirOut = false; }
    else continue;
    (groups[e.relClass] = groups[e.relClass] || []).push({ other, rel, dirOut, w: e.w });
  }
  return groups;
}

/* Grouped connections (8 canonical classes, verbatim labels) — rendered on
   EVERY entity page (Task 4.1 item 3; the audit found it missing on degree>=3). */
function connectionsHtml(groups) {
  const cards = [];
  for (const cls of Object.keys(groups)) {
    const members = groups[cls].map(c =>
      `<button class="ego-card" data-open="${esc(c.other)}">${esc(NODE_BY_ID[c.other].label)} <span class="source-note">· ${esc(c.rel)}</span></button>`);
    cards.push(`<div class="conn-group" data-class="${cls}"><h3>${esc(cls)}</h3>${members.join('')}</div>`);
  }
  return `<div class="ego-cards">${cards.join('')}</div>`;
}

/* While the entity takeover is open, the split view + app bar are inert so
   focus cannot reach controls hidden behind the overlay (WCAG 2.2 2.4.11). */
function setBackgroundInert(on) {
  for (const sel of ['.shell', '.appbar', '.skip-link']) {
    const el = document.querySelector(sel);
    if (el) el.inert = !!on;
  }
}

function openEntity(nid, originEl) {
  const n = NODE_BY_ID[nid];
  if (!n) return;
  const wasOpen = !!state.currentEntity;
  state.currentEntity = nid;
  const view = $('#entity-view');

  /* money callout (mission 2 lives here) */
  let callout = '';
  if (n.moneyFigure) {
    callout = `<div class="money-callout">
      <span class="figure">${esc(n.moneyFigure)}</span> — ${esc(n.moneyBasis || '')}
      <span class="source-note">Source: ${sourceHtml(n.moneySource)}</span>
    </div>`;
  }

  /* tier header + score + method button (no tooltip — plan F9) */
  const ex = (window.PIERCE_DATA.execSummaries || {})[nid];
  const execCard = ex ? `<div class="exec-summary" id="exec-summary">
    <div class="exec-verdict"><span class="exec-kicker">Bottom line</span><span class="exec-conf">confidence: ${esc(ex.confidence || 'n/a')}</span></div>
    <p class="exec-headline">${esc(ex.headline || '')}</p>
    <details class="exec-counter"><summary>The other side</summary><p>${esc(ex.counter || '')}</p></details>
  </div>` : '';
  const header = `<div class="entity-header">
    <h1 id="entity-title" tabindex="-1">${esc(n.label)}</h1>
    <div class="entity-meta">
      <span class="tier-pill">${TIER_LABEL[n.tier]}</span>
      <span class="domain-chip">${esc(n.domain)}</span>
      <span>Rank ${n.rank} of 163 · power ${(n.power).toFixed(3)} <span class="source-note">(network-centrality composite — see method)</span></span>
      <button class="method-btn" id="entity-method-btn">method</button>
    </div>
    <p class="source-note">${esc(n.desc || '')}</p>
  </div>`;

  /* ego block: diagram + grouped connection list on every page (Task 4.1 item 3) */
  const groups = connGroups(nid);
  const deg = DEGREE[nid] || 0;
  let egoBlock = '';
  if (deg >= EGO_DIAGRAM_MIN_DEGREE && deg <= EGO_DIAGRAM_MAX_DEGREE) {
    egoBlock = `<div class="ego-host" id="ego-host" aria-label="Connections of ${esc(n.label)}"></div>${connectionsHtml(groups)}`;
  } else {
    const note = deg > EGO_DIAGRAM_MAX_DEGREE
      ? `<p class="source-note">${deg} direct connections — shown as a grouped list (too dense for a readable diagram).</p>` : '';
    egoBlock = note + connectionsHtml(groups);
  }

  /* wide layout: header spans, grid [TOC rail | main]; prose capped inside.
     Exec summary rides ABOVE the ego/body blocks — the verdict is the first
     thing a reader meets (review: "there's no exec summary"; the old page
     buried it in section 12 nine sections deep). */
  const toc = n.sections.map(s =>
    `<a href="#sec-${esc(s.id)}" data-jump="sec-${esc(s.id)}">${esc(s.title)}</a>`).join('');
  const rail = `<nav class="section-nav" aria-label="On this page"><div class="section-nav-inner">${toc}</div></nav>`;
  const body = `<div class="entity-body" id="entity-body">${n.profile}</div>`;
  const main = `<div class="entity-main">${callout}${execCard}${egoBlock}${body}</div>`;

  $('#entity-content').innerHTML =
    `<div class="entity-layout">${header}<div class="entity-grid">${rail}${main}</div></div>`;
  view.hidden = false;
  document.body.style.overflow = 'hidden';
  setBackgroundInert(true);

  /* wire nav + buttons */
  $('#back-btn').onclick = () => closeEntity();
  const emb = $('#entity-method-btn');
  if (emb) emb.onclick = () => openMethod();
  for (const a of view.querySelectorAll('[data-jump]')) {
    a.addEventListener('click', ev => {
      ev.preventDefault();
      const t = view.querySelector('#' + CSS.escape(a.dataset.jump));
      if (t) {
      const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
    });
  }
  /* ego behaviors */
  if (deg >= EGO_DIAGRAM_MIN_DEGREE && deg <= EGO_DIAGRAM_MAX_DEGREE) drawEgo(n, groups);
  for (const b of view.querySelectorAll('.ego-card[data-open]')) {
    b.addEventListener('click', () => {
      store.set('pierceV3FollowedConnection', true);
      openEntity(b.dataset.open, null);
    });
  }
  if (n.rank === 1) store.set('pierceV3OpenedTop', true);   // mission 1
  if (n.moneyFigure) store.set('pierceV3SeenCallout', true); // mission 2

  /* history: first open from the map PUSHES an entry; entity→entity navigation
     REPLACES it; a deep-link open replaces the load entry. Closing is a
     replace (see closeEntity) — no async back() anywhere. */
  if (wasOpen) {
    history.replaceState({ entity: nid }, '', '#entity/' + nid);
  } else {
    const mHash = location.hash.match(/^#entity\/([a-z0-9-]+)$/);
    if (mHash && mHash[1] === nid) history.replaceState({ entity: nid }, '', location.hash);
    else history.pushState({ entity: nid }, '', '#entity/' + nid);
  }
  $('#entity-title').focus();
  advanceMissions();
}

function closeEntity() {
  const closing = state.currentEntity;
  $('#entity-view').hidden = true;
  $('#entity-content').innerHTML = '';
  document.body.style.overflow = '';
  setBackgroundInert(false);
  state.currentEntity = null;
  /* restore focus to the originating row (keyed by the entity just closed) */
  const back = closing ? document.querySelector(`#dir-body tr[data-id="${closing}"]`) : null;
  if (back) back.focus();
  /* Clear the entity entry IN PLACE. Never history.back() here: that navigation
     is async, and its popstate can land after the next entity opens — closing it
     (measured: an open→close→open sequence closed the re-opened entity). The
     replace keeps "browser Back returns to the map" true without the race, and
     leaves no ghost entry to re-open the entity. */
  if (history.state && history.state.entity) {
    history.replaceState({ entity: null }, '', location.pathname);
  }
}

/* ── Ego-network diagram (same edge list, neighbours only) ─────────── */
function drawEgo(n, groups) {
  const host = $('#ego-host');
  const neigh = new Set();
  for (const cls of Object.keys(groups)) for (const c of groups[cls]) neigh.add(c.other);
  const list = [...neigh];
  const cx = 400, cy = 260;
  const posMe = { x: cx, y: cy };
  const posN = {};
  list.forEach((id, i) => {
    const ang = (2 * Math.PI * i) / list.length;
    posN[id] = { x: cx + 260 * Math.cos(ang), y: cy + 190 * Math.sin(ang) };
  });
  const edgesFor = [];
  for (const e of D.edges) {
    if (e.s === n.id && posN[e.t]) edgesFor.push(e);
    else if (e.t === n.id && posN[e.s]) edgesFor.push(e);
  }
  let edgeStr = '';
  for (const e of edgesFor) {
    const a = posN[e.s === n.id ? e.t : e.s];
    const money = e.relClass === 'money' ? ' money-edge' : '';
    /* relationship label ON the spoke (review: "I can't see relationships"):
       the verbatim rel sits at the line's midpoint, gold ink for money edges,
       ink-soft otherwise; white halo keeps it legible over crossing lines. */
    const lx = (cx + a.x) / 2, ly = (cy + a.y) / 2;
    const lbl = esc(e.rel || '');
    edgeStr += `<line class="edge${money}" x1="${cx}" y1="${cy}" x2="${a.x}" y2="${a.y}"/>`
      + `<text class="edge-label${money ? ' money-edge-label' : ''}" x="${lx}" y="${ly}" dy="-3" text-anchor="middle">${lbl}</text>`;
  }
  let nodeStr = `<circle class="node" cx="${cx}" cy="${cy}" r="${nodeR(n.power)}" fill="${domainColor(n.domain)}"><title>${esc(n.label)}</title></circle>`;
  for (const id of list) {
    const p = posN[id], m = NODE_BY_ID[id];
    nodeStr += `<circle class="node" data-id="${esc(id)}" cx="${p.x}" cy="${p.y}" r="${Math.max(9, nodeR(m.power))}" fill="${domainColor(m.domain)}"><title>${esc(m.label)}</title></circle>`;
    nodeStr += `<text x="${p.x}" y="${p.y - Math.max(9, nodeR(m.power)) - 4}" font-size="10" text-anchor="middle" fill="#1B1B1B">${esc(m.label)}</text>`;
  }
  const clsColorNote = Object.keys(groups).map(k =>
    `<span class="key"><span style="color:${CLASS_COLOR[k]}">#</span>${esc(k)}</span>`).join(' ');
  host.innerHTML = `<svg viewBox="0 0 800 520" role="img" aria-label="Ego network of ${esc(n.label)}: ${list.length} direct connections.">${edgeStr}${nodeStr}</svg>
    <div class="map-legend" style="position:static;margin-top:8px;">${clsColorNote}</div>`;
  for (const c of host.querySelectorAll('.node[data-id]')) {
    c.addEventListener('click', () => {
      store.set('pierceV3FollowedConnection', true);
      openEntity(c.dataset.id, null);
    });
  }
}

/* ── Method & Sources modal (native dialog; gate: 1 modal) ─────────── */
function methodHtml() {
  const tiers = D.tiers.map(t => `<tr><td>${esc(t.label)}</td><td>${esc(t.range)}</td><td>${esc(t.note)}</td></tr>`).join('');
  const money = D.nodes.filter(n => n.moneyFigure).map(n =>
    `<tr><td>${esc(n.label)}</td><td>${esc(n.moneyFigure)}</td><td>${esc(n.moneyBasis || '')}</td><td>${sourceHtml(n.moneySource)}</td></tr>`).join('');
  return `<p>Every entity's composite power score combines four normalized measures — weighted degree (35%), betweenness (25%), eigenvector centrality (20%), and PageRank (20%) — then adds a published veto bonus for actors holding unique legal powers, capped so hubs and parties cannot rank above the officials they serve. Rankings come from the researched record, not the formula alone.</p>
  <h3>Veto bonus (script constants, scripts/compute_power.py VETO_BONUS — hub/party caps in the same script follow skeptic-ranking.md)</h3>
  <p class="source-note">ryan-mello +0.30 · puyallup-tribe +0.30 · jblm +0.28 · chamber +0.20 · keith-swank +0.16 · mary-robnett +0.14 · multicare +0.10 · anders-ibsen +0.10 · nathe-lawver +0.10 · tom-pierson +0.10 · john-wiborg +0.08 · dona-ponepinto +0.08 · john-mccarthy +0.06 · news-tribune +0.05 · ltg-mcfarlane +0.05 · bill-sterud +0.05<br>The centrality method: <a href="../26-power-methodology.md">evidence/26-power-methodology.md</a></p>
  <h3>Tier bands</h3><table><tbody>${tiers}</tbody></table>
  <h3>Sourced money figures</h3><table><tbody>${money}</tbody></table>
  <p class="source-note">The score does NOT measure: informal access, personal trust, or future intent. Full method: <a href="../26-power-methodology.md">evidence/26-power-methodology.md</a> · money basis: <a href="../28-source-of-economic-power.md">evidence/28-source-of-economic-power.md</a></p>`;
}

function openMethod() {
  const dlg = $('#method-modal');
  if (!$('#method-body').innerHTML) $('#method-body').innerHTML = methodHtml();
  dlg.showModal();
  store.set('pierceV3OpenedMethod', true);
  advanceMissions();
}

/* ── Routing (deep links; back returns to map) ─────────────────────── */
function route() {
  const mHash = location.hash.match(/^#entity\/([a-z0-9-]+)$/);
  if (mHash && NODE_BY_ID[mHash[1]]) {
    if (state.currentEntity !== mHash[1]) openEntity(mHash[1], null);
    return;
  }
  if (state.currentEntity) closeEntity();
}
window.addEventListener('popstate', route);

/* ── Init ──────────────────────────────────────────────────────────── */
function renderMapIfNeeded() {
  const pane = $('#map-pane');
  if (!pane || pane.clientWidth === 0) return;   // stacked layout / hidden
  renderMap();
  if (state.moneyOn) applyMoney();               // preserve user's toggle
}

let resizeTimer = null;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    if (!state.currentEntity) renderMapIfNeeded();
  }, 150);
});

function init() {
  initMissionState();
  $('#appbar-thesis').innerHTML = `${esc(D.thesis)}`;
  $('#method-btn').addEventListener('click', openMethod);
  $('#method-close').addEventListener('click', () => $('#method-modal').close());
  wireSorters();
  wireFilters();
  wireMoneyToggle();
  renderDirectory();
  renderMap();
  renderLegend();
  renderMissionStrip();
  route();
}
init();