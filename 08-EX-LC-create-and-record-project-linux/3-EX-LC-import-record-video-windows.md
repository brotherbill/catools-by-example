# /caTools/LearningCurve/3-EX-LC-import-raw-video-windows.md

This exercise covers the **Windows‑only** portion of the workflow.  
It begins after the Linux machine has uploaded the **project ZIP** to Dropbox.

Windows receives **only the ZIP file**:

```
catools-lc.zip
```

This ZIP contains the entire Linux‑side project folder (`catools-lc/`) at the correct level.  
Its internal contents — including the MKV, the remuxed MP4, and all scaffolding — are **Linux‑side concerns** and are **not part of the Windows workflow**.

---

# Goals
1. Download the project ZIP from Dropbox  
1. Expand the ZIP into the deterministic Windows project folder  
1. Verify the Windows folder structure  
1. Import the RAW `.mp4` into Camtasia  
1. Perform dehydration  
1. Perform VLC sanity checks  
1. Zip the project for upload  
1. Return Windows to a stateless condition

---

# Download the project ZIP from Dropbox (Windows side)
There is **only one correct Windows download location**.

### **Download must be saved to:**
```
C:\dev\
```

### Steps
1. Open **Dropbox in a web browser**.  
1. In **Dropbox**, **Navigate** directly to the project folder:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
1. Download:
   ```
   catools-lc.zip
   ```
1. When prompted for a save location, choose:
   ```
   C:\dev\
   ```
1. Confirm the file is saved as:
   ```
   C:\dev\catools-lc.zip
   ```

If the browser auto‑downloads to **Downloads**, move the file manually into  
`C:\dev\` before continuing.

---

# Expand the ZIP into the deterministic Windows project folder
1. In **File Explorer** or **Explorer++**, **Navigate** to:
   ```
   C:\dev\
   ```
1. **Right‑click**:
   
   ```
   catools-lc.zip
   ```
1. **Choose**:
   
   ```
   Extract All…
   ```
1. **Extract** to:
   
   ```
   C:\dev\
   ```

After extraction, you must have:

```
C:\dev\catools-lc\ACTIVE\RAW\
C:\dev\catools-lc\ACTIVE\CAMTASIA\
C:\dev\catools-lc\ACTIVE\ENHANCED_AUDIO\
C:\dev\catools-lc\ACTIVE\AUDIATE\
C:\dev\catools-lc\ACTIVE\OUT\
```

If any folder is missing, the ZIP was incorrect — return to Linux.

---

# Verify RAW MP4 exists
Inside the extracted folder, confirm:

```
C:\dev\catools-lc\ACTIVE\RAW\lesson_01.mp4
```

If missing, the Linux ZIP was incomplete.

---

# Copy RAW MP4 into CAMTASIA folder
**Do NOT cut.**  
The RAW folder must retain the original file.

1. **Navigate** to:
   
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
1. **Copy**:
   ```
   lesson_01.mp4
   ```
1. **Paste** into:
   ```
   C:\dev\catools-lc\ACTIVE\CAMTASIA\
   ```

---

# Open Camtasia and prepare a clean workspace
1. **Open** **Camtasia**.  
1. **Click**:
   
   ```
   New Project
   ```
1. In the top menu, **click**:
   ```
   Media → Media Bin
   ```

---

# Import the MP4 into Camtasia
1. Drag:
   ```
   lesson_01.mp4
   ```
   from the CAMTASIA folder into the **Media Bin**.  
1. Drag the clip from the Media Bin onto **Track 1**.

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
1. Right‑click:
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
1. Open **Dropbox in a web browser**.  
1. Navigate to:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
1. Upload:
   ```
   C:\dev\catools-lc.zip
   ```

---

# Tidy up the Windows machine
1. Delete:
   ```
   C:\dev\catools-lc\
   ```
1. Delete:
   ```
   C:\dev\catools-lc.zip
   ```

Windows machine returns to **stateless**.

---

# End of Windows Exercise
This completes the Windows‑only dehydration workflow.  
Linux recording, remuxing, and ZIP creation are handled in a separate exercise.
