# ffmpeg-runner Validation Behavior
###### C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/ffmpeg_runner_validation_behavior.md

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

### 1. File Existence Check

1. ffmpeg-runner must confirm that the input file exists before performing any operation.
2. If the file does not exist, ffmpeg-runner must:
   - exit with code 2  
   - write a deterministic error message to stdout  
   - perform no additional actions  
3. The error message must follow this exact format:

   ```
   ERROR: Input file not found: <filename>
   ```

4. No output files may be created when this condition occurs.

## Notes
- This file will be expanded as behavior is formalized.
- All behavior must be deterministic and cross-platform consistent.

### 2. Deterministic Metadata Extraction

1. After confirming the input file exists, ffmpeg-runner must extract metadata using a deterministic ffprobe command.
2. The command must follow this exact structure:

   ```
   ffprobe -v error -show_entries format=duration:stream=width,height -of json <filename>
   ```

3. The output must be valid JSON and must include:
   - `duration`
   - `width`
   - `height`
4. ffmpeg-runner must parse the JSON and store the values internally.
5. If metadata extraction fails, ffmpeg-runner must:
   - exit with code 3  
   - write a deterministic error message to stdout  
   - perform no additional actions  
6. The error message must follow this exact format:

   ```
   ERROR: Unable to extract metadata: <filename>
   ```

### 3. Deterministic Duration Validation

1. After extracting metadata, ffmpeg-runner must validate that the duration of the input file is exactly 1.00 seconds.
2. Duration must be compared using a tolerance of ±0.01 seconds to account for encoder rounding.
3. If the duration is outside the allowed tolerance, ffmpeg-runner must:
   - exit with code 4  
   - write a deterministic error message to stdout  
   - perform no additional actions  
4. The error message must follow this exact format:

   ```
   ERROR: Invalid duration: <filename> (expected 1.00s)
   ```

5. If the duration is valid, ffmpeg-runner must continue to the next validation step.

### 4. Deterministic Resolution Validation

1. ffmpeg-runner must validate that the input file resolution matches the expected dimensions for the validation asset.
2. For both `video-black-1s.mp4` and `video-white-1s.mp4`, the required resolution is:
   - width: 1920  
   - height: 1080
3. If the resolution does not match exactly, ffmpeg-runner must:
   - exit with code 5  
   - write a deterministic error message to stdout  
   - perform no additional actions  
4. The error message must follow this exact format:

   ```
   ERROR: Invalid resolution: <filename> (expected 1920x1080)
   ```

5. If the resolution is valid, ffmpeg-runner must continue to the next validation step.

### 5. Deterministic Color Validation

1. ffmpeg-runner must validate that the dominant color of the input file matches the expected color for the validation asset.
2. For `video-black-1s.mp4`, the expected RGB value is:
   - R: 0  
   - G: 0  
   - B: 0
3. For `video-white-1s.mp4`, the expected RGB value is:
   - R: 255  
   - G: 255  
   - B: 255
4. ffmpeg-runner must extract a single representative pixel using this exact ffmpeg command:

   ```
   ffmpeg -v error -i <filename> -vf "scale=1:1" -f rawvideo -pix_fmt rgb24 -
   ```

5. The resulting 3-byte output must be compared directly to the expected RGB triplet.
6. If the color does not match exactly, ffmpeg-runner must:
   - exit with code 6  
   - write a deterministic error message to stdout  
   - perform no additional actions  
7. The error message must follow this exact format:

   ```
   ERROR: Invalid color: <filename> (expected <R>,<G>,<B>)
   ```

8. If the color is valid, ffmpeg-runner must continue to the next validation step.

### 6. Deterministic Logging Behavior

1. ffmpeg-runner must produce a deterministic log entry for every major validation step.
2. Each log entry must follow this exact format:

   ```
   [OK] <step-name>: <filename>
   ```

3. The following step-names must be logged in this order:
   - `file-exists`
   - `metadata-extracted`
   - `duration-valid`
   - `resolution-valid`
   - `color-valid`
4. If a step fails, ffmpeg-runner must not log an `[OK]` entry for that step.
5. No timestamps may be included in logs, as they break determinism.
6. Logs must be written to stdout only — no files may be created.

### 7. Deterministic Exit Behavior

1. ffmpeg-runner must exit with a deterministic exit code based on the final validation outcome.
2. The following exit codes are reserved and must be used exactly as defined:

   - `0` — all validation steps passed  
   - `2` — input file not found  
   - `3` — metadata extraction failed  
   - `4` — invalid duration  
   - `5` — invalid resolution  
   - `6` — invalid color  

3. No other exit codes may be used for validation behavior.
4. ffmpeg-runner must not perform any additional actions after determining the exit code.
5. ffmpeg-runner must not produce any output after writing the final error message or final `[OK]` log entry.
6. Exit behavior must be identical across all platforms.

---

## Doctrine Freeze — Validation Behavior (v1.0)

The validation doctrine is now frozen.  
No additional rules, edits, or behavioral changes may be introduced without incrementing the doctrine version number and documenting the change in `chat.md`.

This freeze guarantees:
- deterministic behavior  
- reproducible validation  
- stable implementation  
- predictable E2E testing  
- zero drift across platforms  

Version: 1.0  
Status: FROZEN  
