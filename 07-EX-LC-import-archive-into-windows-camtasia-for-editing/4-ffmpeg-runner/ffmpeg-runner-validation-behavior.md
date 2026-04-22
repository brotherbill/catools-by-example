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

