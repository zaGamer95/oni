# 산소미포함 생존 노트

산소미포함(Oxygen Not Included) 개인 가이드 사이트입니다. 내 플레이 참고용이자 지인 공유용.

배포 주소: https://wonbo.site/oni/

## 배포

`main`에 머지(푸시)하면 `.github/workflows/pages.yml`이 Jekyll로 빌드해서 GitHub Pages에 올립니다.
레포 Settings → Pages → Source는 **GitHub Actions**로 두면 됩니다. 진행 상황은 Actions 탭에서 볼 수 있어요.

## 구조

```
index.md                 홈
guide/00-start.md        게임 시작 설정 (일반/Spaced Out → 모드 → DLC → 행성 마법사)
guide/01-first-cycles.md 첫 5사이클 체크리스트
guide/02-asteroids.md    지형별 시작법
guide/03-build-order.md  단계별 건설 순서
guide/04-biome-expansion.md  바이옴 확장 타이밍
guide/05-build-specs.md  건축 규격 & 팁
guide/06-sustainability.md   장기 평형 설계 (+계산기)
guide/07-numbers.md      수치 치트시트
appendix/sustainability-context.md  부록 A: 지속 가능성 컨텍스트 (수치·설계 총정리, Claude가 먼저 읽는 파일)
CLAUDE.md                Claude용 안내 (사이트에 노출 안 됨)
_sources/                옛 가이드 원본 보관 (사이트에 노출 안 됨)
_layouts/default.html    공통 레이아웃 (사이드바 목차 자동 생성)
_data/media.yml          DLC 이미지·인게임 아이콘 외부 주소 (깨지면 여기만 수정)
_data/nav_groups.yml     사이드바 그룹 (시작하기/초반/중반/후반/사례/참고 자료/부록)
assets/css/style.css     ONI 분위기 테마
assets/js/main.js        모바일 메뉴 + 계산기 (게임 수치는 여기 K 객체에)
```

## 글 추가·수정하기

- 새 페이지: `guide/` 에 `.md` 파일을 만들고 맨 위에 아래 머리말을 붙이면 사이드바에 자동으로 들어갑니다.

  ```yaml
  ---
  title: 페이지 제목
  nav_title: 사이드바에 보일 짧은 제목
  nav_order: 8        # 목차 순서
  permalink: /guide/my-page/
  description: 한 줄 설명
  ---
  ```

- 강조 상자: 인용문(`>`) 바로 다음 줄에 `{: .tip}`, `{: .warn}`, `{: .danger}`, `{: .heat}` 중 하나를 붙입니다.
- 건물 이름은 `한글 이름 (English)` 형식으로 통일합니다.

## 옛 가이드 자료 합치기

옛 자료는 `_sources/` 폴더에 원본 그대로 넣어두세요. 밑줄로 시작하는 폴더라 사이트에는 안 보입니다. 이후 내용별로 `guide/` 페이지에 나눠 합칩니다.

## 로컬 미리보기 (선택)

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000/oni/
```
