# Exercise – Import and Record Video on Linux (OBS Studio)
###### /caTools/LearningCurve/08-EX-LC-record-video-linux/3-EX-LC-import-record-video-linux.md

This exercise covers the **Linux‑only** portion of the workflow.  
Linux is used **only** for recording with OBS Studio and preparing the project ZIP.  
No editing is performed on Linux.  
Linux must remain **stateless** after each session.

---

# Goals
1. Prepare Linux for recording  
1. Launch OBS Studio  
1. Validate the PipeWire capture source  
1. Record the lesson (`lesson_01.mkv`)  
1. Remux to MP4 (`lesson_01.mp4`)  
1. Perform VLC sanity checks  
1. Create the project ZIP (Linux‑exact doctrine)  
1. Upload ZIP to Dropbox (browser only)  
1. Return Linux to a stateless condition  

---

# Prepare Linux for Recording

1. Close all unnecessary applications.  
1. Ensure only the target monitor is active (no virtual displays).  
1. Confirm microphone input is active in Pop!\_OS sound settings.  
1. Ensure OBS Studio is the **only** recording tool running.

---

# Launch OBS Studio

1. Open **OBS Studio** from the Pop!\_OS launcher.  
1. In the bottom‑left, click:
   ```
   Scenes → Default
   ```
1. In **Sources**, ensure there is **only one** source:
   ```
   Screen Capture (PipeWire)
   ```

---

# Validate PipeWire Capture Source

1. Click the **gear icon** next to the source:
   ```
   Screen Capture (PipeWire) → Properties
   ```
1. Ensure the selected monitor is the **exact** display you intend to record.  
1. Ensure:
   - **Cursor Capture**: enabled  
   - **Show Preview**: enabled  

1. Click:
   ```
   OK
   ```

---

# Set Recording Format (MKV)

1. Top menu:
   ```
   File → Settings
   ```
1. Select:
   ```
   Output
   ```
1. Under **Recording**:
   - **Recording Format**:
     ```
     mkv
     ```
   - **Encoder**:
     ```
     Software (x264)
     ```

1. Click:
   ```
   OK
   ```

---

# Start Recording

1. Position all windows exactly as they should appear in the video.  
1. In OBS, click:
   ```
   Start Recording
   ```
1. Perform the lesson normally.

---

# Stop Recording

1. In OBS, click:
   ```
   Stop Recording
   ```

OBS saves the file to:
```
~/Videos/
```

The filename will be timestamped.

---

# Move and Rename the MKV

1. Open **Files** (Pop!\_OS file manager).  
1. Navigate to:
   ```
   Videos
   ```
1. Locate the most recent `.mkv` file.  
1. Move it to:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ```
1. Rename it:
   ```
   lesson_01.mkv
   ```

---

# Sanity Check the MKV (VLC Only)

1. Right‑click:
   ```
   lesson_01.mkv
   ```
1. Choose:
   ```
   Open With → VLC Media Player
   ```
1. Play 5–10 seconds.

Confirm:
- Video exists  
- Audio exists  
- No corruption  
- No silence  
- No stutter  

If any issue is found, re‑record immediately.

---

# Remux MKV to MP4 (Lossless)

1. In OBS, top menu:
   ```
   File → Remux Recordings
   ```
1. Click:
   ```
   ...
   ```
   and select:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/lesson_01.mkv
   ```
1. OBS automatically sets the MP4 output path.

1. Click:
   ```
   Remux
   ```

OBS creates:
```
lesson_01.mp4
```
in the same folder.

---

# Sanity Check the MP4 (VLC Only)

1. Right‑click:
   ```
   lesson_01.mp4
   ```
1. Choose:
   ```
   Open With → VLC Media Player
   ```
1. Play 5–10 seconds.

Confirm:
- Video exists  
- Audio exists  
- No corruption  
- No silence  
- No stutter  

If any issue is found, repeat the remux or re‑record.

---

# Create the Project ZIP (Linux‑Exact Doctrine)

The ZIP must contain **exactly one top‑level folder named `catools-lc`**, matching macOS and Windows.

1. Open **Files**.  
1. Navigate to:
   ```
   ~/dev/catools-lc/
   ```
1. **Select all of the following folders**:
   ```
   ACTIVE
   ROLLBACK_VAULT
   ```
1. Right‑click →  
   ```
   Compress…
   ```
1. Choose:
   ```
   .zip
   ```
1. Name the archive:
   ```
   catools-lc.zip
   ```

Resulting structure:

```
catools-lc.zip
    catools-lc/
        ACTIVE/
        ROLLBACK_VAULT/
```

---

# Upload ZIP to Dropbox (Browser Only)

1. Open a browser.  
1. Navigate to:
   ```
   https://www.dropbox.com/home/caTools/LearningCurve/lesson_01/
   ```
1. Upload:
   ```
   ~/dev/catools-lc.zip
   ```

---

# Tidy Up Linux (Stateless Doctrine)

1. Delete:
   ```
   ~/dev/catools-lc/
   ```
1. Delete:
   ```
   ~/dev/catools-lc.zip
   ```
1. Delete any leftover files in:
   ```
   ~/Videos/
   ```

Linux returns to **stateless**.

---

# End of Linux Recording Exercise
This completes the Linux‑only recording workflow.  
Dehydration and editing occur on Windows in the next exercise.
