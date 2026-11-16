#!/usr/bin/env python3
import json
W="/tmp/claude-0/-home-claude/7fc96507-fa1b-5efb-82ea-d26a70f1a1f1/scratchpad/work/"
CZ=open(W+"cz_data.json",encoding="utf-8").read()
SK=open(W+"sk_data.json",encoding="utf-8").read()

HTML=r'''<!DOCTYPE html>
<html lang="sk"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zubná dostupnosť — Česko a Slovensko</title>
<style>__CSS__</style>
<style>
:root{--ink:#0f1722;--panel:#141e2c;--panel2:#1b2836;--line:#2a3a4d;--text:#e8eef4;--muted:#93a4b5;--mint:#31c6a9;--coral:#ff6b5e;--amber:#f2b134;--blue:#3b82f6;--gold:#f5d76e}
*{box-sizing:border-box}
html,body{margin:0;height:100%;font-family:"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;background:var(--ink);color:var(--text)}
#top{min-height:58px;display:flex;align-items:center;gap:12px;padding:8px 14px;background:linear-gradient(180deg,#17222f,#121b27);border-bottom:1px solid var(--line);z-index:1200;position:relative;flex-wrap:wrap}
.brand{font-size:15px;font-weight:700;white-space:nowrap}.brand .tooth{color:var(--mint)}
.flags{display:flex;gap:6px}
.flag{display:flex;align-items:center;gap:7px;background:var(--panel2);border:1px solid var(--line);color:var(--text);border-radius:9px;padding:6px 12px;font-size:13px;cursor:pointer;transition:.15s;white-space:nowrap}
.flag .fi{font-size:17px;filter:grayscale(1) opacity(.55);transition:.15s}
.flag.on{border-color:var(--mint);background:rgba(49,198,169,.14);color:#fff}.flag.on .fi{filter:none}.flag:hover{border-color:var(--mint)}
.filters{display:flex;gap:9px;align-items:flex-end;flex-wrap:wrap;margin-left:auto}
.fgrp{display:flex;flex-direction:column;gap:2px}.fgrp label{font-size:9.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.fgrp select{background:var(--panel2);color:var(--text);border:1px solid var(--line);border-radius:7px;padding:4px 7px;font-size:12px;max-width:200px}
.fgrp.off{display:none}
.btn{background:var(--panel2);border:1px solid var(--line);color:var(--text);border-radius:8px;padding:6px 11px;font-size:12px;cursor:pointer;white-space:nowrap}
.btn:hover{border-color:var(--mint)}.btn.gold{border-color:rgba(245,215,110,.5);color:var(--gold)}
#app{display:flex;height:calc(100% - 58px)}
#side{width:360px;min-width:300px;background:linear-gradient(180deg,var(--panel),var(--ink));border-right:1px solid var(--line);overflow-y:auto;padding:16px 16px 28px;z-index:1000}
#map{flex:1;height:100%}
h1{font-size:16px;margin:0 0 2px;font-weight:700}
.sub{font-size:11.5px;color:var(--muted);margin-bottom:12px;line-height:1.5}
.bigrow{display:flex;gap:8px;margin:10px 0}
.stat{flex:1;background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:9px 10px}
.stat b{display:block;font-size:18px;color:var(--mint);font-variant-numeric:tabular-nums}.stat span{font-size:10.5px;color:var(--muted)}
h2{font-size:11.5px;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin:18px 0 7px;border-bottom:1px solid var(--line);padding-bottom:5px}
.okres{display:grid;grid-template-columns:128px 1fr 40px;align-items:center;gap:8px;font-size:11.5px;margin:4px 0}
.bar{height:8px;border-radius:4px;background:var(--panel2);overflow:hidden}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--blue),var(--mint))}
.okres .v{text-align:right;color:var(--muted);font-variant-numeric:tabular-nums}
.gap{font-size:12px;line-height:1.4;background:var(--panel2);border:1px solid var(--line);border-left:3px solid var(--coral);border-radius:8px;padding:8px 10px;margin:6px 0;cursor:pointer}
.gap:hover{border-color:var(--coral)}.gap b{color:var(--text)}.gap .m{color:var(--muted)}
.opp{border-left-color:var(--gold)}.opp:hover{border-color:var(--gold)}.opp .sc{float:right;color:var(--gold);font-weight:700;font-variant-numeric:tabular-nums}
.legend{font-size:12px;line-height:1.7;color:var(--muted)}.dot{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.grad{height:10px;border-radius:5px;background:linear-gradient(90deg,#2b6cff,#31c6a9,#f2e34c,#ff8c3a,#e63946);margin:6px 0 2px}
.gradlbl{display:flex;justify-content:space-between;font-size:10.5px;color:var(--muted)}
.note{font-size:10.5px;color:var(--muted);line-height:1.55;margin-top:16px;border-top:1px dashed var(--line);padding-top:10px}.note a{color:var(--mint)}
.leaflet-popup-content-wrapper{background:var(--panel);color:var(--text);border-radius:10px;border:1px solid var(--line)}
.leaflet-popup-tip{background:var(--panel)}
.leaflet-popup-content{margin:12px 14px;font-size:13px;line-height:1.5;max-width:300px}
.pp-title{font-size:15px;font-weight:700;margin-bottom:2px}.pp-sub{font-size:11px;color:var(--muted);margin-bottom:8px}
.pp-kv{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:12.5px;margin:6px 0}.pp-kv .k{color:var(--muted)}
.pp-badge{display:inline-block;font-size:11px;padding:2px 8px;border-radius:20px;margin:2px 4px 6px 0}
.b-good{background:rgba(49,198,169,.15);color:var(--mint);border:1px solid rgba(49,198,169,.4)}
.b-mid{background:rgba(242,177,52,.12);color:var(--amber);border:1px solid rgba(242,177,52,.4)}
.b-bad{background:rgba(255,107,94,.12);color:var(--coral);border:1px solid rgba(255,107,94,.4)}
.b-eco{background:rgba(245,215,110,.12);color:var(--gold);border:1px solid rgba(245,215,110,.4)}
.pp-list{max-height:170px;overflow-y:auto;margin-top:6px;border-top:1px solid var(--line);padding-top:6px}
.pp-d{padding:5px 0;border-bottom:1px dashed var(--line);font-size:12px}.pp-d b{font-weight:600}.pp-d a{color:var(--mint);text-decoration:none}.pp-d .adr{color:var(--muted);font-size:11px}
.ins{display:inline-block;font-size:10px;padding:1px 6px;border-radius:10px;border:1px solid var(--line);color:var(--muted);margin:2px 4px 0 0}.ins.y{color:var(--mint);border-color:rgba(49,198,169,.4)}
.leaflet-tooltip{background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:6px;font-size:12px;padding:3px 8px;box-shadow:0 2px 8px rgba(0,0,0,.35)}
.leaflet-tooltip-top:before{border-top-color:var(--line)}.leaflet-tooltip-bottom:before{border-bottom-color:var(--line)}
.leaflet-container{background:#dfe8ee;font:inherit;outline:none}.leaflet-interactive:focus{outline:none}
#burger{display:none;position:fixed;top:66px;left:10px;z-index:1100;background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:8px;padding:7px 11px}
@media(max-width:860px){#side{position:fixed;left:0;top:58px;bottom:0;width:88%;max-width:340px;transform:translateX(-102%);transition:transform .25s}#side.open{transform:none}#burger{display:block}.fgrp select{max-width:130px}}
</style></head>
<body>
<div id="top">
  <div class="brand"><span class="tooth">&#9678;</span> Zubná dostupnosť</div>
  <div class="flags">
    <button class="flag" id="f-CZ"><span class="fi">&#127464;&#127487;</span>Česko</button>
    <button class="flag" id="f-SK"><span class="fi">&#127480;&#127472;</span>Slovensko</button>
  </div>
  <div class="filters">
    <div class="fgrp"><label>Kraj</label><select id="f-kraj"></select></div>
    <div class="fgrp"><label>Špecializácia</label><select id="f-spec"></select></div>
    <div class="fgrp" id="g-ins"><label>Poisťovňa</label><select id="f-ins"><option value="all">všetky</option><option>VšZP</option><option>Dôvera</option><option>Union</option></select></div>
    <div class="fgrp"><label>Pokrytie obce</label><select id="f-cov"><option value="all">všetky obce</option><option value="0">bez zubára</option><option value="lo">pod 4 / 10 tis.</option><option value="hi">4+ / 10 tis.</option></select></div>
    <div class="fgrp"><label>Ekonomika okresu</label><select id="f-eco"></select></div>
    <button class="btn" id="b-xf" title="Stiahne len to, čo prešlo filtrami">⬇ Excel (filter)</button>
    <button class="btn" id="b-xa" title="Stiahne všetko pre aktívnu krajinu">⬇ Excel (všetko)</button>
  </div>
</div>
<button id="burger">☰ Prehľad</button>
<div id="app">
<aside id="side">
  <h1 id="s-title">—</h1><div class="sub" id="s-sub"></div>
  <div class="bigrow">
    <div class="stat"><b id="s-dent">—</b><span>zubných zariadení</span></div>
    <div class="stat"><b id="s-pop">—</b><span>obyvateľov</span></div>
    <div class="stat"><b id="s-avg">—</b><span>/ 10 tis. ob.</span></div>
  </div>
  <h2>Príležitosti na založenie ambulancie</h2>
  <div class="sub" style="margin-bottom:6px">Obce s nedostatkom zubárov, vážené ekonomickou úrovňou okresu (vyššie skóre = väčší potenciál). Klik = na mape.</div>
  <div id="opps"></div>
  <h2>Pokrytie podľa okresov</h2><div id="okresy"></div>
  <h2>Kde chýbajú zubári najviac</h2><div id="gaps"></div>
  <h2>Legenda</h2>
  <div class="legend">
    <div><span class="dot" style="background:var(--coral)"></span>obec / MČ bez zubára</div>
    <div><span class="dot" style="background:var(--amber)"></span>podpriemerné pokrytie (&lt; 4 / 10 tis.)</div>
    <div><span class="dot" style="background:var(--mint)"></span>priemerné a lepšie pokrytie</div>
    <div style="margin-top:6px">Teplotná mapa hustoty (pri oddialení):</div><div class="grad"></div><div class="gradlbl"><span>málo</span><span>veľa</span></div>
    <div style="margin-top:6px;font-size:11px">Veľkosť kruhu ≈ počet obyvateľov. Priblížením sa zobrazia jednotlivé ordinácie (zhluky).</div>
  </div>
  <div class="note" id="srcnote"></div>
</aside>
<div id="map"></div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.heat/0.2.0/leaflet-heat.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<script>
const CZ = __CZ__;
const SK = __SK__;
const KRN_CZ={JMK:'Jihomoravský',ZLK:'Zlínský',OLK:'Olomoucký',MSK:'Moravskoslezský',VYS:'Vysočina',PAK:'Pardubický',HKK:'Královéhradecký',LBK:'Liberecký',ULK:'Ústecký',KVK:'Karlovarský',JHC:'Jihočeský',PLK:'Plzeňský',STC:'Středočeský',PHA:'Praha'};
const C={
 CZ:{data:CZ,name:'Česko',flag:'🇨🇿',krn:KRN_CZ,hasIns:false,gapMin:1500,
     sub:'Všetky registrované miesta zubnej starostlivosti (NRPZS/ÚZIS) — 14 krajov, vrátane pražských obvodov a brnenských mestských častí.',
     src:'Zubári: NRPZS (ÚZIS). Obyvatelia: ČSÚ (per obec). Ekonomika okresov: kúpna sila / ceny bytov (orientačne, per okres). Podklad: Esri Light Gray.'},
 SK:{data:SK,name:'Slovensko',flag:'🇸🇰',krn:SK.krajNames,hasIns:true,gapMin:1000,
     sub:'Zubné ambulancie z oficiálneho registra e-VÚC — Žilinský, Trenčiansky, Trnavský a Banskobystrický kraj (ďalšie pribudnú).',
     src:'Zubári: register e-VÚC (odbor Zubné lekárstvo), stav 11/2026, s reálnou GPS, telefónom a zmluvnými poisťovňami. Obyvatelia: ŠÚ SR, SODB 2021. Ekonomika okresov: ÚPSVR — podiel disponibilných uchádzačov o zamestnanie (PDU), 09/2026, priemer SR 4,02 %. Podklad: Esri Light Gray.'}
};
const ECO_W={'nejvyšší v ČR':1.35,'nejvyšší v kraji':1.3,'vyšší (v rámci kraje)':1.2,'nadprůměrná':1.15,'průměrná':1.0,'mírně podprůměrná':0.85,'podprůměrná':0.7,'nejnižší v kraji':0.65,
             'vysoká':1.3,'nadpriemerná':1.15,'priemerná':1.0,'mierne podpriemerná':0.85,'podpriemerná':0.7};
let active='SK', F={kraj:'all',spec:'all',ins:'all',cov:'all',eco:'all'};
const map=L.map('map',{zoomSnap:0.5}).setView([49.4,17.5],7);
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',{attribution:'Tiles &copy; Esri',maxZoom:19,maxNativeZoom:16}).addTo(map);
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer/tile/{z}/{y}/{x}',{maxZoom:19,maxNativeZoom:16}).addTo(map);
const css=v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const fmt=n=>(n==null?'—':(''+Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,' '));
const esc=s=>(s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const covColor=p=>p<=0?css('--coral'):(p<4?css('--amber'):css('--mint'));
const badge=p=>p<=0?'<span class="pp-badge b-bad">bez zubnej ordinácie</span>':(p<4?`<span class="pp-badge b-mid">podpriemer (${p.toFixed(1)} / 10 tis.)</span>`:`<span class="pp-badge b-good">${p.toFixed(1)} / 10 tis. ob.</span>`);
const gmaps=(a,b)=>`https://www.google.com/maps?q=${a},${b}`;
// ---- keys: how a dentist maps to its municipality circle (Praha obvody + Brno MČ handled explicitly)
function dKey(code,d){ return code==='CZ' ? (d.mc?('mc:'+d.mc):('oc:'+d.oc)) : ('oid:'+d.oid); }
function oKey(code,o){ return code==='CZ' ? (o.mc?('mc:'+o.n):('oc:'+o.c)) : ('oid:'+o.id); }
function ecoOf(code,o){ return C[code].data.eco ? C[code].data.eco[o.ok] : null; }
function passEco(code,o){ if(F.eco==='all') return true; const e=ecoOf(code,o); return !!e && e.tier===F.eco; }
function filteredDent(code){
  const D=C[code].data;
  return D.dentists.filter(d=>{
    if(F.kraj!=='all' && d.kr!==F.kraj) return false;
    if(F.spec!=='all' && !((d.s||'').toLowerCase().includes(F.spec.toLowerCase()))) return false;
    if(code==='SK' && F.ins!=='all' && !((d.poi||'').toLowerCase().includes(F.ins.toLowerCase()))) return false;
    return true;
  });
}
let L_cluster=null,L_heat=null,L_obce=null,L_bound=null,L_ghost=null,lastOpp=[],lastDent=[];
function insBadges(poi){const p=(poi||'');return ['VšZP','Dôvera','Union'].map(x=>`<span class="ins ${p.toLowerCase().includes(x.toLowerCase())?'y':''}">${x}</span>`).join('');}
function dentPopup(code,d){
  let h=`<div class="pp-title">${esc(d.n)}</div><div class="pp-sub">${esc(d.s||'')}</div><div class="pp-kv">`;
  const adr=code==='CZ'?[d.u,(d.mc?d.mc+(d.mc.startsWith('Praha')?'':' (Brno)'):d.o)].filter(Boolean).join(', '):[d.u].filter(Boolean).join(', ');
  h+=`<span class="k">Adresa</span><span>${esc(adr)}</span>`;
  if(d.t) h+=`<span class="k">Telefón</span><span>${esc(d.t)}</span>`;
  if(d.e) h+=`<span class="k">E-mail</span><span>${esc(d.e)}</span>`;
  h+=`</div>`;
  if(code==='SK') h+=`<div style="font-size:11px;color:var(--muted)">Zmluvné poisťovne:</div><div>${insBadges(d.poi)}</div>`;
  const lk=[`<a class="gm" href="${gmaps(d.lat,d.lng)}" target="_blank" rel="noopener">Google Maps</a>`];
  if(d.w) lk.unshift(`<a href="${esc(d.w)}" target="_blank" rel="noopener">Web</a>`);
  if(d.det) lk.push(`<a href="${esc(d.det)}" target="_blank" rel="noopener">detail e-VÚC</a>`);
  return h+`<div style="margin-top:6px">${lk.join(' · ')}</div>`;
}
function dentItem(code,d){
  const adr=code==='CZ'?[d.u,(d.mc||d.o)].filter(Boolean).join(', '):(d.u||'');
  const links=[`<a href="${gmaps(d.lat,d.lng)}" target="_blank" rel="noopener">mapa</a>`];
  if(d.w) links.unshift(`<a href="${esc(d.w)}" target="_blank" rel="noopener">web</a>`);
  if(d.det) links.push(`<a href="${esc(d.det)}" target="_blank" rel="noopener">detail</a>`);
  if(d.t) links.push(esc(d.t));
  return `<div class="pp-d"><b>${esc(d.n)}</b><div class="adr">${esc(d.s||'')}</div><div class="adr">${esc(adr)}</div>${code==='SK'?`<div>${insBadges(d.poi)}</div>`:''}<div>${links.join(' · ')}</div></div>`;
}
function unitsOf(code){ // municipality-level units to draw: CZ obce(minus Brno)+Brno MČs ; SK obce
  const D=C[code].data;
  if(code==='CZ'){
    const u=D.obce.filter(o=>o.n!=='Brno').map(o=>({...o,key:oKey('CZ',o),isMC:!!o.mc,label:o.n.replace(/\s*\(.*?\)$/,'')}));
    D.mcs.forEach(m=>u.push({...m,ok:'Brno-město',kr:'JMK',key:'mc:'+m.n,isMC:true,label:m.n}));
    return u;
  }
  return D.obce.map(o=>({...o,key:oKey('SK',o),isMC:false,label:o.n}));
}
function render(){
  const code=active,Cn=C[code],D=Cn.data;
  [L_cluster,L_heat,L_obce,L_bound,L_ghost].forEach(l=>l&&map.removeLayer(l));
  const other=code==='CZ'?'SK':'CZ';
  L_ghost=L.geoJSON(C[other].data.kraj,{interactive:false,style:{color:'#8a9aab',weight:1.2,fill:true,fillColor:'#9aa7b4',fillOpacity:.07,opacity:.45,dashArray:'3 5'}}).addTo(map);
  L_bound=L.layerGroup().addTo(map);
  L.geoJSON(D.okresy,{interactive:false,style:{color:'#5b7288',weight:1.2,dashArray:'5 4',fill:false,opacity:.8}}).addTo(L_bound);
  L.geoJSON(D.kraj,{interactive:false,style:{color:css('--mint'),weight:2.4,fill:false,opacity:.9}}).addTo(L_bound);
  const dents=filteredDent(code); lastDent=dents;
  const cnt={}; dents.forEach(d=>{const k=dKey(code,d); cnt[k]=(cnt[k]||0)+1;});
  const byKey={}; dents.forEach(d=>{const k=dKey(code,d);(byKey[k]=byKey[k]||[]).push(d);});
  L_cluster=L.markerClusterGroup({maxClusterRadius:46,showCoverageOnHover:false});
  dents.forEach(d=>{ if(d.lat==null) return;
    const m=L.circleMarker([d.lat,d.lng],{radius:6,color:'#0e7d6b',weight:1.4,fillColor:css('--mint'),fillOpacity:.85});
    m.bindPopup(dentPopup(code,d),{maxWidth:300}); m.bindTooltip(d.n,{direction:'top',opacity:.95,offset:[0,-4]}); L_cluster.addLayer(m); });
  L_heat=L.heatLayer(dents.filter(d=>d.lat!=null).map(d=>[d.lat,d.lng,1]),{radius:26,blur:18,minOpacity:.25,maxZoom:11,gradient:{0.15:'#2b6cff',0.4:'#31c6a9',0.6:'#f2e34c',0.8:'#ff8c3a',1:'#e63946'}});
  L_obce=L.layerGroup();
  const units=unitsOf(code).filter(u=>F.kraj==='all'||u.kr===F.kraj);
  const avg=D.avg||{}; const opp=[];
  units.forEach(u=>{
    if(!passEco(code,u)) return;
    const d=cnt[u.key]||0, noPop=(u.p==null), p10=(!noPop&&u.p>0)?d/u.p*1e4:0;
    if(F.cov==='0'&&d!==0) return; if(F.cov==='lo'&&!(d>0&&p10<4)) return; if(F.cov==='hi'&&!(p10>=4)) return;
    const r=noPop?(d>0?Math.max(5,Math.min(14,4+d)):5):Math.max(5,Math.min(26,Math.sqrt(u.p)/9));
    const fill=noPop?(d>0?css('--mint'):css('--coral')):covColor(p10);
    const c=L.circleMarker([u.lat,u.lng],{radius:r,color:'#22303f',weight:1,fillColor:fill,fillOpacity:.62});
    const eco=ecoOf(code,u);
    let h=`<div class="pp-title">${esc(u.label)}</div><div class="pp-sub">${u.isMC?(u.label.startsWith('Praha')?'obvod Prahy':'mestská časť Brna')+' · ':''}okres ${esc(u.ok)} · ${esc(Cn.krn[u.kr]||u.kr)}</div>`;
    h+=noPop?(d>0?`<span class="pp-badge b-good">${d} zariadení</span>`:`<span class="pp-badge b-bad">bez ordinácie</span>`):badge(p10);
    if(eco) h+=`<span class="pp-badge b-eco">ekonomika: ${esc(eco.tier)}</span>`;
    h+=`<div class="pp-kv"><span class="k">Obyvateľov</span><span>${noPop?'— (údaj bude doplnený)':fmt(u.p)}</span><span class="k">Zubných zariadení</span><span>${d}</span>`;
    if(avg[u.kr]!=null) h+=`<span class="k">Priemer kraja</span><span>${avg[u.kr]} / 10 tis.</span>`;
    if(eco){ h+=`<span class="k">Ekonomika okresu</span><span>${esc(eco.tier)}${eco.pdu!=null?` (PDU ${eco.pdu.toFixed(2)} %)`:''}</span>`; }
    h+=`</div>`; if(eco&&eco.note) h+=`<div style="font-size:11px;color:var(--muted)">${esc(eco.note)}</div>`;
    const list=byKey[u.key]||[]; if(list.length) h+=`<div class="pp-list">${list.map(x=>dentItem(code,x)).join('')}</div>`;
    if(u.isMC&&!u.label.startsWith('Praha')) h+=`<div style="font-size:10.5px;color:var(--muted);margin-top:5px">Priradenie ordinácií k MČ je približné (najbližšie centrum MČ).</div>`;
    c.bindPopup(h,{maxWidth:310}); c.bindTooltip(noPop?`${esc(u.label)} · ${d} ord.`:`${esc(u.label)} · ${fmt(u.p)} ob. · ${d} ord.`,{direction:'top',opacity:.95,offset:[0,-4]});
    L_obce.addLayer(c);
    // opportunity score: underserved + populous + economically strong okres
    if(!noPop && u.p>=Cn.gapMin && (d===0 || p10<4)){
      const w=eco?(ECO_W[eco.tier]||1):1; const need=d===0?1:Math.max(0,(4-p10)/4);
      opp.push({u,d,p10,eco,score:Math.round(u.p*w*need/100)});
    }
  });
  lastOpp=opp.sort((a,b)=>b.score-a.score);
  refreshZoom(); sidebar(code,dents,cnt,units);
}
function refreshZoom(){const z=map.getZoom();
  if(z<10){if(!map.hasLayer(L_heat))map.addLayer(L_heat);if(map.hasLayer(L_cluster))map.removeLayer(L_cluster);if(!map.hasLayer(L_obce))map.addLayer(L_obce);}
  else{if(map.hasLayer(L_heat))map.removeLayer(L_heat);if(!map.hasLayer(L_obce))map.addLayer(L_obce);if(!map.hasLayer(L_cluster))map.addLayer(L_cluster);}}
map.on('zoomend',refreshZoom);
function sidebar(code,dents,cnt,units){
  const Cn=C[code],D=Cn.data;
  document.getElementById('s-title').textContent=Cn.flag+' '+Cn.name+(F.kraj!=='all'?' — '+(Cn.krn[F.kraj]||F.kraj):'');
  document.getElementById('s-sub').textContent=Cn.sub;
  const totD=dents.length;
  let totP=0; const seenOk={};
  if(code==='CZ'){ D.obce.filter(o=>F.kraj==='all'||o.kr===F.kraj).forEach(o=>totP+=(o.p||0)); }
  else { Object.entries(D.krajPop).forEach(([k,v])=>{ if(F.kraj==='all'||k===F.kraj) totP+=v; }); }
  document.getElementById('s-dent').textContent=fmt(totD);
  document.getElementById('s-pop').textContent=totP>=1e6?(totP/1e6).toFixed(2)+' mil.':fmt(totP);
  document.getElementById('s-avg').textContent=totP?(totD/totP*1e4).toFixed(1):'—';
  // okres coverage (filtered dentists / okres pop)
  const ok={};
  units.forEach(u=>{ok[u.ok]=ok[u.ok]||{p:0,d:0}; ok[u.ok].p+=(u.p||0); ok[u.ok].d+=(cnt[u.key]||0);});
  if(D.okpop) Object.entries(D.okpop).forEach(([k,v])=>{ if(ok[k]) ok[k].p=v; });
  const arr=Object.entries(ok).filter(([k,v])=>v.p>0).map(([k,v])=>({k,per:v.d/v.p*1e4,eco:(D.eco||{})[k]})).sort((a,b)=>b.per-a.per);
  const mx=Math.max(...arr.map(a=>a.per),0.1);
  document.getElementById('okresy').innerHTML=arr.map(o=>`<div class="okres" title="${o.eco?esc(o.eco.tier):''}"><span>${esc(o.k)}</span><span class="bar"><i style="width:${(o.per/mx*100).toFixed(0)}%"></i></span><span class="v">${o.per.toFixed(1)}</span></div>`).join('')+`<div style="font-size:10px;color:var(--muted);margin-top:3px">zariadení na 10 000 obyvateľov${(F.spec!=='all'||F.ins!=='all')?' (filtrované)':''}</div>`;
  // opportunities
  document.getElementById('opps').innerHTML=lastOpp.slice(0,15).map(o=>`<div class="gap opp" data-lat="${o.u.lat}" data-lng="${o.u.lng}"><span class="sc">${o.score}</span><b>${esc(o.u.label)}</b> <span class="m">· okres ${esc(o.u.ok)} · ${fmt(o.u.p)} ob., ${o.d} ord.${o.eco?' · ekonomika: '+esc(o.eco.tier):''}</span></div>`).join('')||'<div class="sub">Žiadne obce nespĺňajú kritériá pri aktuálnych filtroch.</div>';
  // gaps
  const gaps=units.filter(u=>u.p!=null&&u.p>=Cn.gapMin&&(cnt[u.key]||0)===0&&passEco(code,u)).sort((a,b)=>b.p-a.p);
  document.getElementById('gaps').innerHTML=gaps.slice(0,14).map(g=>`<div class="gap" data-lat="${g.lat}" data-lng="${g.lng}"><b>${esc(g.label)}</b> <span class="m">· okres ${esc(g.ok)} · ${fmt(g.p)} ob., 0 ord.</span></div>`).join('')+`<div style="font-size:10px;color:var(--muted);margin-top:3px">Spolu ${gaps.length} obcí nad ${fmt(Cn.gapMin)} ob. bez zubára.</div>`;
  document.querySelectorAll('.gap').forEach(el=>el.onclick=()=>{map.setView([+el.dataset.lat,+el.dataset.lng],13);document.getElementById('side').classList.remove('open');});
  document.getElementById('srcnote').innerHTML=Cn.src+(code==='SK'&&D.ecoMeta?` Zdroj ekonomiky: ${esc(D.ecoMeta.source)}, ${esc(D.ecoMeta.month)}.`:'')+' Skóre príležitosti = obyvatelia × váha ekonomiky okresu × miera nedostatku (0 ordinácií = plná).';
}
function fillSelects(){
  const Cn=C[active],D=Cn.data;
  const kr=document.getElementById('f-kraj'); const krs=Object.keys(Cn.krn).filter(k=>D.dentists.some(d=>d.kr===k)||D.obce.some(o=>o.kr===k));
  kr.innerHTML=`<option value="all">všetky kraje</option>`+krs.map(k=>`<option value="${k}">${esc(Cn.krn[k])}</option>`).join('');
  const set={}; D.dentists.forEach(d=>(d.s||'').split(',').forEach(x=>{x=x.trim();if(x)set[x]=(set[x]||0)+1;}));
  document.getElementById('f-spec').innerHTML=`<option value="all">všetky</option>`+Object.entries(set).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`<option value="${esc(k)}">${esc(k)} (${v})</option>`).join('');
  const tiers={}; Object.values(D.eco||{}).forEach(e=>{tiers[e.tier]=(tiers[e.tier]||0)+1;});
  document.getElementById('f-eco').innerHTML=`<option value="all">všetky úrovne</option>`+Object.entries(tiers).sort((a,b)=>(ECO_W[b[0]]||1)-(ECO_W[a[0]]||1)).map(([k,v])=>`<option value="${esc(k)}">${esc(k)} (${v} okr.)</option>`).join('');
  document.getElementById('g-ins').classList.toggle('off',!Cn.hasIns);
}
function setCountry(code){
  active=code; F={kraj:'all',spec:'all',ins:'all',cov:'all',eco:'all'};
  ['f-ins','f-cov'].forEach(id=>document.getElementById(id).value='all');
  document.getElementById('f-CZ').classList.toggle('on',code==='CZ'); document.getElementById('f-SK').classList.toggle('on',code==='SK');
  fillSelects(); map.fitBounds(L.geoJSON(C[code].data.kraj).getBounds(),{padding:[20,20]}); render();
}
// ---- Excel export
function exportXlsx(all){
  const code=active,Cn=C[code],D=Cn.data;
  const rows=(all?D.dentists:lastDent).map(d=>{
    const base={Krajina:Cn.name,Kraj:Cn.krn[d.kr]||d.kr,Okres:d.ok||(unitsOf(code).find(u=>u.key===dKey(code,d))||{}).ok||'',Obec:d.mc||d.o||'',Názov:d.n,Adresa:d.u||'',Špecializácia:d.s||'',Telefón:d.t||''};
    if(code==='CZ'){base['E-mail']=d.e||'';base['Web']=d.w||'';} else {base['Poisťovne']=d.poi||'';}
    base['Lat']=d.lat;base['Lng']=d.lng;base['Google Maps']=d.lat!=null?gmaps(d.lat,d.lng):'';if(d.det)base['Detail (e-VÚC)']=d.det;
    return base;});
  const ws=XLSX.utils.json_to_sheet(rows); const wb=XLSX.utils.book_new(); XLSX.utils.book_append_sheet(wb,ws,'Zubári');
  // second sheet: municipalities coverage (filtered units)
  const units=unitsOf(code).filter(u=>all||F.kraj==='all'||u.kr===F.kraj); const cnt={}; (all?D.dentists:lastDent).forEach(d=>{const k=dKey(code,d);cnt[k]=(cnt[k]||0)+1;});
  const urows=units.map(u=>{const d=cnt[u.key]||0,e=ecoOf(code,u);return {Kraj:Cn.krn[u.kr]||u.kr,Okres:u.ok,Obec:u.label,Obyvateľov:u.p,'Zubných zariadení':d,'Na 10 tis.':u.p?+(d/u.p*1e4).toFixed(2):'', 'Ekonomika okresu':e?e.tier:'', 'PDU %':e&&e.pdu!=null?e.pdu:''};});
  XLSX.utils.book_append_sheet(wb,XLSX.utils.json_to_sheet(urows),'Obce - pokrytie');
  const tag=all?'vsetko':'filter'; XLSX.writeFile(wb,`zubari-${code.toLowerCase()}-${tag}.xlsx`);
}
document.getElementById('f-CZ').onclick=()=>setCountry('CZ'); document.getElementById('f-SK').onclick=()=>setCountry('SK');
['kraj','spec','ins','cov','eco'].forEach(k=>document.getElementById('f-'+k).onchange=e=>{F[k]=e.target.value;render();});
document.getElementById('b-xf').onclick=()=>exportXlsx(false); document.getElementById('b-xa').onclick=()=>exportXlsx(true);
document.getElementById('burger').onclick=()=>document.getElementById('side').classList.toggle('open');
setCountry('SK');
</script></body></html>'''
import pathlib
B="/tmp/claude-0/-home-claude/7fc96507-fa1b-5efb-82ea-d26a70f1a1f1/scratchpad/work/npmcss/x/package/dist/"
CSS="".join(open(B+f,encoding="utf-8").read() for f in ["leaflet.css","MarkerCluster.css","MarkerCluster.Default.css"])
out=HTML.replace("__CSS__",CSS).replace("__CZ__",CZ).replace("__SK__",SK)
open("/mnt/user-data/outputs/zubari-cesko-slovensko.html","w",encoding="utf-8").write(out)
print("written bytes:",len(out))
