# 4‑EX‑LC‑ffmpeg‑runner — Extract Raw Audio and Video
###### C:/dev/caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\4-EX-LC-ffmpeg-runner.md

### *Operator Exercise — LearningCurve Pipeline*  
### *Do not modify. Do not improvise.*

---

## Purpose
Use **ffmpeg‑runner.exe** to extract raw audio and raw video from the `.trec` file after expanding `lesson_XX_RAW.zip`.

This step occurs **immediately after** the ZIP expansion and **before** importing anything into Camtasia Editor.

---

## Install ffmpeg Binary Assets (One-Time Setup)

1. **Create** the folder:
   ```
   C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\bin\
   ```

2. **Download** this exact file from the official ffmpeg builds page:
   - Open: https://www.gyan.dev/ffmpeg/builds/
   - In the “Release builds” section, locate the file named:
     ffmpeg-8.1-essentials_build.zip
   - **Click directly on the text `ffmpeg-8.1-essentials_build.zip` to begin the download.**
   - When the browser prompts for a download location, **navigate to this exact folder**:
     C:\dev\quarantine\
   - When the browser prompts for a file name, **ensure the file name is exactly**:
     ffmpeg-8.1-essentials_build.zip
   - **Click the `Save` button** to start the download.
   - Do not download “full”, “full-shared”, “git”, “7z”, or other installer variants.
   - **Open File Explorer (or Explorer++)**, navigate to:
     C:\dev\quarantine\
     and confirm that the file **ffmpeg-8.1-essentials_build.zip** is present.


3. **Extract** the ZIP archive to a temporary location.

4. **Copy** the following file into the `bin\` directory:
   ```
   ffmpeg.exe
   ```

5. **Verify** that the file exists:
   ```
   C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\bin\ffmpeg.exe
   ```

6. **Confirm** that the validation folder exists:
   ```
   C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\validation\
   ```

7. **Confirm** that the validation `.trec` file exists:
   ```
   validation-tester.trec
   ```

8. **Run**:
   ```
   ffmpeg-runner.exe
   ```

9. When prompted, **select the folder**:
   ```
   C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\validation\
   ```

10. Wait for extraction to complete.  
    - Raw audio and raw video must appear in:
      ```
      C:\dev\catools-lc\ACTIVE\RAW\
      ```

11. **Verify** that the following files exist:
    - `validation-tester_RAW.wav`  
    - `validation-tester_VIDEO.mp4`

12. **Delete** the validation output files from:
    ```
    C:\dev\catools-lc\ACTIVE\RAW\
    ```

13. **Close** ffmpeg‑runner.

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
