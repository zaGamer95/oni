---
title: 방 크기와 방 배치
nav_title: 방 크기
nav_order: 8.1
nav_num: "8-1"
nav_group: early
nav_parent: core-base
permalink: /guide/core-base/rooms/
description: 방 종류별 크기 범위와 배치도 크기, 층별 방 배치, 한 방에 같이 두면 안 되는 조합, 작업 속도를 올리는 지원 건물(U60) 배치.
---

* 목차
{:toc}

> 전체 도면은 [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }}). 크기는 **벽 안쪽 칸 수.**
{: .tip}

## 방 크기

{: .ico-grid}
- {% include i.html n="Lavatory" %} **세척실 (Washroom)** 16×3 · 사기 +2
- {% include i.html n="Shower" %} **샤워실** 16×4 · 샤워 +3
- {% include i.html n="Comfy_Bed" %} **개인 침실 (Private Bedroom)** 6×4 · +3
- {% include i.html n="Comfy_Bed" %} **호화 막사 (Luxury Barracks)** 16×4 · +2
- {% include i.html n="Mess_Table" %} **큰 회관 (Great Hall)** 24×5 복층 · +4
- {% include i.html n="Gas_Range" %} **주방 (Kitchen)** 24×4
- {% include i.html n="Super_Computer" %} **연구소 (Laboratory)** 24×4 · 연구 +10%
- {% include i.html n="Farm_Station" %} **온실 (Greenhouse)** 15×7 · 성장 2배
- {% include i.html n="Grooming_Station" %} **외양간 (Stable)** 24×4
- {% include i.html n="Coal_Generator" %} **발전소 (Power Plant)** 24×4
- {% include i.html n="Water_Cooler" %} **오락실 (Recreation Room)** 24×4
- {% include i.html n="Mirth_Leaf" %} **자연보호구역 (Nature Reserve)** 통로 3×28 · +6

> 발전소·온실·목장·주방 말고는 **산업 기계 금지** (발전기·전해조·물 체·펌프·제련소). 산소 확산기·배터리·냉장고·미생물 걸죽기·전기 그릴은 괜찮음.
{: .warn}

<details class="nums" markdown="1">
<summary>방 크기 전체 표 (범위·조건·효과)</summary>

| 방 | 크기 범위 | 배치도 크기 | 조건 | 효과 |
|---|---|---|---|---|
| 변소 (Latrine) | 12~64 | 16×4 = 64 | 뒷간 + 세면기 | 사기 +1 |
| 화장실 = 세척실 (Washroom) | 12~64 | **16×3 = 48** (싱크대 2 · 수세식 4 · 싱크대 2, 높이 3) | 수세식 화장실 + 싱크대(Sink), **뒷간 없음** | 사기 +2 |
| 막사 (Barracks) | 12~64 | 16×4 = 64 (초반, 나중에 호화 막사) | 침대 1개 이상 | 사기 +1 |
| 호화 막사 (Luxury Barracks) | 12~64 | **16×4 = 64** (편안한 침대 4, 4칸 폭) | 편안한 침대, **간이 침대 없음**, 장식 1, 천장 4칸 | 사기 +2 |
| 개인 침실 (Private Bedroom) | 24~64 | **6×4 = 24** (침대 4칸 + 장식 2칸) | 편안한 침대 **딱 1개**, 장식 2, 천장 4칸, **뒷벽 전부** | 사기 +3 |
| 식당 (Mess Hall) | 12~64 | 초반 임시 벽으로 **12×5 = 60** | 식탁 | 사기 +3 |
| 샤워실 (방 종류 아님) | 제한 없음 | **16×4** (샤워기 2×4 × 8) | 샤워(Shower), 위생 연구 | 샤워 1회 사기 +3 (약 1사이클), 물 16kg |
| 큰 회관 (Great Hall) | 32~120 | **24×5 = 120, 복층** (발판 18칸 빼면 102) | 식탁 + 장식 20 이상 1개 + 오락 건물 | 사기 +4 |
| 연회장 (Banquet Hall) | 32~120 | 30×4 = 120 | 공동 식탁(Communal Table), 장식, 오락 건물, 장식품 전시, **식탁 없음** | 사기 +6 |
| 주방 (Kitchen) | 12~96 | **24×4 = 96** | 향신료 분쇄기 + 그릴/가스레인지 + 냉장고, **식탁 없음** | 향신료 사용 |
| 연구소 (Laboratory) | 32~120 | **24×4 = 96** (포드 포함) | 연구 건물 2개 | 연구 +10%, 지오튜너·관제소 사용 |
| 온실 (Greenhouse) | 12~96 | 15×7 = 91칸 (3칸 높이 층, 작업대 들어감). 23×5 끼니나무 농장은 작업대가 안 들어가 방 아님 | 재배스테이션 | 비료로 성장 2배 |
| 외양간 (Stable) | 12~96 | **24×4 = 96** (주둥가리·기끌이) / 12×8 = 96 (헐떡이) | 목장 건물 (치장스테이션 등) | 동물 손질 |
| 발전소 (Power Plant) | 12~96 | **24×4 = 96** | 대형 발전기 + 전력 건물 2개 | 마이크로칩으로 발전 +50% |
| 오락실 (Recreation Room) | 12~96 | **24×4 = 96** | 오락 건물 + 장식 | 휴식 시간 사기 보너스 |
| 마사지 클리닉 (Massage Clinic) | 12~64 | **16×4 = 64** | 마사지 테이블 + 장식 | 스트레스 감소 2배 |
| 병원 (Hospital) | 12~96 | 24×4 = 96 | 의료 건물 + 화장실 + 식탁 | 병 전파 감소 |
| 공원 (Park) | 12~64 | 초반 사다리 통로 3×21 ≈ 59 | 공원 표지판 + 야생 식물 2 | 지나가면 사기 +3 |
| 자연보호구역 (Nature Reserve) | 32~120 | **사다리 통로 3×28 ≈ 79** | 공원 표지판 + 야생 식물 4 | 지나가면 사기 +6 |

</details>

## 생활 구역 방 배치

코어 24칸 폭에 아래부터 **포드 → 샤워실 → 화장실 → 식당**, 서쪽 침실 블록, 동쪽 실내 농장·목장.

| 층 (위 → 아래) | 서쪽 (바깥 ← 통로) | 코어 24칸 | 동쪽 (통로 → 바깥) |
|---|---|---|---|
| 1 | 개인 침실 6×4 × 4 + 현관 | 오락실 | 작업장 (저장통·제작) |
| 2 | 주방 24 | **복층 큰 회관** 24×5 (식탁 14) | 실내 온실 B (센털꽃, 15×7) |
| 3 | 개인 침실 6×4 × 4 + 현관 | **화장실 (세척실)** 16×3 + **기계실** 7×3 (물 체·모래·갈대) | ↑ |
| 4 | 개인 침실 6×4 × 4 + 현관 | **샤워실** 16×4 (샤워기 8) + 여유 7×4 | 실내 온실 A (끼니나무, 23×5) |
| 5 | 마사지 클리닉 16 · 호화 막사 16 | **포드층 연구실** (포드 + 연구소 + 슈퍼컴퓨터) | 실내 목장: 주둥가리 24 |
| 6 | 실내 목장: 기끌이 24 | 예비 (병원 등) | 깨끗한 물 수조 30 |

<details class="nums" markdown="1">
<summary>배치 이유</summary>

- 침실은 한 블록 (개인 12 + 호화 막사 4 = 16명분). 침실 줄 끝 5칸은 현관(장식).
- 환경 특수복 거치대는 침실 앞이 아니라 **위험 지역 출구**(텔레포터·격벽 에어락).
- 서쪽 3칸 통로가 자연보호구역 → 침실에서 나오면 바로 버프.
- 식당(높이 5) + 화장실(높이 3) = 9칸 = 보통 두 층, 양옆 격자 유지.
- 샤워실·화장실·기계실(물 체·갈대)은 한 폐쇄 루프 ([배관]({{ '/guide/core-base/envelope/' | relative_url }}#화장실샤워실-폐쇄-루프)).

</details>

## 같이 두면 안 되는 것

업그레이드하려면 초반 건물을 **철거**해야 하는 조합.

| 같이 두면 | 결과 |
|---|---|
| 뒷간 + 수세식 화장실 | 세척실 안 됨 (뒷간 방으로 남음) |
| 간이 침대 + 편안한 침대 | 호화 막사 안 됨 (막사로 남음) |
| 편안한 침대 2개 이상 | 개인 침실 안 됨 (호화 막사가 됨) |
| 식탁 + 주방 설비 | 주방 안 됨. 주방은 **식탁 없는 별도 방** |
| 식탁 + 공동 식탁 | 연회장 안 됨 |
| 식탁 + 침대 (한 방) | 두 조건을 같이 만족 → **기타 방**, 보너스 0 |
| 수동 발전기·펌프·전해조 등 + 생활 방 | 산업 기계라 방 보너스 사라짐 |
| 공원 + 자연보호구역 | 겹쳐서 받지 않음, +6이 +3을 덮어씀 |

## 지원 건물 (U60, 2026-11-19)

근처 호환 건물의 작업 속도를 올림. **일꾼·전력 불필요.**

{: .ico-grid}
- {% include i.html n="Study_Tools" %} **연구 도구 (Study Tools)** 연구 +5%, **최대 4개 겹침**
- {% include i.html n="Cooking_Tools" %} **조리 도구 (Cooking Tools)** 요리 +15%
- {% include i.html n="Workshop_Tools" %} **워크숍 도구 (Workshop Tools)** 제작 +15%, 뒷벽
- {% include i.html n="Forge_Tools" %} **단조 도구 (Forge Tools)** 제련 +15%

<details class="nums" markdown="1">
<summary>크기·연구·재료·범위·호환 건물</summary>

| 지원 건물 | 크기 | 연구 | 재료 | 효과 | 겹침 | 범위 | 호환 건물 |
|---|---|---|---|---|---|---|---|
| **연구 도구** (Study Tools) 책장 | 1×4 | High Culture | 원석 400 kg + 섬유 2 | 연구 속도 **+5%** | **겹침** (최대 4개 = +20%) | 좌우 2칸, 아래 2줄 | 연구소, 슈퍼컴퓨터, 가상 플라네타륨 (Virtual Planetarium), 재료 연구 터미널 (Materials Study Terminal) `SO` |
| **조리 도구** (Cooking Tools) 냄비 걸이 | 3×1 | Home Luxuries | 정제 금속 200 kg | 요리 속도 **+15%** | 안 겹침 | 좌우 2칸, 자기 줄 + 아래 2줄 | 전기 그릴, 가스 레인지, 향신료 분쇄기, 미생물 걸죽기, 튀김기 (Deep Fryer), 스모커 (Smoker), 탈수기 (Dehydrator), 알 크래커 (Egg Cracker), 스시바 (Sushi Bar) |
| **워크숍 도구** (Workshop Tools) 공구 선반 | 3×1, **뒷벽 필요** | Plastic Manufacturing | 금속 광석 400 kg + 목재 100 kg | 제작 속도 **+15%** | 안 겹침 | 좌우 4칸, 자기 줄 + 아래 2줄 | 제작 스테이션 (Crafting Station), 쇄석기, 합판 프레스 (Plywood Press), 분자 제조소 (Molecular Forge), 땜질 스테이션 (Soldering Station) `생체공학`, 가황기 (Vulcanizer) `수중` |
| **단조 도구** (Forge Tools) | 1×2 | Solid Control | 세라믹 600 kg + 정제 금속 200 kg | 제작 속도 **+15%** | 안 겹침 | 좌우 4칸, 자기 2줄 | 금속 제련소, 가마 (Kiln), 유리 제조소 (Glass Forge), 산소석 제련소 (Oxylite Refinery), 우라늄 원심분리기 `SO` |

- 호환 건물 칸이 범위에 **한 칸이라도** 들어가면 적용. 건설 미리보기로 범위 확인 (위키 문서가 아직 stub).
- 연구소는 과학 보너스가 1/3로 계산되니 실제 값은 툴팁으로.

</details>

### 연구실: 연구 건물 양옆에 책장 2칸씩

<div class="bp-wrap" markdown="0">{% include bp/support-lab.svg %}</div>

연구 건물 사이를 **2칸만** 띄우고 책장을 세우면 가운데 책장이 양쪽에 걸려 **6개로 둘 다 +20%.**

### 주방: 조리대 묶음 위에 냄비 걸이 1개

<div class="bp-wrap" markdown="0">{% include bp/support-kitchen.svg %}</div>

조리대 셋을 붙이고 천장 줄에 1개 → 셋 다 +15%.

### 정제·제련: 공구 선반 + 단조 도구

<div class="bp-wrap" markdown="0">{% include bp/support-refining.svg %}</div>

[정제 금속]({{ '/guide/core-base/refining/' | relative_url }})의 14×4 칸. 워크숍 도구는 **뒷벽(건식벽체) 필요.** 금속 제련소(점선)는 냉방실 뒤에.

<details class="nums" markdown="1">
<summary>출처</summary>

[위키 Versions/U60-763796 (11월 QoL 업데이트 패치 노트)](https://oxygennotincluded.wiki.gg/wiki/Versions/U60-763796), [Study Tools](https://oxygennotincluded.wiki.gg/wiki/Study_Tools), [Cooking Tools](https://oxygennotincluded.wiki.gg/wiki/Cooking_Tools), [Workshop Tools](https://oxygennotincluded.wiki.gg/wiki/Workshop_Tools), [Forge Tools](https://oxygennotincluded.wiki.gg/wiki/Forge_Tools). 건물 아이콘 © Klei Entertainment.

</details>
