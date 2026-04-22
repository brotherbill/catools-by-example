# Exercise – Record Video on Windows (Camtasia Recorder)
###### C:/dev/caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing\1-EX-LC-windows\2_EX_LC_record_video_windows.md

## Goals
1. Prepare the Windows recording machine.  
1. Record the video and audio using Camtasia Recorder.  
1. Save recording assets using standardized folders and filenames.  
1. Dehydrate assets into a clean, portable ZIP snapshot.  
1. Upload the ZIP to Dropbox (browser only).  
1. Return the Windows machine to a clean, stateless condition.

---

## Prepare for recording
1. **Open Camtasia Recorder**  
   - The window title is **Camtasia Editor Recorder**.  
   - Ignore the “Editor” part — the Recorder has no editing capabilities.

1. **Verify your inputs**  
   - Confirm the correct screen is selected.  
   - Confirm the correct microphone is selected.  
   - Decide whether to record System Audio (Off to avoid Windows notification sounds).

1. **Perform a microphone sanity check**  
   - Speak into the microphone.  
   - If the voice meter does not move, **close and re‑open Camtasia Recorder**.  
   - Camtasia will record video with no audio and will not warn you.  
   - This check prevents silent‑audio failures.

---

## Record the video and audio
1. **Click** the big red **rec** button.  
1. Wait for the **3‑second countdown**. Pause briefly to allow the recording pipeline to stabilize before beginning.  
1. Perform the lesson.  
1. **Click** the big red **rec** button again to stop the recording.

1. **Save Recording** to:
   ```
   C:\quarantine\
   ```
   with filename:
   ```
   lesson_01.trec
   ```
1. **Click** Save.

1. Saving automatically opens Camtasia Rev.  
1. **Click** Open in Editor → launches **Camtasia Editor – Untitled Project**.

   - **STOP. Do not save. Do not edit.**  
   - Hands off keyboard and mouse.  
   - This machine does not perform editing.

---

## Save Camtasia internal assets
1. In Camtasia Editor:
   ```
   File → Export → Zipped Project...
   ```
1. On the “Export Project As Zip” dialog, change the folder path to:
   ```
   C:\quarantine\
   ```
1. Change File name to:
   ```
   lesson_01_RAW.zip
   ```
1. **Click** Save.

1. Exit Camtasia:
   ```
   File → Exit
   ```
1. When prompted:
   ```
   Save changes to Untitled Project.tscproj?
   ```
   Videographers are conditioned to click Yes when asked to save changes. In this workflow, clicking No is intentional and required. Follow this step exactly as written.
   **Click** No.

1. Open File Explorer (or Explorer++), navigate to:
   ```
   C:\quarantine\
   ```

1. You should see exactly the following two files:
   - `lesson_01.trec`
   - `lesson_01_RAW.zip`

1. Confirm that **only** these two files are present and no others.

---

## Expand ZIP file and save assets in folders
1. Open File Explorer (or Explorer++), navigate to:
   ```
   C:\quarantine\
   ```

1. **Cut**:
   ```
   C:\quarantine\lesson_01_RAW.zip
   ```
   **Paste** into:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```

1. **Expand** the ZIP inside the same folder:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
   - Right‑click `lesson_01_RAW.zip`  
   - Select **Extract All...**  
   - In the “Files will be extracted to this folder” field, **delete the trailing `\lesson_01_RAW`**  
   - Ensure the destination is exactly:
     ```
     C:\dev\catools-lc\ACTIVE\RAW\
     ```
   - **Click** Extract

1. You should now see:
   - `dots.tscshadervid`  
   - `lesson_01.trec`  
   - `lesson_01_RAW.tscproj`  
   - `lesson_01_RAW.zip`

---

## Extract raw audio and video (ffmpeg‑runner)
1. **Run**:
   ```
   ffmpeg-runner.exe
   ```
1. When prompted, **select the folder**:
   ```
   C:\dev\catools-by-example\
   ```
1. Wait for extraction to complete.  
   - Raw audio and raw video will appear automatically in:
     ```
     C:\dev\catools-lc\ACTIVE\RAW\
     ```

---

## Import into Windows Camtasia (Editor)
1. **Open** Windows Camtasia → **STOP**.  
1. **Click** New Project → **STOP**.

1. **Drag**:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\lesson_01.trec
   ```
   into the Media Bin.

1. Right‑click `lesson_01.trec` → **Add to Timeline at Playhead**.  
1. Right‑click the clip on Track 1 → **Separate Audio and Video**.

1. Rename tracks:
   - Track 1 → Video  
   - Track 2 → Audio

---

## Export audio track to ACTIVE\RAW
1. ```
   Export → Export Audio Only...
   ```
1. Folder path:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
1. Filename:
   ```
   lesson_01_RAW.wav
   ```
1. **Click** Save.

---

## Export video as MP4
1. ```
   Export → Local File...
   ```
1. Filename:
   ```
   lesson_01_VIDEO.mp4
   ```
1. File Type:
   ```
   MP4 (Recommended)
   ```
1. Save Location:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
1. **Click** Export.

1. When the exporter finishes:
   - **Click** Open File Location  
   - Confirm the MP4 exists in the correct folder.

1. **Play 5–10 seconds** in your default player.  
   - Must see video.  
   - Must hear audio.  
   - This catches silent‑mic or wrong‑screen failures.

---

## Close Windows Camtasia
1. ```
   File → Exit
   ```
1. When prompted to save:
   ```
   No
   ```

- Saving here contaminates the workflow.  
- This machine does not store `.tscproj` files.

---

## Zip and save to Dropbox
1. Zip all contents of:
   ```
   C:\dev\catools-lc\
   ```
   into:
   ```
   catools-lc_lesson_01_YYYY-MM-DDTHHMMSS.zip
   ```

   - Timestamp must be GMT.  
   - The T is literal.

1. Upload the ZIP to:
   ```
   caTools/LearningCurve/lesson_01/
   ```

---

## Backup C:\dev\catools-lc\ to C:\quarantine
1. **Delete** all contents of:
   ```
   C:\quarantine\
   ```
1. **Copy**:
   ```
   C:\dev\catools-lc\
   ```
   to:
   ```
   C:\quarantine\
   ```

---

## Delete contents of C:\dev\catools-lc\
1. **Delete** everything inside:
   ```
   C:\dev\catools-lc\
   ```
1. The Windows machine is now stateless and ready for the next recording.

---

## Summary
1. This workflow is intentionally different from typical Camtasia usage.  
1. It is designed to prevent silent failures and asymmetric synchronization issues.  
1. Standard folder names, standard filenames, Dropbox as source of truth, and a stateless recording machine ensure survivability.  
1. Every STOP point exists to prevent contamination.  
1. This is our NASA‑grade toggle‑switch discipline — deterministic, repeatable, operator‑grade.
