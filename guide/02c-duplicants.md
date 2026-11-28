---
title: 복제체 고르기 (특성·관심·스트레스 반응)
nav_title: 복제체 고르기
nav_order: 4
nav_group: start
permalink: /guide/duplicants/
description: 시작 화면에서 첫 복제체 3명을 고를 때 보는 관심(Interests), 특성(Traits), 스트레스 반응, 기쁨 반응을 수치와 함께 정리하고, 스킬·사기까지 계산해 추천합니다.
---

## 30초 요약

> **이 조합이 나올 때까지 리롤.**
> 1. **관심이 겹치지 않는 3명:** 연구 (Researching) / 굴착 (Digging) / 농사·건설·목축 중 하나.
> 2. **작업 불가 특성**(시골뜨기 (Yokel)·환공포증 (Trypophobia)·비건설적 (Unconstructive))이 담당 일과 겹치면 리롤.
> 3. **입으로 숨쉼 (Mouth Breather)**, **밑바닥 없는 배 (Bottomless Stomach)** 리롤.
> 4. 스트레스 반응 **폭식가 (Binge Eater)·파괴적 (Destructive)·밴시 (Banshee)** 는 가급적 리롤.
> 5. 바이오닉 팩을 켰어도 **첫 3명은 일반 복제체.**
{: .tip}

## 화면 보는 법

{% include shot.html src="dupe-select-example.jpg" caption="왼쪽 Devon 연구 9, 가운데 Stinky 굴착 9, 오른쪽 Marie 농사·연구·기계 2/2/1." %}

**REROLL 왼쪽 아이콘으로 원하는 관심을 고정하고 리롤**하면 훨씬 빠릅니다.

<details class="nums" markdown="1">
<summary>화면 각 칸의 뜻</summary>

| 위치 | 뜻 |
|---|---|
| **REROLL 왼쪽 아이콘** | 관심 분야 고정. 연구·굴착 같은 분야를 골라 두면 리롤해도 그 관심이 꼭 붙어 나옵니다. **원하는 역할을 먼저 고정하고 리롤**하면 훨씬 빨라요. |
| **오른쪽 얼굴 드롭다운** | 복제체 종류 선택 (일반 / 바이오닉). Bionic Booster Pack을 켰을 때만 나옵니다. |
| **INTERESTS (관심)** | 관심 분야와, 그 덕에 오르는 능력치 (예: Researching → +9 Science) |
| **TRAITS (특성)** | 초록색은 좋은 특성, 빨간색은 나쁜 특성. 아래 회색 줄이 실제 효과 |
| **Stress Reaction** | 스트레스가 100%가 되면 하는 행동 |
| **Overjoyed Response** | 사기(Morale)가 기대치보다 한참 높을 때 가끔 나오는 좋은 행동 |
| 맨 아래 이탤릭 글 | 설정 문구. 게임에 영향 없음 |

</details>

## 관심과 능력치

| 관심 개수 | 분야마다 보너스 |
|---|---|
| 1개 | **+7** (전문가, 초반 연구·굴착에 최고) |
| 2개 | +3 |
| 3개 | +1 (대신 세 분야 1단계 스킬이 사기 0) |

여기에 나쁜 특성의 **추가 포인트**가 관심 분야로 더해집니다. 관심 분야 스킬은 **사기 요구치 −1**, 경험치도 빠름.

<details class="nums" markdown="1">
<summary>관심 분야 목록과 Devon·Stinky·Marie 계산 예</summary>

| 관심 (화면 표기) | 오르는 능력치 | 하는 일 |
|---|---|---|
| Researching | Science (과학) | 연구, 망원경 |
| Digging | Excavation (굴착) | 땅 파기, 동물 공격 |
| Building | Construction (건설) | 건물 짓기·수리 |
| Farming | Agriculture (농업) | 심기·수확·식물 돌보기 |
| Ranching | Husbandry (목축) | 동물 돌보기·포획 |
| Cooking | Cuisine (요리) | 요리 |
| Operating | Machinery (기계) | 정제기·분쇄기 같은 기계 조작, 발전기 튠업 |
| Doctoring | Medicine (의술) | 치료, 약 만들기 |
| Decorating | Creativity (창의력) | 그림·조각 |
| Supplying / Tidying | Strength (힘) | 운반, 청소, 배관 |
| Suit Wearing | Athletics (운동) | 환경 특수복·로켓 관련 스킬 |
| Rocketry (우주 탐사) | Piloting | 로켓 조종 |

- Devon (관심 1개): 7 + 무관심 (Unempathetic) 2 = **과학 +9**
- Stinky (관심 1개): 7 + 주방 위협 (Kitchen Menace) 2 = **굴착 +9**
- Marie (관심 3개): 1씩 + 주방 위협 2 무작위 분배 = 농업 +2 / 과학 +2 / 기계 +1
- 공급 (Supplying)·정리 (Tidying)은 둘 다 근력을 올림. 둘 다 있으면 +3씩 합 6인데 화면엔 양쪽 "+6"으로 잘못 표시.
</details>

<div class="shot-grid" markdown="0">
{% include shot.html src="tooltip-agri-interest.png" caption="관심(농사)에서 오는 농업 +2" %}
{% include shot.html src="tooltip-agri-greenthumb.png" caption="녹색 엄지 (Green Thumb)에서 오는 농업 +3" %}
</div>

관심 보너스와 특성 보너스는 **그냥 더해집니다** (Marie 농업 = 2 + 3 = 5). 일할수록 **최대 +20** 더 자람.

> **과학 (Science)** 은 모든 능력치의 성장 속도를 올리고, **운동 (Athletics)** 은 이동 속도라 모두에게 이득. **기계류 (Machinery)** 는 농사에 도움이 안 됩니다 (조작 기계·튠업 전용).
{: .tip}

<details class="nums" markdown="1">
<summary>능력치 1점당 효과</summary>

| 능력치 | 1점당 효과 |
|---|---|
| **건조 (Construction)** | 건설·수리 속도 +25% |
| **굴착 (Excavation)** | 굴착 속도 +25%, 공격력 +5% |
| **과학 (Science)** | 연구 속도 **+40%**, **능력치 성장 속도 +10%**, 지열 조정 속도 +5% |
| **농업 (Agriculture)** | 수확 속도 +5%, 돌보기 속도 +2.5%, 씨앗 확률 +3.3%, 농부의 손길 지속시간 +10% |
| **축산 (Husbandry)** | 포획 속도 +5%, 손질(Groom) 효과 지속시간 +10% |
| **기계류 (Machinery)** | 기계 조작 속도 +10%, 튠업 지속시간 +2.5%, 수리량 ↑ |
| **운동 (Athletics)** | 이동 속도 +10% |
| **힘 (Strength)** | 청소 속도 +25%, 운반량 +40kg (기본 200kg) |
| **요리 (Cuisine)** | 요리 속도 +5% |
| **의약 (Medicine)** | 약 제작 속도 +10%, 치료 속도 +20% |
| **창의성 (Creativity)** | 미술 작업 속도 +10% |
| **조종 (Piloting)** (우주 탐사) | 로켓 속도 +2.5% |

| 능력치 | 왜 모두에게 좋은가 |
|---|---|
| **과학 (Science)** | 연구만이 아니라 **모든 능력치가 자라는 속도**를 올립니다. Marie의 Science 2는 농사 실력이 **20% 빨리** 크는 효과예요. |
| **운동 (Athletics)** | 이동 속도. 오가는 시간이 줄어서 모든 일이 빨라짐. 환경 특수복을 입으면 −6이 붙어서 외부 인력에게 특히 중요 |
| **힘 (Strength)** | 한 번에 나르는 양. 운반이 많은 초반에 은근히 큼 |

</details>

## 특성

보통 **좋은 것 1 + 나쁜 것 1.** 첫 3명 기준 평가: ✅✅ 노려볼 만 · ✅ 좋음 · ➖ 그만 · ⚠️ 담당 따라 · ❌ 리롤.

| 노려볼 것 ✅✅ | 리롤 ❌ |
|---|---|
| 빨리 배움 (Quick Learner), 두더지 손 (Mole Hands), 번개발가락 (Twinkletoes), 잠수부의 허파 (Diver's Lungs), 교양 없음 (Uncultured) | 입으로 숨쉼 (Mouth Breather), 밑바닥 없는 배 (Bottomless Stomach), 빈혈 (Anemic), 담당과 겹치는 작업 불가 특성 |

> **빨간색인데 사실상 좋은 것:** 주방 위협 (Kitchen Menace, 음식 품질 한 단계 업), 미숙한 아티스트 (Unpracticed Artist, 장식 사기 +5), 무관심 (Unempathetic). 담당이 아닌 일만 깎고 관심 포인트를 줍니다. 반대로 미식가 (Gourmet)·실내 장식가 (Interior Decorator)는 초록색이지만 사기를 깎아요.
{: .tip}

<details class="nums" markdown="1">
<summary>좋은 특성 전체</summary>

| 특성 | 효과 | 희귀도 | 평가 |
|---|---|---|---|
| **빨리 배움 (Quick Learner)** | Science +3 | Rare | ✅✅ 연구 담당이면 최고 |
| **두더지 손 (Mole Hands)** | Excavation +3 | Rare | ✅✅ 굴착 담당이면 최고 |
| **능숙함 (Handy)** | Construction +3 | Uncommon | ✅ 건설 담당 |
| **녹색 엄지 (Green Thumb)** | Agriculture +3 | Common | ✅ 농사 담당 |
| **동물 애호가 (Animal Lover)** | Husbandry +3 | Uncommon | ✅ 목축 담당 |
| **수리공 (Grease Monkey)** | Machinery +3 | Uncommon | ✅ 정제·튠업 담당 |
| **왕근육 (Buff)** | Strength +3 | Rare | ✅ 누구에게 붙어도 쓸모 있음 |
| **번개발가락 (Twinkletoes)** | Athletics +3 | Epic | ✅✅ 이동 +30%. 누구에게나 좋음 |
| **잠수부의 허파 (Diver's Lungs)** | 산소 소비 −25 g/s (−25%) | Epic | ✅✅ 초반 산소 부족을 줄여 줌 |
| **아침형 복제체 (Early Bird)** | 하루 첫 125초 동안 모든 능력치 +2 | Rare | ➖ |
| **올빼미족 (Night Owl)** | 밤에만 모든 능력치 +3 (일정을 바꿔야 의미 있음) | Rare | ➖ |
| **강박의 인상 (Duress to Impress)** | 스트레스 60% 이상일 때 모든 능력치 +7 | Epic | ➖ 스트레스 관리 잘하면 안 켜짐 |
| **강철 위장 (Iron Gut)** | 식중독 면역 | Common | ✅ 화장실·오염된 물 근처 일에 좋음 |
| **세균 저항 (Germ Resistant)** | 병균 저항 +1 | Common | ✅ |
| **줄어든 맛봉오리 (Shrivelled Tastebuds)** | 음식 품질을 한 단계 높게 느낌 (사기 ↑) | Uncommon | ✅ |
| **교양 없음 (Uncultured)** | 장식 사기 보너스 **+20**, 대신 미술 불가 | Common | ✅✅ 사기 걱정이 거의 사라짐 |
| **타고난 세련됨 (Innately Stylish)** | 본인 주변 장식도 +25 | Uncommon | ✅ |
| **간병인 (Caregiver)** | Medicine +3 | Common | ➖ 초반엔 쓸 일 적음 |
| **미식가 (Gourmet)** | Cuisine +3, 대신 음식 품질을 **한 단계 낮게** 느낌 | Common | ⚠️ 요리 담당 아니면 손해 |
| **실내 장식가 (Interior Decorator)** | Creativity +3, 대신 장식 사기 보너스 **−5** | Common | ⚠️ 미술 담당 아니면 손해 |
| **서리 방지 (Frost Proof)** (서리 행성 팩) | 추운 환경 디버프 면역 | Common | ➖ 추운 행성이면 ✅ |
| **록 팬 (Rock Fan)** (우주 탐사) | 유성우 중 모든 능력치 +3 | Rare | ➖ |
| **별이 빛나는 눈 (Starry Eyed)** (우주 탐사) | 우주에 있으면 사기 +10 | Rare | ➖ 나중에 로켓 승무원으로 ✅ |
| **외톨이 (Loner)** (우주 탐사) | 소행성에 혼자 있으면 모든 능력치 +4 | Epic | ➖ 혼자 가는 개척지 담당으로 ✅ |
| **글로우 스틱 (Glow Stick)** (우주 탐사) | 빛 500 lux를 내고 방사능 저항 +33%. 대신 본인도 방사능을 냄 | Epic | ➖ |
| **방사선을 먹는 자 (Radiation Eater)** (우주 탐사) | 방사능을 흡수해 칼로리로 바꿈 (하루 최대 50 kcal) | Epic | ➖ |
| **Skilled: ○○** | 스킬 하나를 **사기 부담 없이** 미리 배운 상태 | Epic~Legendary | ✅ 담당과 맞으면 ✅✅ |

</details>

<details class="nums" markdown="1">
<summary>나쁜 특성: 작업 불가</summary>

| 특성 | 못 하는 일 | 추가 포인트 | 평가 |
|---|---|---|---|
| **환공포증 (Trypophobia)** | 굴착 | +4 | ❌ 초반엔 모두가 파야 함 |
| **비건설적 (Unconstructive)** | 건설 | +4 | ❌ 초반엔 모두가 지어야 함 |
| **시골뜨기 (Yokel)** | 연구 | 0 | ❌ 첫 3명 중엔 피하기 (연구 손이 모자람) |
| **요리공포증 (Gastrophobia)** | 요리 | 0 | ⚠️ 요리 담당만 아니면 괜찮음 |
| **비위가 약함 (Squeamish)** | 치료 | 0 | ➖ 거의 상관없음 |
| **평화주의자 (Pacifist)** | 동물 공격 | 0 | ➖ 거의 상관없음 |

</details>

<details class="nums" markdown="1">
<summary>나쁜 특성: 몸 상태</summary>

| 특성 | 효과 | 추가 포인트 | 평가 |
|---|---|---|---|
| **입으로 숨쉼 (Mouth Breather)** | 산소 소비 **+100 g/s** (2배) | +5 | ❌ 초반 산소가 빠듯해짐 |
| **밑바닥 없는 배 (Bottomless Stomach)** | 칼로리 **+500 kcal/사이클** (1.5배) | +4 | ❌ 초반 식량이 빠듯해짐 |
| **기면증 (Narcoleptic)** | 300~600초마다 15~30초 졸음 (하루 평균 30초) | **+5** | ⚠️ 손해가 생각보다 작음. 포인트 +5라 의외로 쓸 만함 |
| **헛배부름 (Flatulent)** | 10~40초마다 천연가스 100g 방출 (평균 4 g/s) | +3 | ⚠️ 초반 기지에 가스가 쌓임 |
| **시끄럽게 잠 (Loud Sleeper)** | 자면서 3칸 안의 복제체를 깨움 | +1 | ⚠️ 침대를 떨어뜨려 두면 해결 |
| **야공포증 (Nyctophobic)** | 잘 때 불이 켜져 있어야 함 | +2 | ⚠️ 침실에 조명 하나 |
| **알레르기 (Allergies)** | 꽃향기 병균에 닿으면 재채기(병) | +2 | ⚠️ |
| **생물재해 (Biohazardous)** | 병균 저항 −1 | +2 | ⚠️ |
| **과민성 대장 (Irritable Bowel)** | 화장실 속도 −50% | +1 | ➖ |
| **작은 방광 (Small Bladder)** | 방광 차는 속도가 아주 조금 빨라짐 | +1 | ✅ 실제 영향은 거의 없음 (공짜 +1) |
| **초라한 드레서 (Shabby Dresser)** | 본인 주변 장식도 −15 | +1 | ➖ |

</details>

<details class="nums" markdown="1">
<summary>나쁜 특성: 능력치 감소</summary>

| 특성 | 효과 | 추가 포인트 | 평가 |
|---|---|---|---|
| **빈혈 (Anemic)** | Athletics **−5** (이동 −50%) | +5 | ❌ 모든 일이 느려짐 |
| **면 팔 (Noodle Arms)** | Strength −3 | +3 | ⚠️ 운반이 느려짐 |
| **못 파 (Undigging)** | Excavation −3 | +3 | ⚠️ 굴착 담당이면 ❌ |
| **건조물 장애 (Building Impaired)** | Construction −3 | +3 | ⚠️ 건설 담당이면 ❌ |
| **느리게 배움 (Slow Learner)** | Science −3 | +3 | ⚠️ 연구 담당이면 ❌ |
| **식물 살해자 (Plant Murderer)** | Agriculture −3 | +2 | ⚠️ 농사 담당이면 ❌ |
| **크리터 혐오 (Critter Aversion)** | Husbandry −3 | +2 | ⚠️ 목축 담당이면 ❌ |
| **러다이트 (Luddite)** | Machinery −3 | +2 | ⚠️ |
| **무관심 (Unempathetic)** | Medicine −3 | +2 | ✅ 아래 참고 |
| **주방 위협 (Kitchen Menace)** | Cuisine −3, **음식 품질을 한 단계 높게 느낌** | +2 | ✅✅ 아래 참고 |
| **미숙한 아티스트 (Unpracticed Artist)** | Creativity −3, **장식 사기 보너스 +5** | +2 | ✅✅ 아래 참고 |

</details>

<details class="nums" markdown="1">
<summary>사실상 좋은 특성과 음식 품질 사기표</summary>

| 특성 | 손해 | 이득 | 이런 복제체면 추천 |
|---|---|---|---|
| **주방 위협 (Kitchen Menace)** | Cuisine −3 | 관심 +2, **음식 품질 한 단계 업** | 요리 담당이 아닌 **모든 복제체**. 최고의 "나쁜" 특성 |
| **미숙한 아티스트 (Unpracticed Artist)** | Creativity −3 | 관심 +2, **장식 사기 +5** | 미술 담당이 아닌 모든 복제체 |
| **무관심 (Unempathetic)** | Medicine −3 | 관심 +2 | 의사 담당이 아닌 모든 복제체 |
| **크리터 혐오 (Critter Aversion)** | Husbandry −3 | 관심 +2 | 목축 담당이 아닌 복제체 |
| **식물 살해자 (Plant Murderer)** | Agriculture −3 | 관심 +2 | 연구·굴착 담당 |
| **느리게 배움 (Slow Learner)** | Science −3 | 관심 +3 | 굴착·건설 담당 (연구는 다른 사람이) |
| **작은 방광 (Small Bladder)** | 사실상 없음 | 관심 +1 | 누구나 |
| **기면증 (Narcoleptic)** | 하루 평균 30초 졸음 | 관심 **+5** | 굴착·건설처럼 잠깐 멈춰도 되는 담당 |

| 먹는 음식 (품질) | 보통 복제체 사기 | Kitchen Menace / Shrivelled Tastebuds |
|---|---|---|
| 뮤시 바, 식사용 이 (−1) | −1 | 0 |
| **이빵 Liceloaf** (0) | 0 | **+1** |
| 구운 버섯, 그리슬 베리 (+1) | +1 | **+4** |
| 오믈렛, 생선 필레 (+2) | +4 | **+8** |

</details>

## 스트레스 반응

스트레스 100%에 하는 행동. **덜 나쁜 순서:**

{: .ico-grid}
1. **못생긴 울보 (Ugly Crier)** ✅ 물 흘림, 장식도 −30
2. **구토자 (Vomiter)** ➖ 오염된 물
3. **밴시 (Banshee)** ❌ 주변 스트레스 연쇄
4. **파괴적 (Destructive)** ❌ 건물 파손
5. **폭식가 (Binge Eater)** ❌ 6,000 kcal 증발

> 사기를 잘 챙기면 한 번도 안 나올 수 있지만, 초반엔 침실·식당이 없어 사기가 낮습니다. 위험 반응이 셋 중 하나 이상이면 리롤.
{: .danger}

<details class="nums" markdown="1">
<summary>스트레스 반응 상세</summary>

| 순위 | 반응 | 하는 일 | 평가 |
|---|---|---|---|
| 1 | **못생긴 울보 (Ugly Crier)** | 바닥에 앉아 울면서 물 40 g/s를 흘림. 주변 3칸 장식도 −30 (끝나고 1사이클 동안 −15) | ✅ 가장 무난 |
| 2 | **구토자 (Vomiter)** | 오염된 물 200 g/s를 토함. 토하는 동안 칼로리도 빨리 닳음 | ➖ 치우면 되는 수준 |
| 3 | **밴시 (Banshee)** | 8칸 안의 보이는 복제체들에게 스트레스를 줌 (+10%/사이클, 반 사이클 동안) | ❌ 연쇄로 다른 복제체까지 터질 수 있음 |
| 4 | **파괴적 (Destructive)** | 주변 건물과 타일을 부숨 | ❌ 산소·전력 설비가 망가질 수 있음 |
| 5 | **폭식가 (Binge Eater)** | 음식 2,000 kcal를 **3번**(총 6,000 kcal) 먹어 치움. 주변 장식도 −30 | ❌ 복제체 6일치 식량이 한 번에 사라짐. 초반엔 가장 위험 |

</details>

**기쁨 반응 (Overjoyed Response)** 은 사기가 요구치보다 8 이상 높을 때 20~50사이클에 한 번 꼴이라 **고를 때 무시.**

<details class="nums" markdown="1">
<summary>기쁨 반응 상세</summary>

| 순위 | 반응 | 효과 |
|---|---|---|
| 1 | **초생산성 (Super Productive)** | 작업을 10% 확률로 즉시 끝냄 |
| 2 | **벌룬 아티스트 (Balloon Artist)** | 쉬는 시간에 풍선을 나눠 줌. 받은 복제체는 2사이클 동안 Creativity·Science·Cuisine·Medicine·Agriculture·Husbandry +8 |
| 2 | **요들러 (Yodeler)** | 본인 Machinery·Construction·Strength +8, 주변 복제체 +5 (1사이클) |
| 4 | **스파클 스트리커 (Sparkle Streaker)** | 본인 Athletics +8, 지나간 자리의 복제체 Athletics +5 (1사이클) |
| 5 | **스티커 폭탄사 (Sticker Bomber)** | 스티커마다 반경 3칸 장식도 +20 |

</details>

## 스킬과 사기

스킬 단계 숫자만큼 사기 요구치가 오르고, **관심 분야면 −1** (1단계는 공짜). 침실·식당·세척실까지 갖추면 사기 **+8~10** → 요구치 합을 **8 안쪽**으로.

<details class="nums" markdown="1">
<summary>스킬·사기 규칙과 초반 사기 출처</summary>

| 규칙 | 내용 |
|---|---|
| 스킬마다 사기 요구치 | 스킬 화면의 **열(단계) 숫자만큼** 사기 요구치가 오름. 1단계 +1, 2단계 +2, 3단계 +3 |
| **관심 분야 할인** | 관심 있는 분야 스킬은 **사기 요구치 −1** (스킬에 하트 표시). 1단계면 **공짜** |
| 경험치 | 관심 분야 일을 하면 경험치가 더 빨리 쌓임. 드문 일일수록 더 많이 |
| 사기가 모자라면 | 요구치보다 1 낮을 때마다 스트레스 +2.5%/사이클 (최대 +25%) |
| 사기가 남으면 | 요구치보다 2 이상 높으면 스트레스 −20%/사이클 |

| 사기 출처 | 사기 |
|---|---|
| 기본 | +1 |
| New Hope (시작 3명, 첫 3사이클) | +1 |
| 변소(Latrine) / 세척실(Washroom) | +1 / +2 |
| 막사(Barracks) / 개인 침실 | +1 / +3 |
| 식당(Mess Hall) | +3 |
| 이빵(품질 0) / 구운 버섯(품질 +1) | 0 / +1 |
| 쉬는 시간 (일정 칸 수에 따라) | 0~+5 |

</details>

> **외부 인력 (환경 특수복 담당)은 Suit Wearing + 공급 (Supplying) 관심**이 사기 부담이 가장 적습니다 (요구치 4). 특수복이 굴착 +10을 줘서 굴착 관심은 없어도 됨. 프린팅팟에서 나오면 받기.
{: .tip}

<details class="nums" markdown="1">
<summary>외부 인력 스킬 경로와 사기 합계</summary>

| 항목 | 내용 |
|---|---|
| 특수복 효과 | **Excavation +10**, Athletics **−6**, 산소 탱크 75kg, 온도 보호 |
| Athletics −6 없애기 | **외부특수복 훈련 (Exosuit Training)** 스킬 (Suit Wearing 3단계, Athletics +2도 줌) |
| 배우는 길 | Improved Carrying I (Supplying 1단계) → (우주 탐사: Rocket Piloting, Rocketry 1단계) → Suit Sustainability Training (Suit Wearing 2단계) → **외부특수복 훈련 (Exosuit Training)** (3단계) |
| 사기 요구치 합계 | 관심 없음: 1 + 1 + 2 + 3 = **7** · Suit Wearing 관심: 1 + 1 + 1 + 2 = **5** · Suit Wearing + Supplying 관심: **4** |

</details>

## 일반 vs 바이오닉

> **첫 3명은 모두 일반 복제체.** 바이오닉은 하루 전력 뱅크 1개(초반엔 금속 광석 200 kg 일회용)를 먹어서, **땜질 스테이션 (Soldering Station) + 파워 뱅크 충전기 (Power Bank Charger)** 가 갖춰진 중반 초입(사이클 30~50)에 받으세요. 물에 젖으면 스트레스 10배, 일반 복제체와 같은 침실이면 잠을 깨움.
{: .warn}

<details class="nums" markdown="1">
<summary>일반 vs 바이오닉 비교, 공급 연구, 받는 시점</summary>

| | 일반 복제체 | 바이오닉 복제체 |
|---|---|---|
| 먹는 것 | 음식 | 음식 대신 **전력 뱅크(배터리)** |
| 산소 | 주변 공기를 숨 쉼 | **몸속 산소 탱크**에 저장해 두고 씀 |
| 잠 | 침대에서 잠 | 잠 대신 조각 모음(Defragmenting) |
| 따로 챙길 것 | 식량, 화장실 | 전력 뱅크 충전, **기어 오일(Gear Oil)**, 산소 보충 |
| 관심·특성 | 있음 | **없음**. 대신 처음부터 부스터 1개 장착 |
| 능력치 성장 | 일할수록 자람 | **안 자람**. 스킬과 부스터(마이크로칩으로 제작)로만 올림 |
| 약점 | | 물에 젖으면 스트레스가 일반 복제체의 10배 (+200%/사이클) |

| 필요한 것 | 무엇으로 | 연구 / 조건 |
|---|---|---|
| **전력 (초반)** | 금속 파워 뱅크: 금속 광석 200kg, 일회용 | 제작 스테이션(Crafting Station), **고용 (Employment)** (1단계 연구) |
| **전력 (정착)** | 에코 파워 뱅크: 어비살라이트 200kg, **충전해서 재사용** | 땜질 스테이션(Soldering Station): **고급 연구 (Advanced Research)** (2단계 연구) + **전기 엔지니어링 (Electrical Engineering)** 스킬 가진 복제체 |
| 전력 뱅크 충전 | 파워 뱅크 충전기(Power Bank Charger): 480 W, 반 사이클에 1개 충전. **1대로 바이오닉 2명분** | **음향 증폭기 (Sound Amplifiers)** (3단계 연구) |
| **윤활유** (200kg, 하루 20kg 소모) | 기어 밤(Gear Balm, 80kg분): 약제대(Apothecary)에서 물 200kg + 오물 80kg | **약학 (Pharmacology)** + Medicine Compounding 스킬 |
| 윤활유 (정착) | 윤활 스테이션(Lubrication Station): 원유나 식물성 기름으로 한 번에 가득 + 사기 버프 | **여과 (Filtration)** |
| **오물(Gunk) 빼기** (하루 25%씩 참) | 오물 추출기(Gunk Extractor). 없으면 일반 화장실을 쓰는데 **화장실이 막힘** | **위생 (Sanitation)** |
| **산소** (몸속 탱크 240kg, 4사이클분) | 주변 공기를 한꺼번에 빨아들임. 방 하나의 산소를 비울 수도 있어서 통 주입기(Canister Filler)가 편함 | Canister Filler: **휴대용 기체 (Portable Gases)** |

| 시점 | 판단 |
|---|---|
| **사이클 1~10** | **거절.** 산소·식량·화장실 세팅이 먼저. 금속 광석 하루 200kg은 초반 건설과 겹쳐요. |
| **금속 광석이 넉넉하고 부스터가 좋으면** | 받아도 됨. 첫 9사이클은 공짜고, 그 뒤엔 제작 스테이션에서 금속 파워 뱅크를 하루 1개씩 만들면 됩니다. 음식이 안 들어서 식량 부담은 오히려 줄어요. |
| **추천 시점** | **Electrical Engineering 복제체 + 땜질 스테이션 + Sound Amplifiers(파워 뱅크 충전기)** 가 갖춰진 뒤. 이때부터 에코 파워 뱅크를 충전해 돌려서 금속을 안 먹습니다. 보통 **전력이 안정된 중반 초입(사이클 30~50 전후)** 이에요. |

- 뽑힐 때 전력 뱅크 4개(장착) + 금속 파워 뱅크 5개 + 기어 밤 1개 → 약 9사이클은 그냥 버팀.
- Marie처럼 작동 (Operating) 관심이면 전기 엔지니어링 (Electrical Engineering)을 사기 1에 배워 바이오닉 받을 준비가 됨.
</details>

## 추천 시작 3인

| 자리 | 관심 | 있으면 좋은 특성 | 리롤할 특성 |
|---|---|---|---|
| **연구 담당** | Researching (가능하면 1개만) | 빨리 배움 (Quick Learner), 잠수부의 허파 (Diver's Lungs), 주방 위협 (Kitchen Menace) | 시골뜨기 (Yokel), 느리게 배움 (Slow Learner) |
| **굴착 담당** | Digging (가능하면 1개만) | 두더지 손 (Mole Hands), 번개발가락 (Twinkletoes), 왕근육 (Buff) | 환공포증 (Trypophobia), 못 파 (Undigging) |
| **건설·농사 담당** | Building 또는 Farming | 능숙함 (Handy), 녹색 엄지 (Green Thumb) | 비건설적 (Unconstructive), 식물 살해자 (Plant Murderer) |

**공통 리롤:** 입으로 숨쉼, 밑바닥 없는 배, 빈혈, 스트레스 반응 폭식가 / 파괴적 / 밴시.

> **스크린샷 3명이면 그대로 시작 OK.** 역할이 나뉘고 작업 불가 특성이 없음. 위험은 Devon의 폭식가 하나뿐 → 식당·침실을 일찍.
{: .tip}

<details class="nums" markdown="1">
<summary>시뮬레이션: 3명의 역할과 스킬 순서·사기 누적</summary>

| | Devon | Stinky | Marie |
|---|---|---|---|
| 역할 | **연구 전담** | **굴착 → 외부 인력** | **농사 전담 + 튠업 + 예비 연구** |
| 실제 능력치 | Science 9 (연구 +360%, 성장 +90%) | Excavation 9 (굴착 +225%) | Agriculture 5 (수확 +25%, 농부의 손길 +50%) · Science 2 · Machinery 1 |
| 좋은 특성 | Iron Gut ✅ | Germ Resistant ✅ | Green Thumb ✅ |
| 나쁜 특성 | Unempathetic (사실상 좋음, +2가 Science로) | Kitchen Menace (사실상 좋음, +2가 Excavation으로) | Kitchen Menace (사실상 좋음) |
| 스트레스 반응 | **폭식가 (Binge Eater)** ❌ | Vomiter ➖ | Ugly Crier ✅ |
| 우선순위 화면 | 연구 최우선 | 굴착 최우선, 건설·운반 중간 | 농사 최우선, 연구 중간 |

| 순서 | Devon | Stinky | Marie |
|---|---|---|---|
| 1 | Advanced Research (연구 1단계, **0**) → 누적 0 | Hard Digging (굴착 1단계, **0**) → 0 | Improved Farming I (농사 1단계, **0**) → 0 |
| 2 | Field Research (2단계, 1) → 1 | Superhard Digging (2단계, 1) → 1 | Improved Tinkering (Operating 1단계, **0**) → 0 |
| 3 | Astronomy (우주 탐사 2단계, 1) → 2 | Improved Carrying I (Supplying 1단계, 1) → 2 | Crop Tending (농사 2단계, 1) → 1 |
| 4 | Applied Sciences (3단계, 2) → 4 | (우주 탐사) Rocket Piloting (1) → 3 | Electrical Engineering (Operating 2단계, 1) → 2. 발전기 튠업 가능 |
| 5 | | Suit Sustainability (2) → 5 | Advanced Research (연구 1단계, **0**) → 2. 예비 연구원 |
| 6 | | Exosuit Training (3) → **8** | Improved Farming II (농사 3단계, 2) → 4 |

- Marie는 스킬 6개를 찍어도 사기 요구치 4 (관심 3개의 장점).
- Stinky를 외부 인력으로 만들면 요구치 8 → 침실·식당·세척실 필요. 외부특수복 훈련 (Exosuit Training)은 급하지 않음.
</details>

## 요리사

> **요리는 하루 2~3분짜리 일.** Cooking 하나 몰빵보다 **Cooking + 다른 관심 1개**가 낫습니다. W 판(8명)엔 **Cooking + Decorating**(장식도로 모두의 사기 ↑)이 빈자리를 채움.
{: .tip}

<details class="nums" markdown="1">
<summary>요리 시간, 요리 스킬, 두 번째 관심, 8명 추천</summary>

| 메뉴 (1번에 kcal) | 하루 횟수 | Cuisine 0 | **Cuisine 7** | **Cuisine 11** | Cuisine 31 |
|---|---|---|---|---|---|
| 바베큐 Barbeque (4,000) | 2번 | 100초 | 74초 | 65초 | 39초 |
| 구운 버섯 Fried Mushroom (2,800) | 약 3번 | 143초 | 106초 | 92초 | 56초 |
| 그리슬 베리 Gristle Berry (2,000) | 4번 | 200초 | 148초 | 129초 | 78초 |
| 서리 빵 Frost Bun (1,200) | 약 7번 | 333초 | 247초 | 215초 | 131초 |

| 스킬 | 단계 | 열리는 것 | 사기 (Cooking 관심 있을 때) |
|---|---|---|---|
| **그릴 (Grilling)** | 1 | 전기 그릴 사용, Cuisine +2 | 1 → **0** |
| **강화된 조미료 (Enhanced Seasoning)** (Grilling II) | 2 | **가스 레인지**, 향신료 분쇄기 (DLC: 훈연기, 튀김기, 초밥 바), Cuisine +2 | 2 → **1** |
| **파인 다이닝 (Fine Dining)** | 3 | Cuisine +2 | 3 → 2 |

| 조합 | 장점 | 추천 |
|---|---|---|
| **Cooking + Decorating** | 요리 없는 시간에 그림·조각. 장식도가 올라 **모든 복제체의 사기**가 오름. 미술 스킬 1단계 공짜 | ✅✅ |
| **Cooking + Farming** | 수확 → 요리가 한 사람 동선. 농부가 바쁠 때 보조 | ✅ 농부가 1명뿐이면 |
| **Cooking + Ranching** | 달걀·고기 → 오믈렛·바베큐. 목장과 주방을 같이 맡음 | ✅ 목장 담당이 없으면 |
| **Cooking + Operating** | 정제기·튠업을 겸함 | ✅ 기계 담당이 없으면 |
| **Cooking + Doctoring** | 아플 때만 바쁨. 둘 다 짬나는 일 | ➖ |
| Cooking 하나만 | Cuisine +7 | ➖ 하루 몇십 초 빨라질 뿐 |

| 항목 | 추천 |
|---|---|
| 관심 | **Cooking + Decorating** (Cuisine +3, Creativity +3) |
| 스킬 순서 | Grilling (0) → Art Fundamentals (0) → Enhanced Seasoning (1) → 미술 2단계 (1) |
| 사기 요구치 | 4개 다 찍어도 **2** |
| 우선순위 | 요리 최우선, 미술 그다음 |
| 있으면 좋은 특성 | Twinkletoes, Buff, Diver's Lungs |
| 피할 특성 | Gastrophobia (요리 불가), Uncultured (미술 불가), Unpracticed Artist (Creativity −3) |

- 요리는 Cuisine만 쓰고 기계류 (Machinery)는 안 씀 → 러다이트 (Luddite)는 요리와 무관.
- Cuisine 7 vs 11 차이는 하루 10~30초.
- 피할 특성: 요리공포증 (Gastrophobia, 요리 불가).
</details>

다음 단계: [첫 5사이클 체크리스트]({{ '/guide/first-cycles/' | relative_url }})

<details class="nums" markdown="1">
<summary>출처</summary>

- [Duplicant – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Duplicant) (관심 보너스, 특성 전체 수치, 능력치 1점당 효과)
- [Skills – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Skills) (스킬 단계, 관심 할인, 선행 스킬)
- [Morale – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Morale) (사기 출처, 기쁨 반응), [Stress – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Stress) (스트레스 반응)
- [Food Quality – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Food_Quality), [Atmo Suit – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Atmo_Suit), [Bionic Duplicant – ONI Wiki](https://oxygennotincluded.wiki.gg/wiki/Bionic_Duplicant)
- [Power Bank Charger](https://oxygennotincluded.wiki.gg/wiki/Power_Bank_Charger), [Metal Power Bank](https://oxygennotincluded.wiki.gg/wiki/Metal_Power_Bank), [Eco Power Bank](https://oxygennotincluded.wiki.gg/wiki/Eco_Power_Bank), [Soldering Station](https://oxygennotincluded.wiki.gg/wiki/Soldering_Station), [Gear Balm](https://oxygennotincluded.wiki.gg/wiki/Gear_Balm) (바이오닉 공급 수치)
- [Electric Grill](https://oxygennotincluded.wiki.gg/wiki/Electric_Grill), [Gas Range](https://oxygennotincluded.wiki.gg/wiki/Gas_Range), [Cuisine](https://oxygennotincluded.wiki.gg/wiki/Cuisine) (요리 시간, 레시피 kcal)
- 직접 찍은 시작 화면과 능력치 툴팁 스크린샷
</details>
