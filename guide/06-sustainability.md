---
title: 장기 평형 설계 (산소·식량·물·전력·열)
nav_title: 장기 평형 설계
nav_order: 23
nav_group: ref
permalink: /guide/sustainability/
description: 오래 켜둬도 아무것도 동나지 않는 기지 만들기. "재생 가능한 입력"으로 모든 시스템을 바꾸는 게 목표입니다.
---

* 목차
{:toc}

> **모든 소비가 재생 가능한 입력에서 나오면 기지는 영원히 돌아갑니다.** 숫자 기준표·2026 패치는 [부록 A 지속 가능성 컨텍스트]({{ '/appendix/sustainability-context/' | relative_url }}).
{: .tip}

## 초반 → 장기 전환

{: .ico-grid}
- {% include i.html n="Electrolyzer" %} **산소** 조류 → 물 + 전해조 (Electrolyzer)
- {% include i.html n="Water_Sieve" %} **물** 화장실 고리 + 분출구
- {% include i.html n="Bristle_Blossom" %} **식량** 흙 작물 → 물 작물·목장·요리
- {% include i.html n="Hydrogen_Generator" %} **전력** 석탄 → 수소·천연가스·증기 터빈
- {% include i.html n="Thermo_Aquatuner" %} **열** 단열 → 열 삭제

<details class="nums" markdown="1">
<summary>시스템별 초반·장기 입력, 복제체 1명 소비량</summary>

| 시스템 | 초반 (유한 자원) | 장기 (재생 가능) |
|---|---|---|
| 산소 | 조류 + 산소 확산기 | 물 + 전해조 |
| 물 | 웅덩이 퍼오기 | 화장실 고리 + 분출구(Geyser) 길들이기 |
| 식량 | 끼니나무 (흙 소모) | 센털꽃 등 물 작물, 목장 동물, 요리 |
| 전력 | 수동 → 석탄 | 수소(전해조 부산물), 천연가스 분출구, 솔라 패널, 증기 터빈 |
| 열 | 신경 안 씀 | 단열 + 열 삭제 장치 |

| 복제체 1명 | 소비량 |
|---|---|
| 산소 | 100 g/s (사이클당 60 kg) |
| 식량 | 1,000 kcal/사이클 |
| 화장실 | 하루 약 1회 (수세식은 쓴 물보다 많은 오염된 물을 냄) |
| 침대 | 1개 |

</details>

## 계산기

<div class="calc" id="colony-calc">
  <div class="calc-row">
    <label>복제체 수<input id="cc-dups" type="number" min="1" max="100" value="8"></label>
    <label>산소원
      <select id="cc-o2">
        <option value="electrolyzer">전해조</option>
        <option value="diffuser">산소 확산기 (조류)</option>
      </select>
    </label>
    <label>주 식량
      <select id="cc-food">
        <option value="mealwood">끼니나무</option>
        <option value="bristle">센털꽃</option>
      </select>
    </label>
    <label>여유분 (%)<input id="cc-buffer" type="number" min="0" max="100" value="20"></label>
    <label style="flex-direction:row;align-items:center;gap:6px"><input id="cc-cook" type="checkbox" checked style="min-width:0">센털베리 구워 먹기</label>
  </div>
  <div class="calc-out">
    <div><span>필요 산소</span><b id="cc-out-o2">-</b><span>여유분 포함</span></div>
    <div><span>산소 설비</span><b id="cc-out-o2src">-</b><span id="cc-out-o2sub">-</span></div>
    <div><span>필요 칼로리 / 사이클</span><b id="cc-out-kcal">-</b><span>여유분 포함</span></div>
    <div><span id="cc-plant-label">끼니나무 화분</span><b id="cc-out-plants">-</b><span id="cc-out-plantsub">-</span></div>
    <div><span>화장실 고리의 오염된 물 순증</span><b id="cc-out-toilet">-</b><span>사이클당, 수세식 화장실 기준</span></div>
  </div>
</div>

> 기본 수치만 씁니다. 특성·병·작물 온도 때문에 **여유분 20% 이상**.

## 산소: SPOM

{: .ico-grid}
1. {% include i.html n="Electrolyzer" %} **전해조를 밀폐 소형 방에** 수소는 위, 산소는 아래
2. {% include i.html n="Gas_Pump" %} **위 펌프 → 수소 발전기 (Hydrogen Generator)** 800 W
3. {% include i.html n="Gas_Vent" %} **아래 펌프 → 기체 벤트 (Gas Vent)** 기지로
4. {% include i.html n="Water_Geyser" %} **물 공급원 따로** 1대 600 kg/사이클

{% include shot.html src="spom-2x.jpg" caption="18×5칸 모듈 2개. 오버레이별 사진과 센서 설정은 03 건설 순서에." %}

> 산소가 **최소 70°C.** 침실에 바로 뿌리지 말고 냉각 구간을 거치게.
{: .heat}

<details class="nums" markdown="1">
<summary>전해조 수치와 물 문제</summary>

- 물 1 kg/s → 산소 888 g/s + 수소 112 g/s. 1대 ≈ 복제체 8명.
- 수소 발전기 전기로 전해조·펌프를 돌리고 조금 남음 (자급식 산소 모듈).
- 화장실 고리 물은 복제체당 하루 몇 kg뿐. 큰 웅덩이, 물 분출구 (Water Geyser), 서늘한 증기 벤트 (Cool Steam Vent), 얼음 중 하나는 꼭 확보.

</details>

## 물: 화장실 고리 + 분출구

{: .ico-grid}
1. {% include i.html n="Lavatory" %} **수세식 화장실·세면기** 물 → 오염된 물
2. {% include i.html n="Water_Sieve" %} **물 체 (Water Sieve)** 모래로 정화
3. {% include i.html n="Chlorine" %} **염소 방 통과** 150~200초면 살균
4. {% include i.html n="Liquid_Reservoir" %} **남는 오염된 물은 저장** 액체 저장소 (Liquid Reservoir)

<details class="nums" markdown="1">
<summary>물 체·분출구 수치</summary>

- 물 체: 오염된 물 5 kg/s + 모래 1 kg/s → 물 5 kg/s, 120 W. 모래 계속 보충.
- 분출구는 주기적으로 뜨거운 물·증기를 뿜음. 막아서 저장하고 식혀 쓰면 반영구. 증기 터빈을 붙이면 열도 전기로.

</details>

## 식량: 흙 → 물 → 요리

{: .ico-grid}
1. {% include i.html n="Mealwood" %} **초반 끼니나무 (Mealwood)** 흙 소모, 1명당 5그루
2. {% include i.html n="Bristle_Blossom" %} **중반 센털꽃 (Bristle Blossom)** 물 + 빛, 구우면 3그루
3. {% include i.html n="Hatch" %} **후반 목장·고급 요리** 사기 대폭 ↑
4. {% include i.html n="Carbon_Dioxide" %} **CO₂ 속 보관** 부패 정지

> 흙은 결국 떨어집니다. **30~50사이클 안에** 물 작물로. 퇴비 (Compost)로 오염된 흙 → 흙.
{: .tip}

<details class="nums" markdown="1">
<summary>단계별 식량, 음식 품질과 사기</summary>

| 단계 | 주 식량 | 복제체당 | 입력 |
|---|---|---|---|
| 초반 | 끼니나무 | 약 5그루 | 흙 10 kg/사이클 (유한) |
| 중반 | 센털꽃 | 약 4그루 (구우면 3) | 물 20 kg/사이클 + 빛 |
| 중반 | 끼니나무 → 이빵 (Liceloaf) | 요리로 칼로리 ↑ | 물 |
| 후반 | 진눈깨비밀 (Sleet Wheat) + 꼬집후추콩 (Pincha Peppernut) → 고급 요리 | 사기 ↑ | 추운 농장, 물 |
| 후반 | 목장 동물 (주둥가리, 드럽치 등) | 고기·알 | 동물 먹이 |

스킬을 많이 찍은 복제체일수록 기대치가 높아 좋은 음식이 필요합니다.

| 품질 | 사기 보너스 |
|---|---|
| 신의 음식 (Ambrosial, 6) | +16 |
| 최상 (Superb, 5) | +16 |
| 훌륭함 (Great, 4) | +12 |
| 좋음 (Good, 3) | +8 |
| 보통 (Standard, 2) | +4 |
| 나쁨 (Poor, 1) | +1 |
| 끔찍함 (Terrible, 0) | 0 |
| 역겨움 (Grisly, −1) | −1 |

- 냉장고 (Refrigerator) 4°C 이하면 부패 느림. CO₂ 속이면 아예 안 상함 → 맨 아래 CO₂ 구덩이에 보관함.

</details>

## 전력

{: .ico-grid}
- {% include i.html n="Smart_Battery" %} **스마트 배터리 (Smart Battery)** 20% 켜기 / 90% 끄기
- {% include i.html n="Coal_Generator" %} **석탄은 필요할 때만** 상시 가동이면 석탄 600 kg/사이클
- {% include i.html n="Battery" %} **배터리는 필요한 만큼만** 조금씩 방전

<details class="nums" markdown="1">
<summary>발전원별 출력·입력</summary>

| 발전원 | 출력 | 입력 | 재생 가능? |
|---|---|---|---|
| 수동 발전기 | 400W | 복제체 노동 | 노동력 낭비 |
| 석탄 발전기 | 600W | 석탄 1kg/s | 주둥가리 목장이 있으면 반재생 |
| 수소 발전기 | 800W | 수소 100g/s | ✓ 전해조 부산물 |
| 천연가스 발전기 | 800W | 천연가스 90g/s | ✓ 천연가스 분출구가 있으면 |
| 솔라 패널 | 최대 380W | 햇빛 | ✓ 표면 필요, 운석 주의 |
| 증기 터빈 | 최대 850W | 125°C 이상 증기 | ✓ 열 삭제와 겸용 |
| 석유 발전기 | 2,000W | 석유 2kg/s | 석유 분출구·원유 우물 |

- 주둥가리 1마리 ≈ 석탄 70 kg/일. 석탄 발전기 상시 가동엔 많이 필요.

</details>

## 열: 옮기거나, 지우거나

{: .ico-grid}
1. {% include i.html n="Insulated_Tile" %} **초반: 분리** 뜨거운 건물을 절연 타일로
2. {% include i.html n="Wheezewort" %} **초중반: 씨근풀 (Wheezewort)·얼음** 주변 냉각
3. {% include i.html n="Thermo_Aquatuner" %} **중반: 열액체조화기 + 증기 터빈** 표준 해법
4. {% include i.html n="Anti_Entropy_Thermo-Nullifier" %} **후반: 항엔트로피열무효화장치 (Anti Entropy Thermo-Nullifier)** 수소로 열 삭제

{% include shot.html src="steam-cooler.jpg" size="half" caption="위 증기 터빈(+850W), 아래 증기 방 안에 열액체조화기(−1,200W). 설치 순서와 도면은 15 에어컨 설치에." %}

> 열액체조화기·터빈은 **강철 (Steel)** 로. 냉각수가 0°C 아래로 가면 파이프가 얼어 터지니 온도 센서로 제어.
{: .danger}

<details class="nums" markdown="1">
<summary>열원과 냉각 장치 원리</summary>

- 열이 나는 곳: 발전기 (석탄·천연가스·석유), 전해조, 퇴비, 제련소, 작업대, 뜨거운 바이옴.
- 원리: 냉각수 고리가 기지 열을 흡수 → 열액체조화기 (Thermo Aquatuner)가 액체를 14°C 식히고 열을 몸에 쌓음 (1,200 W) → 물 방 안에서 그 물이 끓어 증기 → 위의 증기 터빈 (Steam Turbine)이 증기 열을 전기로 바꾸고 95°C 물로 되돌림.
- 실제 설치는 [15 에어컨 설치]({{ '/guide/core-base/aircon/' | relative_url }}).

</details>

## 5~10사이클마다 점검

{: .ico-grid}
1. **일일 보고서** 산소·칼로리·전력 생산 ≥ 소비
2. **저장량 추세** 식량·물·배터리
3. **온도 오버레이** 농장·침실 25°C 안팎
4. **세균 오버레이** 물·음식
5. **사기·스트레스** 방·음식·장식

모든 추세가 평평하거나 오르면 복제체를 한 명 늘리세요.
