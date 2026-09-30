# 연구 figure 공통 규칙

논문·연구 figure의 제작·수정에 적용한다. 아래 표로 제작 방식을 선택하고 해당 상세 guide만 읽는다. 프로젝트별 figure spec에는 사용한 지침 commit, 주장, terminology, 크기와 출처를 기록한다.

## 제작 방식 선택

| 내용 | 제작 방식 | 상세 guide |
| --- | --- | --- |
| Architecture, pipeline, state, operator, 시간 관계, 정확한 label | Code·Figma·slide·raster editor로 직접 구성한 2D 도식 | [기술 도식](technical-figure-code.md) |
| 수치·통계·실험 결과 | 실제 데이터에서 생성한 plot | [기술 도식](technical-figure-code.md) |
| 관측 frame·장비·실행 화면 | 출처를 확인한 실제 asset | 이 문서의 실제 asset·공개 경계 |
| Cover·teaser·비기술적 concept | 생성 일러스트 허용 | [생성 일러스트](scientific-figure-generation.md) |

- 현재 요청의 역할, 범위, format과 산출물 수를 따른다. PNG/raster는 출력 형식이며 image model 사용 지시가 아니다.
- 작업에 기술 도식과 생성 일러스트가 모두 포함되면 두 상세 guide를 적용한다. 결과나 비교 sheet를 임의로 추가하지 않는다. 빠른 baseline과 아름다운 technical final을 함께 요청하면 같은 evidence map의 baseline과 polished constructed schematic을 만든다.
- Image-model-only technical sketch를 명시적으로 요청하면 정확한 text·connector·operator의 한계를 밝히고 publication-ready 결과로 보고하지 않는다. 추가 제작 방식이나 별도 결과는 요청 범위를 따른다.
- 기존 figure의 내용·배치·용어는 이번 작업에서 유효한 reference인지 확인한다. Rejected artifact는 실패 근거로만 사용한다.

## Brief와 정보량

제작 전에 역할, 한 문장 claim, panel별 질문, target venue/placement, physical size, format, 언어·용어, print/grayscale 조건과 사용할 코드·데이터·이미지 출처를 정한다.

| 역할 | 보여줄 내용 |
| --- | --- |
| Introduction | 하나의 핵심 기여를 가장 크게 두고, 이해에 필요한 input·baseline·output만 포함한다. Loss·shape·보조 경로는 claim에 필수일 때만 둔다. |
| Method·architecture | Panel마다 inference, training objective, temporal schedule 등 하나의 의미 계층을 설명한다. |
| Experiment·result | 실제 조건, 단위, 축, 집계 방법과 결과를 표시한다. |
| Cover·teaser | 문제나 물리적 활동을 소개하고 technical claim은 별도 실제 text 또는 도식에서 설명한다. |

서로 다른 역할을 한 panel에 압축하지 않는다. Main contribution과 supporting context를 같은 면적·대비로 만들지 않는다.

## 실제 asset과 공개 경계

- Observation, benchmark frame, screenshot과 qualitative result는 공식 공개 자료, 재현 가능한 dataset sample 또는 실제 실행 결과를 사용한다. Generated scene나 임의 수치를 evidence 자리에 넣지 않는다.
- Source URL/revision, dataset version, task/scene, frame index, 사용·재배포 범위를 기록한다. 편집용 원본과 crop을 분리한다.
- 실제 asset을 구하지 못했으면 의미가 명확한 text placeholder와 미완료 범위를 표시한다. Fake thumbnail을 만들지 않는다.
- 공개 전 private data와 재배포 조건을 확인한다. Figure-specific spec, 원문, 결과와 evidence map은 대상 프로젝트에 둔다.

## 크기와 출력

- Target venue의 현재 규격을 우선한다. 미정이면 single-column 약 89 mm, double-column 약 182 mm, color/grayscale 300 dpi 이상, black-and-white line art 600 dpi 이상을 작업 기준으로 사용한다.
- Pixel dimension은 최종 physical size와 dpi로 계산한다. 작은 이미지를 확대해 publication quality라고 보고하지 않는다.
- Paper figure의 비율은 column width와 내용으로 정한다. 16:9는 명시적인 slide·video·web placement에 사용한다.
- 실제 사용 크기, 160px thumbnail과 print용 grayscale에서 위계·글자·arrowhead·line style·색 구분을 확인한다. EN/KO가 있으면 가장 긴 label을 실제로 render한다.
- 요청 format을 우선한다. 미지정이면 high-resolution PNG와 용도별 source/provenance를 제공한다. Review용 preview는 검증에 사용하며 별도 결과 수를 임의로 늘리지 않는다.

## 시각 기준

프로젝트의 승인된 token이 없으면 다음을 사용한다.

| 역할 | 색 |
| --- | --- |
| Page / figure surface | `#f4f5f2` / `#fcfdfb` |
| Primary / secondary / muted ink | `#18201c` / `#3f4943` / `#5f6b63` |
| Quiet / strong border | `#d5dbd4` / `#aab5ac` |
| Primary / soft green | `#126954` / `#dcebe5` |
| Identity teal / orange | `#3fa6a0` / `#e88945` |

- Neutral을 주 면적으로 쓰고 green은 주 경로, teal/orange는 작은 강조에 제한한다. 생성 장면의 모든 물체를 이 palette로 칠하지 않는다.
- System sans-serif, sentence case와 절제된 weight를 사용한다. Monospace는 변수·짧은 index에 제한하고 일반 label은 최종 배치에서 약 8pt 이상을 기준으로 검증한다.
- Whitespace로 묶고 필요한 경계만 선으로 표시한다. Panel letter는 작게 두고 caption을 반복하는 slogan·nested card·pill·장식 badge를 넣지 않는다.
- Technical panel은 flat 2D로 구성한다. 실제 3D geometry·trajectory·measurement를 표현할 때만 3D를 사용한다. Module·tensor·operator를 cube, portal, rail, pipe, tank나 기계 부품으로 바꾸지 않는다.
- Mascot, logo watermark, full-image pixelation, blur, bevel, glass, neon과 장식 회로를 넣지 않는다. 형태와 간격은 의미를 설명해야 한다.

## 최종 검토

- 먼저 의미와 출처를 검증한다. 잘못된 artifact 유형, 가짜 evidence, 빠진 disclosure, pseudo-text와 미검증 기술 관계가 있으면 시각 평가 전에 수정한다.
- Required text는 실제 조판된 label·수식·축·legend로 넣는다. Blank plate, pseudo-text 또는 caption으로 의미 누락을 보완하지 않는다.
- 한 문장 claim 또는 broad subject가 2초 안에 보이고, 최종 배치에서 겹침·잘림 없이 읽혀야 한다.
- 나중에 reject된 후보는 현재 status·날짜·이유·대체 방향을 후보 기록에 표시한다. 과거 점수·추천·승인 기록은 history로 남기되 현재 사용 승인을 뜻하지 않는다.
- 새 재사용 규칙은 해당 guide에 갱신하고, 대상 output 폴더에 별도 versioned guideline을 만들지 않는다.

출처 비교는 [figure sources](../references/figure-sources.md), 원격 파일·MCP 연결은 [mcp/README.md](../mcp/README.md)를 따른다.
