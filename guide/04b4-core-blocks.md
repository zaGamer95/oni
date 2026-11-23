---
title: 농장·목장·산업 블록
nav_title: 농장·목장·산업
nav_order: 9.4
nav_num: "9-4"
nav_group: play
nav_parent: core-base
permalink: /guide/core-base/blocks/
description: 격벽 안/밖에 둘 작물과 동물, 온실 규격, 목장 크기, 산업 블록.
---

* 목차
{:toc}

> 전체 도면은 [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }})에 있습니다. 이 페이지는 그중 일부를 자세히 푼 것이에요.
{: .tip}

## 작물: 안에서 키울 것 / 밖에서 키울 것

온도는 공식 위키의 생장 온도 범위입니다. 이 범위를 벗어나면 자라지 않아요.

| 작물 | 생장 온도 | 기체 / 빛 | 어디서 |
|---|---|---|---|
| 끼니나무 (Mealwood) | 10~30°C | 산소·오염 산소·CO₂ | **안** |
| 센털꽃 (Bristle Blossom) | 5~30°C | 빛 200 lux 이상 | **안** (조명) |
| 수렁박 (Bog Bucket) | 10~30°C | 어둠 필요 | **안** |
| 어스름 갓 (Dusk Cap) | 5~35°C | CO₂, 어둠 | **안** (CO₂를 따로 채운 칸) |
| 골무갈대 (Thimble Reed) | 22~37°C | 물·오염수 안도 가능 | 안 (22°C 아래로 내려가지 않게 주의) |
| 벵이과실 (Grubfruit) | 15~50°C | | 안·밖 모두 |
| 진눈깨비밀 (Sleet Wheat) | −55~5°C | | **밖** (추운 쪽) |
| 오물오물 싹 (Nosh Sprout) | −25~0°C | CO₂ | **밖** (추운 쪽) |
| 아물나리 (Balm Lily) | 35~85°C | 염소 | **밖** (염소 온실) |
| 뿌림 소금덩굴 (Dasha Saltvine) | −25~50°C | 염소 | **밖** (염소 온실) |
| 가스풀 (Gas Grass) | 거의 제한 없음 | 빛 10,000 lux 이상 | **밖** (강한 조명, 가스질 음메 먹이) |

> 추운 작물은 격벽 밖이라도 그냥 두면 산업 열 때문에 데워집니다. 외부 온실(추운 작물)은 **산업 블록 반대쪽**에 두고, 원래 추운 바이옴에 붙이거나 냉각 루프 끝을 한 번 더 지나게 하세요.
{: .heat}

## 농장 규격

실내 온실 A(끼니나무 23×5)와 B(센털꽃 15×7)의 칸별 배치, 복제체당 작물 수, 초반 농장 타일 한 줄 단계는 [식당·실내 온실 상세]({{ '/guide/food-early/' | relative_url }})에 따로 정리했습니다.

작물은 대부분 **다 자라면 2칸**, 골무갈대·가스풀은 **3칸**입니다. 농장 타일 1칸 + 작물 칸을 반복해 쌓으면 3칸·4칸 간격이라 생활 구역의 5칸 간격 격자와 안 맞아요. 농업 작업대(2×3)도 2칸 틈에는 안 들어갑니다.

| 온실 | 크기 | 구조 | 방 크기 | 작물 수 |
|---|---|---|---|---|
| 2칸 작물용 | **가로 23 × 높이 5** | 작물 2칸 / 농장 타일 줄 / 작물 2칸. 통로 쪽 끝 3칸 = 사다리 1 + 가운데 줄 일반 타일 2(위층 발판). **층이 2칸이라 작업대(2×3)가 안 들어감** → 비료가 필요 없는 끼니나무 전용 | 20×4 + 3×5 − 2 = **93** | 20 × 2줄 = **40** |
| 3칸 작물용 | **가로 15 × 높이 7** | 작물 3칸 / 농장 타일 줄 / 작물 3칸. 끝 3칸 = 사다리 + 발판 타일 2 + 아래층에 작업대 2×3 | 12×6 + 3×7 − 2 = **91** | 12 × 2줄 = **24** |
| 빛 필요한 2칸 작물 (센털꽃) | **가로 15 × 높이 7** | 조명 줄 / 작물 2칸 / 농장 타일 줄 / 조명 줄 / 작물 2칸. 끝 3칸은 위와 같음 | 12×6 + 3×7 − 2 = **91** | 12 × 2줄 = **24** |

- 농장 타일은 막힌 칸이라 방 크기에 안 들어갑니다. 그래서 2줄까지는 96 이하, 3줄을 쌓으면 넘어요.
- 블록 높이가 생활 구역 격자와 안 맞아도 **양쪽 사다리 통로에 문만 내면** 연결됩니다.

## 목장: 안 / 밖

목장 크기는 동물마다 필요한 칸 수로 정합니다 (공식 위키 Stable 기준, 넘으면 '과밀'). 손질 작업대 2×3, 부화기 2×3, 착유기 2×4라 땅 동물 목장은 **높이 4**면 됩니다.

| 동물 | 쾌적 온도 | 1마리당 칸 | 목장 | 어디서 |
|---|---|---|---|---|
| 주둥가리 (Hatch) | 10~40°C | 12 | 24×4 = 96 → 8마리 | **안** |
| 잎람쥐 (Pip) | 10~40°C | 12 | 24×4 → 8마리 | **안** |
| 기끌이 (Drecko) | 10~60°C | 12 | 24×4 → 8마리 | **안** |
| 헐떡이 (Puft) | 15~55°C | 16 | 12×8 = 96 → 6마리 | **밖** (오염 산소를 먹으니 격벽 안에 두지 않음) |
| 미끌이 (Slickster) | 50~140°C | 12 | 24×4 → 8마리 | **밖** (산업 열 근처, CO₂ 구덩이 옆) |
| 가스질 음메 (Gassy Moo) | −50~50°C | 16 | 22×4 = 88 → 5마리 | **밖** (가스풀 먹이) |
| 플록스 (Flox) | −30~10°C | 12 | 16×4 = 64 → 5마리 | **밖** (추운 쪽) |
| 빛벌레 (Shine Bug) | −70~40°C | 6 | 12×8 → 16마리 | 안·밖 모두 |

- 실내 목장은 농장 옆 **보조 사다리**로 연결하고, 동물이 문틈에 끼지 않게 문은 닫히는 문으로 둡니다.

### 주둥가리 목장 칸별 배치 (24×4)

[배치도]({{ '/guide/core-base/' | relative_url }})에서 포드층 동쪽, 동쪽 통로 바로 옆 24×4 자리입니다. 주둥가리(Hatch)는 1마리당 12칸이라 **96칸 = 딱 8마리**예요.

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 776 315" width="776" role="img" aria-label="주둥가리 목장 24×4 칸별 배치도" style="min-width:0;max-width:776px" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="776" height="315" fill="#11131f"/><rect x="20" y="60" width="696" height="144" fill="#5a4a3a"/><rect x="20" y="60" width="48" height="144" fill="#24452e" fill-opacity=".6"/><line x1="23" y1="72.0" x2="41" y2="72.0" stroke="#f6c445" stroke-width="2"/><line x1="23" y1="96.0" x2="41" y2="96.0" stroke="#f6c445" stroke-width="2"/><line x1="23" y1="120.0" x2="41" y2="120.0" stroke="#f6c445" stroke-width="2"/><line x1="23" y1="144.0" x2="41" y2="144.0" stroke="#f6c445" stroke-width="2"/><line x1="23" y1="168.0" x2="41" y2="168.0" stroke="#f6c445" stroke-width="2"/><line x1="23" y1="192.0" x2="41" y2="192.0" stroke="#f6c445" stroke-width="2"/><line x1="56.0" y1="60" x2="56.0" y2="204" stroke="#ff8a4c" stroke-width="3"/><text x="44" y="220" fill="#acffbd" font-size="11" text-anchor="middle" font-weight="700">동쪽 통로</text><rect x="116" y="84" width="576" height="96" fill="#1c2036"/><line x1="116" y1="84" x2="116" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="140" y1="84" x2="140" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="164" y1="84" x2="164" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="188" y1="84" x2="188" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="212" y1="84" x2="212" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="236" y1="84" x2="236" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="260" y1="84" x2="260" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="284" y1="84" x2="284" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="308" y1="84" x2="308" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="332" y1="84" x2="332" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="356" y1="84" x2="356" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="380" y1="84" x2="380" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="404" y1="84" x2="404" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="428" y1="84" x2="428" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="452" y1="84" x2="452" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="476" y1="84" x2="476" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="500" y1="84" x2="500" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="524" y1="84" x2="524" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="548" y1="84" x2="548" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="572" y1="84" x2="572" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="596" y1="84" x2="596" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="620" y1="84" x2="620" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="644" y1="84" x2="644" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="668" y1="84" x2="668" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="692" y1="84" x2="692" y2="180" stroke="#fff" stroke-opacity=".07"/><line x1="116" y1="84" x2="692" y2="84" stroke="#fff" stroke-opacity=".07"/><line x1="116" y1="108" x2="692" y2="108" stroke="#fff" stroke-opacity=".07"/><line x1="116" y1="132" x2="692" y2="132" stroke="#fff" stroke-opacity=".07"/><line x1="116" y1="156" x2="692" y2="156" stroke="#fff" stroke-opacity=".07"/><line x1="116" y1="180" x2="692" y2="180" stroke="#fff" stroke-opacity=".07"/><rect x="116" y="180" width="576" height="24" fill="#6b6f80"/><rect x="117" y="85" width="574" height="94" fill="none" stroke="#e8c070" stroke-width="2"/><text x="404.0" y="52" fill="#e8c070" font-size="14" font-weight="700" text-anchor="middle">실내 목장: 주둥가리 24×4 = 96칸 (8마리 × 12칸)</text><text x="128.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">1</text><text x="152.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">2</text><text x="176.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">3</text><text x="200.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">4</text><text x="224.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">5</text><text x="248.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">6</text><text x="272.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">7</text><text x="296.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">8</text><text x="320.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">9</text><text x="344.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">10</text><text x="368.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">11</text><text x="392.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">12</text><text x="416.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">13</text><text x="440.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">14</text><text x="464.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">15</text><text x="488.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">16</text><text x="512.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">17</text><text x="536.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">18</text><text x="560.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">19</text><text x="584.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">20</text><text x="608.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">21</text><text x="632.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">22</text><text x="656.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">23</text><text x="680.0" y="79" fill="#cfd3e6" font-size="9" text-anchor="middle">24</text><rect x="165.5" y="109.5" width="45" height="69" rx="3" fill="#e8c070" fill-opacity="0.9"/><text x="188.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">손질</text><text x="188.0" y="154.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">작업대</text><rect x="237.5" y="133.5" width="21" height="45" rx="3" fill="#f4a442" fill-opacity="0.9"/><text x="248.0" y="154.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">먹</text><text x="248.0" y="166.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">이</text><rect x="285.5" y="133.5" width="21" height="45" rx="3" fill="#a9b0d0" fill-opacity="0.9"/><text x="296.0" y="154.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">저</text><text x="296.0" y="166.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">장</text><rect x="333.5" y="109.5" width="21" height="69" rx="3" fill="#8fe3ff" fill-opacity="0.9"/><text x="344.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">하</text><text x="344.0" y="154.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">차</text><rect x="357.5" y="109.5" width="21" height="69" rx="3" fill="#ff9fd0" fill-opacity="0.9"/><text x="368.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">수</text><text x="368.0" y="154.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">거</text><rect x="429.5" y="109.5" width="45" height="69" rx="3" fill="#d38be0" fill-opacity="0.35" stroke="#fff" stroke-dasharray="3 2"/><text x="452.0" y="142.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">부화기</text><text x="452.0" y="154.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">(나중)</text><ellipse cx="512.0" cy="171.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="548.0" cy="171.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="584.0" cy="171.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="620.0" cy="171.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="656.0" cy="171.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="524.0" cy="153.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="572.0" cy="153.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><ellipse cx="632.0" cy="153.0" rx="10.08" ry="7.199999999999999" fill="#b88cff" fill-opacity=".85"/><rect x="96" y="132" width="16" height="48" fill="#8a9bd0"/><text x="20" y="244" fill="#a9b0d0" font-size="11.5">1~2번: 문 앞 길 (비움) · 3~4번 손질 작업대 · 6번 먹이통 · 8번 저장 상자(석탄·알만) · 10번 하차 지점 · 11번 수거 지점</text><text x="20" y="261" fill="#a9b0d0" font-size="11.5">14~15번 부화기는 나중(정제 금속 200 kg) · 17~24번은 비워 두는 놀이 공간 · 바닥은 지은 타일(자연 흙이면 낮에 파고 숨음)</text><text x="20" y="278" fill="#a9b0d0" font-size="11.5">보라 타원 = 주둥가리 8마리 · 조명 필요 없음 (손질 속도는 빛 영향 없음)</text></svg>
</div>
<p class="bp-legend">1칸 = 1타일. 칸 위 숫자는 통로 문에서 센 칸 번호. 점선 = 나중에 놓을 자리. 회색 줄 = 지은 바닥 타일.</p>

| 칸 | 건물 | 크기 · 재료 | 연구 | 왜 여기 |
|---|---|---|---|---|
| 0 (벽) | 문 | 1×2 | – | 동쪽 통로에서 바로 들어옴 |
| 1~2 | 비움 | – | – | 문 앞 길. 문 열릴 때 주둥가리가 문틈에 서 있으면 '갇힘'(행복 −10) |
| 3~4 | **손질 작업대 (Grooming Station)** | 2×3 · 금속 광석 400 kg | 목축 (Ranching) | 목장(Stable) 방 조건. 문 바로 옆이라 목장 담당이 몇 걸음이면 일함 |
| 6 | **사료 공급기 (Critter Feeder)** | 1×2 · 금속 광석 200 kg · 2,000 kg 저장 | 목축 | 먹이를 바닥에 흩뿌리지 않고 여기서 먹음 |
| 8 | **저장 상자 (Storage Bin)** | 1×2 · 400 kg | – | 필터를 **석탄 + 주둥가리 알**만. 복제체가 바닥의 석탄·알을 쓸어 담음 |
| 10 | **생물 하차 지점 (Critter Drop-Off)** | 1×3 · 금속 광석 50 kg | 목축 | 잡아 온 주둥가리를 여기 풀어 줌. 한도 **8** |
| 11 | **생물 수거 지점 (Critter Pick-Up)** | 1×3 · 금속 광석 50 kg | 목축 | 주둥가리 **8마리 넘으면** 남는 놈을 자동으로 잡아 다른 하차 지점으로 |
| 14~15 | 부화기 (Incubator), 나중 | 2×3 · **정제 금속 200 kg** · 240 W | 동물 통제 (Animal Control) | 알을 빨리 부화시켜 처음 채울 때만 씀. 꼭 필요하진 않음 |
| 17~24 | 비움 | – | – | 돌아다니는 공간 |

> 일부 국문 건물 이름(사료 공급기, 하차·수거 지점, 부화기)은 게임 표기와 조금 다를 수 있어요. 괄호 안 영문이 기준입니다.
{: .tip}

#### 필요 조건

- **바닥은 지은 타일**로 깝니다. 주둥가리는 낮에 단단함 20 이하 자연 타일(흙·모래 등)을 파고 숨어서, 맨흙 바닥이면 손질하러 갔을 때 안 보여요.
- **조명은 필요 없습니다.** 손질 시간(12초)은 빛 영향을 안 받아요.
- **온도**는 격벽 안 20~25°C면 충분합니다 (주둥가리 쾌적 10~40°C).
- **목장 담당**은 목축 스킬(Critter Ranching I)이 있어야 손질합니다. Otto가 목축 담당이에요.

#### 먹이와 석탄

| 항목 | 1마리 | 8마리 |
|---|---|---|
| 먹는 양 (길들인 + 행복) | 암석 140 kg / 사이클 | **1,120 kg / 사이클** |
| 석탄 | 70 kg / 사이클 | **560 kg / 사이클** = 석탄 발전기 1대(600 kg)의 93% |

- 사료 공급기 하나(2,000 kg)면 약 **1.8사이클분**입니다. 우선순위를 높게 두세요.
- 먹이는 **사암 (Sandstone)·부순 암석 (Crushed Rock)·모래 (Sand)·점토 (Clay)** 중 남는 것. 암석 분쇄기에서 나온 **모래**를 여기에 쓰면 딱 맞아요.
- **흙 (Dirt)은 주지 마세요.** 끼니나무 농장 타일에 써야 하고, 흙을 먹으면 세이지 주둥가리 알이 나올 확률이 올라갑니다. 퇴적암 (Sedimentary Rock)을 먹이면 돌 주둥가리 확률이 오릅니다.
- 손질을 받으면 행복 +5 → '행복' 상태라 먹는 양·석탄이 100%, 번식도 빠릅니다. 손질이 끊기면(길든 기본 행복 −1) 생산이 20%로 떨어져요.

#### 8마리 유지하기

1. **처음 채우기:** 야생 주둥가리를 목축 담당이 잡으면(Wrangle) 하차 지점(한도 8)으로 데려옵니다. 야생은 손질을 이틀 연속 받으면 길듭니다.
2. **알:** 행복한 주둥가리는 알을 낳습니다. 알도 칸 수 계산에 들어가서 9번째가 생길 것 같으면 '비좁음(Cramped)'으로 번식만 느려지고 행복은 안 깎여요. 알은 저장 상자로 쓸어 담고, 나중에 **알 깨는 기계 (Egg Cracker)**로 요리 재료로 씁니다.
3. **넘칠 때:** 알이 목장 안에서 부화해 9마리가 되면 '붐빔(Crowded)'으로 행복이 깎입니다. 그래서 **생물 수거 지점을 주둥가리 8**로 맞춰 두면 넘는 녀석을 목장 담당이 잡아 **다른 방의 하차 지점**(두 번째 목장, 또는 고기용 방)으로 옮깁니다.
4. 생물 감지기 (Critter Sensor, 정제 금속 25 kg)는 수거 지점이 있으면 없어도 됩니다. 부화기를 쓸 때 "8마리 넘으면 부화기 끄기"에 쓰면 돼요.

## 산업 블록 (격벽 밖, 기지 아래)

| 시설 | 크기 | 메모 |
|---|---|---|
| 발전소 | 24×4 = 96 | 코어 바로 아래(물 처리 밑), 사이에 단열 바닥. 석탄 발전기 3×3, 수소 발전기 4×3, 전력 제어소 2×4. 높이 4에 딱 맞음 |
| SPOM | 12×4, 단열 | 전기분해기 2×2 + 기체 펌프 2×2. 1대 = 물 1 kg/s → 산소 888 g/s ≈ 복제체 8명분 |
| 수소 발전기 | 9×4, 단열 | SPOM 수소를 바로 태움 |
| 냉방실 | 14×4, 단열 | 수냉 조절기, 나중에 위에 증기 터빈(5×3) |
| 정제·제련 | 14×4, 단열 | **발전소 바로 동쪽**. 금속 정제기 3×4, 암석 분쇄기 4×4가 딱 4칸이라 들어감. 정제기 1.2 kW라 발전소 헤비와트에 연결판으로 바로 이음 ([9-8]({{ '/guide/core-base/refining/' | relative_url }})) |
| CO₂ 구덩이 | 가로 전체 × 3 | 맨 아래. 미끌이 목장 바로 옆 |
