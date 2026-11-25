# CLAUDE.md

Korean Oxygen Not Included (산소미포함) guide site for W's own play and for sharing with friends. Jekyll, deployed by GitHub Actions to https://wonbo.site/oni/ on every push to `main`.

## Read first

- **`appendix/sustainability-context.md`**: the project's context file. Per-dupe needs, crop/critter/generator numbers, stable farm/ranch designs, closed loops, W's current run, and the 2026 patch log (last checked: U60-763796, 2026-11-19). Answer gameplay questions from it, and update it, including its patch log, when numbers change.
- When a number differs, the in-game tooltip wins, then the wiki (`https://oxygennotincluded.wiki.gg/wiki/<Page>?action=raw`), then this file.

## Conventions

- The guide is written for **Spaced Out!**. Early/mid/late are defined by research: mid starts at Materials Science Research, late starts at Data Analysis Research.
- Call them "복제체", never 듀플리컨트. Use the Korean game UI terms (와이어, 파이프, 기체 파이프, 환경 특수복). Write names as `한글 (English)`; the English name is the reliable key.
- Pages live in `guide/*.md` with front matter `nav_order` / `nav_num` / `nav_group` / `permalink`. Sidebar groups are in `_data/nav_groups.yml`. Callouts use a blockquote plus `{: .tip|.warn|.danger|.heat}`.
- Top bar has two sections, 가이드 / 사례. Each group in `_data/nav_groups.yml` has `section: guide|case`; the sidebar and prev/next pager show only the current section. Case pages live at `/guide/case/...` with the hub at `/guide/case/` (`guide/case-index.md`); a new case gets its own `section: case` group, and chapters use `nav_key` / `nav_parent`.
- The top-right version badge comes from `_data/versions.yml`. Site default is `game_version` in `_config.yml`; a page (e.g. a case played on an older patch) overrides it with its own `game_version:` front matter key.
- Images: official Klei art and in-game icons with credit. No hand-drawn SVG illustrations. Generated tile-scale plan diagrams are fine.
- Reply to W in Korean.
