---
title: 에어컨 설치 (수냉 조절기 + 증기 터빈)
nav_title: 에어컨 설치
nav_order: 9.9
nav_num: "9-9"
nav_group: play
nav_parent: core-base
permalink: /guide/core-base/aircon/
description: 단열 격벽 기지를 20~25°C로 유지하는 냉방 설계. 냉방실 도면, 수냉 조절기·냉각 루프·온도 센서 설치 순서, 열 계산, 증기 터빈으로 열 지우기, 문제 해결.
---

* 목차
{:toc}

> [9-3 단열·냉방 시작하기]({{ '/guide/core-base/envelope/' | relative_url }}#단열냉방-시작하기-단계별)의 4·5단계를 한 페이지로 자세히 푼 것입니다. 수치는 공식 위키 건물·원소 데이터 기준이에요.
{: .tip}

## 한 줄 요약

**기지 안 바닥을 도는 냉각수 고리 하나 + 격벽 밖 냉방실 하나.** 냉각수가 기지 열을 주워 냉방실로 가져가면, **수냉 조절기**가 그 열을 냉방실 오염수(약 20톤)에 버립니다. 냉방실 물이 끓어 증기가 되면 그 위에 **증기 터빈**을 얹어 열을 전기로 바꿔 지웁니다.

## 설계: 열이 어디서 와서 어디로 가나

에어컨은 열을 **막고 → 옮기고 → 지우는** 세 부분입니다. 하나라도 빠지면 언젠가 다시 더워져요.

| 부분 | 하는 일 | 장치 | 페이지 |
|---|---|---|---|
| **막기** | 열이 기지로 안 들어오게 | 열원을 격벽 밖으로, 단열 타일 격벽, SPOM 산소 식히기 | [9-3 1~3단계]({{ '/guide/core-base/envelope/' | relative_url }}#1단계-열원-찾기-지금-바로) |
| **옮기기** | 기지 안 열을 냉방실로 | 냉각 루프(파이프 고리) + 수냉 조절기 + 온도 센서 | 이 페이지 1~6단계 |
| **지우기** | 냉방실에 쌓인 열을 없애기 | 증기 터빈 (열 → 전기) | 이 페이지 7단계 |

```
  기지 안 (20~25°C)            격벽            냉방실 (격벽 밖)
  ─────────────────            ────            ────────────────
  복제체·조명·펌프 열   →  냉각수(오염수)가 주움  →  수냉 조절기: 냉각수 −14°C
  실내 온실 바닥 밑                                   ↓ 뺀 열은 냉방실 물로
  ↑ 4~18°C로 돌아옴     ←  절연 파이프로 통과    ←  물 20톤이 데워짐 → 끓어서 증기
                                                      ↓
                                                   증기 터빈: 증기 열 → 전기 (열이 사라짐)
```

### 왜 이렇게 정했나

| 결정 | 이유 |
|---|---|
| 냉방실은 **격벽 밖**, 발전소 옆 | 수냉 조절기는 열을 지우지 않고 **자기 몸으로 옮깁니다.** 조절기와 냉방실은 계속 뜨거워지니 기지 밖에. 발전소 옆이라 헤비와트 와이어도 짧음 |
| 냉각수는 **오염수** | 조절기는 지나가는 액체를 **14°C** 식힙니다. 물은 0°C 근처에서 얼어 파이프가 터지지만 **오염수는 −20.65°C**에서 얼어 여유가 큽니다. 파이프 속이라 냄새(오염 산소)도 안 나요. W 화면에서도 오염수 24.9°C로 돌림 |
| 조절기는 **금 아말감** | 기본 과열 온도 **125°C**. 증기 터빈은 125°C 넘는 증기가 있어야 돌아서 구리로 지으면 터빈 단계에서 고장. 금 아말감은 **+50 → 175°C**. 나중에 금속 정제기 열까지 받으면 **강철(+200 → 325°C)** 로 하나 더 |
| 냉방실 물 **약 20톤** | 터빈이 생기기 전까지 열을 받아 두는 통. 많을수록 천천히 데워져 시간을 벌고, 적을수록 빨리 증기가 돼 터빈을 서둘러야 함 (아래 열 계산) |
| 센서 **18°C 이상 켜기** | 돌아오는 냉각수가 18°C 아래면 기지는 이미 충분히 시원한 것. 꺼 두면 전기(1.2 kW)와 냉방실 열이 줄고, 나오는 물도 18 − 14 = **4°C 아래로 안 내려감** |
| 기지 안 파이프는 **그냥 액체 파이프** | 기지 안에서는 열을 **주워야** 하니 단열하면 안 됨. 격벽을 지나 냉방실까지 가는 구간만 **절연 액체 파이프** |
| 루프는 **격벽 바닥 줄 + 실내 온실 밑** | 열은 위로 오르고 아래(발전소)에서 올라오니 바닥이 1순위. 끼니나무·센털꽃은 30°C 넘으면 안 자라서 온실 밑을 꼭 지나게 |

> 기체용 **열 조절기**(Thermo Regulator)도 있지만 기체 1 kg/s만 식혀서 한 번에 옮기는 열이 약 14 kDTU/s, 수냉 조절기(오염수 10 kg/s, **약 585 kDTU/s**)의 40분의 1입니다. 기지 전체 냉방은 수냉 조절기로 하세요.
{: .tip}

## 준비물

| 건물 | 크기 | 재료 | 연구 | 전력 |
|---|---|---|---|---|
| **단열 타일 (Insulated Tile)** | 1×1 | 원료 광물 400 kg/칸. **세라믹**이 화성암보다 열을 3배 덜 전함 (0.62 vs 2) | 온도 조절 (Temperature Modulation, 3단계) | – |
| **절연 액체 파이프 (Insulated Liquid Pipe)** | 1×1 | 원료 광물 400 kg/칸 (화성암 OK) | 개선된 파이프 (Improved Plumbing, 3단계) | – |
| 액체 파이프 (Liquid Pipe) | 1×1 | 원료 광물 100 kg/칸 | 액체 파이프 (Plumbing) | – |
| **수냉 조절기 (Thermo Aquatuner)** | 2×2 | **금속 광석 1,200 kg** (금 아말감) | **액체 조율 (Liquid Tuning, 4단계)** | **1,200 W** |
| **액체 파이프 온도 센서 (Liquid Pipe Thermo Sensor)** | 1×1 | 정제 금속 25 kg | 액체 조율 | – |
| 자동화 와이어 | 1×1 | 정제 금속 5 kg/칸 | 자동화 | – |
| **헤비와트 와이어 (Heavi-Watt Wire)** + 연결판 (Joint Plate) | 1×1 | 금속 광석 100 kg/칸 | 고급 전력 조절 (Advanced Power Regulation) | 최대 20 kW |
| 액체 펌프 (Liquid Pump) | 2×2 | 금속 광석 400 kg | 액체 파이프 | 240 W (처음 채울 때만) |
| 7단계: **증기 터빈 (Steam Turbine)** | 5×3 | **정제 금속 800 kg** + 개스킷 재료 4 kg | 재생 에너지 (Renewable Energy, 5단계) | **최대 +850 W** |
| 7단계: 방열 액체 파이프 (Radiant Liquid Pipe) | 1×1 | 정제 금속 50 kg/칸 | 액체 조율 | – |

정제 금속은 1~6단계에 **센서 25 kg + 자동화 와이어 몇 칸 ≈ 75 kg**뿐이라 [암석 분쇄기]({{ '/guide/core-base/refining/' | relative_url }})로 충분합니다.

## 냉방실 도면 (14×4)

**칸 수 그대로** 그린 도면입니다 (격자 1칸 = 1타일). 위치는 [전체 도면]({{ '/guide/core-base/#후반-완성-배치도' | relative_url }})의 냉방실, 격벽 바로 아래 발전소 옆이에요. 냉방실 위 3칸은 **증기 터빈 자리로 비워 둡니다.**

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 622 410" width="622" role="img" aria-label="냉방실 칸별 도면: 수냉 조절기, 오염수, 증기 터빈 자리" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect x="1.4210854715202004e-14" y="0.0" width="622.0" height="410.0" fill="#11131f" /><rect x="120" y="40" width="352" height="22" fill="#7a5a44" /><text x="131.0" y="55.0" fill="#f3e3d3" font-size="10" text-anchor="start">단열 격벽 (위 = 생활 구역)</text><rect x="142" y="62" width="308" height="66" fill="#151827" /><rect x="120" y="128" width="352" height="22" fill="#7a5a44" /><rect x="120" y="238" width="352" height="22" fill="#7a5a44" /><rect x="120" y="150" width="22" height="88" fill="#7a5a44" /><rect x="450" y="150" width="22" height="88" fill="#7a5a44" /><rect x="120" y="62" width="22" height="66" fill="#7a5a44" /><rect x="450" y="62" width="22" height="66" fill="#7a5a44" /><rect x="142" y="150" width="308" height="88" fill="#1c2036" /><rect x="142" y="216" width="308" height="22" fill="#2c6d8c" /><rect x="142" y="194" width="132" height="22" fill="#2c6d8c" /><line x1="142" y1="62" x2="142" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="164" y1="62" x2="164" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="186" y1="62" x2="186" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="208" y1="62" x2="208" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="230" y1="62" x2="230" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="252" y1="62" x2="252" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="274" y1="62" x2="274" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="296" y1="62" x2="296" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="318" y1="62" x2="318" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="340" y1="62" x2="340" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="362" y1="62" x2="362" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="384" y1="62" x2="384" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="406" y1="62" x2="406" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="428" y1="62" x2="428" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="450" y1="62" x2="450" y2="238" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="62" x2="450" y2="62" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="84" x2="450" y2="84" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="106" x2="450" y2="106" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="128" x2="450" y2="128" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="150" x2="450" y2="150" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="172" x2="450" y2="172" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="194" x2="450" y2="194" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="216" x2="450" y2="216" stroke="#fff" stroke-opacity=".07"/><line x1="142" y1="238" x2="450" y2="238" stroke="#fff" stroke-opacity=".07"/><text x="153.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">1</text><text x="175.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">2</text><text x="197.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">3</text><text x="219.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">4</text><text x="241.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">5</text><text x="263.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">6</text><text x="285.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">7</text><text x="307.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">8</text><text x="329.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">9</text><text x="351.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">10</text><text x="373.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">11</text><text x="395.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">12</text><text x="417.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">13</text><text x="439.0" y="34" fill="#cfd3e6" font-size="9" text-anchor="middle">14</text><rect x="165" y="63" width="108" height="64" fill="#8a9bd0" fill-opacity=".28" stroke="#8a9bd0" stroke-width="2" stroke-dasharray="5 3"/><text x="219.0" y="97.0" fill="#e9ecf8" font-size="10" text-anchor="middle" font-weight="700">증기 터빈 5×3</text><text x="219.0" y="109.0" fill="#c9d1f0" font-size="9" text-anchor="middle">(7단계, 나중에)</text><path d="M171 164 L175 156 L179 164" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><path d="M193 164 L197 156 L201 164" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><path d="M215 164 L219 156 L223 164" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><path d="M237 164 L241 156 L245 164" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><path d="M259 164 L263 156 L267 164" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><rect x="341" y="195" width="42" height="42" fill="#e0b060" stroke="#11131f"/><text x="362.0" y="208.0" fill="#11131f" font-size="10" text-anchor="middle" font-weight="700">수냉</text><text x="362.0" y="228.0" fill="#11131f" font-size="10" text-anchor="middle" font-weight="700">조절기</text><path d="M307 51 L307 73" fill="none" stroke="#ff9a5c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/><path d="M307 73 L175 73" fill="none" stroke="#ff5c8a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/><path d="M175 73 L153 73 L153 183 L351 183 L351 205" fill="none" stroke="#ff9a5c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/><path d="M373 205 L373 183 L395 183 L395 51" fill="none" stroke="#5fd0ff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/><path d="M263 117 L285 117 L285 161" fill="none" stroke="#ffe284" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/><rect x="279" y="155" width="12" height="12" fill="#ffe284"/><line x1="114" y1="216" x2="340" y2="216" stroke="#acffbd" stroke-width="3" stroke-dasharray="7 4"/><rect x="123" y="209" width="16" height="14" fill="#24452e" stroke="#acffbd"/><line x1="114" y1="117" x2="164" y2="117" stroke="#acffbd" stroke-width="3" stroke-dasharray="7 4" stroke-opacity=".6"/><text x="112" y="220.0" fill="#acffbd" font-size="10" text-anchor="end">발전소 ←</text><text x="112" y="121.0" fill="#acffbd" font-size="10" text-anchor="end">발전소 ←</text><text x="480" y="39.0" fill="#5fd0ff" font-size="10" text-anchor="start">↑ 기지로 (차가움)</text><text x="480" y="55.0" fill="#ff9a5c" font-size="10" text-anchor="start">↓ 기지에서 (18°C+)</text><text x="480" y="165.0" fill="#a9b0d0" font-size="10" text-anchor="start">공기·증기층</text><text x="480" y="220.0" fill="#8fe3ff" font-size="10" text-anchor="start">오염수 약 20톤</text><text x="480" y="143.0" fill="#f3e3d3" font-size="10" text-anchor="start">천장 = 단열 타일</text><rect x="20" y="277" width="14" height="12" fill="#7a5a44"/><text x="40" y="287" fill="#e9ecf8" font-size="10" text-anchor="start">단열 타일 (격벽·냉방실 벽)</text><rect x="300" y="277" width="14" height="12" fill="#2c6d8c"/><text x="320" y="287" fill="#e9ecf8" font-size="10" text-anchor="start">오염수 (바닥 1줄 + 6칸 ≈ 20톤)</text><line x1="20" y1="305" x2="34" y2="305" stroke="#ff9a5c" stroke-width="4"/><text x="40" y="309" fill="#e9ecf8" font-size="10" text-anchor="start">돌아오는 냉각수: 절연 액체 파이프</text><line x1="300" y1="305" x2="314" y2="305" stroke="#ff5c8a" stroke-width="4"/><text x="320" y="309" fill="#e9ecf8" font-size="10" text-anchor="start">방열 액체 파이프 (터빈 식히기, 7단계 때)</text><line x1="20" y1="327" x2="34" y2="327" stroke="#5fd0ff" stroke-width="4"/><text x="40" y="331" fill="#e9ecf8" font-size="10" text-anchor="start">식은 냉각수: 절연 액체 파이프 → 기지</text><line x1="300" y1="327" x2="314" y2="327" stroke="#ffe284" stroke-width="4"/><text x="320" y="331" fill="#e9ecf8" font-size="10" text-anchor="start">터빈이 내보내는 95°C 물 → 액체 배출구</text><line x1="20" y1="349" x2="34" y2="349" stroke="#acffbd" stroke-width="3" stroke-dasharray="4 2"/><text x="40" y="353" fill="#e9ecf8" font-size="10" text-anchor="start">헤비와트 와이어 (벽은 연결판으로)</text><path d="M303 352 L307 344 L311 352" fill="none" stroke="#c9d1f0" stroke-width="1.5"/><text x="320" y="353" fill="#e9ecf8" font-size="10" text-anchor="start">터빈이 증기를 빨아들이는 5칸</text></svg>
</div>

- 수냉 조절기는 **바닥 오른쪽**에 두고, 터빈은 **왼쪽 위**에. 터빈이 빨아들이는 천장 밑 5칸과 조절기가 떨어져 있어야 뜨거운 증기가 터빈 쪽으로 잘 갑니다.
- 냉방실 안을 지나는 냉각수 파이프도 **절연 액체 파이프**로. 일반 파이프면 조절기에 들어가기 전에 냉방실 열을 다시 주워 와서 냉방이 약해져요.
- 왼쪽 벽 아래 초록 칸이 헤비와트 **연결판**. 헤비와트 와이어는 타일을 그냥 못 지나갑니다.

{% include shot.html src="steam-cooler.jpg" size="half" caption="W 기존 가이드의 실제 냉방실. 위에 증기 터빈, 아래 단열 타일로 막은 방 안에 수냉 조절기." %}

## 단계별 설치

### 0단계: 먼저 막기 (9-3의 1~3단계)

- [ ] 온도 오버레이로 격벽 안 **30°C 넘는 곳**을 찾아 석탄 발전기·암석 분쇄기·전기분해기(SPOM)·전기 그릴을 격벽 밖으로
- [ ] 단열 타일: **격벽 바닥 줄 → 냉방실 4면 → 통로 → 나머지** 순서
- [ ] SPOM 산소 파이프를 격벽 밖 **오염수 수조 속 10칸**쯤 지나게 (70°C → 수조 온도)

> 이걸 안 하고 에어컨부터 달면 조절기가 쉬지 않고 돌아서 냉방실이 몇 배 빨리 뜨거워집니다. **에어컨은 막고 남은 열만 옮기는 장치**예요.
{: .warn}

### 1단계: 냉방실 파고 벽 세우기

- [ ] 격벽 바로 아래, 발전소 옆에 **안쪽 14×4**를 비웁니다. 위로 3칸(터빈 자리)도 같이 파 두기
- [ ] 벽·천장·바닥을 전부 **단열 타일**로 (16×6 테두리 ≈ 40칸, 원료 광물 약 16톤). 냉방실은 100°C를 넘어가니 처음부터 단열
- [ ] 출입구는 하나만, 나중에 막을 수 있게 **문 대신 타일 한 칸 비우기 → 다 지으면 타일로 막기**. 냉방실은 복제체가 드나들 일이 없습니다

### 2단계: 오염수 약 20톤 채우기

- [ ] 근처 **오염수 웅덩이**(습지 바이옴)에 액체 펌프 → 파이프 → 냉방실 안 **액체 배출구**로 20톤. 바닥 1줄(14톤) + 둘째 줄 절반쯤
- [ ] 다 차면 펌프·배출구를 떼고 입구 타일을 막습니다
- [ ] 오염수가 모자라면 양을 줄여도 됩니다 (5~10톤). 대신 더 빨리 끓으니 **7단계 터빈을 그만큼 서두르기**

> 화장실 오염수 수조(사이클당 약 180 kg)로 20톤을 채우려면 100사이클이 넘게 걸려요. 바깥 웅덩이에서 한 번에 퍼 오는 게 맞습니다.
{: .tip}

### 3단계: 수냉 조절기 + 전기

- [ ] **액체 조율** 연구 → 수냉 조절기를 **금 아말감 1,200 kg**으로 냉방실 바닥 오른쪽에 (도면의 10~11번 칸)
- [ ] 발전소 **헤비와트 와이어**에서 바로 끌어오기. 벽은 **연결판**으로 통과. 일반 와이어는 1 kW까지라 1.2 kW 조절기를 못 버팁니다
- [ ] 헤비와트 와이어는 장식도 −25라 **격벽 안으로는 들이지 않기** (냉방실이 격벽 밖이라 자연스럽게 해결)

### 4단계: 냉각 루프 깔기

냉각수가 가는 길은 **한 줄짜리 고리**입니다. 펌프 없이 수냉 조절기가 직접 밀어 줍니다.

```
조절기 출구 ─(절연)→ 격벽 통과 ─(일반 파이프)→ 격벽 안 바닥 줄 → 실내 온실 밑 → 생활 코어 바닥
     ↑                                                                    │
     └───(절연)── 냉방실 ←── 격벽 통과 ←── [온도 센서] ←─────────────────┘
```

- [ ] 조절기 **출구**에서 **절연 액체 파이프**로 냉방실 천장 → 산업층 → 격벽까지
- [ ] 격벽 안은 **일반 액체 파이프**로 **바닥 줄을 따라 한 바퀴**: 실내 온실 A·B 바닥 밑, 생활 코어 바닥, 침실 블록 바닥. 파이프는 타일 뒤로 지나가도 됩니다
- [ ] 돌아오는 길도 **절연 액체 파이프**로 격벽 → 냉방실 → 조절기 **입구**
- [ ] 고리 길이는 **100칸 안팎**이면 충분. 너무 길면 처음 채울 오염수만 늘어나요 (칸당 10 kg)

> 나중에 정제 금속이 남으면 **실내 온실 구간만 방열 액체 파이프**로 바꾸세요 (칸당 정제 금속 50 kg). 일반 파이프보다 열을 빨리 주워서 온실이 먼저 식습니다. 처음엔 일반 파이프로 충분해요.
{: .tip}

### 5단계: 냉각수 채우기 (처음 한 번)

- [ ] 오염수 수조 바닥 **액체 펌프**의 출구 파이프를 고리 아무 곳에나 잠깐 잇습니다
- [ ] 액체 오버레이에서 고리 전체가 **칸마다 10 kg**으로 차면(펌프가 "출구 막힘"이 됨) **잇는 파이프 한 칸을 철거**
- [ ] 조절기는 지나가는 액체 **질량만큼** 열을 옮깁니다. 칸당 10 kg으로 꽉 차야 1.2 kW 값을 제대로 함

### 6단계: 온도 센서로 켜고 끄기

- [ ] **액체 파이프 온도 센서**를 **돌아오는 줄**, 격벽 안에서 **격벽을 나가기 직전** 일반 파이프 칸에
- [ ] 설정: **18°C 이상(Above)이면 초록 신호** → 자동화 와이어로 조절기에 연결
- [ ] 기지 안에 두는 이유: 센서가 냉방실 근처에 있으면 냉방실 열 때문에 실제보다 높게 읽어서 조절기가 쉬지 않습니다

| 돌아오는 냉각수 | 조절기 | 나오는 냉각수 |
|---|---|---|
| 18°C 이상 (기지가 따뜻함) | **켜짐** | 들어온 온도 − 14°C (예: 22°C → 8°C) |
| 18°C 아래 (충분히 시원) | 꺼짐 | – |

### 확인: 처음 5사이클

- [ ] 온도 오버레이에서 **실내 온실 바닥 → 생활 코어** 순서로 초록(20~25°C)이 번지는지
- [ ] 조절기가 **계속 켜져 있으면**: 남은 열원(특히 SPOM 산소 파이프, 격벽 안 펌프·조명)을 다시 찾기
- [ ] **냉방실 온도**를 사이클마다 한 번 보기. 이 숫자가 7단계(증기 터빈) 일정표입니다

## 열 계산: 터빈까지 얼마나 남았나

| 항목 | 값 | 메모 |
|---|---|---|
| 조절기가 한 번에 옮기는 열 | **약 585 kDTU/s** | 오염수 10 kg/s × 비열 4.179 × 14°C |
| 냉방실 오염수 20톤을 30°C → 끓는점 119°C | 약 **750만 kDTU** | 20,000 × 4.179 × 89 |
| 조절기가 **계속** 켜져 있으면 | 약 **21사이클** | 단열을 안 했을 때에 가까움 |
| 단열 후 **4분의 1만** 켜지면 | 약 **85사이클** | 보통 이 정도. 그 안에 재생 에너지 연구 + 정제 금속 800 kg |
| 증기 터빈 최대 | 증기 2 kg/s, **850 W** (200°C 증기일 때) | 125°C 넘는 증기만 씀. 증기를 95°C 물로 바꾸며 열을 지움 |
| 조절기 100% 가동 때 냉방실 | 약 **165°C**에서 균형 | 터빈이 지우는 열 = 조절기가 넣는 열. 금 아말감 175°C 안쪽. 터빈 출력 약 570 W |

> **냉방실이 119°C 근처에서 한동안 멈춰 있는 건 정상**입니다. 오염수가 끓어 증기(+ 흙 1%)로 바뀌는 중이에요. 물이 다 증기가 되면 온도가 다시 오르고, 125°C를 넘으면 터빈이 돌기 시작합니다.
{: .tip}

## 7단계: 증기 터빈 (냉방실 100°C 넘기 전에)

- [ ] 연구 **재생 에너지 (Renewable Energy, 5단계)**, 정제 금속 800 kg 준비 (암석 분쇄기로 광석 1,600 kg)
- [ ] 냉방실 **천장 왼쪽** 단열 타일 위에 **증기 터빈 5×3**. 터빈은 **바로 아래 천장 밑 5칸**에서 증기를 빨아들입니다
- [ ] 터빈 **물 출구 → 파이프 → 냉방실 안 액체 배출구**. 터빈은 증기를 **95°C 물**로 내보내고, 이 물이 다시 데워져 증기가 되는 고리. 출구가 막히면 터빈이 멈춥니다
- [ ] 터빈 **전력 출구 → 발전소 헤비와트 와이어**. 조절기 1.2 kW의 절반쯤을 다시 벌어 옵니다
- [ ] **터빈 식히기:** 터빈은 자기 온도가 **100°C를 넘으면 멈춥니다.** 돌아오는 냉각수 줄을 냉방실로 들어가기 직전에 **방열 액체 파이프로 터빈 뒤를 한 번 지나가게** 하세요 (도면의 분홍 줄, 5칸 = 정제 금속 250 kg). 터빈 열이 냉각수로 들어가고 → 조절기가 다시 냉방실 증기로 → 터빈이 지우는 **자가 냉각**이 됩니다
- [ ] 터빈은 건설 조건에 **전력 기술자 (Power Technician) 스킬**이 붙어 있어요. 안 지어지면 건설 담당 복제체 스킬을 확인

{% include shot.html src="steam-cooler-gas2.jpg" size="half" caption="W 기존 가이드: 터빈이 내보내는 물(노란 파이프)을 다시 증기 방으로." %}

## 8단계: 그 다음 (금속 정제기, 두 번째 조절기)

- 터빈이 돈 뒤에야 [금속 정제기]({{ '/guide/core-base/refining/' | relative_url }})를 짓고, 정제기 냉각수 파이프를 **이 냉방실 안으로 지나가게** 합니다. 정제기 열은 구리 100 kg 한 번에 냉방실 물 20톤이 390°C 오를 양이라, **터빈 없이 정제기를 돌리면 냉방실이 바로 터집니다.**
- 정제기 열까지 받으면 냉방실이 175°C를 넘을 수 있어요. 그때는 **강철 수냉 조절기**로 바꾸거나 하나 더 달고, 터빈도 하나 더 (냉방실 14칸이라 터빈 2대 자리가 있음).
- 기지가 8명 + 온실 2개를 넘어 커지면 수냉 조절기 1대로 모자랄 수 있습니다. 그때도 같은 냉방실에 **조절기를 하나 더** 넣고 루프를 하나 더 돌리면 됩니다.

## 문제 해결

| 증상 | 원인 | 해결 |
|---|---|---|
| 파이프가 터짐 (얼음) | 냉각수가 **깨끗한 물**이고, 차가운 물이 다시 들어와 0°C 아래로 | 냉각수를 **오염수**로 바꾸기. 센서 18°C 이상 설정 확인 |
| 조절기 **과열** 경고 | 구리·철광석 등으로 지어 125°C 한계 | **금 아말감**(175°C)이나 **강철**(325°C)로 다시 짓기. 재료는 교체가 안 되니 철거 후 재건설 |
| 기지가 안 식음 | 고리가 덜 참 / 기지 안 파이프가 절연 / 열원이 남음 | 액체 오버레이로 칸당 10 kg 확인. 기지 안은 **일반 파이프**. SPOM 산소 온도 확인 |
| 조절기가 안 켜짐 | 센서 방향이 반대 (아래면 켜기) | **이상(Above) 18°C**로 |
| 냉방실이 119°C에서 오래 머묾 | 오염수가 끓는 중 | 정상. 터빈 준비 |
| 터빈이 안 돔 | 증기 125°C 미만 / 터빈 자체가 100°C 넘음 / 물 출구 막힘 | 기다리기 / 방열 파이프 자가 냉각 / 출구 파이프를 배출구까지 |
| 냉방실 증기가 기지로 샘 | 천장·벽에 일반 타일이나 문 | 전부 **단열 타일**, 입구는 타일로 막기 |

## 체크리스트

- [ ] 열원 밖으로, 단열 격벽, SPOM 산소 식히기 (9-3)
- [ ] 냉방실 14×4 + 위 3칸, 벽은 전부 단열 타일
- [ ] 오염수 약 20톤
- [ ] 금 아말감 수냉 조절기 + 헤비와트 (연결판)
- [ ] 냉각 루프: 절연 → 기지 안 일반 파이프(바닥 줄·온실 밑) → 절연
- [ ] 오염수로 칸당 10 kg 채우고 펌프 연결 끊기
- [ ] 액체 파이프 온도 센서, 돌아오는 줄 격벽 안, **18°C 이상 켜기**
- [ ] 냉방실 온도 매 사이클 확인 → 100°C 전에 **증기 터빈** + 물 되돌리기 + 방열 파이프 자가 냉각
- [ ] 터빈이 돈 뒤 금속 정제기

<p class="credit">게임 화면 © Klei Entertainment · 비공식 팬 가이드</p>
