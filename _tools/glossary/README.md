# 공식 한글 용어집 도구

- `build.py <po> [build]` → `_data/glossary_ko.yml` 생성. `.po`는 게임 설치 폴더 `StreamingAssets/strings/strings_preinstalled_ko_klei.po` (Klei 공식 한국어). 저작권 때문에 원본 .po는 레포에 넣지 않음.
- `apply_fixes.py <tsv>` → 틀린 이름 → 공식 이름 일괄 치환. 3번째 칸(영어)이 있으면 `틀린 (English)` 짝만 고침.
- `fix_particles.py <tsv>` → 치환 뒤 조사(을/를, 은/는, 이/가, 과/와, 으로/로) 맞춤.
- `fixes_2026-11-28.tsv` → 첫 정리 때 쓴 치환표 (기록용).
