# Exercise – Import and Record Video on Linux (OBS Studio)
###### C:/dev/caTools-by-example/08-EX-LC-create-and-record-project-linux\3_EX_LC_import_record_video_linux.md

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
2. Ensure only the target monitor is active (no virtual displays).  
3. Confirm microphone input is active in Pop!\_OS sound settings.  
4. Ensure OBS Studio is the **only** recording tool running.

---

# Launch OBS Studio

1. Open **OBS Studio** from the Pop!\_OS launcher.  
2. In the bottom‑left, click:
   ```
   Scenes → Default
   ```
3. In **Sources**, ensure there is **only one** source:
   ```
   Screen Capture (PipeWire)
   ```

---

# Validate PipeWire Capture Source

1. Click the **gear icon** next to:
   ```
   Screen Capture (PipeWire)
   ```
   then choose **Properties**.
2. Ensure the selected monitor is the **exact** display you intend to record.  
3. Ensure:
   - **Cursor Capture**: enabled  
   - **Show Preview**: enabled  
4. Click **OK**.

---

# Set Recording Format (MKV)

1. Top menu:
   ```
   File → Settings
   ```
2. Select:
   ```
   Output
   ```
3. Under **Recording**:
   - **Recording Format**:
     ```
     mkv
     ```
   - **Encoder**:
     ```
     Software (x264)
     ```
4. Click **OK**.

---

# Start Recording

1. Position all windows exactly as they should appear in the video.  
2. In OBS, click:
   ```
   Start Recording
   ```
3. Perform the lesson normally.

---

# Stop Recording

1. In OBS, click:
   ```
   Stop Recording
   ```

OBS saves the file to:
```
Home → Videos
```

The filename will be timestamped.

---

# Move and Rename the MKV

1. Open the **Files** app.  
2. Navigate to:
   ```
   Home → Videos
   ```
3. Locate the most recent `.mkv` file.  
4. Drag it into:
   ```
   Home → dev → catools-lc → ACTIVE → RAW
   ```
5. Right‑click → **Rename**:
   ```
   lesson_01.mkv
   ```

---

# Sanity Check the MKV (VLC Only)

1. In **Files**, open:
   ```
   Home/dev/catools-lc/ACTIVE/RAW/
   ```
2. Right‑click:
   ```
   lesson_01.mkv
   ```
3. Choose:
   ```
   Open With → VLC Media Player
   ```
4. Play 5–10 seconds.

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
2. Click the **…** button and select:
   ```
   Home/dev/catools-lc/ACTIVE/RAW/lesson_01.mkv
   ```
3. OBS automatically sets the MP4 output path.  
4. Click:
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
2. Choose:
   ```
   Open With → VLC Media Player
   ```
3. Play 5–10 seconds.

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
2. Navigate to:
   ```
   Home → dev
   ```
3. Right‑click the folder:
   ```
   catools-lc
   ```
4. Select:
   ```
   Compress…
   ```
5. Choose:
   ```
   .zip
   ```
6. Name the archive:
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
2. Navigate to:
   ```
   https://www.dropbox.com/home/caTools/LearningCurve/lesson_01/
   ```
3. Upload:
   ```
   Home/dev/catools-lc.zip
   ```

---

# Tidy Up Linux (Stateless Doctrine)

1. In **Files**, delete:
   ```
   Home/dev/catools-lc/
   ```
2. Delete:
   ```
   Home/dev/catools-lc.zip
   ```
3. Delete any leftover files in:
   ```
   Home/Videos/
   ```

Linux returns to **stateless**.

---

# End of Linux Recording Exercise
This completes the Linux‑only recording workflow.  
Dehydration and editing occur on Windows in the next exercise.
