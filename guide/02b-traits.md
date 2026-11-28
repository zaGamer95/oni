---
title: 월드 트레잇·스토리 트레잇과 시드 리롤
nav_title: 트레잇과 시드 리롤
nav_order: 3
nav_group: start
permalink: /guide/traits/
description: 목적지 선택 화면에 뜨는 트레잇이 무슨 뜻인지, 어떤 조합이 나올 때까지 리롤하면 되는지 정리했습니다.
---

## 어디서 보나

새 게임의 마지막 **목적지 선택 (Choose a Destination)** 화면.

- **월드 트레잇 (World Traits) 탭:** 소행성별 지형 특성. 좌표 옆 🔄 로 **리롤해야만** 바뀜.
- **스토리 트레잇 (Story Traits) 탭:** 묻힌 이야기 건물. **직접 켜고 끔** (리롤 불필요).

## 리롤 기준

> **시작 소행성에 ❌ 0개면 합격.** 근처(텔레포터) 소행성에 ✅가 있으면 더 좋고, 먼 소행성은 무시.
{: .tip}

| 위치 | ✅ 좋음 | ❌ 리롤 |
|---|---|---|
| **시작** | 금속 풍족, 금속 동굴, 언 친구, 지질활성, 지표 아래 해양, 거대 빙하, 언 핵, 울창한 코어 | 금속 부족, 지질휴지, 는지렁이균, 마그마 채널, 화산 활동, 방사성 크러스트, (첫 판) 다른 팟 위치 |
| **근처** | 금속 풍족, 금속 동굴, 지질활성, 추락한 위성, 비정규·갇힌 석유 | 금속 부족 정도 |
| **먼 곳** | 보너스 | 무시 |

예시는 [사례 1 Terrania 시드]({{ '/guide/case/terrania-1/' | relative_url }}): 시작 트레잇 없음 + 근처 금속 풍족 → 바로 시작.

## 월드 트레잇 (23개)

### 좋은 것 ✅

{: .ico-grid}
- {% include i.html n="Trait_MetalRich" %} **금속 풍족 (Metal Rich)** 금속 광석 많음 ✅✅
- {% include i.html n="Trait_MetalCaves" %} **금속 동굴 (Metallic Caves)** 금속 동굴 추가 ✅✅
- {% include i.html n="Trait_DistressSignal" %} **언 친구 (Frozen Friend)** 크라이오탱크 3000 (Cryotank 3000), 복제체 +1
- {% include i.html n="Trait_GeoActive" %} **지질활성 (Geoactive)** 간헐천·분출구 많음
- {% include i.html n="Trait_SubsurfaceOcean" %} **지표 아래 해양 (Subsurface Ocean)** 큰 소금물 바다
- {% include i.html n="Trait_GlaciersLarge" %} **거대 빙하 (Large Glaciers)** 냉각·물
- {% include i.html n="Trait_FrozenCore" %} **언 핵 (Frozen Core)** 코어가 얼음
- {% include i.html n="Trait_LushCore" %} **울창한 코어 (Lush Core)** 코어에 숲

### 나쁜 것 ❌ (시작이면 리롤)

{: .ico-grid}
- {% include i.html n="Trait_MetalPoor" %} **금속 부족 (Metal Poor)** 가장 치명적 ❌❌
- {% include i.html n="Trait_GeoDormant" %} **지질휴지 (Geodormant)** 간헐천 적음
- {% include i.html n="Trait_SlimeSplats" %} **는지렁이균 (Slime Molds)** 는지렁이 지대 산재
- {% include i.html n="Trait_MagmaVents" %} **마그마 채널 (Magma Channels)** 아래쪽 마그마
- {% include i.html n="Trait_Volcanoes" %} **화산 활동 (Volcanic Activity)** 화산 생성
- {% include i.html n="Trait_RadioactiveCrust" %} **방사성 크러스트 (Radioactive Crust)** 지표 방사능

### 상황 따라 ⚠️

{: .ico-grid}
- {% include i.html n="Trait_CrashedSatellites" %} **추락한 위성 (Crashed Satellites)** 근처면 👍, 시작이면 ⚠️
- {% include i.html n="Trait_IrregularOil" %} **비정규 석유 (Irregular Oil)** 석유 산재 👍
- {% include i.html n="Trait_DeepOil" %} **갇힌 석유 (Trapped Oil)** 깊은 석유, 중립
- {% include i.html n="Trait_MisalignedStart" %} **다른 팟 위치 (Alternate Pod Location)** 첫 판이면 피하기
- {% include i.html n="Trait_Geodes" %} **정동 (Geodes)** 희귀 자원 동굴
- {% include i.html n="Trait_BouldersLarge" %} **큰 표석 (Large Boulders)** 바위 (크기 4종), 중립

반대 트레잇(금속 풍족 ↔ 부족, 지질활성 ↔ 휴지, 바위 4종)은 한 소행성에 같이 안 나옵니다. **DLC로 새로 생긴 월드 트레잇은 없음** (2026년 11월, ONI Seed Browser 기준).

## 스토리 트레잇 (6개)

기본 5개 선택. 더 켜면 월드 생성 실패 확률이 오릅니다. 추천 순서:

{: .ico-grid}
1. {% include i.html n="Somnium_Synthesizer" %} **솜늄 합성기 (Somnium Synthesizer)** 전원 능력치 +5
2. {% include i.html n="Printerceptor" %} **프린터셉터 (Printerceptor)** 원하는 씨앗·알
3. **신비한 은둔자 (Mysterious Hermit)** 복제체 Jorge 합류
4. {% include i.html n="Critter_Flux-O-Matic" %} **크리터 플럭스-오-매틱 (Critter Flux-O-Matic)** 변종 동물
5. {% include i.html n="Ancient_Specimen" %} **고대 표본 (Ancient Specimen)** 화석 채석장
6. {% include i.html n="Biobot_Builder" %} **바이오봇 빌더 (Biobot Builder)** 강철 재사용 일꾼

5·6은 둘 중 하나: 화석(건축 재료)이 필요하면 고대 표본. W 판(사례 1)엔 고대 표본만 없음.

### 단계별 공략

<details class="nums" markdown="1">
<summary>솜늄 합성기 (Somnium Synthesizer)</summary>

| 단계 | 할 일 |
|---|---|
| 1. 켜기 | 건물 창 버튼으로 작업 요청 |
| 2. 분석 | 꿈 일지 (Dream Journal) 25개 + 산소 5 kg (산소는 대개 이미 있음) |
| 3. 꿈 일지 | 옆 **파자마 커비 (Pajama Cubby)** 잠옷 입고 자면 300초마다 1개 |
| 완료 | 최대 적성 (Maximum Aptitude) 모드 + 기념품 Model Plane |

- 효과: 콜로니 전체(다른 소행성·로켓 포함) 운동·근력·과학·조종·기계 **+5**, 스트레스 −25%/사이클.
- 유지비: 산소 500 g/s + 꿈 일지 하루 10개 (6명이 휴식 2칸 빼고 계속 자야 하는 양). 켜 두고 일지가 쌓이는 만큼만 버프.
- 바이오닉 복제체는 일지를 못 만들지만 버프는 받음.
</details>

<details class="nums" markdown="1">
<summary>프린터셉터 (Printerceptor)</summary>

| 단계 | 할 일 |
|---|---|
| 1. 켜기 | 가동 시도 → 잠김 |
| 2. 코드 | 맵 다른 곳 **막힌 변기**를 파괴 (Demolition) 스킬로 뚫기 |
| 3. 출력 | 프린팅팟 충전 3번 저장 → 데이터 뱅크 (Data Bank) 25개로 씨앗·알 1개. 같은 걸 또 뽑으면 +25 (최대 275) |
| 완료 | 기념품 Hair Dryer |

- 미발견도 선택 가능: 포자난 (Sporechid), 가스풀, 토성 덫 등. **변종 알은 불가.**
- 늘릴 수 없는 식물 씨앗(예: Flue Coral)에 쓰는 게 가장 이득.
</details>

<details class="nums" markdown="1">
<summary>신비한 은둔자 (Mysterious Hermit)</summary>

| 단계 | 할 일 |
|---|---|
| 1. 노크 | 컨테이너 문 두드리기 → 퀘스트 3개, 순서 자유 |
| 2. 환영 만찬 | 우편함에 품질 +4 (Great) 이상 음식 **3종** |
| 3. 좋은 동네 | 컨테이너와 주변 1칸 평균 장식도 **120 초과** (화강암 카펫 타일) |
| 4. 전력 | **60 W × 3,000초** (5사이클, 끊겨도 됨) |
| 완료 | Jorge 합류 + 250톤 보관함 + 기념품 Rusty Toolbox |

- Jorge: 모든 능력치 +7, 스킬 포인트 +3, Charismatic.
- 보통 늪의 는지렁이 속. 입구부터 소독.
</details>

<details class="nums" markdown="1">
<summary>크리터 플럭스-오-매틱 (Critter Flux-O-Matic)</summary>

| 단계 | 할 일 |
|---|---|
| 1. 켜기 | 버튼으로 작업 요청 |
| 2. 스캔 | 서로 다른 종 5가지 (주둥가리·돌 주둥가리 = 같은 종). 옆에 크리터 투하 (Critter Drop-Off) |
| 완료 | 유전자 조작 모드 + 기념품 Ceramic Morb |

- 기본형 → 지금 낳을 수 있는 변종 중 하나 (알 확률 비율), 변환 뒤 540초 대기.
- 예: 주둥가리 → 돌 50% / 슬기로운 50%, 포크쉘 → 오크쉘 66.7% / 새니쉘 33.3%, 빛벌레 → 썬 버그 100%.
- 알 확률 0% 변종은 불가 (잎람쥐 → 어람쥐 불가).
</details>

<details class="nums" markdown="1">
<summary>고대 표본 (Ancient Specimen)</summary>

- 걸작 (Masterworks) 스킬로 화석 4곳 발굴: 본 표본(사암), 호박 (Amber, 좀비 포자·늪), 냉동 (Frozen, 툰드라), 석화 (Petrified, 기름 바이옴).
- 완료 → **화석 채석장 (Fossil Quarry)**: 다이아몬드 1 kg → 화석 100 kg. 화석은 쇄석기에서 퇴적암 + 석회(강철 재료). 화석 온도 = 넣은 다이아몬드 온도.
</details>

<details class="nums" markdown="1">
<summary>바이오봇 빌더 (Biobot Builder)</summary>

| 단계 | 할 일 |
|---|---|
| 재료 | 강철 300 kg + 좀비 포자 9,850,000개 (기체 파이프, 절반은 이미 있음) |
| 포자 | 방 안 벽 캐비닛의 포자난 씨앗 2개를 **이산화탄소 속에** 심기 |
| 제작 | 고급 의료 (Advanced Medical Care) 스킬 |

- 바이오봇: 10사이클 일하고 멈춤 → 분해하면 강철 300 kg 회수. 마그마·진공·물속·방사선에서도 일함.
- 못 하는 일: 단단한 땅 굴착, 고급 건물, 건물 작동, 청소·수리.
- 좀비 포자 파이프는 생활 구역을 피해서.
</details>

> Prehistoric 팩의 소행성 충돌(Demolior), Frosty 팩의 지열 펌프는 DLC 고정 요소라 스토리 트레잇 탭에 없습니다.
{: .warn}

<details class="nums" markdown="1">
<summary>출처</summary>

- [ONI Seed Browser](https://github.com/StefanOltmann/oni-seed-browser-model), [World Trait](https://oxygennotincluded.wiki.gg/wiki/World_Trait), [Story Trait](https://oxygennotincluded.wiki.gg/wiki/Story_Trait) (U60 확인)
- [Klei 포럼: 월드 트레잇 효과](https://kleiforums.com/forums/topic/108331-world-traits-and-their-effects/), [Steam 토론](https://steamcommunity.com/app/457140/discussions/0/598540711281938576/)
</details>
