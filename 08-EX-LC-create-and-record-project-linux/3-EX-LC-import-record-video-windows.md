# Exercise – Import RAW Video on Windows (Dehydration Workflow)
###### /caTools/LearningCurve/3-EX-LC-import-raw-video-windows.md

This exercise covers the **Windows‑only** portion of the workflow.  
It begins after the Linux machine has uploaded the project ZIP to Dropbox.

Linux recording is handled in a separate exercise.

---

# Important Note About RAW Input Format
This workflow **expects the RAW video file to be in `.mkv` format**, produced by the Linux recording workflow.

If the Linux recording format changes in the future (e.g., `.mov`, `.webm`, `.mp4`),  
**update the import expectations inside this file — the filename of this MD file does not change.**

The dehydration workflow remains the same; only the RAW input format changes.

---

# Goals
1. **Download the project ZIP from Dropbox into the one correct Windows path**  
1. **Ensure the extraction target does not exist**  
1. **Extract the project into the deterministic Windows working folder**  
1. **Import the RAW `.mkv` into Camtasia**  
1. **Perform dehydration**  
1. **Perform VLC sanity checks**  
1. **Zip the project for upload**  
1. **Return Windows to a stateless condition**

---

# Download the ZIP from Dropbox (Windows side)
There is **only one correct Windows download location**.

### **Download must be saved to:**
```
C:\dev\catools-lc.zip
```

### Steps
1. Open your web browser on Windows.  
1. Go to:
   ```
   https://www.dropbox.com
   ```
1. Sign in.  
1. Navigate to:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
1. Click **Download** on:
   ```
   catools-lc.zip
   ```
1. When the browser prompts for a save location, choose:
   ```
   C:\dev\
   ```
1. Confirm the file is saved as:
   ```
   C:\dev\catools-lc.zip
   ```

If the browser auto‑downloads to **Downloads**, move the file manually to `C:\dev\` before continuing.

There is no other valid path.

---

# Ensure extraction target does NOT exist
Before extracting, confirm that the target folder is not already present.

1. Check for:
   ```
   C:\dev\catools-lc\
   ```
1. If it exists, **delete it completely**:
   - Right‑click → Delete  
   - Empty Recycle Bin  

The extraction target must be **absent** to prevent nested folders and contamination.

---

# Extract the project
1. Right‑click:
   ```
   C:\dev\catools-lc.zip
   ```
1. Choose:
   ```
   Extract All…
   ```
1. Extract to:
   ```
   C:\dev\catools-lc\
   ```

This folder is the **only** working directory for Windows dehydration.

---

# Ensure required subfolders exist
The extraction should produce:

```
C:\dev\catools-lc\ACTIVE\RAW\
C:\dev\catools-lc\ACTIVE\CAMTASIA\
C:\dev\catools-lc\ACTIVE\AUDIATE\
C:\dev\catools-lc\ACTIVE\OUT\
```

If any folder is missing, create it manually.

---

# Copy RAW MKV into CAMTASIA folder
**Do NOT cut.**  
The RAW folder must retain the original file.

1. Navigate to:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
1. **Copy**:
   ```
   lesson_01.mkv
   ```
1. **Paste** into:
   ```
   C:\dev\catools-lc\ACTIVE\CAMTASIA\
   ```

---

# Open Camtasia and prepare a clean workspace
1. Open **Camtasia**.  
1. Click:
   ```
   New Project
   ```
   - Do NOT open any existing project  
   - This ensures a clean, empty timeline  
1. In the top menu, click:
   ```
   Media → Media Bin
   ```
   - Ensures the Media Bin panel is visible  
   - If already visible, do nothing  

---

# Import the MKV into Camtasia
1. Drag:
   ```
   lesson_01.mkv
   ```
   from the CAMTASIA folder into the **Media Bin**.  
1. Drag the clip from the Media Bin onto **Track 1**.

*(This workflow assumes a single‑screen Windows setup.)*

---

# Separate audio and video
1. Right‑click the clip →  
   ```
   Separate Audio and Video
   ```
1. Track assignments:
   - Track 1 → video  
   - Track 2 → audio

---

# Rename tracks
1. Track 1 →  
   ```
   VIDEO_RAW
   ```
1. Track 2 →  
   ```
   AUDIO_RAW
   ```

---

# Export RAW WAV
1. Select the audio track (`AUDIO_RAW`).  
1. Export audio as:
   ```
   lesson_01.wav
   ```
1. Save to:
   ```
   C:\dev\catools-lc\ACTIVE\AUDIATE\
   ```

---

# Export RAW MP4
1. Hide the audio track.  
1. Export MP4 as:
   ```
   lesson_01.mp4
   ```
1. Save to:
   ```
   C:\dev\catools-lc\ACTIVE\OUT\
   ```

---

# Sanity check the MP4 (Windows)
1. **Right‑click**:
   ```
   C:\dev\catools-lc\ACTIVE\OUT\lesson_01.mp4
   ```
1. Choose:
   ```
   Open With → VLC Media Player
   ```
1. Play the first 5–10 seconds.

Confirm:
- Video exists  
- Audio exists  
- No corruption  
- No silence  
- No stutter  

If any issue is found, repeat the dehydration steps.

---

# Zip the entire project folder (Windows)
1. In File Explorer, right‑click:
   ```
   C:\dev\catools-lc\
   ```
1. Choose:
   ```
   Send to → Compressed (zipped) folder
   ```
1. Name the ZIP:
   ```
   catools-lc.zip
   ```

---

# Upload ZIP to Dropbox (Windows side)
1. Open your browser → https://www.dropbox.com  
1. Navigate to:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
1. Click:
   ```
   Upload → Files
   ```
1. Select:
   ```
   C:\dev\catools-lc.zip
   ```

---

# Tidy up the Windows machine
1. Delete:
   ```
   C:\dev\catools-lc\
   ```
1. Windows machine returns to **stateless**.

---

# End of Windows Exercise
This completes the Windows‑only dehydration workflow.  
Linux recording is handled in a separate exercise.
