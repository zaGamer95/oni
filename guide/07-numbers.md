---
title: 수치 치트시트
nav_title: 수치 치트시트
nav_order: 24
nav_group: ref
permalink: /guide/numbers/
description: 자주 찾는 건물·작물 수치. 1사이클 = 600초. 패치로 바뀔 수 있으니 게임 안 툴팁으로 최종 확인하세요.
---

* 목차
{:toc}

1사이클 = 600초. 카드에 핵심 숫자, 펼치면 전체 표. 다섯 가지 점검 기준표는 [부록 A 지속 가능성 컨텍스트]({{ '/appendix/sustainability-context/' | relative_url }}).

## 산소

{: .ico-grid}
- {% include i.html n="Oxygen_Diffuser" %} **산소 확산기 (Oxygen Diffuser)** ≈ 5명
- {% include i.html n="Electrolyzer" %} **전해조 (Electrolyzer)** ≈ 8명, 70°C+
- {% include i.html n="Algae_Terrarium" %} **조류 배양기 (Algae Terrarium)** 0.4명

<details class="nums" markdown="1">
<summary>건물별 입력·출력·전력</summary>

| 건물 | 입력 | 출력 | 전력 | 복제체 몇 명분 |
|---|---|---|---|---|
| 산소 확산기 (Oxygen Diffuser) | 조류 550g/s | 산소 500g/s | 120W | 약 5명 |
| 조류 배양기 (Algae Terrarium) | 조류 30g/s + 물 300g/s | 산소 40g/s (+CO₂ 흡수) | — | 0.4명 |
| 전해조 (Electrolyzer) | 물 1kg/s | 산소 888g/s + 수소 112g/s (70°C 이상) | 120W | 약 8명 |

</details>

## 전력

{: .ico-grid}
- {% include i.html n="Coal_Generator" %} **석탄 발전기 (Coal Generator)** 600 W
- {% include i.html n="Hydrogen_Generator" %} **수소 발전기 (Hydrogen Generator)** 800 W
- {% include i.html n="Petroleum_Generator" %} **석유 발전기 (Petroleum Generator)** 2,000 W
- {% include i.html n="Smart_Battery" %} **스마트 배터리 (Smart Battery)** 20 kJ

<details class="nums" markdown="1">
<summary>발전기·배터리 전체</summary>

| 건물 | 출력 / 용량 | 입력 |
|---|---|---|
| 수동 발전기 (Manual Generator) | 400W | 복제체 노동 |
| 석탄 발전기 (Coal Generator) | 600W | 석탄 1kg/s |
| 수소 발전기 (Hydrogen Generator) | 800W | 수소 100g/s |
| 천연가스 발전기 (Natural Gas Generator) | 800W | 천연가스 90g/s (오염된 물·CO₂ 배출) |
| 석유 발전기 (Petroleum Generator) | 2,000W | 석유 2kg/s |
| 증기 터빈 (Steam Turbine) | 최대 850W | 125°C 이상 증기 |
| 솔라 패널 (Solar Panel) | 최대 380W | 햇빛 |
| 배터리 (Battery) | 10kJ | — |
| 스마트 배터리 (Smart Battery) | 20kJ | — |
| 점보 배터리 (Jumbo Battery) | 40kJ | — |

</details>

## 와이어·파이프

{: .ico-grid}
- {% include i.html n="Wire" %} **와이어 (Wire)** 1 kW
- {% include i.html n="Heavi-Watt_Wire" %} **헤비와트 와이어 (Heavi-Watt Wire)** 20 kW
- {% include i.html n="Liquid_Pipe" %} **액체 파이프 (Liquid Pipe)** 10 kg/s
- {% include i.html n="Gas_Pipe" %} **기체 파이프 (Gas Pipe)** 1 kg/s

<details class="nums" markdown="1">
<summary>용량·펌프</summary>

| 항목 | 용량 |
|---|---|
| 와이어 / 전도성 와이어 | 1kW / 2kW |
| 헤비와트 와이어 / 헤비와트 전도성 와이어 | 20kW / 50kW |
| 변압기 / 큰 변압기 | 1kW / 4kW |
| 액체 파이프 | 10kg/s |
| 기체 파이프 | 1kg/s |
| 액체 펌프 / 소형 액체 펌프 | 10kg/s, 240W / 0.5kg/s, 60W |
| 가스 펌프 / 소형 가스 펌프 | 0.5kg/s, 240W / 50g/s, 60W |

</details>

## 물·위생

{: .ico-grid}
- {% include i.html n="Lavatory" %} **수세식 화장실 (Lavatory)** 5 kg → 11.7 kg
- {% include i.html n="Water_Sieve" %} **물 체 (Water Sieve)** 5 kg/s, 120 W
- {% include i.html n="Thermo_Aquatuner" %} **열액체조화기 (Thermo Aquatuner)** −14°C, 1,200 W

<details class="nums" markdown="1">
<summary>건물 수치</summary>

| 건물 | 수치 |
|---|---|
| 수세식 화장실 (Lavatory) | 물 5kg 사용 → 오염된 물 약 11.7kg 배출 (1회당) |
| 물 체 (Water Sieve) | 오염된 물 5kg/s + 모래 1kg/s → 물 5kg/s, 120W |
| 열액체조화기 (Thermo Aquatuner) | 통과 액체 −14°C, 1,200W |

</details>

## 작물

{: .ico-grid}
- {% include i.html n="Mealwood" %} **끼니나무 (Mealwood)** 1명당 5그루
- {% include i.html n="Bristle_Blossom" %} **센털꽃 (Bristle Blossom)** 1명당 4그루 (구우면 3)

<details class="nums" markdown="1">
<summary>수확 주기·칼로리·입력</summary>

| 작물 | 수확 주기 (길들인 상태) | 칼로리 | 복제체당 개수 | 입력 |
|---|---|---|---|---|
| 끼니나무 (Mealwood) | 3사이클 | 600kcal | 약 5개 | 흙 10kg/사이클 |
| 센털꽃 (Bristle Blossom) | 6사이클 | 1,600kcal (구우면 2,000) | 약 4개 (구우면 3개) | 물 20kg/사이클, 빛 |

</details>

## 생물

{: .ico-grid}
- {% include i.html n="Hatch" %} **주둥가리 (Hatch)** 석탄 ≈ 70 kg/일
- {% include i.html n="Pacu" %} **드럽치 (Pacu)** 생선
- {% include i.html n="Puft" %} **헐떡이 (Puft)** 는지렁이

<details class="nums" markdown="1">
<summary>동물별 쓸모</summary>

| 동물 | 쓸모 |
|---|---|
| 주둥가리 (Hatch) | 바위를 먹고 석탄을 냄 (먹은 양의 약 50%). 하루 약 70kg |
| 드럽치 (Pacu) | 물속 동물. 고기(생선) |
| 헐떡이 (Puft) | 오염된 산소를 먹고 는지렁이를 냄 |

</details>

## 음식 보존

{: .ico-grid}
- {% include i.html n="Refrigerator" %} **4°C 이하** 냉장
- {% include i.html n="Ice" %} **−18°C 이하** 냉동
- {% include i.html n="Carbon_Dioxide" %} **CO₂·진공** 부패 정지

<details class="nums" markdown="1">
<summary>조건별 효과</summary>

| 조건 | 효과 |
|---|---|
| 4°C 이하 | 냉장 (부패 느림) |
| −18°C 이하 | 냉동 (부패 거의 없음) |
| CO₂ 속 또는 진공 | 무균 상태 (부패 정지) |

</details>

## 방 크기

{: .ico-grid}
- {% include i.html n="Mess_Table" %} **12~64** 식당·막사·화장실
- {% include i.html n="Farm_Tile" %} **12~96** 온실·주방·발전소
- {% include i.html n="Research_Station" %} **32~120** 큰 회관·연구소

<details class="nums" markdown="1">
<summary>크기별 방 전체</summary>

| 크기 | 해당 방 |
|---|---|
| 12~64칸 | 화장실, 막사, 호화 막사, 식당, 공원 |
| 12~96칸 | 주방, 온실, 목장, 병원, 발전소, 오락실 |
| 24~64칸 | 개인 침실 |
| 32~120칸 | 큰 회관, 연구실, 자연보호구역 |

</details>
