#!/usr/bin/env node
/* audit_probe.js — regression probes for the 2026-10-05 audit cycle (deleg_2ca2d99b).
   Covers the findings fixed after the adversarial audit + zero-context walkthrough:
   A1 mission strip visible · A2 keyboard sort · A3 focus containment (inert) ·
   A4 grouped connections on degree>=3 · A5 hub cap (no hairball) · A6 map legend ·
   A7 modal source links split · A8 no 'See above' · A9 label click → own entity ·
   A10 320px reflow · A11 money edges gray OFF / gold ON · A12 1024px label overlaps.
   Drives the harness Chrome over CDP (same pattern as browser_walkthrough.js).
   Read-only; prints PASS/FAIL per probe; exit 1 on any FAIL. */
'use strict';
const { execSync } = require('child_process');
const fs = require('fs');
const http = require('http');

const URL_ = 'file:///Users/moliver/Documents/Investigations/2608-pierce-leadership/evidence/network/index.html';

function chromeDebugPort() {
  const ps = execSync('ps aux').toString();
  const line = ps.split('\n').find(l => l.toLowerCase().includes('chrome') && l.includes('--user-data-dir='));
  if (!line) throw new Error('harness Chrome not running (launch chrome-mac-arm64 with --remote-debugging-port=0 and a --user-data-dir)');
  const udd = line.match(/--user-data-dir=(\S+)/)[1];
  return fs.readFileSync(`${udd}/DevToolsActivePort`, 'utf8').split('\n')[0].trim();
}
function getJson(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port, path }, r => { let b = ''; r.on('data', c => b += c); r.on('end', () => res(JSON.parse(b))); }).on('error', rej);
  });
}
function putJson(path) {
  return new Promise((res, rej) => {
    const r = http.request({ host: '127.0.0.1', port, path, method: 'PUT' }, r => { let b = ''; r.on('data', c => b += c); r.on('end', () => res(JSON.parse(b))); });
    r.on('error', rej); r.end();
  });
}
let port, ws, mid = 0;
const pending = new Map();
function send(method, params = {}) {
  const id = ++mid;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((res, rej) => pending.set(id, { res, rej }));
}
async function evaljs(expr) {
  const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error('eval: ' + JSON.stringify(r.exceptionDetails).slice(0, 400));
  return r.result.value;
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
const results = [];
function probe(n, ok, detail = '') { results.push(ok); console.log(`${ok ? 'PASS' : 'FAIL'} ${n}${detail ? ' — ' + detail : ''}`); }

(async () => {
  try {
    port = chromeDebugPort();
    const created = await putJson('/json/new?' + encodeURIComponent(URL_));
    const targetId = created.id;
    await sleep(1800);
    const targets = await getJson('/json');
    const page = targets.find(t => t.id === targetId);
    ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise(res => { ws.onopen = res; });
    ws.onmessage = ev => { const m = JSON.parse(ev.data); if (m.id && pending.has(m.id)) { pending.get(m.id).res(m.result); pending.delete(m.id); } };
    await send('Runtime.enable');
    await send('Page.enable');

    /* fresh profile: clear first-run keys, reload */
    await evaljs("localStorage.clear()");
    await send('Page.reload');
    await sleep(2200);

    /* A1. mission strip visible on a true first run (was display:none forever) */
    const strip = await evaljs(`(() => { const s = document.getElementById('mission-strip'); const cs = getComputedStyle(s); return { hidden: s.hidden, display: cs.display, text: s.textContent.slice(0, 60) }; })()`);
    probe('A1 mission strip visible first-run', strip.hidden === false && strip.display !== 'none' && /Mission 1/.test(strip.text), JSON.stringify(strip));

    /* A2. sort headers keyboard operable: 4 real buttons; click sorts by tier */
    const btns = await evaljs("document.querySelectorAll('#dir-table th .th-btn').length");
    await evaljs(`(() => { const b = document.querySelector('#th-tier .th-btn'); b.focus(); b.click(); })()`);
    await sleep(400);
    const sortState = await evaljs(`document.getElementById('th-tier').getAttribute('aria-sort')`);
    probe('A2 sort headers keyboard-operable', btns === 4 && sortState !== null, `buttons=${btns}, tier aria-sort=${sortState}`);

    /* A3. focus containment: shell/appbar inert while entity open */
    await evaljs("openEntity('ryan-mello', null)");
    await sleep(400);
    const inertOn = await evaljs(`(() => ({ shell: document.querySelector('.shell').inert === true, appbar: document.querySelector('.appbar').inert === true }))()`);
    await evaljs("closeEntity()");
    await sleep(400);
    const inertOff = await evaljs("document.querySelector('.shell').inert === false");
    probe('A3 focus containment (inert on open/off on close)', inertOn.shell && inertOn.appbar && inertOff === true, JSON.stringify(inertOn) + ' off=' + inertOff);

    /* A4. connection groups on a degree>=3 page (ryan-mello) — Task 4.1 item 3 */
    await evaljs("openEntity('ryan-mello', null)");
    await sleep(450);
    const conn = await evaljs(`(() => ({ groups: document.querySelectorAll('.conn-group').length, cards: document.querySelectorAll('.conn-group .ego-card').length, diagram: !!document.getElementById('ego-host') }))()`);
    await evaljs("closeEntity()"); await sleep(400);
    probe('A4 grouped connections on ryan-mello (deg 19)', conn.groups > 0 && conn.cards > 0, JSON.stringify(conn));

    /* A5. hub page (county-council, deg 72) uses grouped list, no hairball diagram */
    await evaljs("openEntity('county-council', null)");
    await sleep(500);
    const hub = await evaljs(`(() => ({ diagram: !!document.getElementById('ego-host'), groups: document.querySelectorAll('.conn-group').length, note: !!document.querySelector('.ego-cards') }))()`);
    await evaljs("closeEntity()"); await sleep(400);
    probe('A5 hub page capped to grouped list (no 73-circle hairball)', hub.diagram === false && hub.groups > 0, JSON.stringify(hub));

    /* A6. map legend renders (was dead code, #map-legend empty) */
    const legend = await evaljs(`(() => { const l = document.getElementById('map-legend'); return { len: l.innerHTML.length, text: l.textContent.trim().slice(0, 80) }; })()`);
    probe('A6 map legend rendered', legend.len > 0 && /government/.test(legend.text), legend.text);

    /* A7. modal money-source links: separate anchors, no dead concatenated href */
    await evaljs("openMethod()");
    await sleep(400);
    const modal = await evaljs(`(() => { const rows = [...document.querySelectorAll('#method-body a')]; const hrefs = rows.map(a => a.getAttribute('href')); return { n: hrefs.length, bad: hrefs.filter(h => h.includes(';') || h.includes('%20')).length, sample: hrefs.slice(0, 4) }; })()`);
    await evaljs("document.getElementById('method-modal').close()");
    probe('A7 modal source links split (no dead hrefs)', modal.n > 0 && modal.bad === 0, JSON.stringify(modal.sample) + ' bad=' + modal.bad);

    /* A8. 'See above' gone from rendered pages (settle between opens:
       closeEntity uses history.back(), which is async — probe must not race it) */
    let seen = 0;
    for (const id of ['puyallup-tribe', 'pmba']) {
      await evaljs(`openEntity('${id}', null)`); await sleep(350);
      seen += await evaljs(`/see above/i.test(document.getElementById('entity-content').innerHTML) ? 1 : 0`);
      await evaljs("closeEntity()"); await sleep(400);
    }
    probe('A8 no "See above" on standalone pages', seen === 0, `pages with phrase: ${seen}`);

    /* A9. label click opens ITS OWN entity — real synthesized mouse click.
       Scroll to the top first: earlier steps may leave the document scrolled
       (labels off-viewport → elementFromPoint returns null). A human clicks
       what they can see; the probe must mirror that. */
    await evaljs("window.scrollTo(0, 0)"); await sleep(400);
    const geom = await evaljs(`(() => {
      const l = document.querySelector('.label');
      if (!l) return null;
      const b = l.getBoundingClientRect();
      return { id: l.dataset.id, cx: b.x + b.width / 2, cy: b.y + b.height / 2,
               inView: b.y >= 0 && b.y + b.height <= innerHeight, sy: scrollY };
    })()`);
    await send('Input.dispatchMouseEvent', { type: 'mousePressed', x: geom.cx, y: geom.cy, button: 'left', clickCount: 1 });
    await send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: geom.cx, y: geom.cy, button: 'left', clickCount: 1 });
    await sleep(500);
    const opened = await evaljs("state.currentEntity");
    await evaljs("closeEntity()"); await sleep(400);
    probe('A9 label click resolves to its own entity', opened === geom.id && geom.inView === true, `label ${geom.id} (inView=${geom.inView}, scrollY=${geom.sy}) → opened ${opened}`);

    /* A10. 320px reflow: no page-level horizontal scroll */
    await send('Emulation.setDeviceMetricsOverride', { width: 320, height: 800, deviceScaleFactor: 1, mobile: false });
    await sleep(900);
    const reflow = await evaljs(`(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, tableScroll: !!document.querySelector('.table-scroll') }))()`);
    await send('Emulation.clearDeviceMetricsOverride');
    probe('A10 320px no horizontal page scroll', reflow.sw <= reflow.cw, JSON.stringify(reflow));

    /* A11. money edges neutral when toggle OFF (gold reserved for ON).
       Scoped to the MAIN MAP svg: ego diagrams use class colors per their own
       legend and are not governed by the map toggle. */
    const edgesOff = await evaljs(`(() => { const me = [...document.querySelectorAll('#svg-host svg .money-edge')]; return { n: me.length, goldStroke: me.filter(e => getComputedStyle(e).stroke === 'rgb(184, 134, 11)').length }; })()`);
    await evaljs("document.getElementById('money-toggle').click()"); await sleep(300);
    const edgesOn = await evaljs(`(() => { const me = [...document.querySelectorAll('#svg-host svg .money-edge')]; return { goldStroke: me.filter(e => getComputedStyle(e).stroke === 'rgb(184, 134, 11)').length, opacity: me.filter(e => e.style.opacity === '1').length }; })()`);
    await evaljs("document.getElementById('money-toggle').click()"); await sleep(200);
    probe('A11 money edges gray OFF / gold ON', edgesOff.goldStroke === 0 && edgesOn.goldStroke > 40, `off gold=${edgesOff.goldStroke}, on gold=${edgesOn.goldStroke}, on opacity1=${edgesOn.opacity}`);

    /* A12. 1024x768: zero rendered label overlaps (audit measured 2 with the old
       phantom-rect collision model; labels are now checked at rendered geometry) */
    await send('Emulation.setDeviceMetricsOverride', { width: 1024, height: 768, deviceScaleFactor: 1, mobile: false });
    await send('Page.reload');
    await sleep(2400);
    const overlaps = await evaljs(`(() => {
      const ls = [...document.querySelectorAll('.label')];
      const rs = ls.map(l => { const b = l.getBoundingClientRect(); return { x: b.x, y: b.y, w: b.width, h: b.height }; });
      let n = 0;
      for (let i = 0; i < rs.length; i++) for (let j = i + 1; j < rs.length; j++) {
        const a = rs[i], b = rs[j];
        if (a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y) n++;
      }
      return { overlaps: n, labels: ls.length };
    })()`);
    await send('Emulation.clearDeviceMetricsOverride');
    probe('A12 1024px zero label overlaps', overlaps.overlaps === 0, JSON.stringify(overlaps));

    ws.close();
    console.log(`\n${results.filter(Boolean).length}/${results.length} audit probes PASS`);
    process.exit(results.every(Boolean) ? 0 : 1);
  } catch (e) {
    console.error('PROBE ERROR:', e.message);
    process.exit(2);
  }
})();
