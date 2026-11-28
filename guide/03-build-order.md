---
title: 단계별 건설 순서
nav_title: 단계별 건설 순서
nav_order: 6
nav_group: early
permalink: /guide/build-order/
description: 실제 플레이 스크린샷으로 보는 건설 순서. 극초반 8단계만 잘 해도 복제체는 죽지 않습니다.
---

* 목차
{:toc}

## 전체 흐름

| 구간 | 사이클 | 할 일 |
|---|---|---|
| **극초반** | 1~20 | 화장실 → 산소 → 농장 → 연구 → 침실 → 수조 → 식당 → 석탄 발전기 |
| **초반** | 20~80 | 수조 완성 → 특수복 스킬 → 금속 정제 → 전해조 → 온도 관리 → 간헐천 → 환경 특수복 |
| **중반** | 80~150 | 원유 바이옴 → 지상 개통 → 강철 → 목장 |
| **후반** | 150~ | 운석 대비 → 우주 탐사 → 로켓 재료 |

> 사이클은 참고용. 각 단계가 **안정적으로 도는지** 보고 넘어가세요. 가이드 목차의 초·중·후반은 [연구 기준]({{ '/guide/research/' | relative_url }}#초반중반후반은-연구로-나눕니다)입니다.
{: .tip}

## 극초반 8단계

{: .ico-grid}
1. {% include i.html n="Outhouse" %} **화장실** 바닥 18칸
2. {% include i.html n="Oxygen_Diffuser" %} **산소 확산기 (Oxygen Diffuser)** 1대 ≈ 5명
3. {% include i.html n="Farm_Tile" %} **농장** 1명당 4그루
4. {% include i.html n="Research_Station" %} **연구스테이션 (Research Station)**
5. {% include i.html n="Cot" %} **침실** 간이침대 = 인원
6. {% include i.html n="Water" %} **수조** 물웅덩이 넓히기
7. {% include i.html n="Mess_Table" %} **식당** 사기 +3
8. {% include i.html n="Coal_Generator" %} **석탄 발전기 (Coal Generator)**

> **1~3 (화장실·산소·식량)만 잘 해도 복제체는 죽지 않습니다.**
{: .tip}

### 1. 화장실

{% include shot.html src="bathroom-first.jpg" caption="맨 윗층 18칸: 세면기 (Wash Basin) 4개(나가는 방향) + 뒷간 (Outhouse) 4개. 왼쪽 아래 물웅덩이에 피처 펌프 (Pitcher Pump)." %}

### 2. 산소

{% include shot.html src="oxygen-diffuser.jpg" caption="포드 옆에 산소 확산기·연구스테이션·작업대를 한 줄로. 근처 조류를 캐서 채움." %}

### 3. 농장

{% include shot.html src="farm-liceloaf.jpg" size="half" caption="재배 타일 (Farm Tile) 9칸을 한 줄로, 아래층은 통로. 수확물로 이빵 (Liceloaf) 자동 제작." %}

### 4~5. 연구·침실

연구 순서는 식량 → 전력 → 파이프 → 환기 ([연구 순서]({{ '/guide/research/' | relative_url }})). 침실엔 산업 기계를 두지 않아야 막사 보너스 ([방 규격]({{ '/guide/build-specs/#방room-규격' | relative_url }})).

### 6. 수조

{% include shot.html src="water-tanks.jpg" caption="물웅덩이를 넓게 파서 수조 3개. 가운데 세로 통로로 층 연결. 수세식 화장실·전해조·농장이 전부 이 물을 씀." %}

### 7. 식당

<div class="shot-grid">
{% include shot.html src="mess-hall-early.jpg" caption="초반: 긴 방에 식탁 (Mess Table), 양 끝 문." %}
{% include shot.html src="washroom-dining-stack.jpg" caption="발전형: 위 화장실, 가운데 그림 장식 식당(→ 큰 회관 (Great Hall)), 아래 설비." %}
</div>

### 8. 석탄 발전기

{% include shot.html src="coal-generator-floor.jpg" caption="작업대 층 아래 발전 층. 스마트 배터리로 필요할 때만 가동." %}

## 초반

{: .ico-grid}
1. {% include i.html n="Water" %} **수조 완성** 펌프·파이프 연결
2. {% include i.html n="Atmo_Suit_Dock" %} **외부특수복 훈련 (Exosuit Training)** 레벨 3~4
3. {% include i.html n="Metal_Refinery" %} **금속 제련소 (Metal Refinery)** 정제 금속
4. {% include i.html n="Electrolyzer" %} **전해조 (Electrolyzer)** 18×5 모듈 2개
5. {% include i.html n="Steam_Turbine" %} **증기 터빈 (Steam Turbine)** + 열액체조화기
6. {% include i.html n="Water_Sieve" %} **간헐천 (Geyser)** 길들이기
7. {% include i.html n="Atmo_Suit_Checkpoint" %} **환경 특수복** 위험 구역용

> 환경 특수복 = **전기 + 산소.** 거치대에 와이어와 산소 파이프 둘 다. 금속 제련소 냉각수는 뜨거우니 파이프를 따로.
{: .warn}

{% include shot.html src="bedrooms-exosuit.jpg" caption="침실 앞, 층마다 환경 특수복 거치대. 전도성 와이어(2,000 W) + 기체 파이프(산소)." %}

### 전해조 산소 (18×5 모듈 2개)

{% include shot.html src="spom-2x.jpg" caption="모듈 2개를 위아래로. 버섯 모양 = 가스 펌프, 오른쪽 흰 장치 = 전해조. 방마다 산소·수소를 따로 뽑음." %}

<details class="nums" markdown="1">
<summary>오버레이 4장 (전력·기체·액체·자동화)과 센서 값</summary>

<div class="shot-grid">
{% include shot.html src="spom-power.jpg" caption="전력 오버레이. 가스 펌프 240W, 전해조 120W. 전도성 와이어 한 줄에 현재 480W / 최대 1,440W로 2,000W 한도 안." %}
{% include shot.html src="spom-gas.jpg" caption="기체 오버레이. 파란 파이프 = 산소 → 오른쪽 침실 앞 환경 특수복 거치대로. 분홍 파이프 = 수소 → 발전기로." %}
{% include shot.html src="spom-liquid.jpg" caption="액체 오버레이. 물이 각 모듈 전해조로 들어감." %}
{% include shot.html src="spom-sensors.jpg" caption="자동화 오버레이. 각 방에 압력 센서를 달아 펌프를 제어." %}
</div>

- 압력 센서: **수소 4,000 g / 산소 10,000 g** 넘으면 펌프·전해조 정지.
- 전력: 가스 펌프 240 W, 전해조 120 W. 전도성 와이어 한 줄 480 W / 최대 1,440 W (한도 2,000 W).
- 원리와 물 수급: [장기 평형 설계]({{ '/guide/sustainability/#산소-전해조-시스템-spom' | relative_url }}).
</details>

### 발전소 자동화

{% include shot.html src="power-plant-smartbattery.jpg" caption="점보 배터리 3 + 발전기 3. 스마트 배터리 신호(초록 선)로 켜고 끔." %}

### 온도 관리: 증기 터빈 + 열액체조화기

{% include shot.html src="steam-cooler.jpg" size="half" caption="위 증기 터빈, 아래 밀폐 증기 방(절연 타일) 안에 열액체조화기 (Thermo Aquatuner). 냉각수 열 → 증기 → 전기." %}

<details class="nums" markdown="1">
<summary>오버레이 4장과 전력 수치</summary>

<div class="shot-grid">
{% include shot.html src="steam-cooler-power.jpg" caption="전력 오버레이. 증기 터빈 +850W, 열액체조화기 −1,200W, 펌프 −240W." %}
{% include shot.html src="steam-cooler-liquid.jpg" caption="액체 오버레이. 냉각수(절연 액체 파이프, 오염된 물 24.9°C)가 열액체조화기를 지나며 식은 뒤 기지로 돌아감." %}
{% include shot.html src="steam-cooler-gas.jpg" caption="기체 오버레이. 위쪽 증기 터빈 파이프." %}
{% include shot.html src="steam-cooler-gas2.jpg" caption="터빈이 내보내는 물(노란 파이프)은 다시 증기 방으로." %}
</div>

- 증기 터빈 +850 W, 열액체조화기 −1,200 W, 펌프 −240 W.
</details>

> **물 소독:** 정화한 물을 **염소 (Chlorine) 방**에 150~200초 머물게 파이프 길이를 잡으면 병균이 죽습니다.
{: .tip}

### 두 번째 집

{% include shot.html src="second-base-overview.jpg" caption="가운데 세로 통로 기준으로 층을 쌓고 양쪽으로 방. 맨 아래 수조." %}

참고 영상: [유튜브 1 (24:32~)](https://youtu.be/rGlv657_RFI?t=1472), [유튜브 2](https://www.youtube.com/watch?v=1rRatGw45VU)

## 중반 · 후반 (메모)

| 중반 | 후반 |
|---|---|
| 원유 바이옴 (뜨거움, [타이밍]({{ '/guide/biome-expansion/' | relative_url }})) | 운석 대비 방탄 |
| 지상 개통 (운석 시작) | 우주 탐사 |
| 강철 양산 | 로켓으로 후반 재료 |
| 주둥가리 (Hatch) 목장 ([Reddit](https://www.reddit.com/r/Oxygennotincluded/comments/14yyrl0/automated_hatch_farm_revisited/)) | 극후반 체제 |
