---
title: 단열 격벽·냉방·수조
nav_title: 격벽·냉방·수조
nav_order: 14
nav_group: early
permalink: /guide/core-base/envelope/
description: 단열·냉방을 시작하는 단계별 순서, 냉방 시스템, 깨끗한 물·오염수 수조, 화장실·샤워실 폐쇄 루프(물 정화기 + 갈대 넘침).
---

* 목차
{:toc}

> 전체 도면은 [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }})에 있습니다. 이 페이지는 그중 일부를 자세히 푼 것이에요.
{: .tip}

## 단열·냉방 시작하기: 단계별

> 4·5단계(냉방실·수냉 조절기·증기 터빈)는 **[15 에어컨 설치]({{ '/guide/core-base/aircon/' | relative_url }})**에 도면과 설치 순서, 열 계산까지 자세히 풀어 두었습니다.
{: .tip}

> 사이클 18 무렵, 정제 금속은 암석 분쇄기로만 얻는 상황 기준입니다. **1~3단계는 정제 금속이 하나도 안 들고**, 4단계는 약 75 kg, 5단계(증기 터빈)는 800 kg이 듭니다.
{: .tip}

| 단계 | 할 일 | 연구 | 재료 | 정제 금속 |
|---|---|---|---|---|
| 1 | 온도 오버레이로 열원 찾고 격벽 밖으로 빼기 | – | – | 0 |
| 2 | 단열 타일: 바닥 줄 → 냉방실 → 나머지 | 온도 조절 (Temperature Modulation, 3단계) | 원료 광물 400 kg/칸 | 0 |
| 3 | SPOM 산소 식히기 | – | 가스 파이프 | 0 |
| 4 | 냉방실 + 수냉 조절기 + 냉각 루프 | 개선된 파이프 (3단계) → **액체 조율 (Liquid Tuning, 4단계)**, 고급 전력 조절 | 금속 광석 1,200 kg (조절기) + 헤비와트 | 약 75 kg |
| 5 | 냉방실에 **증기 터빈** → 그 뒤 금속 정제기 | 재생 에너지 (Renewable Energy, 5단계) | 정제 금속 800 kg + 개스킷 | 800 kg |

### 1단계: 열원 찾기 (지금 바로)

- 화면 오른쪽 위 **온도 오버레이**로 격벽 안을 봅니다. 30°C 넘는 곳이 열원이에요.
- 격벽 안에 있으면 안 되는 것: **석탄 발전기, 암석 분쇄기, 전기분해기·SPOM, 금속 정제기, 전기 그릴**. 전부 격벽 밖 산업층(발전소·정제 칸)으로.
- 기지 안에 남는 열원은 복제체, 조명, 펌프, 냉장고 정도라 단열만 해도 온도가 많이 안정됩니다.

### 2단계: 단열 타일 (온도 조절 연구)

**단열 타일 (Insulated Tile)** 은 원료 광물 400 kg. 재료는 **화성암 (Igneous Rock)** 이 무난합니다 (사암·화강암보다 열을 덜 전함). 이미 지은 타일은 그 위에 바로 **교체 건설**이 되고, 자연 타일은 파낸 뒤 짓습니다.

격벽 전체는 약 250칸(≈100톤)이라 한 번에 못 합니다. 열이 들어오는 순서대로:

1. **격벽 바닥 줄** = 기지와 그 아래 발전소·산업층 사이. 열은 위로 올라와서 여기가 1순위. 깨끗한 물 수조 바닥도 이때.
2. **냉방실 4면** (4단계에서 지을 방). 냉방실은 계속 뜨거워지니 처음부터 단열 타일로.
3. **동·서 통로가 격벽을 지나는 곳**: 지금 있는 문 그대로 OK. 나중에 기계식 에어락 (Mechanized Airlock, 금속 광석 400 kg)으로.
4. 나머지 옆·위 테두리. 자연 암반이 두껍게 남은 쪽은 맨 나중.

### 3단계: SPOM 산소 식히기

SPOM 산소는 **70°C 이상**으로 나옵니다. 산소 가스 파이프를 격벽에 들이기 전에 **격벽 밖 오염수 수조 속으로 10칸쯤** 지나가게 해서 식히세요. 4단계 뒤엔 냉방실 안을 지나게 바꿔도 됩니다.

### 4단계: 냉방실 + 수냉 조절기

| 항목 | 값 | 메모 |
|---|---|---|
| 위치 | 격벽 바로 아래, 발전소 옆 냉방실 14×4 | [전체 도면]({{ '/guide/core-base/#후반-완성-배치도' | relative_url }})의 냉방실. **위로 3칸은 비워 두기** (5단계 증기 터빈 5×3 자리) |
| **수냉 조절기 (Thermo Aquatuner)** | 2×2 · 금속 광석 1,200 kg · 1.2 kW | **금 아말감으로 지으세요.** 과열 125°C가 175°C(+50)로 올라가 냉방실이 뜨거워져도 버팀 |
| 열 받는 물 | 냉방실 바닥에 **오염수 약 20톤**, 조절기가 잠기게 | 조절기가 옮긴 열이 이 물에 쌓임 |
| 전력 | 1.2 kW → 일반 와이어(1 kW) 불가 | 발전소 **헤비와트 와이어 (Heavi-Watt Wire, 칸당 금속 광석 100 kg)** 에 바로. 벽은 헤비와트 연결판 (Joint Plate)으로 통과 |
| 냉각 루프 | **오염수** 권장 (−20.65°C에서 얼어 물보다 안전) | 냉방실 → **절연 액체 파이프**(격벽 통과 구간만) → 격벽 안 **바닥 줄을 따라 일반 액체 파이프로 한 바퀴** (실내 온실 바닥 밑 꼭) → 절연 액체 파이프 → 조절기 |
| 자동화 | **액체 파이프 온도 센서** (정제 금속 25 kg) | 돌아오는 줄, **격벽 안에서 냉방실로 나가기 직전** 파이프에. **18°C 이상이면 켜기** → 루프 물이 4~18°C라 얼지 않고 기지는 20~25°C |

- 루프는 끝을 조절기 입구로 다시 이으면 펌프 없이 돕니다. 처음 한 번만 액체 펌프로 파이프를 꽉 채우고(조절기는 칸당 10 kg일 때 효율이 좋음) 펌프 연결을 끊으세요.
- 정제 금속은 센서 25 kg + 자동화 와이어 몇 칸 ≈ **75 kg**뿐이라 분쇄기로 충분합니다.

> **냉방실 물은 계속 뜨거워집니다.** 수냉 조절기는 열을 지우지 않고 옮기기만 해요. 단열을 먼저 해 둘수록 천천히 오르지만, 언젠가 100°C를 넘습니다. 그래서 **5단계 증기 터빈을 미루지 마세요.** 금 아말감 조절기는 175°C까지 버팁니다.
{: .warn}

### 5단계: 증기 터빈 → 그 다음 금속 정제기

- 냉방실 물이 끓어 **125°C 넘는 증기**가 되면, 냉방실 천장(비워 둔 3칸)에 **증기 터빈 (Steam Turbine)** 5×3을 얹습니다. 열을 지우면서 전기도 만듭니다.
- 정제 금속 800 kg = 암석 분쇄기로 광석 1,600 kg (16회, 약 1사이클). 분쇄기는 격벽 밖이라 괜찮아요.
- [금속 정제기]({{ '/guide/core-base/refining/' | relative_url }})는 냉각수 파이프를 이 냉방실 물속으로 지나가게 하면 **터빈 전에도** 쓸 수 있습니다. 구리 100 kg 한 번에 냉방실 물 20톤이 약 **0.4°C** 오를 뿐이에요. 냉방실이 차가울 때 몰아서 (구리는 냉방실 55°C 아래, 철 40°C 아래. 강철은 터빈 뒤). (예전 "390°C"는 단위 오류였습니다)

> **씨근풀 (Wheezewort)** 씨앗이 있으면 실내 통로에 심어 두세요. 열을 진짜로 지우는 식물이라(산소 속 길든 것 약 5 kDTU/s, 인광석 비료 필요) 냉방실 물이 데워지는 속도를 늦춰 줍니다.
{: .tip}

## 단열 격벽: 안과 밖 나누기

생활 구역과 바깥을 **단열 타일 격벽**으로 완전히 나누고, 안쪽만 냉방해서 **20~25°C**로 유지합니다. 복제체는 0~45°C 사이면 춥거나 덥다는 상태가 안 붙지만, 실내 작물(끼니나무·센털꽃 등)이 대부분 30°C를 넘으면 자라지 않아서 기준은 작물에 맞춥니다.

| | 격벽 **안** (20~25°C) | 격벽 **밖** |
|---|---|---|
| 들어가는 것 | 생활 구역 코어·침실 블록, 실내 온실 A·B, 실내 목장 2개, **깨끗한 물 수조** | 산업(발전·SPOM·정제), 냉방실, **오염수 수조**, 외부 온실·외부 목장, CO₂ 구덩이 |
| 연결 | 서쪽·동쪽 사다리 통로. 두 통로 아래 끝(격벽 줄)에 **가로로 돌린 기계식 에어락** | 아래 발전소·산업층은 통로를 타고 에어락을 지나 내려감. 침실 블록 특수복 거치대에서 환경 특수복을 입고 나감 |

- 격벽은 **열전도율이 가장 낮은 재료**로 만든 단열 타일로 두릅니다 (초반엔 화성암·세라믹, 후반엔 인슐라이트).
- 격벽을 지나는 문은 전부 기계식 에어락. 문은 가로로 돌려 지을 수 있어서 세로 통로에도 씁니다.
- **SPOM 산소는 최소 70°C**로 나옵니다. 산소 파이프가 격벽 안으로 들어가기 전에 냉각 루프나 수조를 지나게 해서 식힌 뒤 배출하세요. 안 그러면 실내 열의 대부분이 여기서 들어옵니다.

### 냉방 시스템

| 단계 | 장치 | 위치 | 메모 |
|---|---|---|---|
| 초반 | 씨근풀 (Wheezewort) | 실내 통로·온실 | 주변 기체를 식혀 주는 식물. 비료를 주면 더 셈 |
| 중반 | **수냉 조절기 (Thermo Aquatuner)** + 냉각 루프 | 냉방실 (격벽 밖, 산업층) | 지나가는 액체를 한 번에 14°C 식히고, 그 열은 장치 자체로 옮김. 전력 1.2 kW. 액체는 10 kg씩 꽉 채워 보내야 효율이 좋음 |
| 후반 | 수냉 조절기 + **증기 터빈** | 냉방실 위 | 조절기 열로 125°C 이상 증기를 만들어 터빈이 열을 지우고 전기도 생산 |

- 냉각 루프([전체 도면]({{ '/guide/core-base/#후반-완성-배치도' | relative_url }})의 하늘색 점선)는 **격벽 안 바닥 줄**을 따라 한 바퀴 돌고 다시 냉방실로 나갑니다. 실내 온실 바닥 밑을 꼭 지나가게 하세요.
- 조절기 자체는 뜨거워지니 **반드시 격벽 밖** 냉방실에 둡니다.

### 수조

물은 두 수조로 나누고, **깨끗한 물은 격벽 안**, **오염수는 격벽 밖**에 둡니다.

| 수조 | 위치 | 크기 | 쓰는 곳 |
|---|---|---|---|
| **깨끗한 물 수조** | 격벽 안 맨 아래 동쪽 (원래 오른쪽 아래 웅덩이를 넓힘) | 30×4 = 120칸 ≈ 120톤 (칸당 최대 약 1톤) | 실내 온실 관개, 전기분해기. 화장실·샤워실 루프는 처음 한 번 채울 때만 |
| **오염수 수조** | 격벽 바로 아래 서쪽, **격벽 밖** | 17×4 = 68칸 ≈ 68톤 | 공장·냉방용 오염수. 화장실·샤워실은 자체 폐쇄 루프라 여기로 안 옴 |
| 왼쪽 아래 웅덩이 | 그대로 둠, 격벽 밖 | 자연 크기 | 예비 물, 외부 온실 관개 |

- **깨끗한 물을 격벽 안에 두는 이유:** 물은 열을 많이 머금어서 120톤짜리 수조가 실내 온도를 잡아 주는 완충 역할을 합니다. 관개수도 실내 온도 그대로 들어가요. 수조 바닥은 아래 발전소 열이 안 올라오게 **단열 타일**로 깝니다.
- **오염수 수조는 위를 막으세요.** 오염수는 공기와 닿으면 오염 산소를 뿜는데, 위 칸 기압이 1.8 kg 이상이면 멈춥니다 (공식 위키). 꽉 채우거나 위를 액체·타일로 막으면 됩니다.
- **화장실·샤워실은 따로 폐쇄 루프**로 돌립니다 (아래 [화장실·샤워실 폐쇄 루프](#화장실샤워실-폐쇄-루프)). 수조 물은 처음 채울 때만 씁니다.
- 펌프는 수조 **맨 바닥**에 둡니다 (액체 펌프 2×2, 초당 10 kg, 잠겨 있어야 작동). 소형 액체 펌프는 5단계 연구라 초반엔 일반 액체 펌프를 씁니다.

#### 물 수지 (1사이클 = 600초 기준)

| 항목 | 물 | 메모 |
|---|---|---|
| 수세식 화장실 1회 | 물 5 kg 쓰고 오염수 11.7 kg 나옴 | **오히려 늘어남** (+6.7 kg) |
| 싱크대(Sink) 1회 | 물 5 kg → 오염수 5 kg | 그대로 |
| 샤워기(Shower) 1회 | 물 16 kg → 오염수 16 kg | 그대로. 8명이면 하루 128 kg. 폐쇄 루프 안에서 돎 |
| 전기분해기 1대 | **−600 kg / 사이클** (초당 1 kg) | 제일 큰 소비처. 1대 ≈ 복제체 8명 산소 |
| 센털꽃 1그루 | −20 kg / 사이클 | 온실 하나(40그루)면 −800 kg |
| 끼니나무 | 물 대신 흙 | 물 안 씀 |

> 깨끗한 물 수조 120톤은 전기분해기 1대만 돌려도 **약 200사이클**, 센털꽃 온실까지 같이 쓰면 약 85사이클이면 바닥납니다. 그 전에 **물 분출구·증기 분출구 같은 간헐천**을 찾아 깨끗한 물 수조로 연결하세요. 화장실 루프에서 넘치는 오염수는 세균이 있어 수조로 보내지 않고 갈대에 줍니다.
{: .tip}

## 화장실·샤워실 폐쇄 루프

화장실(수세식 + 싱크대)과 샤워실을 **물 정화기 하나로 묶은 폐쇄 루프**로 돌립니다. 처음 한 번 물을 채우면 깨끗한 물이 더 들지 않고, 수세식 화장실 때문에 물이 오히려 늘어나니 **넘치는 오염수는 갈대가 받습니다.** 공식 위키의 자급 화장실(Self Sustainable Bathrooms) 가이드와 같은 구조예요.

### 위치: 샤워실을 화장실 바로 아래에

| 층 | 크기 | 들어가는 것 |
|---|---|---|
| 식당층 (맨 위) | 복층 큰 회관 24×5 | 루프와 상관없음. 화장실과 높이를 맞춘 짝 (3 + 1 + 5 = 보통 두 층) |
| 화장실층 | **화장실(세척실) 16×3** + 벽 + **기계실 7×3** | 싱크대 2 · 수세식 4 · 싱크대 2 / 물 정화기 4×3 · 모래 저장 상자 · 갈대 |
| 샤워실층 (포드 바로 위) | **샤워실 16×4** + 벽 + 여유 7×4 | 샤워기 2×4 × 8 |

- 화장실과 샤워실이 바닥 한 줄만 사이에 둬서 세로 배관이 몇 칸이면 끝납니다. 식당은 화장실 바로 위라 식당·화장실 높이 짝도 그대로예요.
- 물 정화기는 **세척실 안에 두면 안 되니**(산업 기계) 벽 하나 건너 기계실에 둡니다. 위키 가이드도 "정화기와 모래 상자는 화장실 옆 별도 방"을 권해요. 모래를 정화기 옆에 쌓아 두면 나르는 거리가 짧습니다.
- 특수복 거치대·보관함은 여기 안 둡니다.

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 704 403" width="704" role="img" aria-label="화장실과 샤워실 폐쇄 루프 배관도" style="min-width:0;max-width:704px" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="704" height="403" fill="#11131f"/><rect x="24" y="60" width="660" height="242" fill="#5a4a3a"/><rect x="90" y="82" width="352" height="66" fill="#1c2036"/><text x="116" y="163.4" fill="#e9ecf8" font-size="10.5" font-weight="700">화장실 (세척실) 16×3</text><rect x="464" y="82" width="154" height="66" fill="#1c2036"/><text x="490" y="163.4" fill="#e9ecf8" font-size="10.5" font-weight="700">기계실 7×3</text><rect x="90" y="170" width="352" height="88" fill="#1c2036"/><text x="116" y="273" fill="#e9ecf8" font-size="10.5" font-weight="700">샤워실 16×4</text><rect x="464" y="170" width="154" height="88" fill="#1c2036"/><text x="490" y="273" fill="#e9ecf8" font-size="10.5" font-weight="700">여유 7×4</text><rect x="24" y="60" width="66" height="242" fill="#24452e"/><text x="57.0" y="316" fill="#acffbd" font-size="10" text-anchor="middle">서쪽 통로</text><rect x="618" y="60" width="44" height="242" fill="#24452e" fill-opacity=".5"/><rect x="91.5" y="83.5" width="41" height="63" rx="3" fill="#9fe8ff" fill-opacity=".9"/><text x="112.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">싱크</text><rect x="135.5" y="83.5" width="41" height="63" rx="3" fill="#9fe8ff" fill-opacity=".9"/><text x="156.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">싱크</text><rect x="355.5" y="83.5" width="41" height="63" rx="3" fill="#9fe8ff" fill-opacity=".9"/><text x="376.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">싱크</text><rect x="399.5" y="83.5" width="41" height="63" rx="3" fill="#9fe8ff" fill-opacity=".9"/><text x="420.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">싱크</text><rect x="179.5" y="83.5" width="41" height="63" rx="3" fill="#ffffff" fill-opacity=".9"/><text x="200.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">수세식</text><rect x="223.5" y="83.5" width="41" height="63" rx="3" fill="#ffffff" fill-opacity=".9"/><text x="244.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">수세식</text><rect x="267.5" y="83.5" width="41" height="63" rx="3" fill="#ffffff" fill-opacity=".9"/><text x="288.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">수세식</text><rect x="311.5" y="83.5" width="41" height="63" rx="3" fill="#ffffff" fill-opacity=".9"/><text x="332.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">수세식</text><rect x="465.5" y="83.5" width="85" height="63" rx="3" fill="#c0c8e0" fill-opacity=".9"/><text x="508.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">물 정화기</text><rect x="553.5" y="105.5" width="19" height="41" rx="3" fill="#a9b0d0" fill-opacity=".9"/><text x="563.0" y="130.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">모래</text><rect x="575.5" y="83.5" width="19" height="63" rx="3" fill="#9be36b" fill-opacity=".9"/><text x="585.0" y="119.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">갈대</text><rect x="574" y="148" width="22" height="22" fill="#6bbf4a" stroke="#fff" stroke-width="1"/><rect x="91.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="112.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="135.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="156.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="179.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="200.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="223.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="244.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="267.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="288.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="311.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="332.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="355.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="376.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><rect x="399.5" y="171.5" width="41" height="85" rx="3" fill="#bfe6ff" fill-opacity=".9"/><text x="420.0" y="218.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">샤워</text><polyline points="541.0,137.0 101.0,137.0 101.0,247.0 431.0,247.0" fill="none" stroke="#4fa8ff" stroke-width="4" stroke-linejoin="round" stroke-opacity=".95"/><polyline points="112.0,71.0 453.0,71.0 475.0,71.0" fill="none" stroke="#c98a3a" stroke-width="4" stroke-linejoin="round" stroke-opacity=".95"/><polyline points="112.0,181.0 453.0,181.0 453.0,71.0" fill="none" stroke="#c98a3a" stroke-width="4" stroke-linejoin="round" stroke-opacity=".95"/><polyline points="475.0,71.0 475.0,93.0 607.0,93.0 607.0,159.0 585.0,159.0" fill="none" stroke="#7be36b" stroke-width="3" stroke-linejoin="round" stroke-opacity=".95" stroke-dasharray="5 3"/><polyline points="519.0,71.0 519.0,93.0" fill="none" stroke="#c98a3a" stroke-width="4" stroke-linejoin="round" stroke-opacity=".95"/><rect x="466" y="64" width="62" height="14" fill="#ffd34a" stroke="#11131f"/><text x="497.0" y="55" fill="#ffd34a" font-size="10.5" font-weight="700" text-anchor="middle">액체 다리 →</text><text x="24" y="336" fill="#4fa8ff" font-size="11.5">파랑 = 물 (정화기 → 싱크·수세식 8 → 서쪽 끝에서 아래로 → 샤워기 8, 마지막 샤워기에서 끝)</text><text x="24" y="353" fill="#c98a3a" font-size="11.5">갈색 = 오염수 (출구마다 짧게 위로 빼서 천장 줄에 모음, 출구끼리 한 줄로 잇지 않기) → 액체 다리 → 물 정화기</text><text x="24" y="370" fill="#7be36b" font-size="11.5">초록 점선 = 넘침: 액체 다리 입구에서 가지 → 수경 재배 타일의 갈대 (다리 쪽이 먼저, 꽉 차면 갈대로)</text><text x="24" y="32" fill="#e9ecf8" font-size="15" font-weight="700">화장실·샤워실 폐쇄 루프 (샤워실이 화장실 바로 아래)</text></svg>
</div>

### 필요한 것

| 건물 | 크기 | 재료 | 연구 | 물 |
|---|---|---|---|---|
| **수세식 화장실 (Lavatory)** ×4 | 2×3 | 금속 광석 400 kg | 위생 (Sanitation, 2단계) | 물 5 kg 들어가고 **오염수 11.7 kg** 나옴 (식중독 세균) |
| **싱크대 (Sink)** ×4 | 2×3 | 금속 광석 400 kg | 위생 | 물 5 kg → 오염수 5 kg |
| **샤워기 (Shower)** ×8 | 2×4 | 금속 광석 400 kg | 위생 | 물 16 kg → 오염수 16 kg. 사기 +3 |
| **물 정화기 (Water Sieve)** | 4×3 | 금속 광석 200 kg | 증류 (Distillation, 3단계) | 오염수 5 kg/s → 물. 모래 1 kg/s, 120 W. **세균은 못 없앰** |
| **액체 다리 (Liquid Bridge)** | 3×1 | 원료 광물 100 kg | 액체 파이프 (Plumbing) | 우선순위 밸브 역할 |
| **수경 재배 타일 (Hydroponic Farm)** + 갈대 씨앗 | 1×1 | 금속 광석 100 kg | 농업 (Agriculture) | 파이프로 오염수를 받는 농장 타일. 갈대는 **오염수 160 kg/사이클** |
| 액체 파이프 | | 원료 광물 | 액체 파이프 | |

### 기계실 7×3 상세

화장실(16칸) 동쪽에 벽 한 칸(16번)을 두고, 17~23번 칸 × 높이 3으로 팝니다. 바닥 줄 아래는 샤워실 천장, 천장 줄은 식당 바닥입니다.

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 846 450" width="846" role="img" aria-label="기계실 7×3 확대 배치도" style="min-width:0;max-width:846px" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="846" height="450" fill="#11131f"/><rect x="40" y="70" width="506" height="230" fill="#5a4a3a"/><rect x="40" y="116" width="46" height="138" fill="#1c2036"/><text x="63.0" y="132" fill="#cfd3e6" font-size="11" text-anchor="middle">화장실</text><rect x="132" y="116" width="322" height="138" fill="#1c2036"/><rect x="500" y="70" width="46" height="230" fill="#24452e" fill-opacity=".6"/><text x="523.0" y="316" fill="#acffbd" font-size="11" text-anchor="middle">동쪽 통로</text><rect x="132" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="132" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="132" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="178" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="178" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="178" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="224" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="224" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="224" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="270" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="270" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="270" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="316" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="316" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="316" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="362" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="362" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="362" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="408" y="116" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="408" y="162" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><rect x="408" y="208" width="46" height="46" fill="none" stroke="#fff" stroke-opacity=".07"/><text x="155.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">17</text><text x="201.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">18</text><text x="247.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">19</text><text x="293.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">20</text><text x="339.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">21</text><text x="385.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">22</text><text x="431.0" y="62" fill="#cfd3e6" font-size="11" text-anchor="middle">23</text><rect x="134" y="118" width="180" height="134" rx="4" fill="#c0c8e0" fill-opacity=".9"/><text x="224.0" y="183.0" fill="#11131f" font-size="13" font-weight="700" text-anchor="middle">물 정화기</text><text x="224.0" y="199.0" fill="#11131f" font-size="10.5" text-anchor="middle">4×3 · 120 W</text><rect x="318" y="164" width="42" height="88" rx="4" fill="#a9b0d0" fill-opacity=".9"/><text x="339.0" y="206.0" fill="#11131f" font-size="13" font-weight="700" text-anchor="middle">모래</text><rect x="364" y="118" width="42" height="134" rx="4" fill="#9be36b" fill-opacity=".9"/><text x="385.0" y="183.0" fill="#11131f" font-size="13" font-weight="700" text-anchor="middle">갈대</text><rect x="362" y="254" width="46" height="46" fill="#6bbf4a" stroke="#fff" stroke-width="1.5"/><text x="385.0" y="281.0" fill="#11131f" font-size="9.5" font-weight="700" text-anchor="middle">수경</text><rect x="94" y="162" width="30" height="92" fill="#8a9bd0"/><rect x="462" y="162" width="30" height="92" fill="#8a9bd0"/><polyline points="63.0,93.0 155.0,93.0" fill="none" stroke="#c98a3a" stroke-width="5" stroke-linejoin="round"/><rect x="135" y="78" width="132" height="30" fill="#ffd34a" stroke="#11131f"/><text x="201.0" y="97.0" fill="#11131f" font-size="11" font-weight="700" text-anchor="middle">액체 다리 →</text><polyline points="247.0,93.0 247.0,139.0" fill="none" stroke="#c98a3a" stroke-width="5" stroke-linejoin="round"/><polyline points="155.0,93.0 155.0,139.0 431.0,139.0 431.0,277.0 385.0,277.0" fill="none" stroke="#7be36b" stroke-width="4" stroke-linejoin="round" stroke-dasharray="7 4"/><polyline points="293.0,231.0 63.0,231.0" fill="none" stroke="#4fa8ff" stroke-width="5" stroke-linejoin="round"/><text x="40" y="344" fill="#e9ecf8" font-size="12">17~20번: 물 정화기 · 21번: 모래 저장 상자(모래만, 우선순위 높게) · 22번: 수경 재배 타일 위 갈대 · 23번: 지나다니는 칸</text><text x="40" y="362" fill="#c98a3a" font-size="12">갈색: 오염수가 천장 줄(식당 바닥)로 와서 액체 다리 → 정화기 입력구</text><text x="40" y="380" fill="#7be36b" font-size="12">초록 점선: 다리 입구 칸에서 가지 → 23번으로 내려가 → 22번 수경 재배 타일 (넘칠 때만)</text><text x="40" y="398" fill="#4fa8ff" font-size="12">파랑: 정화기 출력구 → 서쪽 벽을 지나 화장실 아래 줄로</text><text x="40" y="416" fill="#a9b0d0" font-size="12">문: 서쪽(16번) = 화장실, 동쪽(24번) = 동쪽 통로. 모래는 동쪽 통로로 들어옴</text><text x="40" y="30" fill="#e9ecf8" font-size="16" font-weight="700">기계실 7×3 확대 (화장실 동쪽 옆)</text></svg>
</div>

| 칸 | 건물 | 크기 · 재료 | 설정 |
|---|---|---|---|
| 16 (벽) | 문 | 1×2 | 화장실 쪽 출입 |
| 17~20 | **물 정화기 (Water Sieve)** | 4×3 · 금속 광석 200 kg · 120 W | 일반 와이어 OK. 높이 3이라 방 높이를 꽉 채움 |
| 21 | **저장 상자 (Storage Bin)** | 1×2 · 원료 광물 400 kg | **모래만** 받게, 우선순위 높게. 정화기 옆이라 나르는 거리 0 |
| 22 | **갈대 (Thimble Reed)** | 바닥 줄(15번 줄)에 **수경 재배 타일 (Hydroponic Farm)** 1×1 · 금속 광석 100 kg | 타일에 넘침 파이프 연결, 씨앗 심기. 22~37°C |
| 23 | 비움 | – | 지나다니는 칸 + 넘침 파이프가 지나가는 세로 줄 |
| 24 (벽) | 문 | 1×2 | 동쪽 통로. 모래는 이쪽으로 들어옴 |

**짓는 순서**

1. 연구: 위생 → 증류 (물 정화기), 농업 (수경 재배 타일). 액체 다리는 액체 파이프 연구라 이미 있음.
2. 7×3 파기 → 16번·24번 벽에 문 → 바닥 22번 칸은 일반 타일 대신 수경 재배 타일.
3. 물 정화기, 모래 상자 → 와이어 연결 (120 W, 정화기는 하루 1분 정도만 돌아서 전기는 거의 안 씀).
4. 파이프 (아래 배관 순서 3번): 오염수 줄은 천장 줄(식당 바닥 타일 속)로 들어와 **액체 다리** → 정화기 입력구. 다리 입구 칸에서 가지를 내려 23번 줄을 타고 22번 수경 재배 타일로. 물은 정화기 출력구에서 서쪽 벽을 지나 화장실로.
5. 갈대 씨앗 심기 → 처음 채우기(배관 순서 4번).

**정화기 부산물: 오염된 흙**

- 정화기는 물을 걸러낼 때 오염된 흙 (Polluted Dirt)을 0.2 kg/s 내놓습니다. 우리 루프는 하루 약 1분이라 **사이클당 약 10 kg**.
- 오염된 흙은 **저장 상자 안에서도 오염 산소를 뿜습니다** (위키, 물에 잠겨 있지 않으면). 그래서 기계실에 쌓지 말고, 청소 우선순위를 높여 **퇴비 더미 (Compost)**로 보내세요. 퇴비 더미는 오염된 흙을 흙으로 바꿔서 끼니나무 농장 타일에 다시 씁니다.
- 모래는 사이클당 약 52 kg (정화한 물 1 kg당 모래 0.2 kg). 암석 분쇄기 모래면 충분합니다.

### 배관 순서

1. **물 줄 (파랑):** 물 정화기 출구 → 화장실층 바닥 줄을 따라 싱크대·수세식 8개를 **한 줄로 차례로** → 서쪽 끝에서 한 층 내려가 → 샤워기 8개를 한 줄로 → **마지막 샤워기 입구에서 끝**. 건물은 필요한 만큼만 빼 가요.
2. **오염수 줄 (갈색):** 각 건물 출구에서 **짧게 위로 빼서** 천장 줄에 모읍니다. 위키 경고: 출구는 연결된 파이프 칸이 완전히 비어 있어야 나오기 때문에, **출구끼리 한 줄로 곧게 이으면 막힙니다.** 샤워기 쪽 모음 줄은 샤워실 천장을 지나 16번 칸 벽을 타고 올라와 화장실 쪽 줄과 만납니다.
3. **액체 다리로 우선순위** ([자세히](#우선순위-액체-다리-자세히)): 모인 오염수 → **액체 다리** → 물 정화기 입구. 그리고 **액체 다리 입구 칸에서 가지**를 하나 빼서 갈대 수경 재배 타일로 보냅니다. 위키 규칙: 다리 입구에 다른 파이프가 붙어 있으면 **다리가 꽉 찰 때까지 다리로만** 흐릅니다. 그래서 정화기가 먼저 받고, 루프가 꽉 차서 넘칠 때만 갈대로 갑니다.
4. **처음 채우기:** 깨끗한 물 수조 펌프(또는 수동 펌프·병 비우개)를 물 줄에 잠깐 이어서 파이프를 꽉 채운 뒤 **연결을 끊습니다.** 이후엔 수조 물을 안 씁니다.

### 우선순위 액체 다리 자세히

**왜 필요한가.** 파이프가 두 갈래로 나뉘면 액체 덩어리(패킷)가 **번갈아 반씩** 갈라져 갑니다 (위키: round-robin). 그냥 가지를 치면 오염수 절반이 갈대로 새서 정화기 쪽 물이 모자라요. 그래서 "정화기 먼저, 남을 때만 갈대"로 순서를 정해 줘야 합니다.

**액체 다리의 성질 (위키 Bridge Tricks).** 액체 다리 입구가 파이프에 붙어 있으면, **다리 출구 쪽 파이프에 자리가 있는 한 다리가 패킷을 항상 먼저 가져갑니다.** 다리가 못 받을 때만 패킷이 원래 파이프를 따라 계속 갑니다. 즉 다리 출구 쪽 = 1순위, 다리 입구 칸에서 이어지는 파이프 = 넘침 길.

```
오염수 모음 줄 ─→ [다리 입구]══액체 다리══[다리 출구] ─→ 물 정화기   (1순위)
                      │
                      └─→ 23번 줄 아래로 ─→ 갈대 수경 재배 타일        (넘칠 때만)
```

**짓는 법 (기계실 천장 줄)**

1. 오염수 모음 줄을 정화기 입력구까지 먼저 다 깝니다.
2. 정화기 입력구 바로 앞 파이프 **3칸을 철거**하고 그 자리에 **액체 다리 (3×1)**를 놓습니다. 다리 가운데 화살표가 **정화기 쪽**을 향해야 해요 (흰색 = 입구, 초록 = 출구, 놓기 전에 O 키로 회전). 다리는 벽·바닥 타일 속에도 놓을 수 있어서 식당 바닥 줄에 그대로 묻힙니다.
3. 넘침 파이프는 **다리 입구 칸에서 바로** 끌어냅니다. 입구보다 한 칸이라도 앞에서 가지를 치면 보통 갈림길이 돼서 반반 나뉘어요.
4. 넘침 파이프를 23번 줄로 내려 22번 수경 재배 타일 입구에 연결합니다.

**실제로 어떻게 흐르나**

| 상황 | 흐름 |
|---|---|
| 평소 (누가 화장실·샤워를 씀) | 물 줄이 비면 정화기가 돌고 → 정화기 입력 쪽이 비고 → 오염수는 **전부 다리로** 정화기에 |
| 물 줄이 꽉 참 (아무도 안 씀) | 정화기 출력이 막혀 정화기가 멈춤 → 다리 출구 파이프가 참 → 다리가 못 받음 → 오염수가 **넘침 줄로** 갈대에 |
| 하루 동안 | 수세식이 넣은 물보다 6.7 kg씩 더 내놔서, 사이클당 약 54 kg이 이렇게 갈대로 빠짐 |

**흔한 실수**

- 다리 방향을 반대로 놓음 → 정화기에 아무것도 안 감. 화살표 확인.
- 다리 입구가 아니라 그 앞 파이프에서 가지를 침 → 반반 갈라져 정화기 물이 모자람.
- 넘침 줄 끝이 막힘 (갈대를 안 심었거나, 22°C 아래로 식어 갈대가 멈춤) → 넘침이 갈 곳이 없어 **오염수가 거꾸로 차서 화장실 출구가 막힙니다.** 갈대 상태를 먼저 보세요.

> **안전장치 (선택):** 넘침 줄에 같은 방법으로 **액체 다리를 하나 더** 둡니다. 다리 출구 → 갈대 (1순위), 다리 입구 칸에서 가지 → 격벽 밖 오염수 수조의 **액체 배출구**. 갈대가 멈춰도 넘침이 수조로 빠져서 화장실이 안 막혀요.
{: .tip}

> **반대로 쓰는 법:** 다리 **출구**를 파이프 중간에 붙이면, 그 파이프에 자리가 있을 때만 다리 쪽 물이 들어갑니다 (2순위 공급). 나중에 루프 물이 모자랄 일이 생기면, 깨끗한 물 수조 펌프를 이렇게 물 줄에 붙여 두면 정화기 물이 우선이고 모자랄 때만 수조 물이 들어가요. 지금 루프는 물이 늘기만 해서 필요 없어요.
{: .tip}

### 물 수지 (8명, 1사이클)

| 건물 | 들어가는 물 | 나오는 오염수 |
|---|---|---|
| 수세식 (8회) | 40 kg | 94 kg |
| 싱크대 (8회) | 40 kg | 40 kg |
| 샤워기 (8회) | 128 kg | 128 kg |
| **합계** | **208 kg** | **262 kg** |

- 루프가 사이클마다 **약 54 kg 늘어납니다** (수세식 1회 +6.7 kg). 이게 넘침이고, 갈대 1그루가 하루 160 kg까지 받으니 **갈대 하나로 충분**합니다. 넘침이 160 kg보다 적어서 갈대는 물이 끊기는 동안 쉬며 천천히 자라요. 갈대 섬유는 환경 특수복·생물 콘도 재료입니다.
- 위키 기준 갈대 1그루 = 수세식 약 24회분 넘침. 복제체가 20명 넘게 늘면 갈대를 하나 더.
- 물 정화기는 사이클당 1분 정도만 돌고 모래를 약 52 kg 씁니다 (암석 분쇄기 부산물로 충분).

> **루프 물은 세균이 있습니다.** 정화기는 식중독 세균을 못 없애요. 이 물은 화장실·샤워실 전용이고, 넘친 오염수도 갈대에만 줍니다. 미생물 분쇄기·워터 쿨러·온실·전기분해기에는 절대 잇지 마세요 (위키 경고).
{: .warn}

> **갈대는 22~37°C에서만 자랍니다.** 기지를 20°C 아래로 식히면 갈대가 멈추니, 냉방 루프는 기계실 바닥 밑으로 지나가지 않게 하세요.
{: .tip}
