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


3. **Extract** the ZIP archive into the quarantine folder:
   - **Open** File Explorer (or Explorer++).
   - **Navigate** to:
     ```
     C:\dev\quarantine\
     ```
   - **Locate** the file:
     ```
     ffmpeg-8.1-essentials_build.zip
     ```
   - **Right-click** the file `ffmpeg-8.1-essentials_build.zip`.
   - **Click** `Extract All...`.
   - In the “Files will be extracted to this folder” field, **ensure** the folder path is:
     ```
     C:\dev\quarantine\
     ```
   - **Click** `Extract` to begin extraction.
   - **Validate** the extraction results:
     1. **Confirm** that the extracted folder:
        ```
        ffmpeg-8.1-essentials_build
        ```
        is a **sibling** to the ZIP file:
        ```
        ffmpeg-8.1-essentials_build.zip
        ```
        inside:
        ```
        C:\dev\quarantine\
        ```
     2. **Open** the folder:
        ```
        ffmpeg-8.1-essentials_build
        ```
        and **confirm** that it contains files and subfolders directly.  
        The folder must **not** contain another nested folder named:
        ```
        ffmpeg-8.1-essentials_build
        ```

4. **Copy** the `ffmpeg.exe` file into the `bin\` directory:
   - **Open** File Explorer (or Explorer++).
   - **Navigate** to:
     ```
     C:\dev\quarantine\ffmpeg-8.1-essentials_build\bin\
     ```
     (This is where the actual `ffmpeg.exe` file is located. It is nested one level down.)
   - **Locate** the file:
     ```
     ffmpeg.exe
     ```
   - **Right-click** `ffmpeg.exe`.
   - **Click** `Copy`.
   - **Navigate** to the destination folder:
     ```
     C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\bin\
     ```
   - **Right-click** inside the folder.
   - **Click** `Paste`.

5. **Create** the validation folder inside the `4-ffmpeg-runner` directory:

   - **Open** File Explorer (or Explorer++).
   - **Navigate** to:
     ```
     C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\
     ```
   - If using File Explorer, **Right-click** in the files pane and **Click** `New` → `Folder`.
   - If using Explorer++, **Click**:
     ```
     Actions → New Folder
     ```
   - **Type**:
     ```
     validation
     ```
   - **Press** Enter.

6. **Copy** the validation `.trec` file into the `validation\` folder:

   - **Open** File Explorer (or Explorer++).
   - **Navigate** to:
     ```
     C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\
     ```
   - **Locate** the file:
     ```
     validation-tester.trec
     ```
     (This file is a pre‑generated, known‑good validation asset committed to the repo.)
   - **Right-click** `validation-tester.trec`.
   - **Click** `Copy`.
   - **Navigate** to:
     ```
     C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\validation\
     ```
   - **Right-click** inside the folder.
   - **Click** `Paste`.

7. **Run**:
   ```
   ffmpeg-runner.exe
   ```

8. When prompted, **select the folder**:
   ```
   C:\dev\catools-by-example\07-EX-LC-import-archive-into-windows-camtasia-for-editing\4-ffmpeg-runner\validation\
   ```

9. Wait for extraction to complete.  
    - Raw audio and raw video must appear in:
      ```
      C:\dev\catools-lc\ACTIVE\RAW\
      ```

10. **Verify** that the following files exist:
    - `validation-tester_RAW.wav`  
    - `validation-tester_VIDEO.mp4`

11. **Delete** the validation output files from:
    ```
    C:\dev\catools-lc\ACTIVE\RAW\
    ```

12. **Close** ffmpeg‑runner.

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
