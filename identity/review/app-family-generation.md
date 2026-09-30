# P5 source와 export

현재 사용 범위는 [identity 목록](../README.md), 선택 근거는 [review](app-family-review.md), 제작 규격은 [app-icons](../../guides/app-icons.md)를 따른다.

## Source

- [build_app_family_p4.py](../tools/build_app_family_p4.py)는 과거 후보 재현용이며 production export에 사용하지 않는다.
- [build_app_family_p5.py](../tools/build_app_family_p5.py): 실제 `64×64` RGB source. Image model을 사용하지 않는다.
- [promote_app_family_p5.py](../tools/promote_app_family_p5.py): `2048×2048` nearest-neighbor export와 metadata.
- Source와 master checksum은 [metadata](../approved/apps/metadata.json)에 둔다.
- 기준 이미지는 [approved base](../approved/gnaroshi-base-v1.png)이며 [source candidate](../candidates/07-cel-shaded.png)와 byte-identical하다.

## 명령

저장소 루트에서 실행한다. Python과 Pillow가 필요하다.

```bash
python3 identity/tools/build_app_family_p5.py --output-dir identity/review/candidates
python3 identity/tools/build_app_family_review.py --candidate-dir identity/review/candidates --output-dir identity/review
python3 identity/tools/promote_app_family_p5.py --output-dir <export-directory>
```

- Review PNG와 candidate binary는 Git-ignored 경로에 생성한다.
- Review sheet는 16/32/64/128/256px, light/dark, square/circular/approximate macOS mask를 검사한다.
- 현재 source의 renderer 의존성은 version pin이 없다. 기존 승인 master와 pixel·checksum 일치를 별도로 확인하고, 차이가 있으면 새 후보로 검토한다. 이 명령은 다른 application repository를 갱신하지 않는다.
