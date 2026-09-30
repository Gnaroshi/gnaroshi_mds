# 이미지 제작과 screenshot

이미지 제작·편집·export와 제품 screenshot 사용에 적용한다.

## 형식

- 별도 vector 요청이 없으면 full-color image generation, identity, illustration과 scene은 raster로 만든다. PNG·WebP·AVIF·JPEG master를 보존하고 platform에 맞춰 export한다.
- SVG·EPS·AI·vector PDF를 full-color 생성 이미지의 기본 산출물로 만들지 않는다. PNG라는 요청만으로 image-generation model을 선택하지 않는다.
- 기능·메뉴바 icon은 [app-icons](app-icons.md)의 vector/template 규칙을 따른다.
- 논문·연구 figure는 [research-figures](research-figures.md), 앱·웹 identity는 [app-icons](app-icons.md)와 [asset 목록](../identity/README.md)을 따른다.

## 실제 application screenshot

- 실제 executable 또는 해당 repository UI component가 렌더링한 화면을 사용한다.
- Host, private path, paper title, transcript와 process argument 등 운영 data를 공개하지 않는다.
- Privacy-safe demo fixture·capture harness는 허용하되 화면과 caption에 demo임을 표시한다. 실제 연구 성과·운영 activity로 제시하지 않는다.
- Empty·setup-only·error-only 화면이 핵심 user scenario를 설명하지 못하면 production project image로 쓰지 않는다.
- Source commit, dirty state, fixture source, capture command와 redaction 범위를 대상 프로젝트에 기록한다.
- Crop, responsive encoding과 neutral letterbox는 허용하되 plausible value나 fake terminal output을 합성하지 않는다.
- 실제 screenshot·사진·도식·본문에 pixelation filter를 적용하지 않는다.
