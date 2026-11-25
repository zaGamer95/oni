---
title: "사례 1 · 1-1: Persephazon 열 문제와 드레코 목장 (사이클 108)"
nav_title: "열 문제·드레코 목장"
nav_order: 30.2
nav_num: "1-1"
nav_group: case
nav_parent: case1-perse
dlc: spaced-out
game_version: u60-2026-11-20
eyebrow: 사례 1 · 1-1
permalink: /guide/case/terrania-1/drecko-ranch/
description: 에어컨이 아직 없는데 메인 기지가 데워져 농장이 멈춘 상황. 시드가 미리 깔아둔 오브젝트(텔레포터, 우라늄, 차가운 증기 분출구, 천연 가스 분출구, 공급 텔레포터)를 피해 기지를 다듬고, SPOM 없이 전기분해기 하나로 수소를 채워 2LegitCity식 드레코 목장(22×11)을 앉히는 계획.
---

* 목차
{:toc}

> [사례 1 · 1장]({{ '/guide/case/terrania-1/persephazon/' | relative_url }})의 시작 행성 **Persephazon** 이야기입니다. 아직 W가 검토 중인 **계획안**이에요. 실제로 지어보고 맞는 부분만 남깁니다.
{: .tip}

## 상황 (사이클 108)

- **열:** 메인 기지 온도가 올라 **농장이 멈췄고 식량이 빠듯해졌습니다.** 수냉 조절기·증기 터빈이 아직 없어 [에어컨]({{ '/guide/core-base/aircon/' | relative_url }})은 못 씁니다.
- **식량:** 작물 한 종류에 기대면 이렇게 한 번에 무너집니다. **식량원을 여러 개**로 나누고, **목축을 더 적극적으로** 하기로 했어요.
- **목장:** 유튜버 **2LegitCity**의 목장 디자인을 따라가기로 하고, 첫 번째로 **드레코 목장 (Drecko Ranch)** 을 짓습니다. ([참고 영상](https://www.youtube.com/watch?v=VlnqM4lLKWA))

## 시드가 깔아둔 오브젝트

일반 가이드의 기지 모양을 그대로 쓰면 안 되는 이유입니다. 시드마다 위치가 정해진 건물·분출구가 있어서, **기지를 이것들에 맞춰 조금씩 비틀어야** 합니다. 프린팅 포드 기준이에요.

| 위치 (포드 기준) | 오브젝트 | 다루는 법 |
|---|---|---|
| 왼쪽 위 | **텔레포터** (Oozato 연결) | 그대로 둠. 통로만 확보 |
| 텔레포터 바로 위 | **우라늄 광석** | **당분간 파지 않기.** 나중에 [수동 래드볼트 생성기]({{ '/guide/research/late/' | relative_url }})용 |
| 텔레포터 아래 | 옛 농장 (②) | 지금 잘 안 돎. 아래 분출구 열 때문으로 추정 |
| 그 아래 | **차가운 증기 분출구** (①, Cool Steam Vent) | 열원. 단열로 가둠 |
| 오른쪽 아래 | **천연 가스 분출구** (③, Natural Gas Geyser) | 열원. 기지를 이쪽으로 넓히지 않기 |
| 그 아래 | **공급 텔레포터 출력** (④) | Oozato에서 물자가 들어오는 곳. 막지 않기 |
| ④의 오른쪽 | **차가운 증기 분출구** 2번 | 열원 |
| 포드 한가운데 한참 아래 | **공급 텔레포터 입력** (⑤) | Oozato로 보내는 곳. 운반 동선 확보 |

{% include shot.html src="case1-seed-objects-east.jpg" caption="③ 천연 가스 분출구(주황), ④ 공급 텔레포터 출력, ⑤ 공급 텔레포터 입력. 사이클 108." %}

## 에어컨 없이 열 줄이기

에어컨이 생기기 전까지는 **열을 만들지 않고, 들어오지 못하게 막는 것**이 전부입니다.

1. **열원부터 가두기.** ① 차가운 증기 분출구는 약 110°C 증기를 뿜고, 바로 위에 ② 농장이 있습니다. 열은 위로 올라오니 **분출구 방 천장과 농장 바닥을 단열 타일**로 바꿉니다. ③ 천연 가스 분출구 쪽도 단열 벽으로 막고, 기지는 반대 방향으로 키웁니다.
2. **바이옴 온도를 읽고 기지 모양을 맞추기.** 온도 오버레이(F3)로 보면 시원한 바이옴이 어디인지 보입니다. **열을 내는 건물(발전기, 정제기)은 기지 바깥 아래쪽**, **식물과 침실은 시원한 쪽**에 둡니다.
3. **열에 강한 작물로 바꾸기.** 이미 뜨거워진 자리에는 끼니나무(10~30°C) 대신 **핀차 후추 (Pincha Pepper, 35~70°C)** 나 **그럽과일 (Spindly Grubfruit, 15~50°C)** 을 심습니다. 끼니나무는 시원한 곳으로 옮겨요.
4. **뜨거운 물은 전기분해기로.** 전기분해기는 들어온 물이 19.45°C보다 뜨거우면 **오히려 열을 지웁니다** (산소·수소가 70°C로 나가며 물보다 열을 덜 들고 나감). 분출구 쪽 뜨거운 물을 전기분해기에 쓰는 이유예요. 단, 나오는 70°C 기체를 생활 구역에 바로 풀면 안 됩니다.

## 식량원 늘리기 순서

| 순서 | 식량원 | 왜 |
|---|---|---|
| 1 | 해치 (Hatch) 목장 | 돌만 먹고 고기·석탄. 열에 강함 |
| 2 | **드레코 (Drecko) 목장** (이 페이지) | 섬유·플라스틱이 주목적, 고기는 덤. 끼니나무를 같이 키움 |
| 3 | 파쿠 (Pacu) 어장 | 분출구 옆 웅덩이를 그대로 씀 |
| 4 | 열에 강한 작물 | 핀차 후추, 그럽과일 |

## 드레코 목장 위치: A 자리

{% include shot.html src="case1-drecko-site-a.jpg" caption="① 차가운 증기 분출구, ② 멈춘 농장, A = 드레코 목장 22×11 자리. 화면 비율로 잰 추정이라 게임에서 칸 수를 꼭 확인하세요." %}

- **왜 A인가:** 중앙 빨간 바닥 아래로 이미 사다리를 놓아 둔 빈 공간이라 팔 양이 적고, 우라늄·텔레포터 통로와 겹치지 않습니다. 빨간 바닥 아래로 약 14칸 여유가 있어 **위쪽 바위를 파면 11칸 높이**가 나와요.
- **조심할 점:** ① 분출구와 약 10칸 거리입니다. **서쪽 벽은 단열 타일**로 짓습니다.
- **확인할 것:** 배경색이 정글 바이옴처럼 보이는데, 맞다면 수소가 원래 있어서 채우기가 더 쉽습니다 (추측).

## 목장 도면 (22×11, 2층)

영상과 같은 22칸 × 11칸 2층 구조입니다. 위층은 수소로 채워 **드레코 비늘이 자라는 곳**, 아래층은 끼니나무 농장이에요. 수소는 가볍고 산소·CO₂는 무거워서, **아래층 바닥에는 산소가 깔리고** 끼니나무가 숨을 쉽니다 (끼니나무는 산소·오염된 산소·CO₂가 필요).

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 808 494" width="808" role="img" aria-label="드레코 목장 22×11 칸별 도면과 전기분해기 수소 주입 장치" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="808" height="494" fill="#11131f"/><rect x="40" y="40" width="484" height="242" fill="#7a5a44" fill-opacity="1"/><rect x="62" y="62" width="264" height="88" fill="#3a2f55" fill-opacity="1"/><rect x="62" y="150" width="440" height="22" fill="#5b5e6e" fill-opacity="1"/><rect x="62" y="172" width="242" height="44" fill="#3a2f55" fill-opacity="1"/><rect x="62" y="216" width="242" height="44" fill="#1f4a5a" fill-opacity="1"/><rect x="62" y="150" width="22" height="22" fill="#8a8fa8" fill-opacity="0.7"/><rect x="282" y="150" width="22" height="22" fill="#8a8fa8" fill-opacity="0.7"/><rect x="84" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M95 238 L95 200 M95 216 l-6 -6 M95 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="106" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M117 238 L117 200 M117 216 l-6 -6 M117 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="128" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M139 238 L139 200 M139 216 l-6 -6 M139 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="150" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M161 238 L161 200 M161 216 l-6 -6 M161 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="172" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M183 238 L183 200 M183 216 l-6 -6 M183 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="194" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M205 238 L205 200 M205 216 l-6 -6 M205 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="216" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M227 238 L227 200 M227 216 l-6 -6 M227 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><rect x="238" y="238" width="22" height="22" fill="#6b8f3a" fill-opacity="1" stroke="#11131f" stroke-width="2"/><path d="M249 238 L249 200 M249 216 l-6 -6 M249 220 l6 -6" stroke="#acffbd" stroke-width="2" fill="none"/><path d="M286 150 v22 M300 150 v22 M286 161 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M286 172 v22 M300 172 v22 M286 183 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M286 194 v22 M300 194 v22 M286 205 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M286 216 v22 M300 216 v22 M286 227 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M286 238 v22 M300 238 v22 M286 249 h14" stroke="#d8c08a" stroke-width="1.5"/><rect x="282" y="282" width="110" height="22" fill="#7a5a44" fill-opacity="1"/><rect x="304" y="238" width="66" height="44" fill="#2c6d8c" fill-opacity="1"/><rect x="304" y="216" width="22" height="22" fill="#1f4a5a" fill-opacity="1"/><rect x="348" y="216" width="22" height="22" fill="#24303a" fill-opacity="1"/><rect x="348" y="172" width="154" height="44" fill="#24303a" fill-opacity="1"/><rect x="370" y="216" width="132" height="44" fill="#24303a" fill-opacity="1"/><rect x="392" y="216" width="22" height="44" fill="#ffe284" fill-opacity="0.9"/><text x="403.0" y="241.0" fill="#11131f" font-size="8" text-anchor="middle" font-weight="700">검</text><rect x="414" y="194" width="22" height="66" fill="#9fb7ff" fill-opacity="0.8"/><text x="425.0" y="230.0" fill="#11131f" font-size="8" text-anchor="middle" font-weight="700">슈</text><rect x="436" y="194" width="22" height="66" fill="#9fb7ff" fill-opacity="0.8"/><text x="447.0" y="230.0" fill="#11131f" font-size="8" text-anchor="middle" font-weight="700">슈</text><rect x="458" y="194" width="22" height="66" fill="#9fb7ff" fill-opacity="0.8"/><text x="469.0" y="230.0" fill="#11131f" font-size="8" text-anchor="middle" font-weight="700">슈</text><rect x="502" y="216" width="22" height="44" fill="#9c7b52" fill-opacity="1"/><text x="513.0" y="276.5" fill="#f3e3d3" font-size="9" text-anchor="middle">문</text><rect x="84" y="106" width="22" height="44" fill="#e07a3a" fill-opacity="1"/><text x="95.0" y="89.2" fill="#ffd2b0" font-size="8" text-anchor="middle" font-weight="700">투입</text><rect x="128" y="84" width="66" height="66" fill="#c9a0ff" fill-opacity="0.85"/><text x="161.0" y="114.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">털깎이</text><text x="161.0" y="126.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">작업장</text><rect x="216" y="106" width="44" height="44" fill="#ffd166" fill-opacity="0.9"/><text x="238.0" y="125.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">손질</text><text x="238.0" y="137.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">작업대</text><rect x="260" y="106" width="44" height="44" fill="#8fd3ff" fill-opacity="0.9"/><text x="282.0" y="125.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">자동</text><text x="282.0" y="137.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">청소기</text><rect x="304" y="106" width="22" height="44" fill="#bbbbbb" fill-opacity="0.9"/><text x="315.0" y="131.0" fill="#11131f" font-size="8" text-anchor="middle" font-weight="700">보관</text><rect x="194" y="62" width="22" height="22" fill="#ff7ad9" fill-opacity="1"/><text x="205.0" y="76.96000000000001" fill="#fff" font-size="9" text-anchor="middle">▼</text><rect x="348" y="62" width="154" height="88" fill="#1c2036" fill-opacity="1"/><rect x="348" y="62" width="44" height="44" fill="#ff7ad9" fill-opacity="0.85"/><text x="370.0" y="81.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">H₂</text><text x="370.0" y="93.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">펌프</text><rect x="392" y="106" width="44" height="44" fill="#5fd0ff" fill-opacity="0.9"/><text x="414.0" y="125.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">전기</text><text x="414.0" y="137.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">분해기</text><rect x="458" y="106" width="44" height="44" fill="#7ad97a" fill-opacity="0.9"/><text x="480.0" y="125.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">O₂</text><text x="480.0" y="137.0" fill="#11131f" font-size="9" text-anchor="middle" font-weight="700">펌프</text><path d="M484 150 v22 M498 150 v22 M484 161 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M484 172 v22 M498 172 v22 M484 183 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M484 194 v22 M498 194 v22 M484 205 h14" stroke="#d8c08a" stroke-width="1.5"/><path d="M370 62 L370 26 L205.0 26 L205.0 62" fill="none" stroke="#ff7ad9" stroke-width="4" stroke-linejoin="round"/><circle cx="282" cy="26" r="6" fill="#11131f" stroke="#ffe284" stroke-width="2"/><text x="282" y="17" fill="#ffe284" font-size="9" text-anchor="middle">차단 밸브</text><path d="M480 106 L554 106" fill="none" stroke="#7ad97a" stroke-width="4"/><text x="558" y="110" fill="#7ad97a" font-size="10" text-anchor="start">O₂ → 아래층 바닥, 남으면 생활구역 밖</text><path d="M554 139.0 L414 139.0" fill="none" stroke="#5fd0ff" stroke-width="4" stroke-dasharray="6 3"/><text x="558" y="143.0" fill="#5fd0ff" font-size="10" text-anchor="start">물 ← 분출구 옆 웅덩이</text><text x="194" y="57.4" fill="#e9ecf8" font-size="9" text-anchor="middle"></text><text x="51.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">1</text><text x="73.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">2</text><text x="95.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">3</text><text x="117.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">4</text><text x="139.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">5</text><text x="161.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">6</text><text x="183.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">7</text><text x="205.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">8</text><text x="227.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">9</text><text x="249.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">10</text><text x="271.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">11</text><text x="293.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">12</text><text x="315.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">13</text><text x="337.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">14</text><text x="359.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">15</text><text x="381.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">16</text><text x="403.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">17</text><text x="425.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">18</text><text x="447.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">19</text><text x="469.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">20</text><text x="491.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">21</text><text x="513.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">22</text><text x="34" y="106" fill="#cfd3e6" font-size="10" text-anchor="end">위층</text><text x="34" y="216" fill="#cfd3e6" font-size="10" text-anchor="end">아래층</text><rect x="20" y="328" width="14" height="12" fill="#7a5a44"/><text x="40" y="338" fill="#e9ecf8" font-size="10" text-anchor="start">벽·바닥 (서쪽 벽은 단열 타일)</text><rect x="350" y="328" width="14" height="12" fill="#3a2f55"/><text x="370" y="338" fill="#e9ecf8" font-size="10" text-anchor="start">수소 (드레코 비늘이 자라는 층)</text><rect x="20" y="348" width="14" height="12" fill="#1f4a5a"/><text x="40" y="358" fill="#e9ecf8" font-size="10" text-anchor="start">산소·CO₂ (무거워서 아래로 가라앉음, 끼니나무 호흡용)</text><rect x="350" y="348" width="14" height="12" fill="#6b8f3a"/><text x="370" y="358" fill="#e9ecf8" font-size="10" text-anchor="start">농장 타일 + 끼니나무 8그루</text><rect x="20" y="368" width="14" height="12" fill="#2c6d8c"/><text x="40" y="378" fill="#e9ecf8" font-size="10" text-anchor="start">액체 잠금: 바닥 1칸 판 U자, 14열 천장이 물에 잠김</text><rect x="350" y="368" width="14" height="12" fill="#9fb7ff"/><text x="370" y="378" fill="#e9ecf8" font-size="10" text-anchor="start">슈 = 대기 슈트 거치대, 검 = 슈트 검문소</text><rect x="20" y="388" width="14" height="12" fill="#ff7ad9"/><text x="40" y="398" fill="#e9ecf8" font-size="10" text-anchor="start">수소 가스 파이프 → 천장 기체 배출구 (한 번 채우면 밸브 잠금)</text><rect x="350" y="388" width="14" height="12" fill="#8a8fa8"/><text x="370" y="398" fill="#e9ecf8" font-size="10" text-anchor="start">층 사이 메시 타일 / 사다리 구멍 (축사 합계 약 95칸 ≤ 96)</text><text x="20" y="426" fill="#a9b0d0" font-size="10" text-anchor="start">영상(2LegitCity) 구조를 칸 단위로 옮긴 개념도. 건물 정확한 칸은 영상을 따르세요.</text></svg>
</div>

- **축사 크기:** 축사(Stable)는 **12~96칸**까지만 방으로 인정됩니다. 위층 왼쪽(12×4)과 아래층(11×4)을 합쳐 약 95칸으로 맞추고, 오른쪽 위는 벽으로 잘라 **전기분해기 방**으로 씁니다.
- **드레코 수:** 한 마리당 12칸이라 95칸이면 **7마리**까지. 알은 바로 꺼냅니다 (알도 칸을 차지).
- **입구:** 문 → 슈트 검문소 → 대기 슈트 거치대 3개 → **액체 잠금** → 축사. 안은 수소라 슈트를 입고 들어가요.
- 건물 칸은 개념도입니다. 정확한 칸 배치는 영상을 따르세요.

## 수소 채우기: SPOM 없이 전기분해기 하나로

**드레코는 수소를 먹지 않아요.** 그래서 목장은 **한 번만 채우면** 됩니다.

| 항목 | 값 |
|---|---|
| 기체 칸 | 축사 약 95칸 − 건물 ≈ 80칸 (위층 위주) |
| 필요한 수소 | 칸당 0.5~1 kg → **약 75~150 kg** (낮은 압력이어도 드레코는 괜찮음) |
| 전기분해기 1대 | 물 1 kg/s → 산소 888 g/s + **수소 112 g/s**, 120 W |
| 걸리는 시간 | 150 kg ÷ 0.112 kg/s ≈ 1,340초 = **약 2.2사이클** |
| 물 | 약 1.3톤 (분출구 옆 웅덩이) |

**순서**

1. A 자리를 파고 벽·바닥·액체 잠금까지 짓습니다. **끼니나무는 아직 심지 않아요.**
2. 오른쪽 위 방에 **전기분해기 + 기체 펌프 2대** (천장 = 수소, 바닥 = 산소). 물은 웅덩이에서 액체 펌프로 끌어옵니다.
3. **산소는 먼저 아래층 바닥으로** 보내 끼니나무용 산소층을 깔고, 남는 산소는 **생활 구역 밖**으로 보냅니다. 전기분해기 기체는 **70°C 이상**이라 지금처럼 더운 기지에 바로 풀면 안 돼요.
4. 수소는 가스 파이프로 축사 천장 배출구에. 2~3사이클 뒤 다 차면 **차단 밸브를 잠급니다.** 수소 파이프를 웅덩이에 방열 파이프로 한 번 지나가게 하면 덜 뜨겁게 들어갑니다.
5. 방이 30°C 아래로 식으면 끼니나무 8그루를 심고 드레코를 투입합니다.
6. 나중에 이 방에 **수소 발전기**와 펌프를 더하면 그대로 [Half Rodriguez SPOM]({{ '/guide/sustainability/' | relative_url }}#산소-전기분해기-시스템-spom)의 시작이 됩니다.

## 글로시 드레코로 플라스틱까지

- **글로시 드레코 (Glossy Drecko)** 는 비늘 대신 **플라스틱**을 줍니다. 끼니나무를 먹이면 일반 드레코 알에서도 글로시가 조금씩 나와요.
- 쾌적 온도: 드레코 20~50°C, 끼니나무 10~30°C → **방은 20~30°C**로.
- 털깎이 작업장 (Shearing Station)은 **목축(Critter Ranching) 스킬**이 있는 복제체가 씁니다. 이 판에선 **마이메**(건축+목축) 담당.

## 이 판에서 확인할 것

- [ ] A 자리 실제 칸 수 (22×11이 들어가는지)
- [ ] 온도 오버레이(F3)로 A 자리 온도 (20~30°C인지)
- [ ] 영상 속 아래층이 산소를 어떻게 잡아두는지 (위 도면과 다르면 영상 쪽을 따름)
