---
title: 초기 발전소 설계와 관리
nav_title: 발전소
nav_order: 10
nav_group: early
permalink: /guide/core-base/power/
description: 수동 발전기에서 석탄 발전기로 넘어가는 법, 발전소 24×4 칸별 배치, 와이어 등급과 회로 나누기, 스마트 배터리 자동화, 주둥가리 석탄, 열·CO₂, 수소·천연가스·석유 발전으로 가는 순서.
---

* 목차
{:toc}

> 전체 도면은 [중앙 기지 배치도]({{ '/guide/core-base/' | relative_url }})에 있습니다. 발전소는 그 도면에서 **격벽 밖, 코어 아래 예비 층 바로 밑 24×4** 자리예요. 수치는 공식 위키 기준입니다.
{: .tip}

## 지금 할 일 (사이클 10, 복제체 5명)

- [ ] 격벽 밖 코어 아래 발전소 자리 **24×4** 를 파고 바닥을 깝니다. 위 천장 줄은 단열 타일(격벽)이에요.
- [ ] **석탄 발전기 (Coal Generator) 1대** + **배터리 (Battery) 2개** 를 놓고 일반 **와이어 (Wire)** 하나로 통로를 따라 기지까지 잇습니다.
- [ ] 발전기 옆에 **저장 상자 (Storage Bin)** 를 석탄 전용으로 하나. 굴착에서 나온 석탄을 여기에 모읍니다.
- [ ] 새 발전기가 돌면 포드층의 **수동 발전기 (Manual Generator)** 를 철거 → 연구실이 방으로 인정되고, 그 자리는 나중에 **슈퍼컴퓨터 (Super Computer)**.
- [ ] 다음 목표: 정제 금속을 모아 **스마트 배터리 (Smart Battery)** + 자동화 와이어로 발전기 자동 켜고 끄기. 정제 금속 500 kg 뽑는 법은 [12 정제 금속]({{ '/guide/core-base/refining/' | relative_url }}).

## 전기를 얼마나 쓰나

복제체 5명 무렵 기지에서 전기를 먹는 건물입니다 (위키 수치, 돌아갈 때만 씀).

| 건물 | 전력 | 메모 |
|---|---|---|
| 연구소 (Research Station) | 60 W | 연구할 때만 |
| 슈퍼컴퓨터 (Super Computer) | 120 W | 나중. 생각보다 적게 먹음 |
| 미생물 분쇄기 (Microbe Musher) | 240 W | 요리할 때만 |
| 전기 그릴 (Electric Grill) | 60 W | |
| 산소 확산기 (Oxygen Diffuser) | 120 W | 조류 → 산소 |
| 전기분해기 (Electrolyzer) | 120 W | 물 1 kg/s → 산소 888 g/s (70°C) |
| 액체 펌프 (Liquid Pump) | 240 W | 10 kg/s |
| 기체 펌프 (Gas Pump) | 240 W | 500 g/s |
| 물 정화기 (Water Sieve) | 120 W | |
| 천장 조명 (Ceiling Light) | 10 W | 개당 |

지금 단계에서 한꺼번에 다 돌아도 **약 800~900 W**, 평균은 그보다 훨씬 낮습니다. 그래서 **석탄 발전기 1대(600 W) + 배터리** 면 충분하고, 모자라는 순간은 배터리가 메워요.

## 발전기 비교

| 발전기 | 크기 | 전력 | 연료 | 열 | 메모 |
|---|---|---|---|---|---|
| 수동 발전기 (Manual Generator) | 2×2 | 400 W | 복제체가 달림 | 1 kDTU/s | 산업 기계라 방 보너스를 깸. 초반 임시용 |
| **석탄 발전기 (Coal Generator)** | 3×3 | **600 W** | 석탄 1 kg/s (600 kg/사이클) | 9 kDTU/s | CO₂ 20 g/s (110°C) |
| 천연가스 발전기 (Natural Gas Generator) | 4×3 | 800 W | 천연가스 90 g/s | 10 kDTU/s | 오염수·CO₂ 나옴. 가스 분출구가 있으면 |
| 수소 발전기 (Hydrogen Generator) | 4×3 | 800 W | 수소 100 g/s | 4 kDTU/s | SPOM과 짝. 깨끗함 |
| 석유 발전기 (Petroleum Generator) | 3×4 | 2,000 W | 석유·에탄올 2 kg/s | 20 kDTU/s | CO₂ 500 g/s, 오염수. 후반 |

> 석탄 발전기는 **배터리가 꽉 차도 석탄을 계속 태웁니다.** 자동화 없이 두면 석탄이 그냥 사라져요. 스마트 배터리 자동화를 최대한 빨리 붙이세요.
{: .warn}

## 발전소 배치도 (24×4)

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 688 514" width="688" role="img" aria-label="발전소 칸별 배치도: 초반과 중반" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="688" height="514" fill="#11131f"/><rect x="86" y="50" width="572" height="132" fill="#5a4a3a"/><rect x="108" y="72" width="528" height="88" fill="#1c2036"/><line x1="108" y1="72" x2="108" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="130" y1="72" x2="130" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="152" y1="72" x2="152" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="174" y1="72" x2="174" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="196" y1="72" x2="196" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="218" y1="72" x2="218" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="240" y1="72" x2="240" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="262" y1="72" x2="262" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="284" y1="72" x2="284" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="306" y1="72" x2="306" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="328" y1="72" x2="328" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="350" y1="72" x2="350" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="372" y1="72" x2="372" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="394" y1="72" x2="394" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="416" y1="72" x2="416" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="438" y1="72" x2="438" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="460" y1="72" x2="460" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="482" y1="72" x2="482" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="504" y1="72" x2="504" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="526" y1="72" x2="526" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="548" y1="72" x2="548" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="570" y1="72" x2="570" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="592" y1="72" x2="592" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="614" y1="72" x2="614" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="636" y1="72" x2="636" y2="160" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="72" x2="636" y2="72" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="94" x2="636" y2="94" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="116" x2="636" y2="116" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="138" x2="636" y2="138" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="160" x2="636" y2="160" stroke="#fff" stroke-opacity=".07"/><rect x="109" y="73" width="526" height="86" fill="none" stroke="#ff7a5c" stroke-width="2"/><text x="119.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">1</text><text x="141.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">2</text><text x="163.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">3</text><text x="185.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">4</text><text x="207.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">5</text><text x="229.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">6</text><text x="251.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">7</text><text x="273.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">8</text><text x="295.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">9</text><text x="317.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">10</text><text x="339.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">11</text><text x="361.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">12</text><text x="383.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">13</text><text x="405.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">14</text><text x="427.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">15</text><text x="449.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">16</text><text x="471.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">17</text><text x="493.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">18</text><text x="515.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">19</text><text x="537.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">20</text><text x="559.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">21</text><text x="581.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">22</text><text x="603.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">23</text><text x="625.0" y="66" fill="#cfd3e6" font-size="9" text-anchor="middle">24</text><rect x="20" y="50" width="66" height="132" fill="#24452e"/><line x1="45" y1="61.0" x2="61" y2="61.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="83.0" x2="61" y2="83.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="105.0" x2="61" y2="105.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="127.0" x2="61" y2="127.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="149.0" x2="61" y2="149.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="171.0" x2="61" y2="171.0" stroke="#f6c445" stroke-width="2"/><line x1="75.0" y1="50" x2="75.0" y2="182" stroke="#ff8a4c" stroke-width="3"/><text x="53.0" y="197" fill="#acffbd" font-size="11" text-anchor="middle" font-weight="700">통로</text><rect x="90" y="116" width="14" height="44" fill="#8a9bd0"/><rect x="86" y="68" width="572" height="4" fill="#e0b060"/><rect x="219.5" y="95.5" width="63" height="63" rx="3" fill="#ff7a5c" fill-opacity=".9"/><text x="251.0" y="125.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄</text><text x="251.0" y="137.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">발전기</text><rect x="307.5" y="95.5" width="63" height="63" rx="3" fill="#ff7a5c" fill-opacity=".3" stroke="#fff" stroke-dasharray="3 2"/><text x="339.0" y="131.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">2호기</text><rect x="285.5" y="117.5" width="19" height="41" rx="3" fill="#a9b0d0" fill-opacity=".9"/><text x="295.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄</text><rect x="483.5" y="117.5" width="19" height="41" rx="3" fill="#8fe3ff" fill-opacity=".9"/><text x="493.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">배</text><rect x="505.5" y="117.5" width="19" height="41" rx="3" fill="#8fe3ff" fill-opacity=".9"/><text x="515.0" y="142.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">배</text><rect x="527.5" y="117.5" width="41" height="41" rx="3" fill="#5fd0ff" fill-opacity=".3" stroke="#fff" stroke-dasharray="3 2"/><text x="548.0" y="142.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">스마트</text><rect x="109.5" y="117.5" width="41" height="41" rx="3" fill="#ffe284" fill-opacity=".3" stroke="#fff" stroke-dasharray="3 2"/><text x="130.0" y="142.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">변압</text><rect x="153.5" y="117.5" width="41" height="41" rx="3" fill="#ffe284" fill-opacity=".3" stroke="#fff" stroke-dasharray="3 2"/><text x="174.0" y="142.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">변압</text><rect x="593.5" y="73.5" width="41" height="85" rx="3" fill="#e0a0ff" fill-opacity=".3" stroke="#fff" stroke-dasharray="3 2"/><text x="614.0" y="114.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">제어</text><text x="614.0" y="126.0" fill="#e9ecf8" font-size="10" font-weight="700" text-anchor="middle">소</text><path d="M229.0 138 V83.0 H515.0 M53.0 83.0 H108" fill="none" stroke="#f6e27a" stroke-width="3"/><text x="20" y="24" fill="#e9ecf8" font-size="15" font-weight="700">초반 (사이클 10~30): 발전소 24×4, 석탄 발전기 1대부터</text><text x="20" y="216" fill="#a9b0d0" font-size="11.5">노랑 줄 = 일반 와이어(1 kW) 한 회로 · 점선 = 나중에 놓을 자리 · 위 주황 줄 = 단열 격벽(이 방은 격벽 밖)</text><text x="20" y="232" fill="#a9b0d0" font-size="11.5">6~8번 석탄 발전기 · 9번 석탄 저장 상자 · 18~19번 배터리 2개 · 점선 자리는 비워 둠</text><rect x="86" y="302" width="572" height="132" fill="#5a4a3a"/><rect x="108" y="324" width="528" height="88" fill="#1c2036"/><line x1="108" y1="324" x2="108" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="130" y1="324" x2="130" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="152" y1="324" x2="152" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="174" y1="324" x2="174" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="196" y1="324" x2="196" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="218" y1="324" x2="218" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="240" y1="324" x2="240" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="262" y1="324" x2="262" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="284" y1="324" x2="284" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="306" y1="324" x2="306" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="328" y1="324" x2="328" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="350" y1="324" x2="350" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="372" y1="324" x2="372" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="394" y1="324" x2="394" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="416" y1="324" x2="416" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="438" y1="324" x2="438" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="460" y1="324" x2="460" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="482" y1="324" x2="482" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="504" y1="324" x2="504" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="526" y1="324" x2="526" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="548" y1="324" x2="548" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="570" y1="324" x2="570" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="592" y1="324" x2="592" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="614" y1="324" x2="614" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="636" y1="324" x2="636" y2="412" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="324" x2="636" y2="324" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="346" x2="636" y2="346" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="368" x2="636" y2="368" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="390" x2="636" y2="390" stroke="#fff" stroke-opacity=".07"/><line x1="108" y1="412" x2="636" y2="412" stroke="#fff" stroke-opacity=".07"/><rect x="109" y="325" width="526" height="86" fill="none" stroke="#ff7a5c" stroke-width="2"/><text x="119.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">1</text><text x="141.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">2</text><text x="163.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">3</text><text x="185.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">4</text><text x="207.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">5</text><text x="229.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">6</text><text x="251.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">7</text><text x="273.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">8</text><text x="295.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">9</text><text x="317.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">10</text><text x="339.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">11</text><text x="361.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">12</text><text x="383.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">13</text><text x="405.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">14</text><text x="427.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">15</text><text x="449.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">16</text><text x="471.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">17</text><text x="493.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">18</text><text x="515.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">19</text><text x="537.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">20</text><text x="559.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">21</text><text x="581.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">22</text><text x="603.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">23</text><text x="625.0" y="318" fill="#cfd3e6" font-size="9" text-anchor="middle">24</text><rect x="20" y="302" width="66" height="132" fill="#24452e"/><line x1="45" y1="313.0" x2="61" y2="313.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="335.0" x2="61" y2="335.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="357.0" x2="61" y2="357.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="379.0" x2="61" y2="379.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="401.0" x2="61" y2="401.0" stroke="#f6c445" stroke-width="2"/><line x1="45" y1="423.0" x2="61" y2="423.0" stroke="#f6c445" stroke-width="2"/><line x1="75.0" y1="302" x2="75.0" y2="434" stroke="#ff8a4c" stroke-width="3"/><text x="53.0" y="449" fill="#acffbd" font-size="11" text-anchor="middle" font-weight="700">통로</text><rect x="90" y="368" width="14" height="44" fill="#8a9bd0"/><rect x="86" y="320" width="572" height="4" fill="#e0b060"/><rect x="219.5" y="347.5" width="63" height="63" rx="3" fill="#ff7a5c" fill-opacity=".9"/><text x="251.0" y="383.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄 1</text><rect x="307.5" y="347.5" width="63" height="63" rx="3" fill="#ff7a5c" fill-opacity=".9"/><text x="339.0" y="383.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄 2</text><rect x="395.5" y="347.5" width="63" height="63" rx="3" fill="#ff7a5c" fill-opacity=".9"/><text x="427.0" y="383.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄 3</text><rect x="285.5" y="369.5" width="19" height="41" rx="3" fill="#a9b0d0" fill-opacity=".9"/><text x="295.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄</text><rect x="373.5" y="369.5" width="19" height="41" rx="3" fill="#a9b0d0" fill-opacity=".9"/><text x="383.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">석탄</text><rect x="483.5" y="369.5" width="41" height="41" rx="3" fill="#5fd0ff" fill-opacity=".9"/><text x="504.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">스마트</text><rect x="527.5" y="369.5" width="41" height="41" rx="3" fill="#5fd0ff" fill-opacity=".9"/><text x="548.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">스마트</text><rect x="109.5" y="369.5" width="41" height="41" rx="3" fill="#ffe284" fill-opacity=".9"/><text x="130.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">변압 1</text><rect x="153.5" y="369.5" width="41" height="41" rx="3" fill="#ffe284" fill-opacity=".9"/><text x="174.0" y="394.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">변압 2</text><rect x="593.5" y="325.5" width="41" height="85" rx="3" fill="#e0a0ff" fill-opacity=".9"/><text x="614.0" y="366.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">제어</text><text x="614.0" y="378.0" fill="#11131f" font-size="10" font-weight="700" text-anchor="middle">소</text><path d="M141.0 335.0 H559.0" fill="none" stroke="#ff4a4a" stroke-width="6" stroke-opacity=".8"/><path d="M119.0 368 V328.4 H53.0 M163.0 368 V350.4 H53.0" fill="none" stroke="#f6e27a" stroke-width="3"/><path d="M251.0 403.2 H515.0" fill="none" stroke="#6fdc6f" stroke-width="2.5" stroke-dasharray="5 3"/><text x="20" y="276" fill="#e9ecf8" font-size="15" font-weight="700">중반 (사이클 40~): 석탄 3대 + 스마트 배터리 자동화 + 헤비와트 + 변압기</text><text x="20" y="468" fill="#a9b0d0" font-size="11.5">빨강 굵은 줄 = 헤비와트 와이어(20 kW, 발전소 안에서만) · 노랑 2줄 = 변압기마다 일반 와이어(1 kW) 회로 하나씩 통로로</text><text x="20" y="484" fill="#a9b0d0" font-size="11.5">초록 점선 = 자동화 와이어 (스마트 배터리 50% 이하 켜기, 90% 이상 끄기) · 23~24번 전력 제어소</text></svg>
</div>
<p class="bp-legend">1칸 = 1타일. 칸 위 숫자는 통로 문에서 센 칸 번호. 주황 = 발전기, 회색 = 석탄 저장 상자, 하늘 = 배터리, 노랑 = 변압기, 보라 = 전력 제어소. 왼쪽이 가운데 통로.</p>

| 칸 | 초반 | 중반 이후 |
|---|---|---|
| 1~4 | 비움 | **변압기 (Power Transformer) 2개** (2×2). 회로마다 1개 |
| 6~8 | **석탄 발전기 1호기** | 그대로 |
| 9 | 석탄 저장 상자 (1×2) | 그대로 |
| 10~12 | 비움 | 석탄 발전기 2호기 |
| 13 | – | 석탄 저장 상자 |
| 14~16 | – | 석탄 발전기 3호기 |
| 18~19 | **배터리 2개** (1×2) | 스마트 배터리 (2×2) |
| 20~21 | 비움 | 스마트 배터리 2개째 |
| 23~24 | 비움 | **전력 제어소 (Power Control Station)** 2×4 (방 높이 4에 딱 맞음) |

- 석탄 발전기는 **바닥 가운데 칸**으로 석탄을 받습니다. 저장 상자를 바로 옆에 두면 나르는 거리가 0에 가까워요.
- 이 방은 **발전소 (Power Plant)** 방이 됩니다: 대형 발전기 1개 이상 + 전력 건물 2개 이상, 12~96칸. 나중에 전력 제어소에서 만든 **마이크로칩**으로 발전기를 손보면 같은 연료로 **+50%** (몇 사이클 지속, 전기 공학 스킬 필요).
- 수소 발전기는 SPOM 옆 **별도 9×4 방**에 둡니다 ([11 농장·목장·산업]({{ '/guide/core-base/blocks/' | relative_url }}) 산업 블록).

## 수동 발전기에서 넘어가는 순서

1. 발전소 자리를 파고 석탄 발전기 + 배터리 2개를 지어 와이어로 연결.
2. 같은 와이어를 기존 기지 회로에 이어 붙입니다. 이 순간부터 수동 발전기와 석탄 발전기가 한 회로를 같이 채워요.
3. 석탄 저장 상자에 석탄이 쌓이고 배터리가 차는 걸 확인하면 **수동 발전기 철거**.
4. 포드층 연구실에 산업 기계가 사라져 **연구실 (Laboratory)** 방이 됩니다 (연구 건물 2개 필요). 수동 발전기 자리는 슈퍼컴퓨터 자리.

> 수동 발전기를 남겨 둘 이유는 없습니다. 달리는 복제체 시간이 아깝고, 어디에 두든 그 방 보너스를 깨요.
{: .tip}

## 와이어 등급과 회로 나누기

| 와이어 | 최대 | 재료 | 메모 |
|---|---|---|---|
| **와이어 (Wire)** | 1 kW | 금속 광석 25 kg | 지금 쓰는 것 |
| 전도성 와이어 (Conductive Wire) | 2 kW | 정제 금속 25 kg | Low-Resistance Conductors 연구 |
| 헤비와트 와이어 (Heavi-Watt Wire) | 20 kW | 금속 광석 100 kg | Advanced Power Regulation 연구. 타일을 못 뚫고 장식이 나쁨 → **발전소 안에서만** |
| 변압기 (Power Transformer) | 출력 1 kW | 2×2 | 위쪽이 입력, 아래쪽이 출력 |
| 대형 변압기 (Large Power Transformer) | 출력 4 kW | 3×2, 정제 금속 | |

**규칙**

1. 한 회로에 흐르는 전력이 와이어 최대치를 넘으면 **과부하**로 와이어가 망가집니다. 일반 와이어는 1 kW부터 위험해요.
2. 지금은 한 회로(1 kW)로 충분합니다. 소비가 1 kW에 가까워지면 **회로를 둘로 나눕니다**: ① 생활 구역(연구소·분쇄기·조명) ② 물·산소(펌프·전기분해기·정화기).
3. 발전기가 2대를 넘으면 발전기·배터리를 **헤비와트 와이어 하나**에 모으고, 회로마다 **변압기 1개**를 거쳐 일반 와이어로 내보냅니다. 변압기 출력이 1 kW라 일반 와이어가 절대 과부하되지 않아요.
4. **배터리는 변압기 앞(헤비와트 쪽)에만** 둡니다. 변압기 뒤 일반 와이어 회로에 배터리를 달면 배터리는 출력 제한이 없어서 그 회로를 과부하시킬 수 있어요.
5. 와이어는 층 바닥 줄을 따라 깔고, 통로에서는 한 줄로 내립니다. 방을 바꿔도 다시 안 뜯어요.

## 스마트 배터리 자동화

| 배터리 | 크기 | 용량 | 새는 양 | 재료 |
|---|---|---|---|---|
| 배터리 (Battery) | 1×2 | 10 kJ | 1 kJ/사이클 | 금속 광석 200 kg |
| **스마트 배터리 (Smart Battery)** | 2×2 | 20 kJ | 0.4 kJ/사이클 | **정제 금속** 200 kg, Sound Amplifiers 연구 |
| 점보 배터리 (Jumbo Battery) | 2×2 | 40 kJ | 2 kJ/사이클 | 금속 광석 400 kg |

1. 스마트 배터리를 발전기와 같은 전력 회로에 잇습니다.
2. **자동화 와이어 (Automation Wire)** 로 스마트 배터리 출력 → 석탄 발전기들의 자동화 입력을 잇습니다.
3. 설정: **낮은 기준 50% / 높은 기준 90%**. 50% 아래로 떨어지면 초록 신호 → 발전기 켜짐, 90%를 넘으면 빨강 → 꺼짐.
4. 꺼진 발전기에는 복제체가 석탄을 채우지 않으니, 저장 상자에서 석탄이 남아 있게 됩니다.

> 스마트 배터리는 같은 회로 배터리들의 **평균 충전율**을 봅니다. **점보 배터리와 같이 쓰면** 점보가 다 안 차서 판단이 어긋나니, 이 회로엔 스마트 배터리만 두세요.
{: .warn}

> **정제 금속 구하기:** 금속 정제기는 전기를 많이 먹으니 초반엔 **암석 분쇄기 (Rock Crusher)** 로 금속 광석을 갈면 절반이 정제 금속이 됩니다. 스마트 배터리 1개 = 정제 금속 200 kg.
{: .tip}

## 석탄 공급: 광맥 + 주둥가리

| 공급원 | 양 | 메모 |
|---|---|---|
| 맵의 석탄 광맥 | 수 톤 | 초반엔 이걸로 충분. 굴착 우선순위를 높여 저장 상자로 |
| **주둥가리 (Hatch)** 1마리 | 돌 140 kg/사이클 → **석탄 70 kg/사이클** | 모래·사암·흙·점토 등 아무 돌이나 먹음 |
| 실내 목장 24×4 (8마리) | 석탄 **560 kg/사이클** | 석탄 발전기를 평균 **약 560 W** 로 계속 돌릴 양 |

- 석탄 발전기 1대를 쉬지 않고 돌리려면 주둥가리 약 **8.5마리**가 필요합니다 (위키). 스마트 배터리로 필요할 때만 돌리면 훨씬 적게 들어요.
- 주둥가리 목장은 [격벽 안 동쪽, 포드층 옆]({{ '/guide/core-base/blocks/' | relative_url }})이라 동쪽 통로로 두 층만 내려가면 발전소입니다. 목장 안에는 석탄 저장 상자를 두지 말고, 바닥에 떨어진 석탄을 복제체가 발전소 석탄 저장 상자로 바로 옮기게 하세요 (발전소 상자 우선순위 높게). 중반엔 컨베이어로 바꿉니다.

## 열과 CO₂: 냉방 없이 얼마나 버티나

### 열은 발전기 수가 아니라 쓰는 전력에 비례

석탄 발전기는 **돌 때만** 열을 냅니다. 스마트 배터리로 꺼져 있으면 열도 0이에요. 그래서 발전기를 2대, 3대로 늘려도 **기지가 실제로 쓰는 평균 전력이 같으면 열도 같습니다.**

| 항목 | 값 (1대가 돌 때) | 근거 |
|---|---|---|
| 발전기 자체 열 | **9,000 DTU/s** | 위키 |
| CO₂ 배출 | 20 g/s, **110°C 이상** | 위키 |
| CO₂가 가져오는 열 | 약 1,400 DTU/s | 0.846 × 20 × (110 − 30°C 방) |
| 합계 | **약 10.4 kDTU/s ≈ 600 W당** | → **1 W 쓸 때마다 약 17 DTU/s** |
| 과열 온도 | **75°C** (금 아말감으로 지으면 +50 → **125°C**) | 위키. 배터리 등 다른 전력 건물도 대부분 75°C |

### 평균 전력별 열과 최악의 온도 상승

"최악"은 열이 **벽·바닥으로 하나도 안 빠지고** 방 공기(96칸, 약 1.5 kg/칸)와 안의 건물(발전기 구리 광석 800 kg 등)만 데운다고 친 값입니다. 실제로는 바닥·벽 너머 자연 암석이 열을 받아 가서 이보다 훨씬 느리게 오릅니다.

| 기지 평균 전력 | 필요 발전기 | 열 / 사이클 | 최악 상승 / 사이클 | 판단 |
|---|---|---|---|---|
| 300 W (지금, 5명) | 1대, 절반 가동 | 3.1 MDTU | 약 5°C | **냉방 없이 OK** |
| 500 W | 1대, 83% 가동 | 5.2 MDTU | 약 9°C | OK. 암석 벽·온도 블록 필수, 5사이클마다 확인 |
| 800 W | 2대 | 8.3 MDTU | 약 9°C | 주변 암석이 서서히 달궈짐. **냉방실 준비 시작** |
| 1,200 W | 2대 상시 | 12.5 MDTU | 약 14°C | **냉방 필요** |
| 1,800 W | 3대 상시 | 18.7 MDTU | 약 16°C | **냉방 필수** (증기 터빈으로 되살리기) |

**주변 암석이 받아 주는 양:** 발전소를 자연 암석 속에 파면 바닥·양옆 첫 줄 자연 타일만 약 34칸입니다. 칸당 1톤 안팎 × 비열 0.8 정도라 **1°C 올리는 데 약 27 MDTU** 가 들어요. 평균 500 W(5.2 MDTU/사이클)면 이 첫 줄을 50°C 올리는 데 **250사이클 넘게** 걸리는 셈입니다. 다만 공기·발전기에서 암석으로 열이 옮겨가는 속도가 느려서, 발전기 주변 공기는 암석보다 먼저 뜨거워집니다.

### 결론

- **지금(평균 300~500 W, 발전기 1대)은 냉방 없이 괜찮습니다.** 발전소를 자연 암석 속에 파고, 아래 세 가지만 지키세요.
- **발전기 2대가 늘 돌기 시작하면(평균 1 kW 가까이, 복제체 8명 무렵 사이클 40 전후)** 냉방실을 지을 준비를 합니다.
- **3호기를 놓기 전에는 냉방이 있어야 합니다.**
- 시점보다 **온도로 판단**하세요: 발전기 온도가 **50°C를 넘거나 사이클당 2°C 넘게 오르면** 냉방을 시작할 때입니다.

### 냉방 전까지 지킬 세 가지

1. **단열은 천장(격벽)만.** 바닥과 양옆 벽은 일반 타일이나 자연 암석으로 두세요. 사방을 단열 타일로 막으면 열이 갇혀서 오히려 빨리 과열됩니다.
2. **온도 블록 (Tempshift Plate)** 을 발전기 뒤 벽에 깔면 발전기 열이 주변 타일로 빨리 퍼집니다. 화강암처럼 열을 잘 전하는 돌로 지으세요.
3. 발전기는 가능하면 **금 아말감 (Gold Amalgam)** 으로 지어 과열 온도를 125°C로 올립니다.

- 통로에서 발전소로 들어가는 문은 **격벽을 지나므로 기계식 에어락**입니다. 뜨거운 CO₂가 통로로 새지 않아요.
- 얼음 바이옴에서 **씨근풀 (Wheezewort)** 을 구하면, 농장 타일에 심은 1그루가 CO₂ 1 kg/s를 5°C 식혀 **약 4.2 kDTU/s** 를 지웁니다 (인회석 4 kg/사이클). 2~3그루면 발전기 1대분 열을 상쇄해요.

### CO₂

- 1대가 쉬지 않고 돌면 CO₂ **12 kg/사이클**. 평균 500 W면 약 10 kg/사이클이라, 방 안에 수십 사이클은 그냥 쌓여도 괜찮습니다. 복제체는 석탄 채우러 잠깐 들어갈 때 숨을 참아요.
- 많이 쌓이면 **기체 펌프**로 맨 아래 CO₂ 구덩이·미끌이 목장으로 뺍니다. 뜨거운 CO₂를 빼면 열도 같이 나가요. 나중엔 **탄소 흡수기 (Carbon Skimmer)**.

## 업그레이드 순서

| 시기 | 할 일 | 발전량 |
|---|---|---|
| 사이클 10~20 (지금) | 석탄 발전기 1 + 배터리 2, 일반 와이어 1회로. 수동 발전기 철거 | 600 W |
| 사이클 20~40 | 암석 분쇄기로 정제 금속 → **스마트 배터리 자동화**. 석탄 2호기. 주둥가리 목장 시작. 회로 둘로 나누기 | 1,200 W |
| 사이클 40~ | 석탄 3호기, **헤비와트 + 변압기**, 전력 제어소 마이크로칩(+50%) | 1,800~2,700 W |
| SPOM 가동 후 | 전기분해기(120 W) 수소 112 g/s → **수소 발전기** 800 W. 펌프 2개(480 W) 빼도 **약 +200 W 남고 산소는 공짜** | +200 W, 산소 8명분 |
| 천연가스 분출구 발견 시 | 천연가스 발전기 (90 g/s → 800 W) | +800 W/대 |
| 후반 | 석유 발전기 2 kW, 산업 열 → 증기 터빈 | 2,000 W/대 |

## 매일 볼 것

1. **전력 오버레이**에서 회로별 "사용 중 / 최대" 를 확인. 1 kW 와이어 회로가 800 W를 넘기 시작하면 회로를 나누세요.
2. **배터리 충전 그래프**가 하루 내내 바닥이면 발전기가 모자란 것, 늘 꽉 차 있으면 자동화가 빠진 것.
3. **석탄 저장 상자 잔량**: 하루 사용량(발전기 1대 최대 600 kg)보다 많이 남아 있는지.
4. 발전소 **온도**와 CO₂ 높이.
5. 정전이 나면 펌프·전기분해기가 먼저 멈춰 산소가 끊깁니다. 이 회로를 가장 먼저 살리세요.
