---
title: 건축 규격 & 팁
nav_title: 건축 규격 & 팁
nav_order: 22
nav_group: ref
permalink: /guide/build-specs/
description: 층 높이, 방 크기, 동선, 와이어·파이프 용량, 재료 고르는 법. 나중에 뜯어고치지 않도록 처음부터 맞춰두면 좋은 규격들.
---

* 목차
{:toc}

## 기지 뼈대

{: .ico-grid}
- {% include i.html n="Tile" %} **방 내부 높이 4** 층 간격 5
- {% include i.html n="Mesh_Tile" %} **방 너비 16** 4×16 = 64
- {% include i.html n="Ladder" %} **사다리 + 소방서 폴** 나란히
- {% include i.html n="Pneumatic_Door" %} **가로 통로 2칸** 복제체 키

<div class="bp-wrap" markdown="0">
{% include bp/build-floors.svg %}
</div>

> 뜨거운 가스는 위로, CO₂는 아래로. **발전 구역은 절연 타일로 따로 감싸고**, CO₂는 맨 아래 구덩이에.
{: .heat}

<details class="nums" markdown="1">
<summary>규격 이유 표와 이동 규칙</summary>

| 항목 | 추천 | 이유 |
|---|---|---|
| 방 내부 높이 | **4칸** | 호화 막사(Luxury Barracks)·개인 침실은 천장 4칸 이상이 조건. 대부분 건물이 3칸 이하라 여유 있음 |
| 층 간격 | 5칸 (내부 4 + 바닥 1) | 위 규격에 맞춰 반복 |
| 방 하나 너비 | 12~16칸 | 4×16 = 64칸 → 대부분 방의 최대 크기와 딱 맞음 |
| 중앙 통로 | 사다리 + 소방서 폴 나란히 | 올라갈 땐 사다리, 내려갈 땐 소방서 폴(Fire Pole)이 훨씬 빠름 |
| 가로 통로 | 2칸 높이 | 복제체 키 |


- 1칸 턱은 사다리 없이 오르내림. 플라스틱 사다리 (Plastic Ladder)가 더 빠름. 넓어지면 수송 튜브 (Transit Tube).

</details>

{% include shot.html src="second-base-overview.jpg" caption="두 번째 기지: 가운데 세로 통로 기준으로 층을 반복, 양옆으로 방, 바닥 쪽 수조." %}

## 방 (Room) 규격

벽·문·타일로 **완전히 막힌 공간** + 조건 건물. 방 오버레이로 확인. 배치도 크기는 [방 크기]({{ '/guide/core-base/rooms/' | relative_url }}).

> 대부분의 방은 **산업 기계 금지.** 한 방이 여러 조건을 동시에 만족하면 '기타 방'(보너스 0).
{: .warn}

<details class="nums" markdown="1">
<summary>방 종류별 크기·조건·효과</summary>

| 방 | 크기 | 필요한 것 | 효과 |
|---|---|---|---|
| 변소 (Latrine) | 12~64 | 뒷간 + 세면기 | 사기 +1 |
| 세척실 (Washroom) | 12~64 | 수세식 화장실 + 물이 연결된 싱크대(Sink), 뒷간 없음 | 사기 +2 |
| 막사 (Barracks) | 12~64 | 침대 1개 이상 | 사기 +1 |
| 호화 막사 (Luxury Barracks) | 12~64 | 편안한 침대(Comfy Bed), 간이 침대 없음, 장식품 1개, **천장 4칸** | 사기 +2 |
| 개인 침실 (Private Bedroom) | 24~64 | 편안한 침대 정확히 1개, 장식품 2개, 천장 4칸, 뒷벽 | 사기 +3 |
| 식당 (Mess Hall) | 12~64 | 식탁 | 사기 +3 |
| 큰 회관 (Great Hall) | 32~120 | 식탁 + 장식(20 이상) + 오락 건물 | 사기 +4 |
| 주방 (Kitchen) | 12~96 | 향신료 분쇄기 + 그릴/가스레인지 + 냉장고, 식탁 없음 | 향신료 분쇄기 사용 가능 |
| 온실 (Greenhouse) | 12~96 | 재배스테이션(Farm Station) | 비료로 성장 속도 2배 (1사이클) |
| 외양간 (Stable) | 12~96 | 치장스테이션 등 목장 건물 | 동물 길들이기 가능 |
| 연구소 (Laboratory) | 32~120 | 연구 건물 2개 | 연구 효율 +10% |
| 공원 (Park) | 12~64 | 공원 표지판 + 야생 식물 2개 | 사기 +3 |
| 자연보호구역 (Nature Reserve) | 32~120 | 공원 표지판 + 야생 식물 4개 | 사기 +6 |
| 발전소 (Power Plant) | 12~96 | 대형 발전기 + 전력 건물 2개 | 마이크로칩으로 발전량 +50% |

</details>

## 화장실 동선

<div class="bp-wrap" markdown="0">
{% include bp/bath-flow.svg %}
</div>

**화장실 → 세면기 → 문** 순서로, 나가는 길이 세면기를 통과하게 (세면기엔 방향이 있음). 첫 화장실은 바닥 18칸에 4 + 4.

## 에어락

{: .ico-grid}
- {% include i.html n="Pneumatic_Door" %} **공압 문 2개** 초반, 조금 샘
- {% include i.html n="Mechanized_Airlock" %} **기계식 에어록 (Mechanized Airlock)** 전기, 덜 샘
- {% include i.html n="Water" %} **액체 잠금 (Liquid Lock)** 안 샘, 전기 0

<details class="nums" markdown="1">
<summary>비교 표와 액체 잠금 원리</summary>

| 방법 | 장점 | 단점 |
|---|---|---|
| 공압 문 (Pneumatic Door) 2개 | 초반에 바로 가능 | 열릴 때 기체가 조금 샘 |
| 기계식 에어록 (Mechanized Airlock) | 빠르고 덜 샘 | 전기 필요 |
| 액체 잠금 (Liquid Lock) | 기체가 아예 못 지나감, 전기 불필요 | 만드는 법이 조금 까다로움 |


**액체 잠금:** 통로를 U자로 낮게 파서 바닥에 액체를 채우고 천장을 액체 표면까지 내려 막음. 복제체는 숨을 참고 지나감.

</details>

## 와이어

{: .ico-grid}
1. {% include i.html n="Coal_Generator" %} **발전기 → 헤비와트 → 배터리** 발전 구역 안에서만
2. {% include i.html n="Power_Transformer" %} **배터리 → 변압기** 회로마다
3. {% include i.html n="Research_Station" %} **일반 와이어 → 건물** 회로당 1 kW 이하

<details class="nums" markdown="1">
<summary>와이어 등급과 규칙</summary>

| 와이어 | 용량 | 용도 |
|---|---|---|
| 와이어 (Wire) | 1kW | 일반 회로 |
| 전도성 와이어 (Conductive Wire) | 2kW | 조금 큰 회로 |
| 헤비와트 와이어 (Heavi-Watt Wire) | 20kW | 발전기 ↔ 변압기 사이 주 간선. 장식 패널티 큼 |
| 헤비와트 전도성 와이어 (Heavi-Watt Conductive Wire) | 50kW | 후반 주 간선 |


**추천 구조**

1. **발전기들** → 헤비와트 와이어 → **배터리들** (발전 구역 안에서만)
2. 배터리 → **변압기 A** → 일반 와이어 → 생활 구역 건물들 (합계 1kW 이하)
3. 배터리 → **변압기 B** → 일반 와이어 → 농장·작업장 건물들 (합계 1kW 이하)

- 변압기(Power Transformer, 1kW)·큰 변압기(Large Power Transformer, 4kW)로 회로를 쪼갭니다.
- 헤비와트 와이어는 생활 구역을 지나가지 않게 합니다. (장식 수치가 크게 떨어짐)
- 회로마다 소비 전력을 전력 오버레이에서 확인하세요.

</details>

## 파이프

<details class="nums" markdown="1">
<summary>파이프 용량과 펌프</summary>

| 파이프 | 1칸당 최대 | 펌프 |
|---|---|---|
| 액체 파이프 | 10kg/s | 액체 펌프 10kg/s (240W), 소형 액체 펌프 0.5kg/s (60W) |
| 기체 파이프 | 1kg/s | 가스 펌프 0.5kg/s (240W), 소형 가스 펌프 50g/s (60W) |


- 서로 다른 물질이 섞이면 출구에서 막힘 → 필터나 분기로.
- 뜨거운 액체는 절연 파이프 (Insulated Pipe). 출구가 막히면 펌프가 멈추니 오버플로 출구를 하나.

</details>

## 재료 고르기

같은 건물도 **재료에 따라 성질이 달라집니다.** 절연은 화성암·세라믹·절연석, 열 전달은 금속·화강암, 고온 건물은 강철(+200°C)·금 아말감(+50°C).

<details class="nums" markdown="1">
<summary>목적별 좋은 재료·피할 재료</summary>

| 목적 | 좋은 재료 | 피할 재료 |
|---|---|---|
| 절연 타일 (열 차단) | 화성암(Igneous Rock), 세라믹(Ceramic), 후반엔 절연석(Insulite) | 금속, 화강암 |
| 열 전달 (냉각판 등) | 금속, 화강암, 다이아몬드 | 단열 재료 |
| 고온 건물 | 강철(+200°C 과열 한계), 금 아말감(+50°C) | 납(과열 한계가 낮음) |
| 일반 바닥·벽 | 사암(Sandstone), 화성암 | — |

</details>

작은 팁은 [플레이 팁]({{ '/guide/tips/' | relative_url }}).
