---
title: 중앙 기지 배치도
nav_title: 중앙 기지 배치도
nav_order: 8
nav_group: play
permalink: /guide/core-base/
description: 방마다 크기, 포드 주변 핵심 구역 배치, 초반 임시 배치에서 뜯지 않고 확장하는 법, 초반 시설 철거·재활용, 휴식 시간 분리(교대 일정)까지.
---

* 목차
{:toc}

## 한 줄 요약

**층 = 내부 4칸 + 바닥 1칸, 방 = 가로 16칸(16×4=64), 가운데 = 사다리 + 소방봉.** 이 격자만 처음부터 지키면 초반 시설을 철거해도 방 테두리는 그대로 두고 안의 건물만 바꿔 끼우면 됩니다.

| 규격 | 값 | 이유 |
|---|---|---|
| 층 높이 | 5칸 (내부 4 + 바닥 1) | 포드(Printing Pod)가 4×4, 고급 숙소·개인 침실은 천장 4칸 조건 |
| 작은 방 | **16×4 = 64** | 침실·화장실·식당·공원 최대치 64에 딱 맞음 |
| 큰 방 | 24×4 = 96 | 온실·주방·오락실·발전소·목장·병원 최대치 |
| 아주 큰 방 | 30×4 = 120 | 대연회장·연구실·자연 보호구역 최대치 |
| 중앙 통로 | 2칸 (사다리 + 소방봉) | 올라갈 땐 사다리, 내려갈 땐 소방봉(내려가는 속도 4배) |
| 방 사이 벽 | 1칸 | 벽 칸은 방 크기에 안 들어감 |

## 방 크기 전체 표

공식 위키(Room Overlay) 기준입니다. 크기는 **벽 안쪽 칸 수**입니다. ★ 표시는 이 페이지 배치도에서 쓰는 크기입니다.

| 방 | 크기 범위 | 추천 (가로×세로) | 조건 | 효과 |
|---|---|---|---|---|
| 간이 화장실 (Latrine) | 12~64 | 8×4 → ★16×4 | 간이 화장실 + 세면대 | 사기 +1 |
| 세면실 (Washroom) | 12~64 | ★16×4 | 수세식 화장실 + 물 연결 세면대(Sink), **간이 화장실 없음** | 사기 +2 |
| 공동 침실 (Barracks) | 12~64 | ★16×4 (간이 침대 8 / 편한 침대 4) | 침대 1개 이상 | 사기 +1 |
| 고급 숙소 (Luxury Barracks) | 12~64 | ★16×4 | 편한 침대, **간이 침대 없음**, 장식 1, 천장 4칸 | 사기 +2 |
| 개인 침실 (Private Bedroom) | 24~64 | ★6×4 = 24 (침대 4칸 + 장식 2칸) | 편한 침대 **딱 1개**, 장식 2, 천장 4칸, 뒷벽 전부 | 사기 +3 |
| 식당 (Mess Hall) | 12~64 | ★16×4 | 식탁 | 사기 +3 |
| 대연회장 (Great Hall) | 32~120 | ★16×4 (식당 그대로) | 식탁 + 장식 20 이상 1개 + 오락 건물 | 사기 +4 |
| 연회장 (Banquet Hall) | 32~120 | 16×4 ~ 24×4 | 공용 식탁(Communal Table), 장식, 오락 건물, 장식품 전시, **식탁 없음** | 사기 +6 |
| 주방 (Kitchen) | 12~96 | ★16×4 | 향신료 분쇄기 + 그릴/가스레인지 + 냉장고, **식탁 없음** | 향신료 사용 |
| 연구실 (Laboratory) | 32~120 | ★16×4 | 연구 건물 2개 | 연구 +10%, 지오튜너·관제소 사용 |
| 온실 (Greenhouse) | 12~96 | ★16×4 ~ 24×4 | 농업 작업대 | 비료로 성장 2배 |
| 목장 (Stable) | 12~96 | 24×4 | 목장 건물 (손질 작업대 등) | 동물 손질 |
| 발전소 (Power Plant) | 12~96 | ★16×4 ~ 24×4 | 대형 발전기 + 전력 건물 2개 | 마이크로칩으로 발전 +50% |
| 오락실 (Recreation Room) | 12~96 | ★16×4 | 오락 건물 + 장식 | 휴식 시간 사기 보너스 |
| 마사지실 (Massage Clinic) | 12~64 | 8×4 | 마사지 테이블 + 장식 | 스트레스 감소 2배 |
| 병원 (Hospital) | 12~96 | 16×4 | 의료 건물 + 화장실 + 식탁 | 병 전파 감소 |
| 공원 (Park) | 12~64 | ★16×4 | 공원 표지판 + 야생 식물 2 | 지나가면 사기 +3 |
| 자연 보호구역 (Nature Reserve) | 32~120 | ★16×4 ~ 30×4 | 공원 표지판 + 야생 식물 4 | 지나가면 사기 +6 |

> 발전소·온실·목장·주방 말고는 거의 다 **산업 기계 금지**입니다. 수동 발전기를 포함한 모든 발전기, 전기분해기, 물 정화기, 펌프, 금속 정제기가 산업 기계예요. 반대로 산소 확산기, 조류 테라리움, 보관함, 배터리, 미생물 분쇄기, 전기 그릴, 냉장고, 퇴비 더미는 산업 기계가 **아닙니다**.
{: .warn}

## 후반 완성 배치도

포드가 있는 층을 기준(포드층)으로, 위로 생활, 아래로 농장·물·산업이 쌓입니다. 칸마다 16칸 방이고, 가운데 노란 줄이 사다리, 주황 줄이 소방봉, 하늘색 막대가 문입니다.

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 794 310" width="794" role="img" aria-label="후반 완성 배치도" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="794" height="310" fill="#11131f"/><rect x="74" y="0" width="720" height="10" fill="#5a4a3a"/><text x="6" y="36" fill="#a9b0d0" font-size="12">2층</text><rect x="74" y="10" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="10" width="160" height="40" fill="#2c4a2a" stroke="#a3ff84" stroke-width="1.5"/><text x="164.0" y="28" fill="#a3ff84" font-size="12" font-weight="700" text-anchor="middle">개인 침실 ×2</text><text x="164.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">각 6×4, 뒷벽 + 장식 2</text><rect x="254" y="10" width="160" height="40" fill="#2c4a2a" stroke="#a3ff84" stroke-width="1.5"/><text x="334.0" y="28" fill="#a3ff84" font-size="12" font-weight="700" text-anchor="middle">개인 침실 ×2</text><text x="334.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">각 6×4</text><rect x="454" y="10" width="160" height="40" fill="#1f3550" stroke="#42a4f4" stroke-width="1.5"/><text x="534.0" y="28" fill="#42a4f4" font-size="12" font-weight="700" text-anchor="middle">오락실</text><text x="534.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">오락 건물 + 장식</text><rect x="624" y="10" width="160" height="40" fill="#4a2830" stroke="#ff848e" stroke-width="1.5"/><text x="704.0" y="28" fill="#ff848e" font-size="12" font-weight="700" text-anchor="middle">마사지실 · 병원</text><rect x="74" y="50" width="720" height="10" fill="#5a4a3a"/><text x="6" y="86" fill="#a9b0d0" font-size="12">1층</text><rect x="74" y="60" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="60" width="160" height="40" fill="#2c4a2a" stroke="#a3ff84" stroke-width="1.5"/><text x="164.0" y="78" fill="#a3ff84" font-size="12" font-weight="700" text-anchor="middle">고급 숙소</text><text x="164.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">편한 침대 4 + 장식</text><rect x="254" y="60" width="160" height="40" fill="#24452e" stroke="#acffbd" stroke-width="1.5"/><text x="334.0" y="78" fill="#acffbd" font-size="12" font-weight="700" text-anchor="middle">자연 보호구역</text><text x="334.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">공원 표지판 + 야생 식물 4+</text><rect x="454" y="60" width="160" height="40" fill="#20434a" stroke="#84fff4" stroke-width="1.5"/><text x="534.0" y="78" fill="#84fff4" font-size="12" font-weight="700" text-anchor="middle">세면실</text><text x="534.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">수세식 화장실 4 + 세면대(Sink) 4</text><rect x="624" y="60" width="160" height="40" fill="#2c4a2a" stroke="#a3ff84" stroke-width="1.5"/><text x="704.0" y="78" fill="#a3ff84" font-size="12" font-weight="700" text-anchor="middle">개인 침실 ×2</text><rect x="74" y="100" width="720" height="10" fill="#5a4a3a"/><text x="6" y="136" fill="#a9b0d0" font-size="12">포드층</text><rect x="74" y="110" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="110" width="160" height="40" fill="#4a4226" stroke="#ffe284" stroke-width="1.5"/><text x="164.0" y="128" fill="#ffe284" font-size="12" font-weight="700" text-anchor="middle">주방</text><text x="164.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">전기 그릴 · 향신료 분쇄기 · 냉장고</text><rect x="254" y="110" width="160" height="40" fill="#4a4226" stroke="#ffe284" stroke-width="1.5"/><text x="334.0" y="128" fill="#ffe284" font-size="12" font-weight="700" text-anchor="middle">대연회장</text><text x="334.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">식탁 + 워터 쿨러 + 장식 20+</text><rect x="454" y="110" width="160" height="40" fill="#3c2a48" stroke="#d38be0" stroke-width="1.5"/><text x="534.0" y="128" fill="#d38be0" font-size="12" font-weight="700" text-anchor="middle">연구실</text><text x="534.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">포드 + 연구소 + 슈퍼컴퓨터</text><rect x="624" y="110" width="160" height="40" fill="#4a3420" stroke="#f4a442" stroke-width="1.5"/><text x="704.0" y="128" fill="#f4a442" font-size="12" font-weight="700" text-anchor="middle">작업장</text><text x="704.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">방 아님: 산업 기계 OK</text><rect x="74" y="150" width="720" height="10" fill="#5a4a3a"/><text x="6" y="186" fill="#a9b0d0" font-size="12">지하 1</text><rect x="74" y="160" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="160" width="160" height="40" fill="#3b4720" stroke="#cdf248" stroke-width="1.5"/><text x="164.0" y="178" fill="#cdf248" font-size="12" font-weight="700" text-anchor="middle">온실 A</text><text x="164.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">농장 타일 + 농업 작업대</text><rect x="254" y="160" width="160" height="40" fill="#3b4720" stroke="#cdf248" stroke-width="1.5"/><text x="334.0" y="178" fill="#cdf248" font-size="12" font-weight="700" text-anchor="middle">온실 B</text><text x="334.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">농장 타일 + 농업 작업대</text><rect x="454" y="160" width="160" height="40" fill="#4a3420" stroke="#f4a442" stroke-width="1.5"/><text x="534.0" y="178" fill="#f4a442" font-size="12" font-weight="700" text-anchor="middle">물 처리</text><text x="534.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">물 정화기 · 액체 펌프</text><rect x="624" y="160" width="160" height="40" fill="#1d3358" stroke="#6aa8ff" stroke-width="1.5"/><text x="704.0" y="178" fill="#6aa8ff" font-size="12" font-weight="700" text-anchor="middle">수조</text><rect x="74" y="200" width="720" height="10" fill="#5a4a3a"/><text x="6" y="236" fill="#a9b0d0" font-size="12">지하 2</text><rect x="74" y="210" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="210" width="160" height="40" fill="#4a3420" stroke="#f4a442" stroke-width="1.5"/><text x="164.0" y="228" fill="#f4a442" font-size="12" font-weight="700" text-anchor="middle">전기분해기 산소</text><text x="164.0" y="243" fill="#d6dbef" font-size="9.5" text-anchor="middle">단열 타일로 감싸기</text><rect x="254" y="210" width="160" height="40" fill="#4a3420" stroke="#f4a442" stroke-width="1.5"/><text x="334.0" y="228" fill="#f4a442" font-size="12" font-weight="700" text-anchor="middle">발전소</text><text x="334.0" y="243" fill="#d6dbef" font-size="9.5" text-anchor="middle">석탄/수소 발전기 + 전력 건물</text><rect x="454" y="210" width="160" height="40" fill="#4a3420" stroke="#f4a442" stroke-width="1.5"/><text x="534.0" y="228" fill="#f4a442" font-size="12" font-weight="700" text-anchor="middle">정제 · 제련</text><text x="534.0" y="243" fill="#d6dbef" font-size="9.5" text-anchor="middle">금속 정제기 등</text><rect x="624" y="210" width="160" height="40" fill="#1d3358" stroke="#6aa8ff" stroke-width="1.5"/><text x="704.0" y="228" fill="#6aa8ff" font-size="12" font-weight="700" text-anchor="middle">수조 2 / 오염수</text><rect x="74" y="250" width="720" height="10" fill="#5a4a3a"/><text x="6" y="286" fill="#a9b0d0" font-size="12">지하 3</text><rect x="74" y="260" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="260" width="700" height="40" fill="#2a2b33" stroke="#7d7f8f" stroke-width="1.5"/><text x="434.0" y="278" fill="#7d7f8f" font-size="12" font-weight="700" text-anchor="middle">CO₂ 구덩이</text><text x="434.0" y="293" fill="#d6dbef" font-size="9.5" text-anchor="middle">탄소 제거기 · 무거운 기체가 모이는 곳</text><rect x="424" y="0" width="20" height="250" fill="#2a2618"/><line x1="425" y1="5" x2="433" y2="5" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="15" x2="433" y2="15" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="25" x2="433" y2="25" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="35" x2="433" y2="35" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="45" x2="433" y2="45" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="55" x2="433" y2="55" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="65" x2="433" y2="65" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="75" x2="433" y2="75" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="85" x2="433" y2="85" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="95" x2="433" y2="95" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="105" x2="433" y2="105" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="115" x2="433" y2="115" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="125" x2="433" y2="125" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="135" x2="433" y2="135" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="145" x2="433" y2="145" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="155" x2="433" y2="155" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="165" x2="433" y2="165" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="175" x2="433" y2="175" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="185" x2="433" y2="185" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="195" x2="433" y2="195" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="205" x2="433" y2="205" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="215" x2="433" y2="215" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="225" x2="433" y2="225" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="235" x2="433" y2="235" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="245" x2="433" y2="245" stroke="#f6c445" stroke-width="1"/><line x1="439.0" y1="0" x2="439.0" y2="250" stroke="#ff8a4c" stroke-width="2"/><rect x="246" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="74" y="300" width="720" height="10" fill="#5a4a3a"/></svg>
</div>
<p class="bp-legend">1칸 = 1타일. 방 = 16×4(64칸), 층 간격 5칸. 초록 침실 · 노랑 식사 · 청록 화장실 · 보라 연구 · 연두 농장 · 주황 산업 · 파랑 물.</p>

### 하루 동선: 침실 → 화장실 → 식당 → 일

1. **1층 고급 숙소**에서 일어나서
2. 바로 옆 **자연 보호구역**을 지나 통로로 나옵니다 (사기 +6, 매일 저절로).
3. 통로 건너 **세면실**에서 볼일 보고 손 씻고
4. 소방봉으로 한 층 내려가 **대연회장**에서 밥 먹고
5. 같은 층 **연구실**이나 아래층 **온실·산업층**으로 출근합니다.

침실로 가는 길이 보호구역을 **반드시 통과**하게 만드는 게 핵심입니다. 그래서 숙소는 통로에 직접 붙이지 않고 보호구역 바깥쪽에 둡니다.

### 층별 역할

| 층 | 서쪽 바깥 | 서쪽 안쪽 | 동쪽 안쪽 | 동쪽 바깥 |
|---|---|---|---|---|
| 2층 | 개인 침실 ×2 (6×4) | 개인 침실 ×2 | 오락실 | 마사지실·병원 |
| 1층 | 고급 숙소 | **자연 보호구역** | 세면실 | 개인 침실 ×2 |
| 포드층 | 주방 | 대연회장 | 연구실 (포드 포함) | 작업장 (방 아님) |
| 지하 1 | 온실 A | 온실 B | 물 처리 | 수조 |
| 지하 2 | 전기분해기 산소 | 발전소 | 정제·제련 | 수조 2 / 오염수 |
| 지하 3 | CO₂ 구덩이 (가로 전체) | ← | ← | ← |

> 지하 2 산업층은 뜨겁습니다. 지하 1(온실)과 지하 2 사이 바닥은 **단열 타일**로 깔고, 산업층 둘레도 단열 타일로 감싸세요. CO₂는 무거워서 맨 아래 구덩이로 저절로 모입니다.
{: .heat}

## 초반 임시 배치 (사이클 1~20 정도)

처음엔 위 도면의 **안쪽 칸 위주로** 파서 씁니다. 중요한 건 **벽과 바닥 줄을 처음부터 최종 위치에 놓는 것**입니다. 그래야 나중에 방 안 건물만 바꿉니다.

<div class="bp-wrap" markdown="0">
<svg viewBox="0 0 794 310" width="794" role="img" aria-label="초반 임시 배치도" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans KR, sans-serif"><rect width="794" height="310" fill="#11131f"/><rect x="74" y="0" width="720" height="10" fill="#5a4a3a"/><text x="6" y="36" fill="#a9b0d0" font-size="12">2층</text><rect x="74" y="10" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="10" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="164.0" y="28" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="164.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="254" y="10" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="334.0" y="28" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="334.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="454" y="10" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="534.0" y="28" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="534.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="624" y="10" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="704.0" y="28" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="704.0" y="43" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="74" y="50" width="720" height="10" fill="#5a4a3a"/><text x="6" y="86" fill="#a9b0d0" font-size="12">1층</text><rect x="74" y="60" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="60" width="160" height="40" fill="#2c4a2a" stroke="#a3ff84" stroke-width="1.5"/><text x="164.0" y="78" fill="#a3ff84" font-size="12" font-weight="700" text-anchor="middle">공동 침실</text><text x="164.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">간이 침대 3</text><rect x="254" y="60" width="160" height="40" fill="#24452e" stroke="#acffbd" stroke-width="1.5"/><text x="334.0" y="78" fill="#acffbd" font-size="12" font-weight="700" text-anchor="middle">통로 → 공원 예정</text><text x="334.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">바닥은 원래 흙/사암 그대로</text><rect x="454" y="60" width="160" height="40" fill="#20434a" stroke="#84fff4" stroke-width="1.5"/><text x="534.0" y="78" fill="#84fff4" font-size="12" font-weight="700" text-anchor="middle">간이 화장실 방</text><text x="534.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">간이 화장실 2 + 세면대 2</text><rect x="624" y="60" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="704.0" y="78" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="704.0" y="93" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="74" y="100" width="720" height="10" fill="#5a4a3a"/><text x="6" y="136" fill="#a9b0d0" font-size="12">포드층</text><rect x="74" y="110" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="110" width="160" height="40" fill="#30344a" stroke="#a9b0d0" stroke-width="1.5"/><text x="164.0" y="128" fill="#a9b0d0" font-size="12" font-weight="700" text-anchor="middle">보관함 · 작업대</text><text x="164.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">임시 → 주방 자리</text><rect x="254" y="110" width="160" height="40" fill="#4a4226" stroke="#ffe284" stroke-width="1.5"/><text x="334.0" y="128" fill="#ffe284" font-size="12" font-weight="700" text-anchor="middle">식당</text><text x="334.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">미생물 분쇄기 + 식탁 3</text><rect x="454" y="110" width="160" height="40" fill="#30344a" stroke="#a9b0d0" stroke-width="1.5"/><text x="534.0" y="128" fill="#a9b0d0" font-size="12" font-weight="700" text-anchor="middle">포드 + 연구소</text><text x="534.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">수동 발전기·배터리 (임시)</text><rect x="624" y="110" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="704.0" y="128" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="704.0" y="143" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="74" y="150" width="720" height="10" fill="#5a4a3a"/><text x="6" y="186" fill="#a9b0d0" font-size="12">지하 1</text><rect x="74" y="160" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="160" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="164.0" y="178" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="164.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="254" y="160" width="160" height="40" fill="#3b4720" stroke="#cdf248" stroke-width="1.5"/><text x="334.0" y="178" fill="#cdf248" font-size="12" font-weight="700" text-anchor="middle">화분 농장</text><text x="334.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">식사나무 · 털열매 꽃</text><rect x="454" y="160" width="160" height="40" fill="#30344a" stroke="#a9b0d0" stroke-width="1.5"/><text x="534.0" y="178" fill="#a9b0d0" font-size="12" font-weight="700" text-anchor="middle">수동 펌프 · 산소 확산기</text><text x="534.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">임시</text><rect x="624" y="160" width="160" height="40" fill="#1d3358" stroke="#6aa8ff" stroke-width="1.5"/><text x="704.0" y="178" fill="#6aa8ff" font-size="12" font-weight="700" text-anchor="middle">웅덩이</text><text x="704.0" y="193" fill="#d6dbef" font-size="9.5" text-anchor="middle">→ 수조로</text><rect x="74" y="200" width="720" height="10" fill="#5a4a3a"/><text x="6" y="236" fill="#a9b0d0" font-size="12">지하 2</text><rect x="74" y="210" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="210" width="330" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="249.0" y="228" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="249.0" y="243" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="454" y="210" width="160" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="534.0" y="228" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="534.0" y="243" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="624" y="210" width="160" height="40" fill="#1d3358" stroke="#6aa8ff" stroke-width="1.5"/><text x="704.0" y="228" fill="#6aa8ff" font-size="12" font-weight="700" text-anchor="middle">웅덩이 아래쪽</text><rect x="74" y="250" width="720" height="10" fill="#5a4a3a"/><text x="6" y="286" fill="#a9b0d0" font-size="12">지하 3</text><rect x="74" y="260" width="720" height="40" fill="#5a4a3a"/><rect x="84" y="260" width="700" height="40" fill="#1a1c28" stroke="#3a3f5c" stroke-width="1.5" stroke-dasharray="4 3"/><text x="434.0" y="278" fill="#3a3f5c" font-size="12" font-weight="700" text-anchor="middle">미굴착</text><text x="434.0" y="293" fill="#d6dbef" font-size="9.5" text-anchor="middle">나중에 확장</text><rect x="424" y="0" width="20" height="250" fill="#2a2618"/><line x1="425" y1="5" x2="433" y2="5" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="15" x2="433" y2="15" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="25" x2="433" y2="25" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="35" x2="433" y2="35" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="45" x2="433" y2="45" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="55" x2="433" y2="55" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="65" x2="433" y2="65" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="75" x2="433" y2="75" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="85" x2="433" y2="85" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="95" x2="433" y2="95" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="105" x2="433" y2="105" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="115" x2="433" y2="115" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="125" x2="433" y2="125" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="135" x2="433" y2="135" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="145" x2="433" y2="145" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="155" x2="433" y2="155" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="165" x2="433" y2="165" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="175" x2="433" y2="175" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="185" x2="433" y2="185" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="195" x2="433" y2="195" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="205" x2="433" y2="205" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="215" x2="433" y2="215" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="225" x2="433" y2="225" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="235" x2="433" y2="235" stroke="#f6c445" stroke-width="1"/><line x1="425" y1="245" x2="433" y2="245" stroke="#f6c445" stroke-width="1"/><line x1="439.0" y1="0" x2="439.0" y2="250" stroke="#ff8a4c" stroke-width="2"/><rect x="246" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="30" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="80" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="130" width="6" height="20" fill="#8a9bd0"/><rect x="246" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="180" width="6" height="20" fill="#8a9bd0"/><rect x="416" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="446" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="616" y="230" width="6" height="20" fill="#8a9bd0"/><rect x="74" y="300" width="720" height="10" fill="#5a4a3a"/></svg>
</div>
<p class="bp-legend">점선 = 아직 안 판 곳. 초반엔 6칸만 써도 충분합니다.</p>

| 자리 | 초반에 둘 것 | 방 |
|---|---|---|
| 1층 서쪽 바깥 | 간이 침대 3 | 공동 침실 (+1) |
| 1층 서쪽 안쪽 | 그냥 통로. **바닥을 타일로 덮지 말고** 원래 흙/사암 그대로 | (나중에 공원 → 보호구역) |
| 1층 동쪽 안쪽 | 간이 화장실 2 + 세면대 2 (+ 퇴비 더미) | 간이 화장실 (+1) |
| 포드층 서쪽 안쪽 | 미생물 분쇄기 + 식탁 | 식당 (+3) |
| 포드층 동쪽 안쪽 | 포드 + 연구소 + 수동 발전기 + 배터리 | 방 보너스 없음 (임시) |
| 포드층 서쪽 바깥 | 보관함, 작업대 | 없음 |
| 지하 1 서쪽 안쪽 | 화분 농장 (식사나무, 털열매 꽃) | 없음 |
| 지하 1 동쪽 | 수동 펌프, 산소 확산기 / 웅덩이 | 없음 |

> 처음 파는 순서: 포드층 좌우 → 가운데 통로(사다리) → 1층(침실·화장실) → 지하 1(농장·물). 위층부터 파면 물이 새는 일이 줄어듭니다.
{: .tip}

## 한 방에 같이 두면 안 되는 것 (중첩 불가)

방 조건끼리 부딪혀서, 업그레이드하려면 **초반 건물을 꼭 철거해야** 하는 조합입니다.

| 같이 두면 | 결과 |
|---|---|
| 간이 화장실 + 수세식 화장실 | 세면실 안 됨 (간이 화장실 방으로 남음) |
| 간이 침대 + 편한 침대 | 고급 숙소 안 됨 (공동 침실로 남음) |
| 편한 침대 2개 이상 | 개인 침실 안 됨 (고급 숙소가 됨) |
| 식탁 + 주방 설비 | 주방 안 됨. 주방은 **식탁 없는 별도 방** |
| 식탁 + 공용 식탁 | 연회장 안 됨 |
| 식탁 + 침대 (한 방) | 두 조건을 같이 만족 → **기타 방**, 보너스 0 |
| 수동 발전기·펌프·전기분해기 등 + 생활 방 | 산업 기계라 방 보너스 사라짐 |
| 공원 + 자연 보호구역 | 겹쳐서 받지 않음, +6이 +3을 덮어씀 (같은 방 업그레이드로 해결) |

## 초반 시설 철거 시점과 그 자리 재활용

| 초반 시설 | 자리 | 철거 시점 | 그 자리 재활용 |
|---|---|---|---|
| 간이 화장실 ×2 + 세면대 | 1층 동쪽 안쪽 | 물 정화기가 돌아가고 수세식 화장실 연구 후 | 같은 방에 **수세식 화장실 4 + 세면대(Sink) 4** (각 2칸 폭이라 16칸에 딱). 세면실 +2. 퇴비 더미는 지하 1 농장 쪽으로 |
| 간이 침대 ×3 | 1층 서쪽 바깥 | 플라스틱이 모여 편한 침대를 **한 번에 전부** 바꿀 수 있을 때 | 같은 방에 편한 침대(4칸 폭이라 방 하나에 4개) + 장식 1 → 고급 숙소 +2. 5명째부터는 1층 동쪽 바깥·2층에 개인 침실(6×4)로 분가 |
| 수동 발전기 | 포드층 동쪽 안쪽 | 지하 2 발전소에 석탄 발전기가 돈 뒤 | 그 자리에 **슈퍼컴퓨터** → 연구소와 합쳐 연구실(+10%). 포드 불빛 범위라 작업 속도도 빠름 |
| 미생물 분쇄기 | 포드층 서쪽 안쪽 | 주방(전기 그릴) 완성 후 | 식탁 늘리고 **워터 쿨러 + 장식 20 이상** → 대연회장 +4 |
| 배급 상자 | 식당 근처 | 냉장고 지은 뒤 | 철거. 냉장고는 주방에 |
| 보관함·작업대 | 포드층 서쪽 바깥 | 주방 지을 때 | **주방** (전기 그릴 + 향신료 분쇄기 + 냉장고, 식탁 없이). 보관함은 포드층 동쪽 바깥 작업장으로 |
| 화분 | 지하 1 서쪽 안쪽 | 농장 타일 + 농업 작업대 연구 후 | 같은 칸을 농장 타일로 → 온실 A·B (작업대 각 1개) |
| 수동 펌프, 산소 확산기 | 지하 1 동쪽 안쪽 | 액체 펌프·전기분해기 가동 후 | 물 처리 구역 (물 정화기, 액체 펌프). 산업 기계라 방으로 묶지 않음 |
| 그냥 통로 | 1층 서쪽 안쪽 | 공원 표지판 연구 직후 | 표지판 + 야생 식물 2 = 공원 +3 → 식물 4개 되면 같은 방이 **자연 보호구역 +6** |

> **야생 식물**은 화분·농장 타일에 심은 게 아니라 **자연 타일에서 자란 식물**입니다. 보호구역 자리는 포드 주변에서 야생 식물이 원래 있던 쪽으로 정하고, 그 칸 바닥은 파지 말고 남기세요. 핍(Pip)을 데려오면 자연 타일에 씨앗을 심어주는데, 3개 넘게 몰아서는 안 심으니 간격을 두세요.
{: .tip}

## 확장 규칙 (뜯지 않고 늘리기)

- **가운데 통로는 위아래로만** 늘립니다. 통로 위치는 절대 안 옮깁니다.
- **좌우는 16칸 단위로 바깥에** 붙입니다 (서쪽 3번째, 동쪽 3번째…). 벽 1칸 + 방 16칸.
- **위로는 주거**(개인 침실, 오락실), **아래로는 산업**(정제, 목장, 2차 발전)이 늘어납니다.
- 96칸·120칸짜리 큰 방이 필요하면 **바깥 날개만** 24칸·30칸으로 넓게 팝니다.
- 바닥 줄(5칸 간격)에 맞춰 파이프·와이어를 깔면, 방을 바꿔도 배관을 다시 안 뜯습니다.
- 기지가 가로로 50칸을 넘으면 운송관(Transit Tube)을 통로 옆에 추가하세요.

## 휴식 시간 분리 (교대 일정)

복제체 전원이 같은 일정이면 휴식·취침·목욕 시간에 **모두 한꺼번에** 화장실·식탁·통로로 몰립니다. 일정을 조별로 나눠 **6칸씩 밀어두면** 한 번에 몰리는 인원이 1/4로 줄어요.

### 실제 일정 예시 (4교대)

<div class="sch" role="img" aria-label="4개 조 일정: 각 조의 휴식 2칸, 취침 3칸, 목욕 1칸이 6칸씩 밀려 있음"><div class="sch-row"><span class="sch-name"></span><div class="sch-bar"><span class="h">0</span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h">6</span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h">12</span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h">18</span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span><span class="h"></span></div></div><div class="sch-row"><span class="sch-name">오전조<small>양자역학싫어요</small></span><div class="sch-bar"><span class="B">목</span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="D">휴</span><span class="D">휴</span><span class="S">잠</span><span class="S">잠</span><span class="S">잠</span></div></div><div class="sch-row"><span class="sch-name">낮조<small>말랑</small></span><div class="sch-bar"><span class="W"></span><span class="D">휴</span><span class="D">휴</span><span class="S">잠</span><span class="S">잠</span><span class="S">잠</span><span class="B">목</span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span></div></div><div class="sch-row"><span class="sch-name">저녁조<small>감자</small></span><div class="sch-bar"><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="D">휴</span><span class="D">휴</span><span class="S">잠</span><span class="S">잠</span><span class="S">잠</span><span class="B">목</span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span></div></div><div class="sch-row"><span class="sch-name">새벽조<small>(비어 있음)</small></span><div class="sch-bar"><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="D">휴</span><span class="D">휴</span><span class="S">잠</span><span class="S">잠</span><span class="S">잠</span><span class="B">목</span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span><span class="W"></span></div></div><div class="sch-legend"><span class="W"></span>일 <span class="D">휴</span>휴식 <span class="S">잠</span>취침 <span class="B">목</span>목욕 · 1칸 = 25초, 하루 24칸 · 맨 왼쪽 5칸 = 아침(아침형 보너스), 맨 오른쪽 3칸 = 밤(올빼미형 보너스)</div></div>

네 조 모두 **일 18칸 · 휴식 2칸 · 취침 3칸 · 목욕 1칸**으로 기본 일정과 같은 구성이고, 시작 위치만 6칸씩 다릅니다.

| 조 | 휴식 | 취침 | 목욕 | 일 |
|---|---|---|---|---|
| 오전조 | 19~20 | 21~23 | 0 | 1~18 |
| 낮조 | 1~2 | 3~5 | 6 | 7~23, 0 |
| 저녁조 | 7~8 | 9~11 | 12 | 13~23, 0~6 |
| 새벽조 | 13~14 | 15~17 | 18 | 19~23, 0~12 |

### 왜 좋은가

- **화장실 줄이 없어짐.** 복제체는 하루에 최소 한 번 화장실을 갑니다. 목욕 시간이 조마다 다르니 같은 화장실을 돌아가며 씁니다. 공식 위키도 "화장실은 공용이라 목욕 시간이 일정 분리에 가장 좋은 칸"이라고 설명해요.
- **식탁이 덜 필요함.** 배고픈 복제체는 휴식 시간에 밥을 먹습니다. 휴식 시간이 겹치지 않으니 식탁은 **가장 큰 조 인원수만큼**이면 충분해요.
- **통로가 안 막힘.** 출퇴근 시간이 분산되어 사다리·소방봉에서 서로 비켜 기다리는 시간이 줄어요.
- **잠 깨우는 사고가 줄어듦.** 코골이(Loud Sleeper)·방귀쟁이(Flatulent)는 같이 자는 복제체를 깨웁니다. 같은 시간에 자는 인원이 적을수록 피해가 작아요.
- **일이 24시간 돌아감.** 항상 3개 조가 일하고 있어서 연구소·작업대가 쉬지 않습니다.

### 시설 개수 기준

| 시설 | 일정 하나일 때 | 4교대일 때 |
|---|---|---|
| 침대 | 인원수 | **인원수 그대로** (침대는 복제체마다 하나씩 배정되어 나눠 쓰지 않음) |
| 식탁 | 인원수 | 가장 큰 조 인원수 |
| 화장실 | 인원 ÷ 2 정도 | 조마다 1~2개면 충분 (경험치. 한 조 4명까지 화장실 2개) |
| 세면대 | 화장실과 같은 수 | 화장실과 같은 수 |

> 조를 나눠도 **침대 수는 안 줄어요.** 그래서 침실 면적은 그대로고, 줄어드는 건 화장실·식탁·통로 혼잡입니다. 위 배치도의 세면실(화장실 4 + 세면대 4)이면, 4교대에 조당 4명(총 16명)이어도 목욕 시간마다 한 조가 화장실 4개를 나눠 쓰는 셈이라 여유롭습니다.
{: .warn}

### 주의할 점

- **침실은 어둡게.** 빛은 수면 방해(Interrupted Sleep) 원인입니다. 다른 조가 깨어 있는 동안에도 자는 조가 있으니, 침실에 조명을 두지 말고 햇빛이 드는 지표 근처에 침실을 만들지 마세요.
- **배고픔·꽉 찬 방광도 잠을 깨웁니다.** 휴식(밥) → 취침 → 목욕 순서를 그대로 두면 자기 전에 먹고, 일어나서 볼일을 봐서 안전해요.
- **올빼미형(Night Owl)** 은 하루 맨 오른쪽 3칸(21~23)에 모든 능력치 +3입니다. 오전조는 그 시간에 자니까 보너스를 버려요. **낮조·저녁조·새벽조**에 넣으세요.
- **아침형(Early Bird)** 은 맨 왼쪽 5칸(0~4)에 모든 능력치 +2입니다. 낮조는 그 시간에 쉬고 자니까 손해예요. **오전조·저녁조·새벽조**에 넣으세요.
- **휴식 칸을 늘리면 사기가 오릅니다.** 첫 칸을 뺀 휴식 칸 하나당 사기 +1, 최대 +4. 지금은 2칸이라 +1이에요. 사기가 모자라면 일 칸을 휴식으로 바꾸세요.
- 목욕과 휴식 사이가 **10칸 넘게 벌어지면** 하루에 화장실을 두 번 갑니다. 지금 일정처럼 붙여 두는 게 좋아요.
- 자는 동안 스태미나가 100%가 안 되면, 취침이 끝난 뒤 이어지는 일·목욕 칸까지 계속 잡니다 (휴식 칸에서는 깸). 그래서 취침 3칸이면 보통 충분해요.
- 복제체 3~4명일 땐 효과가 작습니다. **6명 이상**부터 확실히 체감돼요.

## 테라니아 적용 메모

- 포드가 맵 가운데라 **포드 바로 옆(서쪽)에 통로**를 세우고, 포드는 연구실 칸에 넣습니다.
- 포드 **오른쪽 아래 웅덩이**가 가장 가까우니 동쪽 아래(지하 1·2 동쪽 바깥)를 수조로 씁니다. 그래서 물 처리·세면실을 동쪽에 몰았어요.
- **왼쪽 아래 웅덩이**는 나중에 2번 수조나 오염수 저장으로 씁니다.
- 연구 전담 복제체는 포드층 연구실, 농사 담당은 지하 1 온실, 굴착 담당은 위 "처음 파는 순서"대로 파면 됩니다.
