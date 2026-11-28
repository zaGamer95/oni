---
title: "부록 B: 공식 한글 용어집"
nav_title: 공식 한글 용어집
nav_order: 41
nav_num: "B"
nav_group: appendix
eyebrow: 부록 B
permalink: /appendix/glossary/
description: "게임에 들어 있는 Klei 공식 한국어 번역에서 뽑은 이름 1,800여 개. 한글이나 영어 어느 쪽으로도 찾을 수 있습니다."
---

이 사이트의 이름은 모두 **게임 공식 한국어판** 표기를 따르고, `한글 (English)`로 같이 씁니다. 영어 UI로 하든 한글 UI로 하든 아래에서 바로 찾아보세요.

> 출처: 게임 설치 폴더의 `strings_preinstalled_ko_klei.po` (빌드 {{ site.data.glossary_ko._source.build }}), 이름 {{ site.data.glossary_ko._source.terms }}개. 번역이 어색해도 게임 표기 그대로 둡니다. "같은 영어, 다른 번역"은 게임 안에서도 두 가지로 나오는 경우예요.
{: .tip}

<div class="gl-wrap" markdown="0">
<div class="gl-bar">
  <input id="gl-q" type="search" placeholder="한글 또는 English로 찾기 (예: 기끌이, Drecko)" autocomplete="off">
  <select id="gl-cat">
    <option value="">전체</option>
    <option value="critter">생물·식물</option><option value="seed">씨앗</option><option value="geyser">분출구</option>
    <option value="building">건물</option><option value="element">원소</option><option value="item">아이템·음식</option>
    <option value="equipment">장비</option><option value="skill">스킬</option><option value="skill_group">관심 분야</option>
    <option value="chore_group">작업 종류</option><option value="attribute">능력치</option><option value="trait">특성</option>
    <option value="disease">질병</option><option value="research">연구</option><option value="room">방</option>
    <option value="world_trait">월드 특성</option><option value="subworld">바이옴</option><option value="world">소행성</option>
    <option value="cluster">클러스터</option><option value="robot">로봇</option>
  </select>
  <span id="gl-n"></span>
</div>
<table class="gl-table">
<thead><tr><th>한글</th><th>English</th><th>분류</th></tr></thead>
<tbody id="gl-body">
{%- assign cats = "critter:생물·식물,seed:씨앗,geyser:분출구,building:건물,element:원소,item:아이템·음식,equipment:장비,skill:스킬,skill_group:관심 분야,chore_group:작업 종류,attribute:능력치,trait:특성,disease:질병,research:연구,room:방,world_trait:월드 특성,subworld:바이옴,world:소행성,cluster:클러스터,robot:로봇,story_trait:스토리 특성" | split: "," -%}
{%- for t in site.data.glossary_ko -%}
{%- assign en = t[0] -%}{%- assign d = t[1] -%}
{%- if en == "_source" -%}{%- continue -%}{%- endif -%}
{%- assign label = d.cat -%}
{%- for c in cats -%}{%- assign kv = c | split: ":" -%}{%- if kv[0] == d.cat -%}{%- assign label = kv[1] -%}{%- endif -%}{%- endfor %}
<tr data-c="{{ d.cat }}"><td>{{ d.ko }}{% if d.also %} <small>({{ d.also | join: ", " }})</small>{% endif %}</td><td>{{ en }}</td><td>{{ label }}</td></tr>
{%- endfor %}
</tbody>
</table>
</div>

<style>
.gl-bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:12px 0;position:sticky;top:0;background:var(--bg,#fff);padding:8px 0;z-index:2}
.gl-bar input{flex:1 1 220px;min-width:0;padding:8px 10px;font-size:16px;border:1px solid #9994;border-radius:6px;background:transparent;color:inherit}
.gl-bar select{padding:8px;font-size:15px;border:1px solid #9994;border-radius:6px;background:transparent;color:inherit}
#gl-n{font-size:13px;opacity:.7}
.gl-table{width:100%;border-collapse:collapse;font-size:15px}
.gl-table th,.gl-table td{padding:5px 8px;border-bottom:1px solid #9993;text-align:left;vertical-align:top}
.gl-table td:nth-child(3){font-size:13px;opacity:.7;white-space:nowrap}
.gl-table small{opacity:.7}
</style>
<script>
(function(){
  var q=document.getElementById('gl-q'), c=document.getElementById('gl-cat'), n=document.getElementById('gl-n');
  var rows=[].slice.call(document.querySelectorAll('#gl-body tr'));
  rows.forEach(function(r){ r._t=r.textContent.toLowerCase(); });
  function run(){
    var s=q.value.trim().toLowerCase(), k=c.value, shown=0;
    rows.forEach(function(r){ var ok=(!k||r.dataset.c===k)&&(!s||r._t.indexOf(s)>=0); r.style.display=ok?'':'none'; if(ok)shown++; });
    n.textContent=shown+'개';
  }
  q.addEventListener('input',run); c.addEventListener('change',run);
  var h=decodeURIComponent(location.hash.slice(1)); if(h){ q.value=h; }
  run();
})();
</script>
