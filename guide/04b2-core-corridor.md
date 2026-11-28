---
title: 사다리 통로와 하루 동선
nav_title: 통로·동선
nav_order: 8.2
nav_num: "8-2"
nav_group: early
nav_parent: core-base
permalink: /guide/core-base/corridor/
description: 침실과 코어 사이 사다리 통로를 자연보호구역으로 쓰는 법과 침실 → 화장실 → 식당 → 샤워 동선.
---

* 목차
{:toc}

> 전체 도면은 [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }}).
{: .tip}

## 사다리 통로 = 자연보호구역

자연보호구역은 **지나가기만 해도 사기 +6.** 방을 따로 두지 않고 **서쪽 통로 자체**를 보호구역으로.

<div class="bp-wrap" markdown="0">
{% include bp/core-corridor.svg %}
</div>
<p class="bp-legend">1칸 = 1타일. 위·왼쪽 눈금 = 칸 번호(5칸마다 굵은 선, 10칸마다 더 굵은 선), 노란 치수선 = 방 안쪽 칸 수(벽 제외). 건물·타일은 실제 크기의 인게임 아이콘이고, 아이콘에 마우스를 올리면 이름이 나와요.</p>

{: .ico-grid}
- {% include i.html n="Mirth_Leaf" %} **식물 칸** 1칸 (야생 식물)
- {% include i.html n="Ladder" %} **사다리 (Ladder)** 올라갈 때
- {% include i.html n="Fire_Pole" %} **소방서 폴 (Fire Pole)** 내려갈 때 4배 빠름
- {% include i.html n="Pneumatic_Door" %} **문** 층마다 양쪽, 통로를 독립 방으로

<details class="nums" markdown="1">
<summary>통로 규격 (크기·식물 수·금지 사항)</summary>

| 항목 | 값 | 설명 |
|---|---|---|
| 통로 폭 | **3칸** = 식물 1 + 사다리 1 + 소방서 폴 1 | 사다리·소방서 폴 칸에는 식물을 못 심어서 식물 칸을 하나 더 팜 |
| 방 경계 | 층마다 **양쪽 문** + 아래 끝 **가로 에어락** | 문도 방 경계라, 통로가 층 방들과 섞이지 않고 혼자 방 1개가 됨 |
| 크기 | 초반 3 × 21 ≈ **59칸** → 후반 격벽 안 3 × 30 ≈ **85칸** | 보호구역 32~120 안. 자연 타일 칸은 크기에서 빠짐 |
| 야생 식물 | 층 바닥 줄마다 1개 → **5개** (+ 매달린 식물) | 보호구역 조건 4개 이상 |
| 공원 표지판 | 1개 | 통로 어디든 |
| 금지 | 산업 기계 | 통로에 펌프·발전기·전해조 두지 않기 |

</details>

### 야생 식물 만드는 법

{: .ico-grid}
1. {% include i.html n="Dirt" %} **층 바닥 줄 흙 남기기**<br>자연 타일
2. **잎람쥐 (Pip)** 데려오기<br>씨앗을 주워 심음
3. {% include i.html n="Mealwood" %} **층마다 1개 → 5개**<br>끼니나무·센털꽃

화분·재배 타일은 야생이 아닙니다. 심을 동안만 통로 문을 잠가 잎람쥐를 가두세요.

> **초반엔 공원(+3), 나중에 보호구역(+6).** 통로가 64칸을 넘으면 공원 조건이 깨지니 그 전에 식물 4개. 잎람쥐가 없으면 원래 있던 야생 식물 옆에 작은 공원이 차선.
{: .warn}

## 하루 동선

{: .ico-grid}
1. {% include i.html n="Comfy_Bed" %} **침실** 서쪽 블록
2. {% include i.html n="Mirth_Leaf" %} **통로** 사기 +6
3. {% include i.html n="Lavatory" %} **화장실** 볼일 + 손 씻기
4. {% include i.html n="Mess_Table" %} **식당** 한 층 위
5. {% include i.html n="Shower" %} **샤워실** 화장실 아래
6. {% include i.html n="Research_Station" %} **출근** 연구실·온실·목장

어디서 어디로 가든 **서쪽 통로를 한 번은 지나니** 버프를 놓치는 복제체가 없습니다.
