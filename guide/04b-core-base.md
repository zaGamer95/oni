---
title: 중앙 기지 배치도
nav_title: 중앙 기지 배치도
nav_order: 8
nav_group: early
permalink: /guide/core-base/
description: 한눈에 보는 전체 도면과 핵심 규칙. 방 크기, 통로, 단열 격벽·냉방·수조, 농장·목장·산업, 초반 전환, 교대 일정은 하위 페이지로 나눴어요.
nav_key: core-base
---

## 목표: 매일 하는 4가지를 가운데에

{: .ico-grid}
- {% include i.html n="Comfy_Bed" %} **침실** 매일 잠
- {% include i.html n="Shower" %} **샤워실** 매일 샤워
- {% include i.html n="Mess_Table" %} **식당** 매일 식사
- {% include i.html n="Lavatory" %} **화장실** 매일 볼일

네 방을 기지 **가운데에 붙이고**, 그 사이 사다리 통로를 **자연보호구역**으로 만들어 지나갈 때마다 사기 버프. 농장·목장·산업은 코어 밖.

## 핵심 규칙 3개

{: .ico-grid}
1. {% include i.html n="Tile" %} **층 = 내부 4 + 바닥 1**<br>세로 고정, 가로만 정함
2. {% include i.html n="Ladder" %} **서쪽 3칸 · 동쪽 2칸 통로**<br>식물 + 사다리 + 소방서 폴
3. {% include i.html n="Mesh_Tile" %} **방 가로 = 최대 크기 ÷ 4**<br>64 → 16, 96 → 24, 120 → 30

| 최대 크기 | 가로 × 세로 | 해당 방 |
|---|---|---|
| 64 | **16 × 4** | 화장실(세척실), 샤워실, 호화 막사, 식당, 마사지 클리닉 |
| 96 | **24 × 4** | 주방, 오락실, 병원, 발전소, 땅 동물 목장 |
| 120 | **30 × 4** 또는 **24 × 5** | 큰 회관(이 도면은 24×5 복층), 연회장, 연구실 |
| 자연보호구역 | **사다리 통로가 겸함** | 방 하나를 따로 안 쓰고, 침실과 코어 사이 서쪽 통로 전체를 보호구역으로 만듦 ([8-2 통로·동선]({{ '/guide/core-base/corridor/' | relative_url }})) |
| 개인 침실 | **6 × 4 = 24** | 최소 크기가 24라 딱 이 크기. 침대 1개짜리라 크게 지을 이유가 없음 |
| 온실·하늘 동물 목장 | 격자 밖 | 작물·동물 높이에 맞춘 **별도 블록** ([11 농장·목장·산업]({{ '/guide/core-base/blocks/' | relative_url }})) |

<details class="nums" markdown="1">
<summary>규격 이유 (층 높이·통로·벽)</summary>

| 규격 | 값 | 이유 |
|---|---|---|
| 층 높이 | 5칸 (내부 4 + 바닥 1) | 프린팅팟(Printing Pod)이 4×4, 호화 막사·개인 침실은 천장 4칸 조건 |
| 통로 | **서쪽 3칸 (식물 1 + 사다리 + 소방서 폴), 동쪽 2칸** | 올라갈 땐 사다리, 내려갈 땐 소방서 폴(내려가는 속도 4배). 식물 칸 덕에 통로가 그대로 자연보호구역 |
| 방 사이 벽 | 1칸 | 벽 칸은 방 크기에 안 들어감 |

</details>

## 후반 완성 배치도

<div class="bp-wrap" markdown="0">
{% include bp/core-base-late.svg %}
</div>
<p class="bp-legend">1칸 = 1타일. 위·왼쪽 눈금 = 칸 번호(5칸마다 굵은 선, 10칸마다 더 굵은 선), 노란 치수선 = 방 안쪽 칸 수(벽 제외), 노란 점선 = 단열 격벽. 아이콘은 실제 크기, 마우스를 올리면 이름.</p>

포드 위로 **샤워실 → 화장실 → 식당**을 세로로 쌓고(W 기존 가이드 방식), 격벽 안은 20~25°C, 밖은 발전소·SPOM·냉방실·오염된 물 수조.

<details class="nums" markdown="1">
<summary>코어 층별 크기와 들어가는 것</summary>

| 코어 층 (아래 → 위) | 크기 | 들어가는 것 |
|---|---|---|
| 예비 (포드 아래) | 24×4 = 96 | 병원 등 나중에 |
| 포드층 연구실 | 24×4 = 96 | 프린팅팟(Printing Pod) 4×4 + 연구소 + 슈퍼컴퓨터 |
| **샤워실** | 16×4 + 여유 7×4 | 샤워(Shower) 2×4 × 8대. 화장실과 같은 폐쇄 루프 |
| **화장실 (세척실)** | **16×3 = 48** + 옆 **기계실 7×3** | 싱크대 2 · 수세식 4 · 싱크대 2. 기계실에 물 체 + 모래 상자 + 갈대 (루프 넘침 처리) |
| 식당 → **복층 큰 회관** | **24×5 = 120** | 가운데 줄에 발판 타일, 위아래로 식탁 14 + 워터 쿨러(꺼 둠). 서쪽 통로 건너 주방 24×4 |
| 오락실 | 24×4 = 96 | 오락 건물 |

- **높이 4가 아닌 두 층:** 화장실은 건물 높이 3이라 3칸, 식당은 높이 5에 발판을 깔아 복층. 3 + 1 + 5 = 9칸 = 보통 층 두 개라 양옆 격자가 맞음.
- "세척실 (Washroom)"이 게임의 화장실 방 이름. 샤워는 한 번에 물 16 kg, 사기 +3 → 8명이면 하루 약 128 kg. 배관은 [폐쇄 루프]({{ '/guide/core-base/envelope/' | relative_url }}#화장실샤워실-폐쇄-루프).
- 환경 특수복 거치대는 침실이 아니라 **위험 지역으로 나가는 출구**에.

</details>

<details class="nums" markdown="1">
<summary>테라니아 적용 메모</summary>

- 포드가 맵 가운데 → 포드층이 코어 맨 아래, 바로 위 샤워실.
- 포드 오른쪽 아래 웅덩이 → 동쪽 아래 깨끗한 물 수조(격벽 안). 왼쪽 아래 웅덩이 → 격벽 밖 오염된 물 수조(외부 온실 관개).
- 발전소는 예비 층 아래 **격벽 밖**, 사이에 단열 바닥 ([발전소]({{ '/guide/core-base/power/' | relative_url }})).
- 8명 예산·역할·행성 진출은 [8명 중반 설계]({{ '/guide/midgame-8/' | relative_url }}).

</details>

## 세부 페이지

<ul class="sub-list">
  <li><a href="{{ '/guide/core-base/rooms/' | relative_url }}"><b>8-1 방 크기와 방 배치</b><span>방 종류별 크기 범위와 배치도 크기, 층별 방 배치, 한 방에 같이 두면 안 되는 조합.</span></a></li>
  <li><a href="{{ '/guide/core-base/corridor/' | relative_url }}"><b>8-2 사다리 통로와 하루 동선</b><span>가운데 사다리 통로를 자연보호구역으로 쓰는 법과 침실 → 화장실 → 식당 → 일 동선.</span></a></li>
  <li><a href="{{ '/guide/core-base/early/' | relative_url }}"><b>8-3 초반 배치·철거·확장</b><span>사이클 1~20 임시 배치, 초반 시설을 언제 뜯고 그 자리를 어떻게 쓰는지, 뜯지 않고 늘리는 규칙.</span></a></li>
  <li><a href="{{ '/guide/core-base/shifts/' | relative_url }}"><b>8-4 교대 일정 (휴식 시간 분리)</b><span>4교대로 휴식·취침 시간을 나눠 화장실·식탁·통로 혼잡을 줄이는 법과 시설 개수 기준.</span></a></li>
</ul>

이 배치도에 붙여 짓는 시설은 플레이 순서대로 따로 번호를 붙였어요.

<ul class="sub-list">
  <li><a href="{{ '/guide/food-early/' | relative_url }}"><b>9 식당·실내 온실</b><span>끼니나무 농장과 초반 식당, 실내 온실 규격.</span></a></li>
  <li><a href="{{ '/guide/core-base/power/' | relative_url }}"><b>10 초기 발전소 설계와 관리</b><span>석탄 발전기·배터리 배치, 와이어 등급과 회로, 스마트 배터리 자동화, 주둥가리 석탄, 업그레이드 순서.</span></a></li>
  <li><a href="{{ '/guide/core-base/blocks/' | relative_url }}"><b>11 농장·목장·산업 블록</b><span>격벽 안/밖에 둘 작물과 동물, 온실 규격, 목장 크기, 산업 블록.</span></a></li>
  <li><a href="{{ '/guide/core-base/refining/' | relative_url }}"><b>12 정제 금속 시작하기</b><span>쇄석기로 필요한 500 kg만 뽑기, 금속 제련소 연구·전력·냉각수·열 계산과 위치.</span></a></li>
  <li><a href="{{ '/guide/core-base/envelope/' | relative_url }}"><b>14 단열 격벽·냉방·수조</b><span>생활 구역을 단열 격벽으로 감싸 20~25°C로 유지하는 법, 냉방 시스템, 깨끗한 물·오염된 물 수조.</span></a></li>
  <li><a href="{{ '/guide/core-base/aircon/' | relative_url }}"><b>15 에어컨 설치</b><span>냉방실 14×4 도면, 열액체조화기·냉각 루프·18°C 온도 센서 설치 순서, 열 계산, 증기 터빈으로 열 지우기, 문제 해결.</span></a></li>
</ul>

<script>
(function(){var m={"방-크기-전체-표":"rooms","생활-구역-방-크기":"rooms","한-방에-같이-두면-안-되는-것-중첩-불가":"rooms","사다리-통로--자연보호구역":"corridor","하루-동선-침실--화장실--식당--일":"corridor","단열-격벽-안과-밖-나누기":"envelope","냉방-시스템":"envelope","수조":"envelope","작물-안에서-키울-것--밖에서-키울-것":"blocks","농장-규격":"blocks","목장-안--밖":"blocks","산업-블록-격벽-밖-동쪽":"blocks","초반-임시-배치-사이클-120-정도":"early","초반-시설-철거-시점과-그-자리-재활용":"early","확장-규칙-뜯지-않고-늘리기":"early","휴식-시간-분리-교대-일정":"shifts","실제-일정-예시-4교대":"shifts","왜-좋은가":"shifts","시설-개수-기준":"shifts","주의할-점":"shifts"};var h=decodeURIComponent(location.hash.slice(1));if(m[h]){location.replace("{{ '/guide/core-base/' | relative_url }}"+m[h]+"/#"+encodeURIComponent(h));}})();
</script>
