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

> 일반 가이드는 "대부분의 판에 맞는 순서"이고, 이 페이지는 **한 판에 완전히 맞춘 기록**입니다. 이 판에서 더 나은 순서가 나오면 일반 가이드도 고칩니다. 반영한 내용은 [아래](#이-판에서-가이드로-옮긴-것)에 모았어요.
{: .tip}

## 챕터

| 장 | 행성 | 내용 |
|---|---|---|
| [1장 Persephazon]({{ '/guide/case/terrania-1/persephazon/' | relative_url }}) | 시작 행성 | 기지 세우기, 안정화, 텔레포터로 두 번째 행성 보내기 |
| [1-1 열 문제·드레코 목장]({{ '/guide/case/terrania-1/drecko-ranch/' | relative_url }}) | 시작 행성 | 에어컨 없이 열 막기, 2LegitCity식 드레코 목장 (사이클 108) |
| [2장 Oozato]({{ '/guide/case/terrania-1/oozato/' | relative_url }}) | 기름 늪 | 전력 0에서 자립까지, 단계 A~E (사이클 108) |
| [2-1 사이클 142 점검]({{ '/guide/case/terrania-1/oozato/check-142/' | relative_url }}) | 기름 늪 | 다섯 질문으로 본 Oozato, 닫힌 고리 |
| [2-2 단계별 플랜]({{ '/guide/case/terrania-1/oozato/plan/' | relative_url }}) | 기름 늪 | 0~8단계, 2명 → 4~6명 |
| [2-3 기지 배치 v2]({{ '/guide/case/terrania-1/oozato/layout/' | relative_url }}) | 기름 늪 | 텔레포터 홀 식당, 개인 침실, 세로 통로 |
| [3장 세 번째 행성과 그다음]({{ '/guide/case/terrania-1/next/' | relative_url }}) | 방사능 숲 외 | 첫 로켓, 이후 행성 순서 |

## 시작 설정: 행성 트레잇

{% include shot.html src="case1-traits.jpg" caption="이 판의 시작 화면. Terrania 클러스터, 생존 확률 Ideal, 스토리 트레잇 5개." %}

| 항목 | 값 |
|---|---|
| 게임 | Spaced Out! + 모든 DLC |
| 클러스터 | **Terrania 클러스터** (시작: Terrania 소행성, 사암 시작) |
| 좌표 | `SNDST-C-933086379-HIJYM31-V9-CKZRH…` (스크린샷에서 잘린 부분까지) |
| 생존 확률 | Ideal |

### 소행성별 트레잇

| 소행성 | 거리 | 트레잇 | 이 판에서의 의미 |
|---|---|---|---|
| **Terrania** (시작) | | 없음 | 나쁜 트레잇 없음 → 합격 |
| **방사능 숲** (Irradiated Forest) | 근처 | **Metal Rich + Metallic Caves** ✅✅ | 세 번째 행성. 우라늄에 금속까지 많은 곳 |
| **기름 늪** (Oily Swamp) | 근처, **텔레포터** | **Metallic Caves** ✅ | 두 번째 행성. 원유·황에 금속 광석 동굴까지 |
| 툰드라 (Tundra) | 먼 곳 | Metal Poor | 늦게 가니 상관없음 |
| 습지 (Marshy) | 먼 곳 | **Metal Rich** ✅ | 네 번째 후보 |
| 레골리스 (Regolith) | 먼 곳 | **Frozen Friend** ✅ | 냉동 탱크 1명 더. 결원 충원용 |
| 무 (Moo), 물 (Water) | 먼 곳 | 없음 | |

**스토리 트레잇 5개:** Somnium Synthesizer, Mysterious Hermit, Printerceptor, Critter Flux-O-Matic, Biobot Builder. 각각 무엇인지는 [3 트레잇과 시드 리롤]({{ '/guide/traits/#스토리-트레잇-전체-6개' | relative_url }}).

**왜 이 시드로 시작했나:** 시작 행성에 ❌가 없고, **가까운 두 행성(텔레포터로 가는 기름 늪, 첫 로켓으로 가는 방사능 숲)이 둘 다 금속 트레잇**이에요. 시작 행성을 안정시킨 뒤 옆 행성을 같이 키우는 이 판의 흐름에 딱 맞는 시드였습니다.

## 복제체 (사이클 108 기준)

{% include shot.html src="case1-duplicants.jpg" caption="사이클 108 복제체 목록. 시작 행성(Persephazon) 6명, 두 번째 행성(Oozato) 2명. 사기는 '지금/요구치'." %}

이 판에서는 행성 이름을 바꿔 부릅니다: 시작 행성 Terrania = **Persephazon**, 두 번째 행성 기름 늪 = **Oozato**.

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

- 목표였던 **8명을 사이클 108에 채웠습니다.** 프린팅 포드 7명 + 냉동 탱크 1명.
- **말랑은 사기 여유가 0**입니다. 굴착 스킬을 많이 찍어서 요구치가 높아요. 스킬을 더 찍기 전에 사기를 올리거나 스킬 포인트를 아껴 두세요. ([18 8명 중반 설계의 사기 예산]({{ '/guide/midgame-8/#사기-예산-행복도-높게-유지' | relative_url }}))
- 두 번째 행성은 **청소+특수복 1명, 굴착+건설 1명**. 굴착과 건설을 둘이서 다 하는 조합이에요.

행복도(사기)는 높게, 시작 행성은 4교대입니다.

## 8명 배치 (이 판)

| 구간 | Persephazon (시작) | Oozato (기름 늪) | 로켓 |
|---|---|---|---|
| 사이클 108 (지금) | 양자역학싫어요, 감자, 마이메, 말랑, 안성재, 젠슨황 (6) | 노먼, 배시시 (2) | |
| 첫 로켓 | 5명 | 2명 | 1명 (조종, 방사능 숲 왕복) |

- 로켓 조종 전담은 따로 안 뽑았습니다. 첫 로켓 때 시작 행성 6명 중 한 명이 Rocketry 스킬을 찍고 다녀오거나, 결원이 생기면 레골리스 냉동 탱크로 채웁니다.

## 이 판에서 가이드로 옮긴 것

| 이 판에서 본 것 | 가이드에 반영 |
|---|---|
| 시작 행성에만 있으면 자원 종류가 모자라 발전이 느림 | 새 페이지 [16 두 번째 행성 병행 개발]({{ '/guide/second-planet/' | relative_url }}): 안정화 체크리스트, 텔레포터 두 종류, 병행 순서 |
| 두 번째 행성은 "자원 공장"이 아니라 같이 크는 기지 | [18 8명 중반 설계]({{ '/guide/midgame-8/' | relative_url }})의 기름 늪 부분을 병행 개발 기준으로 수정 |
| 텔레포트는 연구가 필요 없음 | [7 초반 테크]({{ '/guide/research/early/' | relative_url }}) 3구간 끝에 "여기서 두 번째 행성" 표시 |
| 가까운 행성 트레잇이 시작 행성만큼 중요 | [3 트레잇과 시드 리롤]({{ '/guide/traits/' | relative_url }})의 합격 예시가 이 판의 시드 |
