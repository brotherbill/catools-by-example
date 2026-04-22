# ffmpeg-runner Validation Behavior
###### C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/ffmpeg-runner-validation-behavior.md

## Purpose
This document defines the expected behavior of ffmpeg-runner when processing known, deterministic validation assets.

## Validation Inputs
- `video-black-1s.mp4`
- `video-white-1s.mp4`

## Expected Behavior (to be expanded)
1. ffmpeg-runner must detect the input file.
2. ffmpeg-runner must extract metadata deterministically.
3. ffmpeg-runner must log the operation in a reproducible format.
4. ffmpeg-runner must produce no side effects outside the output folder.
5. ffmpeg-runner must exit with code 0 on success.

## Notes
- This file will be expanded as behavior is formalized.
- All behavior must be deterministic and cross-platform consistent.
