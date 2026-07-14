# Approved Gnaroshi application identity masters

The PNG files in this directory are the owner-approved P5 production masters selected on 2026-07-14. They are deterministic nearest-neighbor exports from the 64px `hero-instrument` sources in `identity/tools/build_app_family_p5.py`.

Applications copy the relevant master into their own repository and generate platform assets locally. Builds must not download these files from `gnaroshi_mds`.

Refresh and verify the canonical files with:

```bash
python3 identity/tools/promote_app_family_p5.py \
  --output-dir identity/approved/apps
```

`metadata.json` records the source candidate, source and master SHA-256 values, export date, dimensions and target platforms. The full-color masters are not menu-bar or toolbar icons.
