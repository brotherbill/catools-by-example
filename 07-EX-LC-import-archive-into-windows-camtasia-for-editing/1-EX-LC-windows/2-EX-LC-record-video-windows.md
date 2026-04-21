# Exercise – Record Video on Windows (Camtasia Recorder)
###### /caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/2-EX-LC-record_video-windows.md

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
   - Ignore the “Editor” part — the Recorder has **no editing capabilities**.

1. **Verify your inputs**  
   - Confirm the **correct screen** is selected.  
   - Confirm the **correct microphone** is selected.  
   - Decide whether to record **System Audio** (default: do not).

1. **Perform a microphone sanity check**  
   - Speak into the microphone.  
   - If the voice meter does not move, **close and re‑open Camtasia Recorder**.  
   - Camtasia will record video with **no audio** and will not warn you.  
   - This check prevents silent‑audio failures.

---

## Record the video and audio
1. Click the big red **REC** button.  
1. Wait for the **3‑second countdown**.  
1. Perform the lesson.  
1. Click **Stop** to end the recording.

1. **Save Recording** to:
   ```
   C:\quarantine\
   ```
   with filename:
   ```
   lesson_01.trec
   ```

   - This is intentional. `C:\quarantine\` is the safe holding area for unverified content.

1. Saving automatically opens **Camtasia Rev**.  
1. Click **Open in Editor** → launches **Camtasia Editor – Untitled Project**.

   - **STOP. Do not save. Do not edit.**  
   - Hands off keyboard and mouse.  
   - This machine does **not** perform editing.

---

## Save Camtasia internal assets
1. In Camtasia Editor:
   ```
   File → Export → Zipped Project...
   ```
1. Change folder path to:
   ```
   C:\quarantine\
   ```
1. Change filename to:
   ```
   lesson_01_RAW.zip
   ```
1. Click **Save**.

1. Exit Camtasia:
   ```
   File → Exit
   ```
1. When prompted:
   ```
   Save changes to Untitled Project.tscproj?
   ```
   Click **No**.

1. `C:\quarantine\` now contains:
   - `lesson_01.trec`  
   - `lesson_01_RAW.zip`

---

## Expand ZIP file and save assets in folders
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

1. You should now see:
   - `dots.tscshadervid`  
   - `lesson_01.trec`  
   - `lesson_01_RAW.tscproj`  
   - `lesson_01_RAW.zip`

---

## Import into Windows Camtasia (Editor)
1. Open **Windows Camtasia** → **STOP**.  
1. Click **New Project** → **STOP**.

1. **Drag**:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\lesson_01.trec
   ```
   into the **Media Bin**.

1. Right‑click `lesson_01.trec` → **Add to Timeline at Playhead**.  
1. Right‑click the clip on Track 1 → **Separate Audio and Video**.

1. Rename tracks:
   - Track 1 → **Video**  
   - Track 2 → **Audio**

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
1. Click **Save**.

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
1. Click **Export**.

1. When the exporter finishes:
   - Click **Open File Location**  
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
- This machine does **not** store `.tscproj` files.

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

   - Timestamp must be **GMT**.  
   - The **T** is literal.

1. Upload the ZIP to:
   ```
   caTools/LearningCurve/lesson_01/
   ```

---

## Backup C:\dev\catools-lc\ to C:\quarantine
1. Delete all contents of:
   ```
   C:\quarantine\
   ```
1. Copy:
   ```
   C:\dev\catools-lc\
   ```
   to:
   ```
   C:\quarantine\
   ```

---

## Delete contents of C:\dev\catools-lc\
1. Delete everything inside:
   ```
   C:\dev\catools-lc\
   ```
1. The Windows machine is now **stateless** and ready for the next recording.

---

## Summary
1. This workflow is intentionally different from typical Camtasia usage.  
1. It is designed to prevent silent failures and asymmetric synchronization issues.  
1. Standard folder names, standard filenames, Dropbox as source of truth, and a stateless recording machine ensure survivability.  
1. Every STOP point exists to prevent contamination.  
1. This is our NASA‑grade toggle‑switch discipline — deterministic, repeatable, operator‑grade.
