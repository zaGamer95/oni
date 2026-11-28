---
title: "사례 1 · 1-1: Persephazon 열 문제와 기끌이 목장 (사이클 108)"
nav_title: "열 문제·기끌이 목장"
nav_order: 30.2
nav_num: "1-1"
nav_group: case
nav_parent: case1-perse
dlc: spaced-out
game_version: u60-2026-11-20
eyebrow: 사례 1 · 1-1
permalink: /guide/case/terrania-1/drecko-ranch/
description: 에어컨이 아직 없는데 메인 기지가 데워져 농장이 멈춘 상황. 시드가 미리 깔아둔 오브젝트(텔레포터, 우라늄, 서늘한 증기 벤트, 천연 가스 분출구, 공급 텔레포터)를 피해 기지를 다듬고, SPOM 없이 전해조 하나로 수소를 채워 2LegitCity식 기끌이 목장(22×11)을 앉히는 계획.
---

* 목차
{:toc}

> [1장 Persephazon]({{ '/guide/case/terrania-1/persephazon/' | relative_url }})의 **계획안** (W 검토 중). 지어 보고 맞는 부분만 남깁니다.
{: .tip}

## 상황 (사이클 108)

{: .ico-grid}
- {% include i.html n="Mealwood" %} **기지가 데워져 농장 멈춤** 에어컨은 아직 없음
- {% include i.html n="Hatch" %} **식량원 여러 개로** 목축 비중 ↑
- {% include i.html n="Drecko" %} **첫 목장 = 기끌이 (Drecko)** 2LegitCity 디자인 ([영상](https://www.youtube.com/watch?v=VlnqM4lLKWA))

## 시드가 깔아둔 오브젝트: 기지를 여기에 맞춰 비틀기

{% include shot.html src="case1-seed-objects-east.jpg" caption="③ 천연가스 분출구(주황), ④ 공급 텔레포터 출력, ⑤ 공급 텔레포터 입력. 사이클 108." %}

{: .ico-grid}
- {% include i.html n="Teleporter_Transmitter" %} **텔레포터 (왼쪽 위)** 통로만 확보
- {% include i.html n="Uranium_Ore" %} **우라늄 광석** 당분간 파지 않기
- {% include i.html n="Cool_Steam_Vent" %} **서늘한 증기 벤트 ①·2번** 열원, 단열로 가둠
- {% include i.html n="Natural_Gas_Geyser" %} **천연가스 분출구 (Natural Gas Geyser) ③** 이쪽으로 넓히지 않기
- {% include i.html n="Supply_Teleporter_Input" %} **공급 텔레포터 ④출력·⑤입력** 막지 말고 동선 확보

<details class="nums" markdown="1">
<summary>프린팅팟 기준 위치표</summary>

| 위치 (포드 기준) | 오브젝트 | 다루는 법 |
|---|---|---|
| 왼쪽 위 | **텔레포터** (Oozato 연결) | 그대로 둠. 통로만 확보 |
| 텔레포터 바로 위 | **우라늄 광석** | **당분간 파지 않기.** 나중에 [수동 래드볼트 생성기]({{ '/guide/research/late/' | relative_url }})용 |
| 텔레포터 아래 | 옛 농장 (②) | 지금 잘 안 돎. 아래 분출구 열 때문으로 추정 |
| 그 아래 | **서늘한 증기 벤트** (①, Cool Steam Vent) | 열원. 단열로 가둠 |
| 오른쪽 아래 | **천연 가스 분출구** (③, Natural Gas Geyser) | 열원. 기지를 이쪽으로 넓히지 않기 |
| 그 아래 | **공급 텔레포터 출력** (④) | Oozato에서 물자가 들어오는 곳. 막지 않기 |
| ④의 오른쪽 | **서늘한 증기 벤트** 2번 | 열원 |
| 포드 한가운데 한참 아래 | **공급 텔레포터 입력** (⑤) | Oozato로 보내는 곳. 운반 동선 확보 |

</details>

## 에어컨 없이 열 줄이기

{: .ico-grid}
1. {% include i.html n="Insulated_Tile" %} **열원 가두기** 분출구 방 천장·농장 바닥을 절연 타일
2. **온도 오버레이로 배치** 열 건물은 아래 바깥, 식물·침실은 시원한 쪽
3. {% include i.html n="Pincha_Pepperplant" %} **더운 자리엔 더위 작물** 꼬집후추풀 (Pincha Pepperplant)·호리호리한 벵이과실 (Spindly Grubfruit)
4. {% include i.html n="Electrolyzer" %} **뜨거운 물은 전해조로** 19.45°C 넘는 물이면 열을 지움

<details class="nums" markdown="1">
<summary>온도 범위와 이유</summary>

- ① 서늘한 증기 벤트는 약 110°C 증기, 바로 위에 ② 농장. 열은 위로 올라오니 그 사이를 절연.
- 끼니나무 10~30°C, 꼬집후추풀 35~70°C, 호리호리한 벵이과실 15~50°C.
- 전해조: 산소·수소가 70°C로 나가며 들어온 물보다 열을 덜 들고 나감. 대신 70°C 기체를 생활 구역에 바로 풀면 안 됨.

</details>

## 식량원 늘리는 순서

{: .ico-grid}
1. {% include i.html n="Hatch" %} **주둥가리 (Hatch)** 돌 → 고기·석탄, 열에 강함
2. {% include i.html n="Drecko" %} **기끌이 (Drecko)** 섬유·플라스틱, 고기는 덤
3. {% include i.html n="Pacu" %} **드럽치 (Pacu)** 분출구 옆 웅덩이 그대로
4. {% include i.html n="Pincha_Pepperplant" %} **더위 작물** 꼬집후추풀, 벵이과실

## 기끌이 목장: A 자리, 22×11 2층

{% include shot.html src="case1-drecko-site-a.jpg" caption="① 서늘한 증기 벤트, ② 멈춘 농장, A = 기끌이 목장 22×11 자리. 화면 비율로 잰 추정이라 게임에서 칸 수를 꼭 확인하세요." %}

<div class="bp-wrap" markdown="0">
{% include bp/case1-drecko-ranch.svg %}
</div>

{: .ico-grid}
- {% include i.html n="Hydrogen_Generator" %} **위층: 수소** 기끌이 비늘
- {% include i.html n="Mealwood" %} **아래층: 끼니나무** 바닥에 산소층
- {% include i.html n="Grooming_Station" %} **외양간 (Stable) 94칸** 기끌이 7마리
- {% include i.html n="Atmo_Suit_Checkpoint" %} **입구** 체크포인트 → 슈트 3 → 액체 잠금

<details class="nums" markdown="1">
<summary>왜 A 자리인가, 축사 칸 계산</summary>

- 사다리를 놓아 둔 빈 공간이라 팔 양이 적고 우라늄·텔레포터 통로와 안 겹침. 빨간 바닥 아래 약 14칸 → 위 바위를 파면 11칸 높이.
- ① 분출구와 약 10칸 → **서쪽 벽은 절연 타일.** 배경이 정글 바이옴이면 수소가 원래 있어 채우기 쉬움 (추측).
- 외양간은 12~96칸. 위층 왼쪽 12×4 = 48 + 아래층 11×4 = 44 + 층 사이 구멍 2 = 94. 오른쪽 위는 벽으로 잘라 전해조 방.
- 기끌이 1마리 12칸 → 7마리. 알은 바로 꺼냄 (알도 칸 차지).
- 건물 크기는 위키 기준 (치장스테이션 2×3, 투입구·체크포인트 1×3). 정확한 위치는 영상을 따름.

</details>

## 수소 채우기: 전해조 1대, 약 2.2사이클

> **기끌이는 수소를 먹지 않습니다.** 한 번만 채우면 끝.
{: .tip}

{: .ico-grid}
1. {% include i.html n="Insulated_Tile" %} **벽·바닥·액체 잠금** 끼니나무는 아직
2. {% include i.html n="Electrolyzer" %} **전해조 + 기체 펌프 2** 천장 수소, 바닥 산소
3. {% include i.html n="Gas_Vent" %} **산소는 아래층 바닥 먼저** 남는 건 생활 구역 밖
4. {% include i.html n="Gas_Pipe" %} **수소 차면 밸브 잠금** 30°C 아래로 식으면 투입

<details class="nums" markdown="1">
<summary>수소량·시간 계산과 전체 순서</summary>

| 항목 | 값 |
|---|---|
| 기체 칸 | 축사 약 95칸 − 건물 ≈ 80칸 (위층 위주) |
| 필요한 수소 | 칸당 0.5~1 kg → **약 75~150 kg** (낮은 압력이어도 기끌이는 괜찮음) |
| 전해조 1대 | 물 1 kg/s → 산소 888 g/s + **수소 112 g/s**, 120 W |
| 걸리는 시간 | 150 kg ÷ 0.112 kg/s ≈ 1,340초 = **약 2.2사이클** |
| 물 | 약 1.3톤 (분출구 옆 웅덩이) |

1. A 자리를 파고 벽·바닥·액체 잠금까지 짓습니다. **끼니나무는 아직 심지 않아요.**
2. 오른쪽 위 방에 **전해조 + 기체 펌프 2대** (천장 = 수소, 바닥 = 산소). 물은 웅덩이에서 액체 펌프로 끌어옵니다.
3. **산소는 먼저 아래층 바닥으로** 보내 끼니나무용 산소층을 깔고, 남는 산소는 **생활 구역 밖**으로 보냅니다. 전해조 기체는 **70°C 이상**이라 지금처럼 더운 기지에 바로 풀면 안 돼요.
4. 수소는 가스 파이프로 축사 천장 배출구에. 2~3사이클 뒤 다 차면 **차단 밸브를 잠급니다.** 수소 파이프를 웅덩이에 방열 파이프로 한 번 지나가게 하면 덜 뜨겁게 들어갑니다.
5. 방이 30°C 아래로 식으면 끼니나무 8그루를 심고 기끌이를 투입합니다.
6. 나중에 이 방에 **수소 발전기**와 펌프를 더하면 그대로 [Half Rodriguez SPOM]({{ '/guide/sustainability/' | relative_url }}#산소-전해조-시스템-spom)의 시작이 됩니다.

</details>

## 번질한 기끌이로 플라스틱까지

{: .ico-grid}
- {% include i.html n="Glossy_Drecko" %} **번질한 기끌이 (Glossy Drecko)** 비늘 대신 플라스틱
- {% include i.html n="Mealwood" %} **끼니나무 먹이기** 일반 알에서도 조금씩
- {% include i.html n="Shearing_Station" %} **털 깎기 스테이션 (Shearing Station)** 마이메 (크리터 사육)
- **방 20~30°C** 기끌이 20~50, 끼니나무 10~30

## 확인할 것

- [ ] A 자리 실제 칸 수 (22×11이 들어가는지)
- [ ] 온도 오버레이로 A 자리 온도 (20~30°C인지)
- [ ] 영상 속 아래층이 산소를 어떻게 잡아두는지 (도면과 다르면 영상 쪽)
