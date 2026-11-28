---
title: "실제 플레이 사례 1: Terrania 클러스터"
nav_title: "개요: 시드·복제체"
nav_order: 30
nav_num: "①"
nav_group: case
dlc: spaced-out
game_version: u60-2026-11-20
eyebrow: 실제 플레이 사례 1
permalink: /guide/case/terrania-1/
description: W의 실제 Spaced Out! 판(Terrania 클러스터)을 처음 시드부터 그대로 기록합니다. 시작 행성을 안정시킨 뒤 텔레포터로 두 번째 행성을 같이 키우는 흐름, 그리고 이 판에서 배운 것을 가이드에 어떻게 반영했는지.
---

* 목차
{:toc}

> 일반 가이드는 "대부분의 판에 맞는 순서", 이 페이지는 **한 판의 기록**. 여기서 더 나은 순서가 나오면 가이드도 고칩니다 ([반영한 것](#이-판에서-가이드로-옮긴-것)).
{: .tip}

## 챕터

<details class="nums" markdown="1">
<summary>챕터 목록 (11개)</summary>

| 장 | 행성 | 내용 |
|---|---|---|
| [1장 Persephazon]({{ '/guide/case/terrania-1/persephazon/' | relative_url }}) | 시작 행성 | 기지 세우기, 안정화, 텔레포터로 두 번째 행성 보내기 |
| [1-1 열 문제·기끌이 목장]({{ '/guide/case/terrania-1/drecko-ranch/' | relative_url }}) | 시작 행성 | 에어컨 없이 열 막기, 2LegitCity식 기끌이 목장 (사이클 108) |
| [1-2 사이클 160: 수조·무한 SPOM]({{ '/guide/case/terrania-1/persephazon/cycle-160/' | relative_url }}) | 시작 행성 | 염수 수조, 전해조 3대 SPOM, 터빈 전 전력 |
| [1-3 개인 침실 8칸 배치]({{ '/guide/case/terrania-1/persephazon/bedrooms/' | relative_url }}) | 시작 행성 | 텔레포터를 피해 큰 회관 위에 6×4 침실 6칸 + 기존 침대 2, 병원 |
| [2장 Oozato]({{ '/guide/case/terrania-1/oozato/' | relative_url }}) | 기름 늪 | 전력 0에서 자립까지, 단계 A~E (사이클 108) |
| [2-1 사이클 142 점검]({{ '/guide/case/terrania-1/oozato/check-142/' | relative_url }}) | 기름 늪 | 다섯 질문으로 본 Oozato, 닫힌 고리 |
| [2-2 단계별 플랜]({{ '/guide/case/terrania-1/oozato/plan/' | relative_url }}) | 기름 늪 | 0~8단계, 2명 → 4~6명 |
| [2-3 기지 배치 v2]({{ '/guide/case/terrania-1/oozato/layout/' | relative_url }}) | 기름 늪 | 텔레포터 홀 식당, 개인 침실, 세로 통로 |
| [3장 두 기지 교환 구조]({{ '/guide/case/terrania-1/link/' | relative_url }}) | 두 행성 | Oozato·본진이 주고받는 것, 사이클당 양, 여는 순서 |
| [4장 세 번째 행성과 그다음]({{ '/guide/case/terrania-1/next/' | relative_url }}) | 방사능 숲 외 | 첫 로켓, 이후 행성 순서 |

</details>

## 시드: 가까운 두 행성이 둘 다 금속

{% include shot.html src="case1-traits.jpg" caption="시작 화면. Terrania 클러스터, 생존 확률 Ideal, 스토리 트레잇 5개." %}

{: .ico-grid}
- {% include i.html n="Terrania_Asteroid" %} **Terrania (시작)** 나쁜 트레잇 없음
- {% include i.html n="Oily_Swamp_Asteroid" %} **기름진 늪 소행성 (Oily Swamp Asteroid)** 텔레포터, 금속 동굴 (Metallic Caves)
- {% include i.html n="Irradiated_Forest_Asteroid" %} **방사능 가득한 숲 소행성 (Irradiated Forest Asteroid)** 첫 로켓, 금속 풍족 (Metal Rich) + 금속 동굴
- {% include i.html n="Cryotank_3000" %} **표토 소행성** 언 친구 (Frozen Friend), 결원 충원용

<details class="nums" markdown="1">
<summary>좌표와 소행성별 트레잇 전체</summary>

| 항목 | 값 |
|---|---|
| 게임 | Spaced Out! + 모든 DLC |
| 클러스터 | **Terrania 클러스터** (사암 시작) |
| 좌표 | `SNDST-C-933086379-HIJYM31-V9-CKZRH…` (스크린샷에서 잘린 부분까지) |
| 생존 확률 | Ideal |

| 소행성 | 거리 | 트레잇 | 의미 |
|---|---|---|---|
| **Terrania** (시작) | | 없음 | 합격 |
| **방사능 숲** | 근처 | 금속 풍족 + 금속 동굴 ✅✅ | 세 번째 행성. 우라늄 + 금속 |
| **기름 늪** | 근처, 텔레포터 | 금속 동굴 ✅ | 두 번째 행성. 원유·황 + 금속 광석 |
| 툰드라 | 먼 곳 | 금속 부족 (Metal Poor) | 늦게 가니 무관 |
| 습지 | 먼 곳 | 금속 풍족 ✅ | 네 번째 후보 |
| 표토 | 먼 곳 | 언 친구 ✅ | 냉동 탱크 1명 더 |
| 무, 물 | 먼 곳 | 없음 | |

스토리 트레잇 5개: 솜늄 합성기 (Somnium Synthesizer), 신비한 은둔자 (Mysterious Hermit), 프린터셉터 (Printerceptor), 크리터 플럭스-오-매틱 (Critter Flux-O-Matic), 바이오봇 빌더 (Biobot Builder). 자세히는 [3 트레잇과 시드 리롤]({{ '/guide/traits/#스토리-트레잇-전체-6개' | relative_url }}).

</details>

## 복제체 8명 (사이클 108)

{% include shot.html src="case1-duplicants.jpg" caption="시작 행성 Persephazon(=Terrania) 6명, 두 번째 행성 Oozato(=기름 늪) 2명. 사기는 '지금/요구치'." %}

{: .ico-grid}
- {% include i.html n="Printing_Pod" %} **8명 달성** 프린팅팟 7 + 냉동 탱크 1
- **말랑 사기 여유 0** 굴착 스킬 요구치. 스킬 아껴 두기
- {% include i.html n="Teleporter_Transmitter" %} **Oozato 2명** 청소+특수복, 굴착+건설
- **첫 로켓** 본진 1명이 로켓 공학 (Rocketry) 찍고 왕복

<details class="nums" markdown="1">
<summary>복제체별 역할·위치·사기, 배치 계획</summary>

| 복제체 | 역할 | 있는 곳 | 사기 (지금/요구) | 여유 |
|---|---|---|---|---|
| 양자역학싫어요 | **연구** | Persephazon | 23 / 15 | +8 |
| 감자 | **농사** | Persephazon | 19 / 10 | +9 |
| 마이메 | **건설 + 목축** | Persephazon | 19 / 13 | +6 |
| 말랑 | **굴착** | Persephazon | 14 / 14 | **0** |
| 안성재 | **요리** | Persephazon | 21 / 12 | +9 |
| 젠슨황 | **운반** | Persephazon | 20 / 9 | +11 |
| 노먼 | **청소 + 특수복** (냉동 탱크에서 해동) | Oozato | 12 / 6 | +6 |
| 배시시 | **굴착 + 건설** (뽑아서 보냄) | Oozato | 11 / 1 | +10 |

| 구간 | Persephazon | Oozato | 로켓 |
|---|---|---|---|
| 사이클 108 | 6 | 노먼, 배시시 (2) | |
| 첫 로켓 | 5 | 2 | 1 (방사능 숲 왕복) |

- 4교대, 사기 높게. 사기 예산은 [18 8명 중반 설계]({{ '/guide/midgame-8/#사기-예산-행복도-높게-유지' | relative_url }}).
- 결원이 생기면 표토 소행성 냉동 탱크로 충원.

</details>

## 이 판에서 가이드로 옮긴 것

<details class="nums" markdown="1">
<summary>본 것 → 반영한 페이지</summary>

| 이 판에서 본 것 | 가이드에 반영 |
|---|---|
| 시작 행성에만 있으면 자원 종류가 모자라 발전이 느림 | 새 페이지 [16 두 번째 행성 병행 개발]({{ '/guide/second-planet/' | relative_url }}): 안정화 체크리스트, 텔레포터 두 종류, 병행 순서 |
| 두 번째 행성은 "자원 공장"이 아니라 같이 크는 기지 | [18 8명 중반 설계]({{ '/guide/midgame-8/' | relative_url }})의 기름 늪 부분을 병행 개발 기준으로 수정 |
| 텔레포트는 연구가 필요 없음 | [7 초반 테크]({{ '/guide/research/early/' | relative_url }}) 3구간 끝에 "여기서 두 번째 행성" 표시 |
| 가까운 행성 트레잇이 시작 행성만큼 중요 | [3 트레잇과 시드 리롤]({{ '/guide/traits/' | relative_url }})의 합격 예시가 이 판의 시드 |

</details>
