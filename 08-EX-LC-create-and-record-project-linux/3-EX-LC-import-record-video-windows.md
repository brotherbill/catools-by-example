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
1. Close Camtasia (stateless shutdown)  
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
1. In **Dropbox**, navigate to:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
1. Download:
   ```
   catools-lc.zip
   ```
1. Save to:
   ```
   C:\dev\
   ```

If the browser auto‑downloads to **Downloads**, move the file manually into `C:\dev\` before continuing.

---

# Expand the ZIP into the deterministic Windows project folder
1. Navigate to:
   ```
   C:\dev\
   ```
1. Right‑click:
   ```
   catools-lc.zip
   ```
1. Choose:
   ```
   Extract All…
   ```
1. Extract to:
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
Confirm:
```
C:\dev\catools-lc\ACTIVE\RAW\lesson_01.mp4
```

---

# Copy RAW MP4 into CAMTASIA folder
**Do NOT cut.**

1. Navigate to:
   ```
   C:\dev\catools-lc\ACTIVE\RAW\
   ```
1. Copy:
   ```
   lesson_01.mp4
   ```
1. Paste into:
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
1. Top menu:
   ```
   Media → Media Bin
   ```

---

# Import the MP4 into Camtasia
1. In the **Media Bin**, locate:
   ```
   lesson_01.mp4
   ```
1. **Ensure the playhead is at:**
   ```
   0:00.00
   ```
   - Press **Home** if needed.
1. Right‑click the file →  
   ```
   Add to Timeline at Playhead
   ```

Deterministic placement:
- Timestamp: **0:00.00**  
- Track: **1**

---

# Separate audio and video
1. Right‑click the clip →  
   ```
   Separate Audio and Video
   ```

Track assignments:
- Track 1 → video  
- Track 2 → audio

---

# Rename tracks
1. Track 1 → `VIDEO`  
1. Track 2 → `AUDIO_RAW`

---

# Export RAW WAV
1. Select the audio track:
   ```
   AUDIO_RAW
   ```

1. Top menu:
   ```
   Export → Export Audio Only…
   ```

---

## Save Audio dialog

### 1. Set the **path** (single clean line)
Navigate to:

```
C:\dev\catools-lc\ACTIVE\AUDIATE\
```

Confirm the dialog shows this exact path.

### 2. Set the **file name**
In the **File name** field, type exactly:

```
lesson_01.wav
```

### 3. Save
Click:
```
Save
```

---

# Export RAW MP4
1. In the top menu, click:
   ```
   Export → Local File…
   ```

---

## Save MP4 dialog

### 1. Set the **file name**
In the **File name** field, type exactly:

```
lesson_01.mp4
```

### 2. Set the **path**
Navigate to:

```
C:\dev\catools-lc\ACTIVE\OUT\
```

Confirm the dialog shows this exact path.

### 3. Set File type
In the **File type** field, **select**:
```
MP4 (recommended)
```

### 4. Click Export

### 5. Click Open File Location

---

# Sanity check the MP4 (Windows)
1. **Right‑click** on:
   ```
   lesson_01.mp4
   ```
1. **Choose**:
   ```
   Play With VLC Media Player
   ```
1. **Play** 5–10 seconds.

Confirm:
- Video exists  
- Audio exists  
- No corruption  
- No silence  
- No stutter  

If any issue is found, repeat dehydration.

---

# Close Camtasia (stateless shutdown)

After exporting the WAV and MP4 files, **Camtasia must be closed with zero project state**.

1. In the top menu, click:
   ```
   File → Exit
   ```

2. When Camtasia asks:
   ```
   Save changes to the project file Untitled Project.tscproj?
   ```
   **Click:**
   ```
   No
   ```

### DO NOT:
- Do **NOT** click **Save**
- Do **NOT** save a `.tscproj` file
- Do **NOT** use:
  ```
  File → Export → Zipped Project…
  ```
- Do **NOT** preserve any Camtasia project state

Camtasia on Windows is a **stateless dehydration station**.  
No project files survive this step.

---

# Zip the entire project folder (Windows)

The ZIP must contain **exactly one top‑level folder named `catools-lc`**, matching the Linux workflow.

### **Linux‑exact (A+) Windows procedure**

1. Navigate to:
   ```
   C:\dev\catools-lc\
   ```

2. **Select all of the following folders**:
   ```
   ACTIVE
   CAMTASIA
   AUDIATE
   ENHANCED_AUDIO
   OUT
   ROLLBACK_VAULT
   ```

3. **Right‑click** the selected folders →  
   ```
   Send to → Compressed (zipped) folder
   ```

4. Name the ZIP:
   ```
   catools-lc.zip
   ```

This produces the correct structure:

```
catools-lc.zip
    catools-lc/
        ACTIVE/
        CAMTASIA/
        AUDIATE/
        ENHANCED_AUDIO/
        OUT/
        ROLLBACK_VAULT/
```

---

# Upload ZIP to Dropbox (Windows side)
1. In **Dropbox**, navigate to:
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

Windows returns to **stateless**.

---

# End of Windows Exercise
This completes the Windows‑only dehydration workflow.  
Linux recording, remuxing, and ZIP creation are handled separately.
