---
title: 홈
description: 산소미포함(Oxygen Not Included) 초반 생존 가이드. 게임 시작 설정부터 첫 100사이클까지.
---

<section class="banner">
  <img src="{{ '/assets/img/official/keyart.jpg' | relative_url }}" alt="Oxygen Not Included 공식 아트. 복제체들과 생물들이 우주를 떠다니는 그림." width="1016" height="314">
  <div class="banner-text">
    <h1>산소미포함 생존 노트</h1>
    <p>새 게임 설정부터 첫 100사이클까지, 순서대로 따라 하는 공략</p>
    <div class="banner-cta">
      <a class="btn rec" href="{{ '/start/#recommended' | relative_url }}">★ 초보 추천 설정으로 바로 시작</a>
      <a class="btn ghost" href="{{ '/start/' | relative_url }}">하나씩 골라보기</a>
    </div>
  </div>
</section>
<p class="credit right">이미지 © Klei Entertainment · 비공식 팬 가이드</p>

<section class="home-block">
  <h2 class="home-h2">지금 어디쯤이에요?</h2>
  <div class="where">
    <a class="where-card" href="{{ '/start/' | relative_url }}">
      <img src="{{ site.data.media.icons.cot }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
      <span><em>STEP 1</em><strong>게임 시작 전</strong><small>일반 / Spaced Out!, 모드, DLC, 행성 고르기</small></span>
    </a>
    <a class="where-card" href="{{ '/guide/first-cycles/' | relative_url }}">
      <img src="{{ site.data.media.icons.outhouse }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
      <span><em>STEP 2</em><strong>막 착륙했어요</strong><small>복제체 고르기, 첫 5사이클 체크리스트</small></span>
    </a>
    <a class="where-card" href="{{ '/guide/build-order/' | relative_url }}">
      <img src="{{ site.data.media.icons.coal_generator }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
      <span><em>STEP 3</em><strong>기지 키우는 중</strong><small>사진으로 보는 건설 순서, 바이옴 확장</small></span>
    </a>
    <a class="where-card" href="{{ '/guide/sustainability/' | relative_url }}">
      <img src="{{ site.data.media.icons.electrolyzer }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
      <span><em>STEP 4</em><strong>기지가 흔들려요</strong><small>산소·식량·전력·열 평형 + 계산기</small></span>
    </a>
  </div>
</section>

<section class="home-block">
  <h2 class="home-h2">로드맵</h2>
  <ol class="roadmap four">
    <li><i>1</i><b>극초반</b><small>사이클 1~20</small><span>화장실, 산소, 농장, 연구, 침실, 수조, 식당, 석탄 발전기</span></li>
    <li><i>2</i><b>초반</b><small>20~80</small><span>수트 스킬, 금속 정제, 전기분해기, 온도 관리, 간헐천</span></li>
    <li><i>3</i><b>중반</b><small>80~150</small><span>원유 바이옴, 지상 개통, 강철, 목장</span></li>
    <li><i>4</i><b>후반</b><small>150~</small><span>운석 대비, 우주 탐사, 로켓, 극후반 체제</span></li>
  </ol>
  <p class="home-more"><a href="{{ '/guide/build-order/' | relative_url }}">사진으로 보는 건설 순서 →</a></p>
</section>

<section class="home-block">
  <h2 class="home-h2">DLC</h2>
  <div class="dlc-grid">
    {% for d in site.data.media.dlc %}
    <a class="dlc" href="{{ d.store }}" target="_blank" rel="noopener">
      <img src="{{ d.header }}" alt="{{ d.name }} 대표 이미지" loading="lazy" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
      <span class="dlc-body"><strong>{{ d.kr }}</strong><em>{{ d.name }}{% if d.released != "" %} · {{ d.released }}{% endif %}</em><small>{{ d.summary }}</small></span>
    </a>
    {% endfor %}
  </div>
</section>

<section class="home-block">
  <h2 class="home-h2">참고 자료</h2>
  <div class="ref-links">
    <a href="{{ '/guide/build-specs/' | relative_url }}"><img src="{{ site.data.media.icons.farm_tile }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">건축 규격 &amp; 팁</a>
    <a href="{{ '/guide/sustainability/' | relative_url }}"><img src="{{ site.data.media.icons.hydrogen_generator }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">장기 평형 + 계산기</a>
    <a href="{{ '/guide/numbers/' | relative_url }}"><img src="{{ site.data.media.icons.smart_battery }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">수치 치트시트</a>
    <a href="{{ '/guide/biome-expansion/' | relative_url }}"><img src="{{ site.data.media.icons.water_sieve }}" alt="" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">바이옴 확장 타이밍</a>
  </div>
</section>
