# video-black-1s.mp4 — Validation Asset
###### C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/validation_source/video_black_1s.md

## Purpose
This asset provides a deterministic 1‑second black video for validating ffmpeg-runner behavior across platforms.

## Generation Command (to be executed later)
```
ffmpeg -f lavfi -i color=c=black:s=1280x720:d=1 -c:v libx264 -pix_fmt yuv420p video-black-1s.mp4
```

## Notes
- Output must be exactly 1.00 seconds.
- Resolution fixed at 1280x720 for predictable encoding behavior.
- Pixel format yuv420p ensures compatibility with all ffmpeg builds.
