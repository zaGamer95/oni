---
title: 두 번째 행성 병행 개발 (텔레포터)
nav_title: 두 번째 행성 병행 개발
nav_order: 16
nav_group: early
dlc: spaced-out
permalink: /guide/second-planet/
description: Spaced Out!은 시작 행성만 파고 있으면 자원 종류가 모자라 발전이 느려집니다. 시작 행성이 안정되면 텔레포터로 두 번째 행성에 복제체를 보내 두 기지를 같이 키우고, 세 번째 행성은 첫 로켓으로 엽니다.
---

* 목차
{:toc}

## 한눈에

{: .ico-grid}
1. {% include i.html n="Terrania_Asteroid" %} **시작 행성 안정화**<br>사이클 25~45
2. {% include i.html n="Teleporter_Transmitter" %} **텔레포터로 1~2명**<br>연구 불필요
3. {% include i.html n="Oily_Swamp_Asteroid" %} **두 번째 기지 같이 키우기**<br>석유·황
4. {% include i.html n="Irradiated_Forest_Asteroid" %} **세 번째는 첫 로켓**<br>우라늄

Spaced Out!은 **행성마다 맡은 자원이 다릅니다.** 시작 행성에만 있으면 석유·황·우라늄이 없어 연구·건설이 같이 멈춰요. 실제 기록은 [사례 1]({{ '/guide/case/terrania-1/' | relative_url }}).

<details class="nums" markdown="1">
<summary>행성별 자원 (Terrania 클러스터)</summary>

| 자원 | 시작 행성 (Terrania) | 두 번째: 기름 늪 (Oily Swamp) | 세 번째: 방사능 숲 (Irradiated Forest) |
|---|---|---|---|
| 원유·석유 | **없음** | 석유층·원유 | |
| 황 | 황무지(Wasteland) 바이옴에 조금 | **황 분출구 (항상 있음)** | |
| 우라늄 | 있을 수도, 조금 | | **방사능 바이옴 (본산지)** |
| 플라스틱 | 번질한 기끌이 (Glossy Drecko) 목장으로만 | 원유 → 정유 → 폴리머 프레스 | |
| 복제체 | 프린팅팟 | **냉동 탱크 1명 (공짜)** | |
| 가는 법 | | **텔레포터** (연구 불필요) | 첫 로켓 (3칸) |


- 사람은 텔레포터 충전 5사이클마다, 자원은 공급 텔레포터로 쉬지 않고. 일찍 열수록 오래 받음.

</details>

## 언제 보내나

- [ ] **산소** 남음 (1명당 100 g/s 이상)
- [ ] **식량** 생산 ≥ 소비, 창고 3사이클치
- [ ] **물** 무한원 연결 (Terrania는 서늘한 증기 벤트)
- [ ] **화장실·샤워** 돌아감
- [ ] **전력** 스마트 배터리 자동
- [ ] **스트레스** 오르는 복제체 없음
- [ ] 떠나는 사람이 빠져도 연구·농사·건설이 돌아감

환경 특수복·연구는 필요 없음 (도착 지점은 보통 숨 쉴 수 있음). 별지도에서 대기만 확인.

## 텔레포터 두 종류

{: .ico-grid}
- {% include i.html n="Teleporter_Transmitter" %} **텔레포터 송신기 (Teleporter Transmitter)** 복제체, 5사이클 충전
- {% include i.html n="Supply_Teleporter_Input" %} **공급 텔레포터 입력 (Supply Teleporter Input)** 고체·액체·기체, 상시

> 공급 텔레포터는 양쪽에서 **현장 연구 (Field Research) 스킬** 복제체가 한 번씩 켜야 합니다. 첫 사람이 스킬을 찍고 가기.
{: .tip}

<details class="nums" markdown="1">
<summary>텔레포터 비교 표</summary>

| | 텔레포터 송신기 (Teleporter Transmitter) | 공급 텔레포터 입력 (Supply Teleporter Input) |
|---|---|---|
| 크기 | 4×3 | 4×3 |
| 보내는 것 | **복제체** | **고체·액체·기체** |
| 조건 | 한 번 쓰면 **5사이클 충전** | **Field Research 스킬** 복제체가 한 번 켜야 함 |
| 목적지 | 정해진 한 곳 | 정해진 한 곳 (공급 텔레포터 출력) |
| 같이 있는 것 | 두 번째 행성 쪽엔 냉동 탱크 | 컨베이어 적재기, 와이어 |

</details>

## 병행 개발 순서

{: .ico-grid}
1. {% include i.html n="Cryotank_3000" %} **출장소 (~5사이클)**<br>냉동 탱크 해동, 침대·뒷간, 공급 텔레포터
2. {% include i.html n="Oxygen_Diffuser" %} **자립 (~15사이클)**<br>현지 산소·식량·화장실·전력
3. {% include i.html n="Crude_Oil" %} **자원 공장**<br>원유·황 ↔ 정제 금속·씨앗

> 기름 늪의 **황 분출구**를 고체 황으로 → 벵이벵이·단벌레 목장 + 벵이과실 → **황 분출구 하나로 자립 기지** (위키 Oily Swamp Asteroid).
{: .tip}

<details class="nums" markdown="1">
<summary>주고받는 자원</summary>

| 방향 | 보내는 것 |
|---|---|
| 두 번째 → 시작 | **원유** (석유·플라스틱·석유 발전기), **황**, 금속 광석 |
| 시작 → 두 번째 | 정제 금속, 씨앗, 음식, 필요한 건물 재료 |

</details>

## 세 번째 행성: 첫 로켓

Terrania의 텔레포터는 **시작 ↔ 기름 늪** 한 쌍뿐. **방사능 숲 (3칸)**은 우주 프로그램 + 이산화탄소 엔진으로. 그 뒤 행성 거리는 [8명 중반 설계]({{ '/guide/midgame-8/#다른-소행성-진출-terrania-클러스터' | relative_url }}).

## 사람 배치

첫 사람은 **Supplying + Suit Wearing** 관심(운반 + 나중 특수복). 두 번째 행성은 1~2명이 같은 시간에 쉬는 일정을 따로.

<details class="nums" markdown="1">
<summary>시점별 배치 표</summary>

| 시점 | 시작 행성 | 두 번째 행성 | 로켓 |
|---|---|---|---|
| 처음 보낼 때 | 나머지 전부 | **운반·특수복** 1명 | |
| 냉동 탱크 해동 후 | 나머지 | 1~2명 (해동 복제체가 남거나 시작 행성으로) | |
| 첫 로켓 | 나머지 | 1~2명 | 조종사 + 1명 |

</details>

<details class="nums" markdown="1">
<summary>출처</summary>

- 공식 위키 (oxygennotincluded.wiki.gg): Teleporter Transmitter, Supply Teleporter Input, Oily Swamp Asteroid, Terrania Asteroid, Cryotank 3000
- 행성별 자원은 Terrania 클러스터 기본 생성 기준입니다. 시드에 따라 트레잇(금속 많음 등)이 붙으니 [트레잇과 시드 리롤]({{ '/guide/traits/' | relative_url }})에서 확인하세요.

</details>
