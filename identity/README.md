# Identity assets

## 현재 사용

| 대상 | Source | 상태 |
| --- | --- | --- |
| 기본 identity와 웹 대표 mark의 reference | [gnaroshi-base-v1.png](approved/gnaroshi-base-v1.png), [metadata](approved/metadata.json) | 2026-07-12 승인. 전체 얼굴 보존 |
| 6개 application role icon | [approved/apps metadata](approved/apps/metadata.json)의 `apps` | 2026-07-14 승인 P5 production masters |
| `gnaroshi-main-p5` / `gnaroshi-main-v1.png` | [기존 export](approved/apps/gnaroshi-main-v1.png) | 과거 승인 이력만 보존. 귀·visor 축약형이므로 현재 웹·global 대표 identity에 사용 금지 |

Master와 source candidate는 덮어쓰거나 삭제하지 않는다. 새 derivative는 [icon 규칙](../guides/app-icons.md)에 따라 만들며 승인되지 않은 후보로 production master를 교체하지 않는다. 웹 full-face pixel master는 아직 이 목록에 등록돼 있지 않다.

## 출처와 재현

- [2020 origin](reference/gnaroshi-origin-2020.jpeg): 사용자가 만든 `gnar + garosh → gnaroshi` reference. 큰 귀, 날카로운 눈, 이빨과 orange/teal 대비를 계승한다.
- [후보 목록](candidates/README.md): 생성 style 탐색. 선택된 `07-cel-shaded.png`는 approved base와 byte-identical하다.
- [P5 선택 기록](review/app-family-review.md): 승인일과 작은 크기의 한계.
- [Application metadata](approved/apps/metadata.json): production 목록, `historicalAssets`, source/master checksum·크기·target. `exportedAt`은 최초 승인 export 날짜이며 재검증 날짜로 덮어쓰지 않는다.

특정 게임의 logo·UI·trademark·원본 asset을 직접 복사하지 않는다.

## P5 재생성

- [build_app_family_p5.py](tools/build_app_family_p5.py)는 `64×64` RGB source를 구성한다. Image model을 사용하지 않는다.
- [promote_app_family_p5.py](tools/promote_app_family_p5.py)는 `2048×2048` nearest-neighbor master와 metadata를 출력한다.
- [build_app_family_p4.py](tools/build_app_family_p4.py)는 과거 후보 재현용이며 production export에 사용하지 않는다.

Python과 Pillow가 필요하다. 저장소 루트에서 실행하며 review PNG와 candidate binary는 Git-ignored 경로에 생성한다.

```bash
python3 identity/tools/build_app_family_p5.py --output-dir identity/review/candidates
python3 identity/tools/build_app_family_review.py --candidate-dir identity/review/candidates --output-dir identity/review
identity_export_dir="$(mktemp -d)"
python3 identity/tools/promote_app_family_p5.py --output-dir "$identity_export_dir"
```

- [Review 도구](tools/build_app_family_review.py)는 16/32/64/128/256px, light/dark, square/circular/approximate macOS mask를 비교한다.
- Renderer 의존성의 version pin이 없어 재생성 결과가 기존 master와 pixel 또는 파일 bytes에서 다를 수 있다. 별도 export 디렉터리에서 source/master checksum과 크기를 metadata에 대조하고 차이가 있으면 새 후보로 검토한다.
- Production에는 저장된 승인 master를 사용한다. 각 application은 master를 자기 repository에 복사하고 platform asset을 local에서 만든다. 위 명령은 다른 application repository를 갱신하지 않는다.
