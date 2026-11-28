---
title: 시작 직후 체크리스트 (사이클 1~5)
nav_title: 첫 5사이클 체크리스트
nav_order: 5
nav_group: early
permalink: /guide/first-cycles/
description: 어떤 지형에서 시작하든 공통으로 먼저 해야 할 일. 지형별 차이는 02에서 다룹니다.
---

> 새 게임을 아직 안 만들었다면 [게임 시작 설정]({{ '/start/' | relative_url }})부터.

## 핵심 원칙

1. **사이클 1 연구스테이션, 사이클 2 화장실.**
2. **위아래보다 옆으로** 넓히기 (시작 바이옴 안 3~4층).
3. **뜨거운 건물은 한 구역에** 모으기.
4. **물은 순환:** 화장실 → 오염된 물 → 물 체 → 물.
5. **복제체 추가는 마지막:** 산소·식량이 1명분 남을 때만.

* 목차
{:toc}

## 시작 전: 복제체 3명

> **연구 / 굴착 / 농사·목축** 1명씩. 관심 분야 겹치지 않게, Destructive·Binge Eater 스트레스 반응은 리롤. 자세히는 [복제체 고르기]({{ '/guide/duplicants/' | relative_url }}).
{: .tip}

## 사이클 1: 연구와 공간

{: .ico-grid}
1. {% include i.html n="Research_Station" %} **연구스테이션 (Research Station)** 가장 먼저. 전기 불필요
2. {% include i.html n="Printing_Pod" %} **좌우로 파기** 위아래로 깊게 파면 위험 바이옴이 열림
3. {% include i.html n="Manual_Generator" %} **수동 발전기 (Manual Generator)** 연구스테이션 다음
4. {% include i.html n="Battery" %} **배터리 (Battery)** 발전기 옆에 1개

우선순위(Priorities) 화면에서 연구 담당은 연구, 나머지는 굴착·건설을 높게. 연구 대기열은 식량 → 전력 → 파이프 → 환기 ([연구 순서]({{ '/guide/research/' | relative_url }})).

{: .ico-grid}
- {% include i.html n="Algae" %} **조류 (Algae)** 초반 산소
- {% include i.html n="Water" %} **물 (Water)** 화장실·세면
- {% include i.html n="Dirt" %} **흙 (Dirt)** 끼니나무 비료

위 세 자원의 위치를 기억해 두세요.

## 사이클 2: 화장실과 잠자리

{: .ico-grid}
- {% include i.html n="Outhouse" %} **뒷간 (Outhouse)** ×4
- {% include i.html n="Wash_Basin" %} **세면기 (Wash Basin)** ×4, 나가는 길목에
- {% include i.html n="Pitcher_Pump" %} **피처 펌프 (Pitcher Pump)** 물웅덩이에 1개
- {% include i.html n="Cot" %} **간이침대 (Cot)** 복제체 수만큼
- {% include i.html n="Ration_Box" %} **배급 상자 (Ration Box)** 식당 쪽 1개

> 화장실이 없으면 바닥에 볼일을 봅니다. 오염된 물 + 식중독 병균. **사이클 2 안에.** 배치 사진은 [건설 순서]({{ '/guide/build-order/' | relative_url }}).
{: .warn}

<details class="nums" markdown="1">
<summary>상세 수치</summary>

- 화장실 구역: 바닥 18칸에 뒷간 4 + 세면기 4. 처음부터 이 크기로 지으면 다시 지을 일이 없음.
- 사이클 1개 = 600초.
</details>

## 사이클 2~3: 식량

{: .ico-grid}
- {% include i.html n="Mealwood" %} **끼니나무 (Mealwood)** 1명당 5그루
- {% include i.html n="Planter_Box" %} **재배 박스 (Planter Box)** 또는 재배 타일 (Farm Tile)
- {% include i.html n="Microbe_Musher" %} **미생물 걸죽기 (Microbe Musher)** 이빵 (Liceloaf)으로 만들면 1명당 4그루. 걸죽바는 비상용

야생 식물은 씨앗용으로 남겨 두기.

<details class="nums" markdown="1">
<summary>상세 수치</summary>

| 항목 | 값 |
|---|---|
| 끼니나무 1그루 | 3사이클마다 600 kcal (하루 200 kcal) |
| 복제체 1명 | 하루 1000 kcal |
| 비료 | 흙 (Dirt) |
| 걸죽바 (Mush Bar) | 흙 + 물, 맛이 없어 사기 하락 |

</details>

## 사이클 3~5: 산소

{: .ico-grid}
- {% include i.html n="Oxygen_Diffuser" %} **산소 확산기 (Oxygen Diffuser)** 조류 투입, 1대 ≈ 5명
- {% include i.html n="Oxylite" %} **산소석 (Oxylite)** 캐서 바닥에 두면 공짜 산소
- {% include i.html n="Carbon_Dioxide" %} **이산화탄소 (CO₂)** 가장 낮은 곳에 구덩이

> 조류는 한정 자원. 확산기는 약 30사이클 버티는 다리 역할, 결국 **전해조 (Electrolyzer)** 로 ([장기 평형 설계]({{ '/guide/sustainability/' | relative_url }})).
{: .warn}

<details class="nums" markdown="1">
<summary>상세 수치</summary>

- 시작 지역 산소는 사이클 5~10쯤 부족해지기 시작.
- CO₂는 산소보다 무거워 기지 바닥에 고임.
</details>

## 사이클 5 점검표

- [ ] 연구스테이션이 쉬지 않음
- [ ] 화장실 + 세면기 동선 OK
- [ ] 침대 = 복제체 수
- [ ] 끼니나무 1명당 5그루 이상
- [ ] 산소 확산기 + 조류 재고
- [ ] 수동 발전기 + 배터리
- [ ] 산소 오버레이(F1)에서 기지 안이 초록
