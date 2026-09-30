# Application masters

[metadata.json](metadata.json)의 `apps`는 2026-07-14 승인된 6개 P5 production master다. `historicalAssets`의 `gnaroshi-main-v1.png`는 당시 승인 이력 보존용이며 현재 웹·global 대표 identity에 사용하지 않는다. 현재 용도는 [identity 목록](../../README.md)을 따른다.

Master는 `64×64` deterministic source의 `2048×2048` nearest-neighbor export다. 각 application은 master를 자기 repository에 복사하고 platform asset을 local에서 만든다.

Source 재실행은 저장소 루트에서 별도 디렉터리로 출력한다. Pillow·PNG encoder 버전이 고정돼 있지 않아 기존 master와 pixel 또는 파일 bytes가 달라질 수 있다. Production에는 저장된 승인 master를 사용하며 재생성 결과로 바로 덮어쓰지 않는다.

```bash
python3 identity/tools/promote_app_family_p5.py --output-dir <export-directory>
```

`sourceSha256`, `masterSha256`, 크기와 target을 metadata와 대조한다. `exportedAt`은 최초 승인 export 날짜이며 재검증 날짜로 덮어쓰지 않는다.
