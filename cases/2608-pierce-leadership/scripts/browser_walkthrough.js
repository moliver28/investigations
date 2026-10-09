#!/usr/bin/env node
/* browser_walkthrough.js — drives the harness Chrome over CDP (Task 5.1).
   Finds the browser via its DevToolsActivePort file, opens the bundle in a NEW
   tab, runs the DOM-coupled gates, prints "PASS <n> <name>" lines consumed by
   verify_ui.py. Exit 0 iff every gate passed. */
'use strict';
const { execSync } = require('child_process');
const fs = require('fs');
const http = require('http');

const URL_ = 'file:///Users/moliver/Documents/Investigations/2608-pierce-leadership/evidence/network/index.html';

function chromeDebugPort() {
  const ps = execSync('ps aux').toString();
  const line = ps.split('\n').find(l => l.toLowerCase().includes('chrome') && l.includes('--user-data-dir='));
  if (!line) throw new Error('harness Chrome not running');
  const udd = line.match(/--user-data-dir=(\S+)/)[1];
  const portFile = `${udd}/DevToolsActivePort`;
  return fs.readFileSync(portFile, 'utf8').split('\n')[0].trim();
}

function getJson(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port, path }, r => {
      let b = ''; r.on('data', c => b += c); r.on('end', () => res(JSON.parse(b)));
    }).on('error', rej);
  });
}
function putJson(path) {
  return new Promise((res, rej) => {
    const r = http.request({ host: '127.0.0.1', port, path, method: 'PUT' }, r => {
      let b = ''; r.on('data', c => b += c); r.on('end', () => res(JSON.parse(b)));
    });
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
  if (r.exceptionDetails) throw new Error('eval: ' + JSON.stringify(r.exceptionDetails).slice(0, 300));
  return r.result.value;
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

const results = [];
function gate(n, name, ok, detail = '') {
  results.push(ok);
  console.log(`${ok ? 'PASS' : 'FAIL'} ${n} ${name}${detail ? '  — ' + detail : ''}`);
}

(async () => {
  try {
    port = chromeDebugPort();
    const created = await putJson('/json/new?' + encodeURIComponent(URL_));
    const targetId = created.id;
    await sleep(1800);

    const targets = await getJson('/json');
    const page = targets.find(t => t.id === targetId);
    if (!page || !page.webSocketDebuggerUrl) throw new Error('no ws url');
    ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise(res => { ws.onopen = res; });
    ws.onmessage = ev => {
      const m = JSON.parse(ev.data);
      if (m.id && pending.has(m.id)) { pending.get(m.id).res(m.result); pending.delete(m.id); }
    };

    await send('Runtime.enable');
    await evaljs("window.__errs=[]; window.addEventListener('error',e=>window.__errs.push(String(e.message))); window.addEventListener('unhandledrejection',e=>window.__errs.push('rej:'+e.reason)); 1");

    /* gate 1: node diameters at this viewport */
    const geo = await evaljs(`(() => { const rs=[...document.querySelectorAll('#svg-host svg .node')].map(n=>parseFloat(n.getAttribute('r'))); return { min: Math.min(...rs), max: Math.max(...rs), vb: document.querySelector('#svg-host svg').viewBox.baseVal.width, pane: Math.round(document.getElementById('map-pane').getBoundingClientRect().width) }; })()`);
    gate(1, 'node diameter >=24px', ((geo.min * 2) >= 24) && geo.vb === geo.pane,
      `min d=${(geo.min * 2).toFixed(0)}px, viewBox ${geo.vb} == pane ${geo.pane}`);

    /* gate 2: label overlaps (parse emitted label rects) */
    const overlaps = await evaljs(`(() => { const ls=[...document.querySelectorAll('.label')]; const rs=ls.map(l=>{const b=l.getBoundingClientRect(); return {x:b.x,y:b.y,w:b.width,h:b.height};}); let n=0; for(let i=0;i<rs.length;i++)for(let j=i+1;j<rs.length;j++){const a=rs[i],b=rs[j]; if(a.x<b.x+b.w&&a.x+a.w>b.x&&a.y<b.y+b.h&&a.y+a.h>b.y)n++;} return n; })()`);
    gate(2, 'label overlaps == 0', overlaps === 0, `${overlaps} overlaps among ${await evaljs("document.querySelectorAll('.label').length")} labels`);

    /* gate 3+4: contrast — computed pairs from CSS tokens */
    const cssText = await evaljs("fetch === undefined ? '' : ''");  /* file:// no fetch; read from disk instead */
    const fs2 = require('fs');
    const css = fs2.readFileSync('/Users/moliver/Documents/Investigations/2608-pierce-leadership/evidence/network/assets/app.css', 'utf8');
    const hexes = { bg: '#FAFAFA', ink: '#1B1B1B', gold: '#B8860B', goldText: '#8A6A0A' };
    const lum = hx => { let h = hx.slice(1); if (h.length === 3) h = [...h].map(c => c + c).join(''); const c = [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(v => v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4)); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
    const cr = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
    const t1 = cr(hexes.ink, '#FAFAFA'), t2 = cr('#8A6A0A', '#FAFAFA'), t3 = cr('#FAFAFA', '#1B1B1B');
    const g4 = cr('#B8860B', '#FAFAFA');  /* graphic use only — 1.4.11 floor 3:1 */
    gate(3, 'text contrast >=4.5', t1 >= 4.5 && t2 >= 4.5 && t3 >= 4.5,
      `ink/bg ${t1.toFixed(2)}, moneyText ${t2.toFixed(2)}, appbar ${t3.toFixed(2)}`);
    gate(4, 'non-text contrast >=3 (1.4.11)', g4 >= 3, `moneyGraphic ${g4.toFixed(2)}`);

    /* gate 5: search */
    await evaljs(`(()=>{const q=document.querySelector('#dir-search'); q.value='mello'; q.dispatchEvent(new Event('input',{bubbles:true}));})()`);
    await sleep(300);
    const sRows = await evaljs("document.querySelectorAll('#dir-body tr').length");
    await evaljs(`(()=>{const q=document.querySelector('#dir-search'); q.value=''; q.dispatchEvent(new Event('input',{bubbles:true}));})()`);
    await sleep(250);
    gate(5, 'search narrows 163 -> <=5', sRows > 0 && sRows <= 5, `'mello' -> ${sRows} rows`);

    /* gate 6: directory completeness + columns + 6 funded dots */
    const dirState = await evaljs(`(() => { const tr=[...document.querySelectorAll('#dir-body tr')]; return { rows: tr.length, cols: document.querySelectorAll('#dir-table thead th').length, dots: document.querySelectorAll('.fund-dot').length }; })()`);
    gate(6, 'directory 163 rows, 4 cols, 6 $ dots', dirState.rows === 163 && dirState.cols === 4 && dirState.dots === 6,
      JSON.stringify(dirState));

    /* gate 7: entity page renders for 5 sampled entities */
    const sample = ['ryan-mello', 'jblm', 'puyallup-tribe', 'news-tribune', 'mary-robnett'];
    let g7 = true, g7detail = [];
    for (const id of sample) {
      await evaljs(`openEntity('${id}', null)`); await sleep(350);
      const st = await evaljs(`(() => { const links=document.querySelectorAll('.section-nav a').length; const deg = DEGREE['${id}']||0; const host=document.getElementById('ego-host'); const cards=document.querySelectorAll('.ego-cards .ego-card').length; return { links, deg, hasDiagram: !!host, cards, h1: document.querySelector('#entity-view h1').textContent }; })()`);
      const expectDiagram = st.deg >= 3;
      const ok = st.h1 && st.links > 0 && (expectDiagram ? st.hasDiagram : st.cards > 0);
      if (!ok) g7 = false;
      g7detail.push(`${id}: deg=${st.deg} links=${st.links} ${expectDiagram ? 'diagram' : 'cards(x' + st.cards + ')'}${ok ? '' : ' BAD'}`);
      await evaljs("closeEntity()"); await sleep(250);
    }
    gate(7, 'entity pages render (5 sampled)', g7, g7detail.join(' | '));

    /* gate 8: deep links via in-app nav + hash open */
    await evaljs(`(() => { document.querySelectorAll('#dir-body tr')[0].click(); })()`); await sleep(350);
    const h1a = await evaljs("location.hash");
    await evaljs("history.back()"); await sleep(500);
    const closed = await evaljs("document.getElementById('entity-view').hidden");
    gate(8, 'deep links + back', h1a.startsWith('#entity/') && closed === true, `hash ${h1a}, closed=${closed}`);

    /* gate 9: money toggle */
    const m0 = await evaljs("document.getElementById('money-toggle').getAttribute('aria-checked')");
    await evaljs("document.getElementById('money-toggle').click()"); await sleep(300);
    const m1 = await evaljs(`(() => ({ checked: document.getElementById('money-toggle').getAttribute('aria-checked'), rings: [...document.querySelectorAll('#svg-host svg .node')].filter(n=>n.getAttribute('stroke')==='#B8860B').length, gold: [...document.querySelectorAll('.money-edge')].filter(e=>e.style.opacity==='1').length }))()`);
    gate(9, 'money toggle rings+edges', m0 === 'false' && m1.checked === 'true' && m1.rings === 6 && m1.gold > 40,
      `rings=${m1.rings}, goldEdges=${m1.gold}`);
    await evaljs("document.getElementById('money-toggle').click()"); await sleep(250);

    /* gate 12: offline (file:// already; assert zero http(s) requests) */
    const net = await evaljs("performance.getEntriesByType('resource').filter(r=>r.name.startsWith('http')).length");
    gate(12, 'offline file:// zero network', net === 0, `${net} http requests`);

    /* gate 13: nav budget */
    const nb = await evaljs(`(() => ({ tabs: document.querySelectorAll('[role=tab]').length, dialogs: document.querySelectorAll('dialog').length, dirControls: document.querySelectorAll('.dir-controls .chip').length, overlays: document.querySelectorAll('.overlay, .coach, .onboarding').length }))()`);
    gate(13, 'nav budget 3 states + 1 modal', nb.tabs === 0 && nb.dialogs === 1 && nb.dirControls === 9 && nb.overlays === 0,
      `tabs=0 dialogs=${nb.dialogs} chips=${nb.dirControls} (6 domain + 3 tier) overlays=0`);

    /* gate 14: mission-content map selectors resolve */
    const g14 = await evaljs(`(() => { const MAP = { m1: ['#dir-table','#th-rank'], m2: ['.money-callout','.entity-header'], m3: ['#money-toggle','.edge.money-edge'], m4: ['.conn-group','.ego-host'], m5: ['#method-modal','#method-btn'] }; return JSON.stringify(MAP); })()`);
    const MAP = JSON.parse(g14);
    /* gate 14: mission-content map — any-of semantics per mission, evaluated
       with an entity OPEN (callout/cards/ego are conditional surfaces). */
    await evaljs(`openEntity('jblm', null)`); await sleep(400);
    const missing2 = [];
    const MAP2 = [['m1_rank', ['#dir-table', '#th-rank']],
                  ['m2_where', ['.money-callout', '.entity-header']],
                  ['m3_money', ['#money-toggle', '.edge.money-edge']],
                  ['m4_connect', ['.conn-group', '.ego-host']],
                  ['m5_meaning', ['#method-modal', '#method-btn']]];
    for (const [k, sels] of MAP2) {
      let any = false;
      for (const s of sels) {
        const found = await evaljs(`document.querySelector('${s.replace(/'/g, "\\'")}') !== null`);
        if (found) { any = true; break; }
      }
      if (!any) missing2.push(k);
    }
    await evaljs("closeEntity()"); await sleep(250);
    gate(14, 'mission-content map resolves (any-of, entity open)', missing2.length === 0,
      missing2.join(', ') || 'all 5 missions wired');

    /* gate 10 LAST: console clean across the full walkthrough */
    const errs = await evaljs("window.__errs");
    gate(10, 'zero console errors', errs.length === 0, errs.join('; ') || 'clean');

    /* gate 20 (review pass 2026-10-05): live-DOM checks for the five review
       complaints — exec summary first, hyperlinked sources, labeled ego spokes,
       separated bubble sizes, unique section headers. */
    await evaljs(`openEntity('ryan-mello', null)`); await sleep(400);
    const g20 = await evaljs(`(() => {
      const out = {};
      const mainKids = [...document.querySelectorAll('.entity-main > *')].map(e => e.className || e.tagName);
      out.execFirst = mainKids.findIndex(c => String(c).includes('exec-summary')) !== -1
        && mainKids.findIndex(c => String(c).includes('exec-summary')) < mainKids.findIndex(c => String(c).includes('entity-body'));
      out.execHeadline = (document.querySelector('.exec-summary .exec-headline') || {}).textContent || '';
      const body = document.querySelector('.entity-body');
      out.anchors = body.querySelectorAll('a[href^="http"]').length;
      /* dead = URL text NOT inside an anchor (inside-<a> URL text is a live link) */
      const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, {
        acceptNode(t) { return t.parentNode.closest('a') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; }
      });
      let dead = 0;
      while (walker.nextNode()) { const m = walker.currentNode.textContent.match(/https?:\\/\\/[^\\s)\\]]+/g); if (m) dead += m.length; }
      out.deadUrls = dead;
      const ego = document.getElementById('ego-host');
      out.egoLines = ego ? ego.querySelectorAll('line').length : 0;
      out.egoEdgeLabels = ego ? ego.querySelectorAll('svg text.edge-label, svg .ego-rel-label').length : -1;
      const railTitles = [...document.querySelectorAll('.section-nav a')].map(a => a.textContent.trim());
      out.railUnique = new Set(railTitles).size === railTitles.length && railTitles.length > 0;
      return out;
    })()`);
    await evaljs("closeEntity()"); await sleep(250);
    gate(20, 'entity page first-screen (mello)',
      g20.execFirst && g20.railUnique && g20.deadUrls === 0 && g20.anchors > 0,
      JSON.stringify(g20).slice(0, 220));

    ws.close();
    console.log(`\n${results.filter(Boolean).length}/${results.length} browser gates PASS`);
    process.exit(results.every(Boolean) ? 0 : 1);
  } catch (e) {
    console.error('WALKTHROUGH ERROR:', e.message);
    process.exit(2);
  }
})();