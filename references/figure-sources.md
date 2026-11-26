# Figure reference sources

연구 그림의 역할·정보량·배치와 논문 발표의 편집 기준을 비교한다. 제출 규격은 작업 시 별도로 확인한다.

- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide): clarity와 단순성을 유지하고 불필요한 panel, color와 detail을 제거한다.
- [Nature research figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/): final size에서 readable text와 production-quality export를 검증한다.
- [PLOS Computational Biology — Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003833): message를 먼저 정하고 figure를 실제 data 또는 model과 연결한다.
- [IEEE Author Center — Resolution and Size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/): intended publication size와 raster resolution을 처음부터 고려한다.
- [Octo paper](https://octo-models.github.io/paper.pdf): overview와 architecture의 정보량을 분리하고, architecture를 text, token group과 arrow가 있는 flat technical graphic으로 설명하는 robotics reference다.
- [π0 paper](https://www.physicalintelligence.company/download/pi0.pdf): introduction figure에서 real robot-task evidence와 concise central method story를 결합하는 reference다.
- [Diffusion Policy paper](https://diffusion-policy.cs.columbia.edu/diffusion_policy_ijrr.pdf): method mechanism, observation, trajectory와 result를 역할별로 분리하는 robotics reference다.
- [RT-1 project and paper](https://robotics-transformer1.github.io/): real robot-task evidence와 labeled model/action explanation의 역할을 분리하는 robotics reference다.
- [OpenVLA project and paper](https://openvla.github.io/): real robot evaluation media와 model overview를 구분해 제시하는 VLA reference다.
- [ACT paper](https://tonyzhaozh.github.io/aloha/aloha.pdf): multi-view observation, state, latent와 action chunk 관계를 readable flat architecture로 설명하는 reference다.

## 논문 발표 슬라이드와 원고

2026-11-26에 아래 버전의 원문을 확인했다. [연구 발표 지침](../guides/research.md#논문-슬라이드와-발표-원고-편집)에 반영한 편집 판단의 출처다.

| 원문 | 확인한 방식과 적용 판단 |
| --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer/blob/a32f24407364c74c812b43c15926d638bee1e072/SKILL.md) | 내용 없이 중요성을 강조하거나 결론을 되풀이하는 문장을 찾고, 확인 가능한 사실로 다시 쓴 뒤 수치·인용·주장 강도를 대조한다. 발표자 노트와 본문 문장에 적용하며, 한국어 전문 용어와 문장부호는 문맥으로 판단한다. |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/SKILL.md) | 장마다 전달할 내용과 말할 내용을 함께 계획하고, 사진·비교·과정 등 내용의 형태에 맞춰 구성을 바꾼다. 슬라이드 흐름과 노트의 역할을 참고하며, 서체·색·장식과 출력 형식은 발표의 요구에 맞춘다. |
| [Anthropic PPTX skill](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/SKILL.md) | 현장 발표와 독립 열람 자료의 정보 밀도를 구분하고, 내용에 맞춘 레이아웃과 전체 슬라이드 렌더링 검수를 참고한다. 그림과 장식은 실제 설명에 필요한지 판단해 넣는다. |
| [dmmdea/humanize-presentations](https://github.com/dmmdea/humanize-presentations/blob/9510a5f5ae6c2689ffc0c4d77f68194c1eaee7f3/README.md) | 기존 PPT 교정에 특화된 참고다. 제목과 화면 요소가 같은 내용을 반복하는지, 발표자 설명이 화면에 그대로 올라와 있는지 확인한다. 과제가 요구하는 제목·절·비교 구조를 보존한다. |

공개 저장소의 예시는 편집 근거로 참고한다. 과제의 필수 내용, 사용자가 지정한 디자인, 논문의 수치와 출처를 우선한다.
