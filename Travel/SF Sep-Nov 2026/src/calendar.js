(function(){
  'use strict';
  function $(id){ return document.getElementById(id); }
  function pad(n){ return (n < 10 ? '0' : '') + n; }
  function lsGet(k, d){ try { var v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } }
  function lsSet(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function el(tag, attrs, kids){
    var n = document.createElement(tag), k;
    if (attrs) for (k in attrs) {
      var v = attrs[k];
      if (v == null || v === false) continue;
      if (k === 'class') n.className = v;
      else if (k === 'text') n.textContent = v;
      else n.setAttribute(k, v === true ? '' : v);
    }
    (kids || []).forEach(function(c){ if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }

  /* ---------- Playbook: filtros de la lista y checklist ---------- */
  document.querySelectorAll('.filters').forEach(function(bar){
    var sec = bar.closest('section');
    bar.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      bar.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var f = b.getAttribute('data-f');
      sec.querySelectorAll('.ev').forEach(function(li){ li.hidden = !(f === 'all' || li.getAttribute('data-v') === f); });
    });
  });
  var todo = lsGet('sf-playbook-todo', {}) || {};
  document.querySelectorAll('.todo input').forEach(function(cb){
    if (todo[cb.id]) cb.checked = true;
    cb.addEventListener('change', function(){ todo[cb.id] = cb.checked; lsSet('sf-playbook-todo', todo); });
  });

  /* ---------- Pestañas ---------- */
  var tabP = $('tab-playbook'), tabC = $('tab-calendar'), panP = $('panel-playbook'), panC = $('panel-calendar');
  function showTab(name){
    var cal = name === 'calendar';
    tabP.setAttribute('aria-selected', cal ? 'false' : 'true');
    tabC.setAttribute('aria-selected', cal ? 'true' : 'false');
    tabP.tabIndex = cal ? -1 : 0; tabC.tabIndex = cal ? 0 : -1;
    panP.hidden = cal; panC.hidden = !cal;
    lsSet('sfcal-tab', name);
    if (cal) render();
  }
  tabP.addEventListener('click', function(){ showTab('playbook'); });
  tabC.addEventListener('click', function(){ showTab('calendar'); });
  [tabP, tabC].forEach(function(t){
    t.addEventListener('keydown', function(e){
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      var other = t === tabP ? tabC : tabP; other.focus(); other.click();
    });
  });

  /* ---------- Calendario: datos ---------- */
  var BASE = [];
  try { BASE = JSON.parse($('base-items').textContent) || []; } catch (e) { BASE = []; }
  var baseById = {};
  BASE.forEach(function(b){ baseById[b.id] = b; });

  var MON = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
  var DOW = ['dom','lun','mar','mié','jue','vie','sáb'];
  var CATS = {
    must:{label:'No faltar', f:'must'}, go:{label:'Ir', f:'go'}, opt:{label:'Si cabe', f:'opt'},
    planb:{label:'Plan B', f:'opt'}, skip:{label:'Saltar', f:'skip'}, own:{label:'Evento propio', f:'own'},
    meet:{label:'Reunión con cliente', f:'meet'}, call:{label:'Llamada', f:'call'}, other:{label:'Otro', f:'other'}
  };
  var FILTERS = [['must','No faltar','must'],['go','Ir','go'],['opt','Si cabe y plan B','opt'],['own','Eventos propios','own'],
                 ['meet','Reuniones','meet'],['other','Otros','other'],['call','Llamadas de German','call'],['skip','Saltar','skip']];
  var EVENT_CATS = {must:1, go:1, opt:1, planb:1, skip:1, own:1};
  var PEOPLE = [['g','German'],['s','Samuel'],['j','Joaquín']];
  var REG = ['sin registro','registrado','aprobado'];

  function dn(s){ var p = s.split('-'); return Math.round(Date.UTC(+p[0], +p[1] - 1, +p[2]) / 864e5); }
  function ds(n){ var d = new Date(n * 864e5); return d.getUTCFullYear() + '-' + pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate()); }
  function mins(t){ var p = String(t).split(':'); return (+p[0]) * 60 + (+p[1]); }
  function isDate(s){ return typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(dn(s)); }
  function isTime(s){ return typeof s === 'string' && /^([01]\d|2[0-3]):[0-5]\d$/.test(s); }
  function str(v, max){ return typeof v === 'string' ? v.slice(0, max || 400).trim() : ''; }
  function safeUrl(u){ u = str(u, 400); return /^https?:\/\//i.test(u) ? u : ''; }
  function fmtT(m){ var h = Math.floor(m / 60) % 24, mm = m % 60; return (h % 12 || 12) + ':' + pad(mm) + (h < 12 ? ' am' : ' pm'); }
  function fmtH(h){ h = h % 24; return (h % 12 || 12) + (h < 12 ? ' am' : ' pm'); }
  function fmtD(day){ var d = new Date(day * 864e5); return DOW[d.getUTCDay()] + ' ' + d.getUTCDate() + ' ' + MON[d.getUTCMonth()]; }

  var DAY0 = dn('2026-09-27'), DAYZ = dn('2026-11-07'), DST_END = dn('2026-11-01');

  function nowIn(tz){
    try {
      var parts = new Intl.DateTimeFormat('en-CA', {timeZone: tz, year:'numeric', month:'2-digit', day:'2-digit', hour:'2-digit', minute:'2-digit', hourCycle:'h23'}).formatToParts(new Date());
      var o = {}; parts.forEach(function(p){ o[p.type] = p.value; });
      return {day: dn(o.year + '-' + o.month + '-' + o.day), min: ((+o.hour) % 24) * 60 + (+o.minute)};
    } catch (e) {
      var d = new Date();
      return {day: dn(d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate())), min: d.getHours() * 60 + d.getMinutes()};
    }
  }
  function weekOf(day){ var w = day - new Date(day * 864e5).getUTCDay(); return Math.min(Math.max(w, DAY0), DAYZ - 6); }

  var narrow = !!(window.matchMedia && window.matchMedia('(max-width: 720px)').matches);
  var st = {
    week: weekOf(nowIn('America/Los_Angeles').day),
    view: lsGet('sfcal-view', narrow ? 'list' : 'week') === 'list' ? 'list' : 'week',
    tz: lsGet('sfcal-tz', 'sf') === 'co' ? 'co' : 'sf',
    filters: {must:true, go:true, opt:true, own:true, meet:true, other:true, call:true, skip:false},
    items: {}, status: {}, conn: 'pending', canWrite: null
  };
  (function(){ var f = lsGet('sfcal-filters', null); if (f && typeof f === 'object') for (var k in st.filters) if (typeof f[k] === 'boolean') st.filters[k] = f[k]; })();

  function fromDoc(id, o, b){
    if (!o || typeof o !== 'object') return null;
    var date = isDate(o.date) ? o.date : (b ? b.date : null);
    if (!date) return null;
    var cat = CATS[o.cat] ? o.cat : (b ? b.cat : 'other');
    var kind = ['free','paid','unknown','na'].indexOf(o.priceKind) >= 0 ? o.priceKind : (b ? b.priceKind : 'unknown');
    var price = str(o.price, 160);
    var short = kind === 'free' ? 'Gratis' : kind === 'paid' ? (price.length > 22 ? price.slice(0, 21) + '…' : price) : kind === 'unknown' ? 'Por confirmar' : '';
    return {
      id: id, title: str(o.title, 140) || (b ? b.title : 'Sin título'), host: b ? b.host : '', cat: cat,
      date: date, endDate: isDate(o.endDate) && dn(o.endDate) >= dn(date) ? o.endDate : '',
      allDay: !!o.allDay, start: isTime(o.start) ? o.start : '', end: isTime(o.end) ? o.end : '',
      place: str(o.place, 160), priceKind: kind, price: price || (kind === 'free' ? 'Gratis' : ''), priceShort: short,
      url: safeUrl(o.url), links: b ? b.links : null, reg: b ? b.reg : '', note: str(o.note, 600),
      by: str(o.by, 40), custom: !b, edited: !!b, endAssumed: false
    };
  }
  function merged(){
    var out = [];
    BASE.forEach(function(b){
      var o = st.items[b.id];
      if (!o) { out.push(b); return; }
      if (o.deleted) return;
      var it = fromDoc(b.id, o, b); out.push(it || b);
    });
    Object.keys(st.items).forEach(function(id){
      if (baseById[id]) return;
      var o = st.items[id]; if (!o || o.deleted) return;
      var it = fromDoc(id, o, null); if (it) out.push(it);
    });
    return out;
  }
  function findItem(id){ var all = merged(); for (var i = 0; i < all.length; i++) if (all[i].id === id) return all[i]; return null; }
  function hiddenBase(){ return Object.keys(st.items).filter(function(id){ return baseById[id] && st.items[id] && st.items[id].deleted; }); }

  function priceTag(it){
    if (it.priceKind === 'na') return null;
    if (it.priceKind === 'free') return {text: it.priceShort || 'Gratis', cls: 'free'};
    if (it.priceKind === 'paid') return {text: it.priceShort || it.price || 'De pago', cls: 'paid'};
    return {text: it.priceShort || 'Por confirmar', cls: 'unknown'};
  }
  function place(it, tz){
    var d = dn(it.date);
    if (it.allDay || !it.start) {
      var e = it.endDate ? dn(it.endDate) : d;
      return {allDay: true, s: d, e: Math.max(e, d)};
    }
    var off = tz === 'co' ? (d < DST_END ? 120 : 180) : 0;
    var a = mins(it.start), b = it.end ? mins(it.end) : a + 60;
    if (b <= a) b = a + 60;
    a += off; b += off;
    var shift = Math.floor(a / 1440); a -= shift * 1440; b -= shift * 1440;
    if (b > 1440) b = 1440;
    return {allDay: false, day: d + shift, a: a, b: b};
  }
  function weekItems(){
    var ws = st.week, we = ws + 6, all = [], timed = [];
    merged().forEach(function(it){
      if (!st.filters[CATS[it.cat].f]) return;
      var p = place(it, st.tz);
      if (p.allDay) { if (p.e < ws || p.s > we) return; all.push({it: it, s: Math.max(p.s, ws), e: Math.min(p.e, we)}); }
      else { if (p.day < ws || p.day > we) return; timed.push({it: it, day: p.day, a: p.a, b: p.b}); }
    });
    all.sort(function(x, y){ return x.s - y.s || (y.e - y.s) - (x.e - x.s); });
    return {all: all, timed: timed};
  }
  function layout(evs){
    evs.sort(function(x, y){ return x.a - y.a || y.b - x.b; });
    var groups = [], cur = [], end = -1;
    evs.forEach(function(e){
      if (cur.length && e.a >= end) { groups.push(cur); cur = []; end = -1; }
      cur.push(e); end = Math.max(end, e.b);
    });
    if (cur.length) groups.push(cur);
    groups.forEach(function(g){
      var cols = [];
      g.forEach(function(e){ var c = 0; while (cols[c] !== undefined && cols[c] > e.a) c++; cols[c] = e.b; e.col = c; });
      g.forEach(function(e){ e.cols = cols.length; });
    });
  }

  /* ---------- Calendario: render ---------- */
  function regCount(id){ var s = st.status[id]; if (!s) return 0; return PEOPLE.filter(function(p){ return (s[p[0]] | 0) > 0; }).length; }
  function aria(it, when){ var pt = priceTag(it); return it.title + ', ' + when + (pt ? ', ' + (it.price || pt.text) : ''); }

  function block(it, e){
    var pt = priceTag(it), timed = !!e;
    var b = el('button', {type: 'button', class: 'evb cat-' + it.cat, title: it.title});
    if (timed) {
      var h = Math.max(20, (e.b - e.a) / 60 * 46 - 2);
      b.setAttribute('aria-label', aria(it, fmtT(e.a) + ' a ' + fmtT(e.b)));
      if (h < 38) {
        b.classList.add('tight'); if (h < 26) b.classList.add('tiny');
        b.appendChild(el('span', {class: 't', text: (pt ? pt.text + ' · ' : '') + it.title}));
      } else {
        b.appendChild(el('span', {class: 't', text: it.title}));
        b.appendChild(el('span', {class: 'm', text: (pt ? pt.text + ' · ' : '') + fmtT(e.a)}));
      }
      b.style.height = h + 'px';
    } else {
      b.setAttribute('aria-label', aria(it, 'todo el día'));
      b.appendChild(el('span', {class: 't', text: (pt ? pt.text + ' · ' : '') + it.title}));
    }
    b.addEventListener('click', function(){ openDetail(it.id); });
    return b;
  }

  function renderWeek(view, w, now){
    var lo = 8 * 60, hi = 20 * 60, HH = 46, i;
    w.timed.forEach(function(e){ lo = Math.min(lo, Math.floor(e.a / 60) * 60); hi = Math.max(hi, Math.ceil(e.b / 60) * 60); });
    var hours = (hi - lo) / 60;
    var head = el('div', {class: 'cal-head'}, [el('div')]);
    for (i = 0; i < 7; i++) {
      var d = st.week + i, dt = new Date(d * 864e5);
      head.appendChild(el('div', {class: d === now.day ? 'today' : null}, [
        el('span', {class: 'dow', text: DOW[dt.getUTCDay()]}),
        el('span', {class: 'dnum', text: String(dt.getUTCDate())}),
        el('span', {class: 'mon', text: MON[dt.getUTCMonth()]})
      ]));
    }
    var lane = el('div', {class: 'lane'});
    w.all.forEach(function(a){
      var b = block(a.it, null);
      b.style.gridColumn = (a.s - st.week + 1) + ' / span ' + (a.e - a.s + 1);
      lane.appendChild(b);
    });
    var allrow = el('div', {class: 'cal-all'}, [el('div', {class: 'gl', text: 'todo el día'}), lane]);
    var body = el('div', {class: 'cal-body'}), gut = el('div', {class: 'gut'});
    gut.style.height = (hours * HH) + 'px';
    for (i = lo / 60 + 1; i < hi / 60; i++) {
      var lab = el('span', {class: 'hr', text: fmtH(i)});
      lab.style.top = ((i - lo / 60) * HH) + 'px';
      gut.appendChild(lab);
    }
    body.appendChild(gut);
    for (i = 0; i < 7; i++) {
      var day = st.week + i;
      var col = el('div', {class: 'col' + (day === now.day ? ' today' : '')});
      col.style.height = (hours * HH) + 'px';
      var evs = w.timed.filter(function(e){ return e.day === day; });
      layout(evs);
      evs.forEach(function(e){
        var b = block(e.it, e);
        b.style.top = ((e.a - lo) / 60 * HH) + 'px';
        b.style.left = 'calc(' + (e.col / e.cols * 100) + '% + 2px)';
        b.style.width = 'calc(' + (100 / e.cols) + '% - 4px)';
        col.appendChild(b);
      });
      if (day === now.day && now.min >= lo && now.min <= hi) {
        var line = el('div', {class: 'now'});
        line.style.top = ((now.min - lo) / 60 * HH) + 'px';
        col.appendChild(line);
      }
      body.appendChild(col);
    }
    var grid = el('div', {class: 'cal-grid'}, [head, allrow, body]);
    view.appendChild(el('div', {class: 'cal-scroll'}, [grid]));
    if (!w.all.length && !w.timed.length) view.appendChild(el('p', {class: 'cal-empty', text: 'Nada en esta semana con los filtros actuales.'}));
  }

  function renderList(view, w, now){
    var list = el('div', {class: 'cal-list'}), any = false, i;
    for (i = 0; i < 7; i++) {
      var d = st.week + i, rows = [];
      w.all.forEach(function(a){ if (a.s <= d && a.e >= d) rows.push({it: a.it, a: -1, label: 'todo el día'}); });
      w.timed.forEach(function(e){ if (e.day === d) rows.push({it: e.it, a: e.a, label: fmtT(e.a) + ' a ' + fmtT(e.b)}); });
      if (!rows.length) continue;
      any = true;
      rows.sort(function(x, y){ return x.a - y.a; });
      var dt = new Date(d * 864e5);
      var ul = el('ul');
      rows.forEach(function(r){
        var it = r.it, pt = priceTag(it), rc = regCount(it.id);
        var right = el('span', {class: 'rt'});
        if (pt) right.appendChild(el('span', {class: 'price ' + pt.cls, text: pt.text}));
        if (rc) right.appendChild(el('span', {class: 'who', text: 'registro ' + rc + '/3'}));
        right.appendChild(el('span', {class: 'who', text: CATS[it.cat].label}));
        var title = el('span', {class: 'tt'}, [it.title]);
        if (it.place) title.appendChild(el('small', {text: it.place}));
        var btn = el('button', {type: 'button', class: 'li-item', 'aria-label': aria(it, r.label)}, [
          el('i', {class: 'cat-' + it.cat}), el('span', {class: 'tm', text: r.label}), title, right
        ]);
        btn.addEventListener('click', function(){ openDetail(it.id); });
        ul.appendChild(el('li', null, [btn]));
      });
      list.appendChild(el('div', {class: 'cal-day' + (d === now.day ? ' today' : '')}, [
        el('div', {class: 'dl'}, [el('b', {text: DOW[dt.getUTCDay()] + ' ' + dt.getUTCDate()}), MON[dt.getUTCMonth()]]), ul
      ]));
    }
    view.appendChild(list);
    if (!any) view.appendChild(el('p', {class: 'cal-empty', text: 'Nada en esta semana con los filtros actuales.'}));
  }

  function renderFilters(){
    var box = $('cal-filters');
    if (!box.firstChild) {
      FILTERS.forEach(function(f){
        var b = el('button', {type: 'button', class: 'fchip', id: 'flt-' + f[0], 'data-f': f[0]}, [el('i', {class: 'cat-' + f[2]}), f[1]]);
        b.addEventListener('click', function(){ st.filters[f[0]] = !st.filters[f[0]]; lsSet('sfcal-filters', st.filters); render(); });
        box.appendChild(b);
      });
    }
    FILTERS.forEach(function(f){ $('flt-' + f[0]).setAttribute('aria-pressed', st.filters[f[0]] ? 'true' : 'false'); });
  }
  function canAdd(){ return !!db && st.canWrite !== false && st.conn !== 'ro' && st.conn !== 'none'; }
  function renderConn(){
    var p = $('cal-conn'); p.textContent = ''; p.className = 'conn';
    var msg;
    if (st.conn === 'ok' && st.canWrite !== false) { p.classList.add('ok'); msg = 'Calendario compartido activo. Lo que agreguen lo ven los tres.'; }
    else if (st.conn === 'ro' || (st.conn === 'ok' && st.canWrite === false)) { p.classList.add('warn'); msg = 'Tu acceso es de solo lectura. Pide a German acceso de Contributor para agregar o editar.'; }
    else if (st.conn === 'pending') msg = 'Conectando con el calendario compartido.';
    else { p.classList.add('warn'); msg = 'Esta vista no tiene conexión con el calendario compartido. Se muestra el plan base y no se puede agregar. Ábrela desde claude.ai con tu sesión.'; }
    p.appendChild(document.createTextNode(msg));
    var hid = hiddenBase();
    if (hid.length && canAdd()) {
      var b = el('button', {type: 'button', class: 'linkbtn', text: 'Restaurar ' + hid.length + (hid.length === 1 ? ' evento oculto' : ' eventos ocultos')});
      b.addEventListener('click', function(){ restoreAll(hid); });
      p.appendChild(b);
    }
    $('cal-add').disabled = !canAdd();
  }
  function render(){
    if (panC.hidden) return;
    var we = st.week + 6, a = new Date(st.week * 864e5), b = new Date(we * 864e5);
    $('cal-title').textContent = a.getUTCDate() + ' ' + MON[a.getUTCMonth()] + ' al ' + b.getUTCDate() + ' ' + MON[b.getUTCMonth()] + ' 2026';
    $('cal-prev').disabled = st.week <= DAY0;
    $('cal-next').disabled = st.week >= DAYZ - 6;
    $('view-week').setAttribute('aria-pressed', st.view === 'week' ? 'true' : 'false');
    $('view-list').setAttribute('aria-pressed', st.view === 'list' ? 'true' : 'false');
    $('tz-sf').setAttribute('aria-pressed', st.tz === 'sf' ? 'true' : 'false');
    $('tz-co').setAttribute('aria-pressed', st.tz === 'co' ? 'true' : 'false');
    renderFilters(); renderConn();
    var view = $('cal-view'); view.textContent = '';
    var now = nowIn(st.tz === 'co' ? 'America/Bogota' : 'America/Los_Angeles'), w = weekItems();
    if (st.view === 'week') renderWeek(view, w, now); else renderList(view, w, now);
  }

  $('cal-prev').addEventListener('click', function(){ st.week = Math.max(DAY0, st.week - 7); render(); });
  $('cal-next').addEventListener('click', function(){ st.week = Math.min(DAYZ - 6, st.week + 7); render(); });
  $('cal-today').addEventListener('click', function(){ st.week = weekOf(nowIn('America/Los_Angeles').day); render(); });
  $('view-week').addEventListener('click', function(){ st.view = 'week'; lsSet('sfcal-view', 'week'); render(); });
  $('view-list').addEventListener('click', function(){ st.view = 'list'; lsSet('sfcal-view', 'list'); render(); });
  $('tz-sf').addEventListener('click', function(){ st.tz = 'sf'; lsSet('sfcal-tz', 'sf'); render(); });
  $('tz-co').addEventListener('click', function(){ st.tz = 'co'; lsSet('sfcal-tz', 'co'); render(); });

  /* ---------- Avisos y diálogos ---------- */
  var toastT = null;
  function toast(msg){
    var t = $('cal-toast'); if (!t) { t = el('div', {class: 'toast', id: 'cal-toast', role: 'status'}); document.body.appendChild(t); }
    t.textContent = msg; t.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(function(){ t.hidden = true; }, 2600);
  }
  function openDlg(d){ try { if (!d.open) d.showModal(); } catch (e) { d.setAttribute('open', ''); } }
  function closeDlg(d){ try { d.close(); } catch (e) { d.removeAttribute('open'); } }
  function errMsg(err){
    var c = err && err.code;
    if (c === 'invalid_argument' || c === 'not_granted' || c === 'revoked') { st.conn = 'ro'; renderConn(); return 'No se pudo guardar. Tu acceso a esta página parece ser de solo lectura: pide a German acceso de Contributor.'; }
    if (c === 'quota_exceeded') return 'El calendario llegó al límite de elementos. Hay que borrar algunos antes de agregar más.';
    return 'No se pudo guardar. Intenta de nuevo en un momento.';
  }

  var dDetail = $('dlg-detail'), dForm = $('dlg-form'), curId = null, editId = null;

  function whenLines(it){
    var sf = place(it, 'sf'), co = place(it, 'co');
    if (sf.allDay) return [sf.s === sf.e ? fmtD(sf.s) + ', todo el día' : fmtD(sf.s) + ' al ' + fmtD(sf.e), ''];
    var sub = fmtT(co.a) + ' a ' + fmtT(co.b) + ' en Colombia' + (co.day !== sf.day ? ', ' + fmtD(co.day) : '');
    if (it.endAssumed) sub += '. El evento no publica hora de cierre: duración estimada';
    return [fmtD(sf.day) + ', ' + fmtT(sf.a) + ' a ' + fmtT(sf.b) + ', hora de San Francisco', sub];
  }
  function row(dl, label, main, sub){
    if (!main) return;
    var dd = el('dd', null, [main]);
    if (sub) dd.appendChild(el('small', {text: sub}));
    dl.appendChild(el('dt', {text: label})); dl.appendChild(dd);
  }
  function renderReg(it){
    var box = $('dd-reg'); box.textContent = '';
    if (!EVENT_CATS[it.cat] && it.cat !== 'other') return;
    var s = st.status[it.id] || {};
    var wrap = el('div', {class: 'regs', role: 'group', 'aria-label': 'Registro de cada uno'});
    PEOPLE.forEach(function(p){
      var v = (s[p[0]] | 0) % 3;
      var b = el('button', {type: 'button', 'data-s': String(v), id: 'reg-' + p[0], text: p[1] + ': ' + REG[v]});
      b.disabled = !canAdd();
      b.addEventListener('click', function(){ cycleReg(it.id, p[0]); });
      wrap.appendChild(b);
    });
    box.appendChild(el('p', {class: 'eyebrow', text: 'Registro de cada uno, toca para cambiar'}));
    box.appendChild(wrap);
  }
  function openDetail(id){
    var it = findItem(id); if (!it) return;
    curId = id;
    var chips = $('dd-chips'); chips.textContent = '';
    chips.appendChild(el('span', {class: 'chip ' + (it.cat === 'must' ? 'must' : it.cat === 'go' || it.cat === 'own' || it.cat === 'meet' ? 'go' : it.cat === 'skip' ? 'skip' : 'opt'), text: CATS[it.cat].label}));
    var pt = priceTag(it);
    if (pt) chips.appendChild(el('span', {class: 'price ' + pt.cls, text: pt.text}));
    if (it.edited) chips.appendChild(el('span', {class: 'who', text: 'editado por el equipo'}));
    $('dd-title').textContent = it.title;
    var dl = $('dd-rows'); dl.textContent = '';
    var w = whenLines(it);
    row(dl, 'Cuándo', w[0], w[1]);
    if (it.host) row(dl, 'Organiza', it.host);
    row(dl, 'Dónde', it.place);
    if (it.priceKind !== 'na') row(dl, 'Precio', it.price || (pt ? pt.text : ''), it.priceKind === 'unknown' ? 'Revisar en el checkout antes de comprar' : '');
    row(dl, 'Registro', it.reg);
    var links = [];
    (it.links || []).forEach(function(l){ var u = safeUrl(l[1]); if (u) links.push([l[0], u]); });
    if (it.url && !links.some(function(l){ return l[1] === it.url; })) links.push(['abrir página', it.url]);
    if (links.length) {
      var dd = el('dd');
      links.forEach(function(l, i){ if (i) dd.appendChild(document.createTextNode(' · ')); dd.appendChild(el('a', {href: l[1], target: '_blank', rel: 'noopener noreferrer', text: l[0]})); });
      dl.appendChild(el('dt', {text: 'Links'})); dl.appendChild(dd);
    }
    row(dl, 'Nota', it.note);
    if (it.by) row(dl, 'Agregó', it.by);
    renderReg(it);
    var ok = canAdd();
    $('dd-edit').disabled = !ok;
    $('dd-delete').disabled = !ok;
    $('dd-delete').textContent = it.custom ? 'Eliminar' : 'Ocultar';
    $('dd-restore').hidden = !(it.edited && ok);
    openDlg(dDetail);
  }
  $('dd-close').addEventListener('click', function(){ closeDlg(dDetail); });
  $('dd-edit').addEventListener('click', function(){ var it = findItem(curId); closeDlg(dDetail); if (it) openForm(it); });
  $('dd-delete').addEventListener('click', function(){
    var it = findItem(curId); if (!it || !db) return;
    var ref = db.collection('items').doc(it.id), p;
    if (it.custom) p = ref.delete(); else p = ref.set({v: 1, base: true, deleted: true, title: it.title, at: new Date().toISOString()});
    $('dd-delete').disabled = true;
    p.then(function(){
      if (it.custom) delete st.items[it.id]; else st.items[it.id] = {deleted: true};
      closeDlg(dDetail); toast(it.custom ? 'Eliminado' : 'Oculto. Se puede restaurar desde la barra del calendario'); render();
    }, function(err){ $('dd-delete').disabled = false; toast(errMsg(err)); });
  });
  $('dd-restore').addEventListener('click', function(){
    if (!db || !curId) return;
    db.collection('items').doc(curId).delete().then(function(){ delete st.items[curId]; closeDlg(dDetail); toast('Volvió al original'); render(); }, function(err){ toast(errMsg(err)); });
  });
  function restoreAll(ids){
    if (!db) return;
    var i = 0;
    (function next(){
      if (i >= ids.length) { toast('Eventos restaurados'); render(); return; }
      var id = ids[i++];
      db.collection('items').doc(id).delete().then(function(){ delete st.items[id]; next(); }, function(err){ toast(errMsg(err)); });
    })();
  }

  /* registro por persona: una escritura a la vez por documento */
  var regBusy = {}, regDirty = {};
  function flushReg(id){
    if (!db) return;
    if (regBusy[id]) { regDirty[id] = true; return; }
    regBusy[id] = true; regDirty[id] = false;
    var s = st.status[id] || {};
    db.collection('status').doc(id).set({g: s.g | 0, s: s.s | 0, j: s.j | 0}).then(function(){
      regBusy[id] = false; if (regDirty[id]) flushReg(id);
    }, function(err){ regBusy[id] = false; regDirty[id] = false; toast(errMsg(err)); });
  }
  function cycleReg(id, key){
    var s = st.status[id] ? {g: st.status[id].g | 0, s: st.status[id].s | 0, j: st.status[id].j | 0} : {g: 0, s: 0, j: 0};
    s[key] = (s[key] + 1) % 3; st.status[id] = s;
    var it = findItem(id); if (it) renderReg(it);
    flushReg(id);
    if (st.view === 'list') render();
  }

  /* ---------- Formulario ---------- */
  function priceKindSel(){ var r = dForm.querySelector('input[name="f-price"]:checked'); return r ? r.value : ''; }
  function syncForm(){
    var allDay = $('f-allday').checked;
    $('f-start-wrap').hidden = allDay; $('f-end-wrap').hidden = allDay;
    $('f-amount').hidden = priceKindSel() !== 'paid';
  }
  function formErr(msg){ var e = $('f-err'); e.textContent = msg || ''; e.hidden = !msg; }
  function openForm(it){
    editId = it ? it.id : null;
    $('df-title').textContent = it ? 'Editar' : 'Agregar al calendario';
    $('f-title').value = it ? it.title : '';
    $('f-cat').value = it ? it.cat : 'meet';
    $('f-by').value = lsGet('sfcal-by', 'German');
    if (['German','Samuel','Joaquín'].indexOf($('f-by').value) < 0) $('f-by').value = 'German';
    $('f-date').value = it ? it.date : ds(Math.min(Math.max(nowIn('America/Los_Angeles').day, st.week), st.week + 6));
    $('f-enddate').value = it && it.endDate ? it.endDate : '';
    $('f-allday').checked = it ? !!(it.allDay || !it.start) : false;
    $('f-start').value = it && it.start ? it.start : '';
    $('f-end').value = it && it.end ? it.end : '';
    $('f-place').value = it ? it.place : '';
    var k = it ? it.priceKind : 'na';
    dForm.querySelectorAll('input[name="f-price"]').forEach(function(r){ r.checked = r.value === k; });
    $('f-amount').value = it && it.priceKind === 'paid' ? it.price : '';
    $('f-url').value = it ? (it.url || (it.links && it.links[0] ? it.links[0][1] : '')) : '';
    $('f-note').value = it ? it.note : '';
    formErr(''); syncForm();
    $('f-save').disabled = false;
    openDlg(dForm);
    $('f-title').focus();
  }
  $('cal-add').addEventListener('click', function(){ if (canAdd()) openForm(null); });
  $('f-cancel').addEventListener('click', function(){ closeDlg(dForm); });
  $('f-allday').addEventListener('change', syncForm);
  dForm.querySelectorAll('input[name="f-price"]').forEach(function(r){ r.addEventListener('change', syncForm); });
  $('f-cat').addEventListener('change', function(){
    var c = $('f-cat').value, k = priceKindSel();
    if (EVENT_CATS[c] && (k === 'na' || !k)) { $('f-price-na').checked = false; }
    if (!EVENT_CATS[c] && !k) $('f-price-na').checked = true;
    syncForm();
  });

  $('cal-form').addEventListener('submit', function(e){
    e.preventDefault();
    if (!db) { formErr('Esta vista no tiene conexión con el calendario compartido.'); return; }
    var title = str($('f-title').value, 140), cat = $('f-cat').value, date = $('f-date').value, endDate = $('f-enddate').value;
    var allDay = $('f-allday').checked, start = $('f-start').value, end = $('f-end').value, k = priceKindSel(), amount = str($('f-amount').value, 120);
    var url = str($('f-url').value, 400);
    if (!title) return formErr('Falta el título.');
    if (!CATS[cat]) return formErr('Elige un tipo.');
    if (!isDate(date) || dn(date) < DAY0 || dn(date) > DAYZ) return formErr('Elige una fecha entre el 27 de septiembre y el 7 de noviembre.');
    if (endDate && (!isDate(endDate) || dn(endDate) < dn(date) || dn(endDate) > DAYZ)) return formErr('El último día debe ser igual o posterior a la fecha de inicio.');
    if (endDate && endDate !== date) allDay = true;
    if (!allDay) {
      if (!isTime(start)) return formErr('Falta la hora de inicio, o marca Todo el día.');
      if (end && (!isTime(end) || mins(end) <= mins(start))) return formErr('La hora de cierre debe ser posterior a la de inicio.');
    }
    if (EVENT_CATS[cat] && (!k || k === 'na')) return formErr('En un evento el precio es obligatorio: marca Gratis, De pago o Por confirmar.');
    if (!k) k = 'na';
    if (k === 'paid' && !amount) return formErr('Escribe el valor de la entrada, por ejemplo $495 por persona.');
    if (url && !safeUrl(url)) return formErr('El link debe empezar por https://');
    var by = $('f-by').value; lsSet('sfcal-by', by);
    var data = {v: 1, title: title, cat: cat, date: date, endDate: endDate && endDate !== date ? endDate : '', allDay: allDay,
      start: allDay ? '' : start, end: allDay ? '' : (end || ''), place: str($('f-place').value, 160),
      priceKind: k, price: k === 'paid' ? amount : k === 'free' ? 'Gratis' : '', url: safeUrl(url), note: str($('f-note').value, 600),
      by: by, base: !!(editId && baseById[editId]), at: new Date().toISOString()};
    var ref = editId ? db.collection('items').doc(editId) : db.collection('items').doc();
    $('f-save').disabled = true; formErr('');
    ref.set(data).then(function(){
      st.items[ref.id] = data;
      closeDlg(dForm); toast('Guardado');
      st.week = weekOf(dn(date)); render();
    }, function(err){ $('f-save').disabled = false; formErr(errMsg(err)); });
  });

  /* ---------- Base compartida ---------- */
  var db = null;
  function snapTo(target){
    return function(snap){
      var o = {};
      snap.docs.forEach(function(d){ var x = d.data(); if (x) { try { o[d.id] = JSON.parse(JSON.stringify(x)); } catch (e) {} } });
      st[target] = o; render();
      if (target === 'status' && dDetail.open && curId) { var it = findItem(curId); if (it) renderReg(it); }
    };
  }
  function lost(){ st.conn = 'none'; db = null; render(); }
  function connect(){
    if (!window.claude || typeof window.claude.use !== 'function') { st.conn = 'none'; render(); return; }
    window.claude.use('db').then(function(d){
      if (!d) { st.conn = 'none'; render(); return; }
      db = d; st.conn = 'ok'; render();
      try {
        d.collection('items').onSnapshot(snapTo('items'), lost);
        d.collection('status').onSnapshot(snapTo('status'), function(){});
      } catch (e) { lost(); }
    }, function(){ st.conn = 'none'; render(); });
    window.claude.use('user').then(function(u){
      if (!u || typeof u.can !== 'function') return;
      u.can('data.write').then(function(v){ if (v === false || v === true) { st.canWrite = v; render(); } });
    }, function(){});
  }

  /* ---------- Arranque ---------- */
  var startTab = (location.hash === '#calendar' || location.hash === '#interactive-calendar') ? 'calendar' : lsGet('sfcal-tab', 'playbook');
  showTab(startTab === 'calendar' ? 'calendar' : 'playbook');
  connect();
  setInterval(function(){ if (!panC.hidden && st.view === 'week' && !dDetail.open && !dForm.open) render(); }, 5 * 60 * 1000);
})();
