---
title: 게임 시작 설정
nav_title: 게임 시작 설정
nav_order: 1
nav_group: start
permalink: /start/
description: 새 게임을 만들 때 고르는 순서 그대로. 모르겠으면 ★추천만 누르면 됩니다.
---

<div class="wz" id="wizard">

  <div class="wz-top">
    <ol class="wz-progress" aria-label="진행 단계">
      <li data-goto="1"><b>1</b><span>게임 모드</span></li>
      <li data-goto="2"><b>2</b><span>모드(Mod)</span></li>
      <li data-goto="3"><b>3</b><span>DLC</span></li>
      <li data-goto="4"><b>4</b><span>행성</span></li>
      <li data-goto="5"><b>✓</b><span>결과</span></li>
    </ol>
    <button type="button" class="btn primary wz-all-rec" data-allrec>★ 전부 추천으로 바로 보기</button>
  </div>

  <!-- STEP 1 -->
  <section class="wz-step" data-step="1">
    <h2>1. 일반으로 할까, Spaced Out!으로 할까?</h2>
    <p class="wz-lead">Spaced Out! DLC가 있으면 메인 메뉴에서 켜고 끌 수 있어요. 켜면 여러 소행성을 오가는 '성단' 맵으로, 끄면 큰 소행성 하나에서 시작합니다.</p>
    <div class="wz-opts">
      <button type="button" class="wz-opt" data-value="base" data-label="일반 (기본 게임)" data-rec>
        <span class="rec">★ 추천</span>
        <strong>일반 (기본 게임)</strong>
        <small>큰 소행성 하나. 자원이 넉넉하고 구조가 단순해서 첫 판에 좋아요. 이 가이드도 이 기준입니다.</small>
      </button>
      <button type="button" class="wz-opt" data-value="so" data-label="Spaced Out!">
        <strong>Spaced Out!</strong>
        <small>작은 소행성 여러 개. 시작 행성 자원이 빨리 떨어지는 대신 로켓으로 일찍 옆 행성에 갑니다. 방사능, 원자력 추가. 두 번째 판부터 추천.</small>
      </button>
    </div>
  </section>

  <!-- STEP 2 -->
  <section class="wz-step" data-step="2">
    <h2>2. 어떤 모드(Mod)를 켤까?</h2>
    <p class="wz-lead">메인 메뉴 → 모드(Mods)에서 켭니다. 게임 업데이트 직후에는 모드가 깨질 수 있으니 첫 판은 가볍게 가세요.</p>
    <div class="wz-opts">
      <button type="button" class="wz-opt" data-value="vanilla" data-label="모드 없이" data-rec>
        <span class="rec">★ 추천</span>
        <strong>모드 없이 시작</strong>
        <small>업데이트로 깨질 걱정이 없고, 가이드 화면과 똑같이 보입니다.</small>
      </button>
      <button type="button" class="wz-opt" data-value="qol" data-label="편의 모드만">
        <strong>편의 모드만</strong>
        <small>게임 밸런스는 그대로 두고 불편한 것만 고치는 모드. 아래 목록 참고.</small>
      </button>
    </div>

    <details class="wz-more">
      <summary>밸런스를 바꾸지 않는 편의 모드 목록</summary>

      <table>
        <thead><tr><th>모드</th><th>하는 일</th></tr></thead>
        <tbody>
          <tr><td>Mod Updater</td><td>스팀이 옛 버전으로 남겨둔 모드를 최신으로 갱신. 모드를 쓴다면 제일 먼저.</td></tr>
          <tr><td>Stock Bug Fix</td><td>기본 게임 버그 여러 개 수정</td></tr>
          <tr><td>Research Queue</td><td>연구를 여러 개 예약</td></tr>
          <tr><td>Show Building Ranges</td><td>건물 효과 범위 표시</td></tr>
          <tr><td>Fast Save</td><td>저장·불러오기 속도 향상</td></tr>
          <tr><td>Falling Sand</td><td>무너지는 모래·흙을 자동으로 굴착 예약</td></tr>
          <tr><td>Efficient Supply</td><td>자잘한 운반 작업 최적화</td></tr>
          <tr><td>Mismatched Wire Finder</td><td>잘못 연결된 와이어·파이프 찾기</td></tr>
          <tr><td>Pliers</td><td>와이어·파이프를 철거하지 않고 연결만 끊기</td></tr>
          <tr><td>Blueprints</td><td>방 배치를 저장해서 재사용</td></tr>
        </tbody>
      </table>

      <p>위 8개 중 앞쪽 대부분은 Peter Han이 관리하는 모드 묶음입니다. 마지막 확인 버전이 U59라서, 최신 게임에서 돌아가는지는 Mod Updater로 먼저 확인하세요.</p>
      <p><b>첫 판에 피할 모드:</b> 맵 생성을 바꾸는 모드(Extra Large Map, Generate More Geysers), 공짜 전력·시작 스탯 조작 같은 치트성 모드.</p>
    </details>
  </section>

  <!-- STEP 3 -->
  <section class="wz-step" data-step="3">
    <h2>3. DLC 콘텐츠를 켤까?</h2>
    <p class="wz-lead">새 게임을 만들 때 가진 DLC의 콘텐츠를 섞을지 고릅니다. DLC마다 전용 시작 행성이 있고, 다른 행성에 생물이나 바이옴을 섞을 수도 있어요.</p>
    <div class="wz-opts">
      <button type="button" class="wz-opt" data-value="off" data-label="DLC 콘텐츠 끄기" data-rec>
        <span class="rec">★ 추천</span>
        <strong>끄고 시작</strong>
        <small>기본 바이옴만. 처음 배울 게 가장 적습니다. 익숙해지면 하나씩 켜세요.</small>
      </button>
      <button type="button" class="wz-opt" data-value="on" data-label="DLC 콘텐츠 켜기">
        <strong>켜고 시작</strong>
        <small>새 생물, 바이옴, 건물이 섞여 나옵니다. 두 번째 판부터 추천.</small>
      </button>
    </div>

    <div class="dlc-grid">
      {% for d in site.data.media.dlc %}
      <a class="dlc" href="{{ d.store }}" target="_blank" rel="noopener">
        <img src="{{ d.header }}" alt="{{ d.name }} 대표 이미지" loading="lazy" referrerpolicy="no-referrer" data-fallback onerror="this.classList.add('img-missing')">
        <span class="dlc-body"><strong>{{ d.kr }}</strong><em>{{ d.name }}{% if d.released != "" %} · {{ d.released }}{% endif %}</em><small>{{ d.summary }}</small></span>
      </a>
      {% endfor %}
    </div>
    <p class="credit">DLC 이미지: Steam 상점 · © Klei Entertainment</p>
  </section>

  <!-- STEP 4 -->
  <section class="wz-step" data-step="4">
    <h2>4. 어떤 행성에서 시작할까?</h2>
    <p class="wz-lead">시작 행성마다 난이도가 크게 다릅니다. 자세한 비교와 행성별 첫 행동은 <a href="{{ '/guide/asteroids/' | relative_url }}">행성 고르기</a>에 있어요.</p>
    <div class="wz-opts three">
      <button type="button" class="wz-opt" data-value="terra" data-label="테라 (Terra)" data-rec>
        <span class="rec">★ 추천</span>
        <strong>테라 (Terra)</strong>
        <small>★☆☆☆☆ 표준 맵. 필요한 바이옴이 다 있고 극단적인 위험이 없어요.</small>
      </button>
      <button type="button" class="wz-opt" data-value="oceania" data-label="오세아니아 (Oceania)">
        <strong>오세아니아 (Oceania)</strong>
        <small>★☆☆☆☆ 테라 + 소금물. 물 걱정이 덜함.</small>
      </button>
      <button type="button" class="wz-opt" data-value="rime" data-label="라임 (Rime)">
        <strong>라임 (Rime)</strong>
        <small>★★☆☆☆ 전체가 추움. 냉각은 쉽고 농사가 까다로움.</small>
      </button>
      <button type="button" class="wz-opt" data-value="verdante" data-label="베르단테 (Verdante)">
        <strong>베르단테 (Verdante)</strong>
        <small>★★☆☆☆ 숲 시작, 자원 풍부, 냉각원 부족.</small>
      </button>
      <button type="button" class="wz-opt" data-value="hard" data-label="고난도 행성">
        <strong>고난도 (아르보리아~오아시스)</strong>
        <small>★★★ 이상. 익숙해진 뒤에 도전.</small>
      </button>
      <button type="button" class="wz-opt" data-value="dlc-planet" data-label="DLC 전용 행성">
        <strong>DLC 행성</strong>
        <small>세레스(서리), 렐리카·마리네아(선사) 등. 해당 DLC를 켰을 때만.</small>
      </button>
    </div>
  </section>

  <!-- RESULT -->
  <section class="wz-step" data-step="5" id="result">
    <h2>내 시작 설정</h2>
    <ul class="wz-summary" id="wz-summary">
      <li><span>게임 모드</span><b data-sum="1">일반 (기본 게임)</b></li>
      <li><span>모드</span><b data-sum="2">모드 없이</b></li>
      <li><span>DLC</span><b data-sum="3">DLC 콘텐츠 끄기</b></li>
      <li><span>행성</span><b data-sum="4">테라 (Terra)</b></li>
    </ul>
    <p class="wz-note" id="wz-note"></p>
    <div class="wz-next">
      <a class="btn primary" href="{{ '/guide/first-cycles/' | relative_url }}">다음: 복제체 고르고 첫 5사이클 →</a>
      <a class="btn ghost" href="{{ '/guide/asteroids/' | relative_url }}">행성별 첫 행동 보기</a>
    </div>
  </section>

  <div class="wz-nav">
    <button type="button" class="btn ghost" data-prev>← 이전</button>
    <button type="button" class="btn rec" data-rec-step>★ 추천 고르고 다음</button>
    <button type="button" class="btn primary" data-next>다음 →</button>
  </div>
</div>
