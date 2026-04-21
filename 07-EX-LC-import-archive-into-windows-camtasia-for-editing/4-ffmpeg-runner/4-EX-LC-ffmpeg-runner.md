# 4‑EX‑LC‑ffmpeg‑runner — Extract Raw Audio and Video
###### /caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/4-EX-LC-ffmpeg-runner.md

### *Operator Exercise — LearningCurve Pipeline*  
### *Do not modify. Do not improvise.*

---

## Purpose
Use **ffmpeg‑runner.exe** to extract raw audio and raw video from the `.trec` file after expanding `lesson_XX_RAW.zip`.

This step occurs **immediately after** the ZIP expansion and **before** importing anything into Camtasia Editor.

---

## Steps

1. **Run**:
   ```
   ffmpeg-runner.exe
   ```

2. When prompted, **select the folder**:
   ```
   C:\dev\catools-by-example\
   ```

3. Wait for extraction to complete.  
   - Raw audio and raw video will appear automatically in:
     ```
     C:\dev\catools-lc\ACTIVE\RAW\
     ```

4. **Close** ffmpeg‑runner.

---

## Expected Results
The following files must now exist in:

```
C:\dev\catools-lc\ACTIVE\RAW\
```

- `lesson_XX_RAW.wav`  
- `lesson_XX_VIDEO.mp4`

If these files are present, continue to the next exercise step.

---

## STOP Conditions
- Do **not** open PowerShell.  
- Do **not** run ffmpeg manually.  
- Do **not** modify filenames.  
- Do **not** move files manually.  
- Do **not** re‑run extraction unless instructed.

---

## Completion
Once both files are present, proceed to:

```
2-EX-LC-record_video-windows.md → Import into Windows Camtasia (Editor)
```
