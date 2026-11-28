---
title: 연구 순서와 타이밍
nav_title: 연구 순서와 타이밍
nav_order: 20
nav_group: ref
dlc: spaced-out
permalink: /guide/research/
description: Spaced Out! 기준 연구 트리를 사이클 구간별로. 무엇을 언제 연구하고, 연구 건물과 연구원은 언제 늘리는지.
---

* 목차
{:toc}

## 한눈에

**1~2단계는 빠르게, 3단계부터 슈퍼컴퓨터 같이, 5단계 전에 래드볼트, 6단계 전에 데이터 뱅크.** 장식·의료는 필요할 때만. 기술 이름 괄호 안 영어를 연구 화면 검색창에 넣으면 찾아집니다.

## 연구 포인트 4종류

{: .ico-grid}
1. {% include i.html n="Research_Station" %} **초급 (Novice)**<br>연구스테이션 · 흙 50 kg/점 · 1단계~
2. {% include i.html n="Super_Computer" %} **고급 (Advanced)**<br>슈퍼 컴퓨터 · 물 50 kg/점 · 3단계~
3. {% include i.html n="Materials_Study_Terminal" %} **응용 과학 (Applied Sciences)**<br>래드볼트 10개/점 · 5단계~
4. {% include i.html n="Virtual_Planetarium" %} **데이터 분석 (Data Analysis)**<br>데이터 뱅크 1개/점 · 6단계~

> 트리 전체에 흙 **178 t**, 물 **173 t**, 래드볼트 **31,050개**, 데이터 뱅크 **1,980개.** 연구스테이션 옆 **흙 저장고**, 슈퍼 컴퓨터 옆 **피처 펌프.** 흙은 퇴비로 보충.
{: .warn}

<details class="nums" markdown="1">
<summary>포인트별 건물·재료·스킬</summary>

| 포인트 | 건물 (해금 기술) | 재료 | 운영 조건 | 처음 필요한 단계 |
|---|---|---|---|---|
| **초급 연구** (Novice) | 연구스테이션 (Research Station), 처음부터 | **흙 (Dirt) 50 kg / 1포인트** | 누구나 | 1단계부터 |
| **고급 연구** (Advanced) | 슈퍼컴퓨터 (Super Computer) ← 고급 연구 (Advanced Research) | **물 (Water) 50 kg / 1포인트**, 복제체가 병으로 날라야 함 | 스킬 **Advanced Research** | 3단계부터 |
| **응용 과학** (Applied Sciences) | 재료 연구 터미널 (Materials Study Terminal) ← 재료 과학 연구 (Materials Science Research) | **래드볼트 (Radbolt) 10개 / 1포인트** | 스킬 **Applied Sciences Research** | 5단계부터 |
| **데이터 분석** (Data Analysis) | 가상 플라네타륨 (Virtual Planetarium) ← 충돌 계획 (Crash Plan) | **데이터 뱅크 (Data Bank) 1개 / 1포인트** | 스킬 **Data Analysis Researcher** | 6단계부터 |

</details>

<details class="nums" markdown="1">
<summary>단계별 기술 1개당 비용</summary>

| 단계 | 기술 수 | 초급 | 고급 | 응용 과학 | 데이터 분석 |
|---|---|---|---|---|---|
| 1 | 7 | 15 | | | |
| 2 | 12 | 20 | | | |
| 3 | 24 | 30 | 20 | | |
| 4 | 21 | 35 | 30 | | |
| 5 | 19 | 40 | 50 | **20** | 0 |
| 6 | 11 | 50 | 70 | 40 | **30** |
| 7 | 5 | 70 | 100 | 370 | 250 |
| 8 | 1 | 100 | 130 | 435 | 400 |
| **전체 합계** | 100 | **3,560** | **3,460** | **3,105** | **1,980** |

</details>

### 연구 속도

Science 9 연구원 혼자 **하루 50~60포인트.** 흙 배달이 더 큰 병목. 연구스테이션은 **프린팅팟 옆**(조명 공짜), 연구 건물 2개로 **연구소 (Laboratory)** 방, 옆에 **연구 도구 (Study Tools)** 책장 최대 4개(+20%).

<details class="nums" markdown="1">
<summary>Science별 1포인트 시간과 보너스</summary>

| 연구원 Science | 조명·연구실 | 1포인트당 |
|---|---|---|
| 9 (시작 직후) | 없음 | 6.8초 |
| 9 | 둘 다 | 6.6초 |
| 11 (Advanced Research 스킬 +2) | 둘 다 | 5.9초 |
| 13 (Field Research까지) | 둘 다 | 5.3초 |
| 4 (예비 연구원, Science 2 + 스킬) | 없음 | 9.8초 |


- **연구 도구 (Study Tools, 2026-11 U60 신규)**: 연구 건물 옆 2칸 안에 책장을 세우면 개당 연구 속도 **+5%**, 여러 개가 겹쳐서 **최대 4개 = +20%**. 연구 High Culture, 원석 400 kg + 섬유 2. 배치는 [지원 건물]({{ '/guide/core-base/rooms/' | relative_url }}#작업-속도-올리는-지원-건물-2026년-11월-패치-u60).
- **조명**: 프린팅팟 (Printing Pod) 바로 옆에 연구소를 두면 조명 보너스를 공짜로 받습니다.
- **연구소 (Laboratory)**: 연구 건물 2개, 32~120칸, 산업 기계 없음. 연구소 + 슈퍼컴퓨터를 한 방에 넣으면 됩니다. [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }})의 30×4 칸에 딱 맞아요. 연구실이 있어야 지오튜너(Geotuner)와 임무통제 스테이션(Mission Control Station)을 쓸 수 있습니다.

</details>

## 초반·중반·후반은 연구로 나눕니다

{: .ico-grid}
1. {% include i.html n="Research_Station" %} **초반** 시작 ~ [초반 테크]({{ '/guide/research/early/' | relative_url }})
2. {% include i.html n="Materials_Study_Terminal" %} **중반** 재료 과학 연구 ~ [중반 테크]({{ '/guide/research/mid/' | relative_url }})
3. {% include i.html n="Virtual_Planetarium" %} **후반** 데이터 분석 ~ [후반 테크]({{ '/guide/research/late/' | relative_url }})

<details class="nums" markdown="1">
<summary>구간별 신호·포인트·핵심</summary>

| 구간 | 시작 신호 | 연구 포인트 | 핵심 | 페이지 |
|---|---|---|---|---|
| **초반** | 게임 시작 | 초급 + 고급 | 생존 → SPOM → **두 번째 행성 (텔레포터)** → 단열 → 냉방 → 특수복 → 첫 로켓. **증기 터빈 없이 버티는 법** | [7 초반 테크]({{ '/guide/research/early/' | relative_url }}) |
| **중반** | **재료 과학 연구** (Materials Science Research) | + 응용 과학 (래드볼트, 5단계부터) | 래드볼트, 증기 터빈, 지오튜너, 납 특수복, 플라스틱, 8명 운영 | [17 중반 테크]({{ '/guide/research/mid/' | relative_url }}) |
| **후반** | **데이터 분석** (Data Analysis) 포인트가 필요한 6단계 | + 데이터 분석 (데이터 뱅크) | 석유 엔진 로켓, 연구용 반응로, 제트 특수복 | [19 후반 테크]({{ '/guide/research/late/' | relative_url }}) |

</details>

## 연구원 스킬과 두 번째 연구원

### 연구 전담 복제체의 스킬 순서

{: .ico-grid}
1. **고급 연구 (Advanced Research)** 사기 0
2. **천문학 (Astronomy)** 사기 1, 망원경
3. **현장 연구 (Field Research)** 사기 1
4. **응용 과학 연구 (Applied Sciences Research)** 사기 2
5. **데이터 분석 연구원 (Data Analysis Researcher)** 사기 2

다 찍으면 Science **+10**, 사기 요구치 **6.**

> **처음 30사이클은 연구원 1명.** 복제체 5~6명(사이클 25~40)에 예비 연구원을 연구스테이션 담당으로.
{: .tip}

<details class="nums" markdown="1">
<summary>스킬 표 (열리는 것·시점)</summary>

| 순서 | 스킬 | 단계 | 사기 (관심 O) | 열리는 것 | 필요한 시점 |
|---|---|---|---|---|---|
| 1 | **Advanced Research** | 1 | 0 | 슈퍼컴퓨터, 유화기 | 고급 연구 기술 직후 (사이클 6~10) |
| 2 | **Astronomy** | 2 | 1 | **망원경**, 밀폐 망원경, 궤도 데이터 수집 실험실, 임무통제 스테이션 | 망원경 지은 직후 |
| 3 | **Field Research** | 2 | 1 | 간헐천 분석, 지오튜너 | Applied Sciences의 선행 |
| 4 | **Applied Sciences Research** | 3 | 2 | **재료 연구 터미널** | 5단계 전 (사이클 60~80) |
| 5 | **Data Analysis Researcher** | 3 | 2 | **가상 플라네타륨** | 6단계 전 |

</details>

<details class="nums" markdown="1">
<summary>스킬 포인트가 들어오는 시점 (추정)</summary>

| 누적 스킬 포인트 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 필요 누적 경험치 | 3,038 | 8,241 | 14,777 | 22,361 | 30,834 |
| 대략 사이클 | 6 | 17 | 30 | 45 | 62 |

</details>

<details class="nums" markdown="1">
<summary>두 번째 연구원은 언제</summary>

| 시점 | 신호 | 할 일 |
|---|---|---|
| **사이클 25~40** (복제체 5~6명) | 3단계에서 연구소와 슈퍼컴퓨터가 번갈아 놀고 있음 | 예비 연구원(예: Marie, Science 2)의 연구 우선순위를 올려 **연구소 담당**으로. 주 연구원은 슈퍼컴퓨터로. Science가 높은 복제체가 연구소를 알아서 가져가니 따로 지정할 필요는 없음 |
| 예비 연구원 스킬 | 슈퍼컴퓨터도 같이 돌리고 싶을 때 | Advanced Research 1개만 찍으면 슈퍼컴퓨터 운영 가능 |
| **사이클 80~** | 5단계: 단말기·천체투영관까지 4개 건물 | 주 연구원은 단말기·천체투영관(스킬이 필요한 쪽), 예비 연구원은 연구소+슈퍼컴퓨터 |
| 복제체 10명 이상 | 연구가 확장 속도를 못 따라감 | 세 번째 연구원 또는 연구소 1개 추가. 흙 배달 일손도 늘어나니 주의 |


- 생체공학 복제체는 연구 부스터 (Researching Booster)를 장착해야 연구.

</details>

## 연구 타임라인

<details class="nums" markdown="1">
<summary>사이클별 연구·건물·연구원·짓는 것</summary>

| 사이클 | 연구 | 연구 건물 | 연구원 | 짓는 것 (건설 순서) |
|---|---|---|---|---|
| 1~8 | 기본 재배 → 식사 준비 → 전력 조절 → 내연 기관 → 고용 → **고급 연구** | 연구소 | 1명 | 수동 발전기 → 농장 → 식당 → 석탄 발전기 |
| 8~20 | 액체 파이프 → 위생 → 환기 → 공기 시스템 → 압력 관리 → 무차별 정제 → 여과 | 연구소 + **슈퍼컴퓨터** + **망원경** | 1명 (Advanced Research, Astronomy) | 수세식 화장실, 수조, 전해조 |
| 20~45 | 고급 전력 제어 → 온도 조절 → 개선된 배관 → 증류 → 정제된 혁신 → 농업 → 화석 연료 | 연구소(Laboratory) 완성 | 1명 → 25~40에 **2명** | SPOM, 단열 격벽, 저장고, 소방서 폴 통로 |
| 45~80 | 액체 튜닝 → 공조 → 위험 방지 → 제련 → 우주 프로그램 → 엔진 → 재료 과학 연구 → 충돌 계획 | + 래드볼트 생성기 | 2명 (Field Research, Applied Sciences) | 냉방 루프, 환경 특수복, 강철, **첫 로켓** |
| 80~150 | 5단계: 재생 가능 에너지, 초과열 제조, 밸브 소형화, 내구성 뛰어난 생명 유지 장치, 방사선 보호 | + **재료 연구 터미널** | 2명 | 증기 터빈, 지오튜너, 우라늄 채굴 |
| 150~ | 6~8단계: 탄화수소 추진 → 개선된 탄화수소 추진, 방사선 정제 | + **가상 플라네타륨** | 2~3명 (Data Analysis) | 석유 엔진 로켓, 연구용 반응로 |

</details>

다음: [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }}) · [플레이 팁]({{ '/guide/tips/' | relative_url }})

<details class="nums" markdown="1">
<summary>출처</summary>

- 연구 트리·단계·비용: [Oxygen Not Included Wiki](https://oxygennotincluded.wiki.gg/) 원본 데이터 (Module:Data/Techs, Module:ResearchCost, Spaced Out! 기준)
- 연구 건물: Research Station, Super Computer, Materials Study Terminal, Virtual Planetarium (Spaced Out), Orbital Data Collection Lab, Telescope (Spaced Out) 문서
- 래드볼트: Radbolt Generator, Manual Radbolt Generator, Radiation 문서
- 스킬과 경험치: Skills 문서
- 소행성 구성: 위키 월드 생성 데이터 (Terrania 성단)

</details>
