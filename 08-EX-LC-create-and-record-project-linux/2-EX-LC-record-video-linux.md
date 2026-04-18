# /caTools/LearningCurve/2-EX-LC-record-video-linux.md

This exercise covers the **Linux‑only** portion of the workflow.  
It ends after uploading the **project ZIP** (containing all project folders and files, including the remuxed `.mp4`) to Dropbox and returning the Linux machine to a **stateless** condition.

Windows dehydration is handled in a separate exercise.

---

# Important Note About Recording Format
Linux records in **`.mkv`** because MKV is crash‑proof and safe.

Immediately after recording, Linux performs a **lossless remux** to **`.mp4`** using OBS Studio.

Windows receives the **ZIP**, which contains the entire `catools-lc` folder, including the `.mp4`.

If the recording format changes in the future (e.g., `.mov`, `.webm`, `.mp4`),  
update the “Recording Format” section inside this file — the filename does not change.

---

# Goals
1. Prepare for recording  
1. Record the video  
1. Perform a VLC sanity check  
1. Move MKV into project scaffolding  
1. Remux MKV → MP4 (lossless)  
1. Create deterministic ZIP (GUI‑only)  
1. Upload ZIP to Dropbox (browser only)  
1. Return Linux to stateless

---

# Remove COSMIC Media Player (one‑time)
1. COSMIC Media Player starts muted and cannot be trusted for sanity checks.  
1. Remove it:
   ```bash
   sudo apt remove cosmic-media-player
   ```

---

# Configure OBS Studio (one‑time setup, verify every session)

## Output Settings
1. Settings → Output → Output Mode:
   ```
   Advanced
   ```
1. Settings → Output → Recording:
   - Type:
     ```
     Standard
     ```
   - Recording Format:
     ```
     mkv
     ```
   - Video Encoder:
     ```
     x264 (software)
     ```
   - Audio Encoder:
     ```
     AAC
     ```
   - Rate Control:
     ```
     CBR
     ```
   - Bitrate:
     ```
     20000
     ```
   - Keyframe Interval:
     ```
     2
     ```
   - CPU Usage Preset:
     ```
     veryfast
     ```
   - Profile:
     ```
     high
     ```

## Video Settings
1. Settings → Video:
   - Base Resolution:
     ```
     1920x1080
     ```
   - Output Resolution:
     ```
     1920x1080
     ```
   - Common FPS:
     ```
     30
     ```

## Audio Settings
1. Settings → Audio:
   - Sample Rate:
     ```
     48 kHz
     ```
   - Channels:
     ```
     Stereo
     ```
1. Disable all global audio devices except the microphone.

---

# Prepare for recording
1. **Open** OBS Studio.  
1. **Verify** capture source:
   ```
   Screen Capture (PipeWire)
   ```
1. **Verify** the correct monitor is selected.  
1. **Verify** microphone is selected and system audio is disabled.  
1. **Speak** into the mic — meter must move.

---

# Record the video
1. **Click** **Start Recording**.  
1. **Perform** the presentation.  
1. **Click** **Stop Recording**.  
1. OBS saves to:
   ```
   ~/junk/
   ```
1. Rename the file:
   ```
   lesson_01.mkv
   ```

---

# Playback sanity check (Linux)
1. Right‑click:
   ```
   ~/junk/lesson_01.mkv
   ```
1. Open With → **VLC Media Player**.  
1. Confirm:
   - Video exists  
   - Audio exists  
   - Mic correct  
   - Screen correct  
   - No corruption  

If audio is missing → re‑record.

---

# Move MKV into project scaffolding
1. Ensure the deterministic folder structure exists:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ~/dev/catools-lc/ACTIVE/CAMTASIA/
   ~/dev/catools-lc/ACTIVE/AUDIATE/
   ~/dev/catools-lc/ACTIVE/OUT/
   ```
1. Move the MKV:
   ```
   ~/junk/lesson_01.mkv  →  ~/dev/catools-lc/ACTIVE/RAW/
   ```

---

# Remux MKV → MP4 (Linux side, lossless)
1. Open OBS Studio.  
1. File → **Remux Recordings**.  
1. Select:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/lesson_01.mkv
   ```
1. OBS auto‑creates:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/lesson_01.mp4
   ```
1. Click **Remux**.  
1. Confirm “Remuxing finished.”  
1. Click **Close**.

The `.mp4` is bit‑for‑bit identical to the `.mkv`.

---

# Create deterministic ZIP (GUI‑only)
The ZIP must contain **exactly one top‑level folder named `catools-lc`**.

1. Open **Files** app.  
1. Navigate to:
   ```
   Home > dev
   ```
1. **Select all** of the following folders:
   ```
   ACTIVE
   ROLLBACK_VAULT
   ```
1. **Right‑click** the selected folders → **Compress**.  
1. In the **Create Archive** dialog:
   - File name:
     ```
     catools-lc
     ```
     *(Do NOT type `.zip` — the system adds it.)*
   - Password: leave blank  
   - Click **Create**
1. This produces:
   ```
   ~/dev/catools-lc.zip
   ```

This ZIP contains the entire project structure at the correct level.

---

# Upload ZIP to Dropbox (browser only)
Linux must use **browser‑only** Dropbox.

1. Open browser → https://www.dropbox.com  

1. In Dropbox, you must **build the full nested folder path**:

   - Ensure the top‑level folder exists:
     ```
     /caTools/
     ```
   - Inside `/caTools/`, create (if missing):
     ```
     LearningCurve
     ```
   - Inside `/caTools/LearningCurve/`, create (if missing):
     ```
     lesson_01
     ```

1. After the nested structure exists, **enter**:
   ```
   /caTools/LearningCurve/lesson_01/
   ```

1. Upload:
   ```
   ~/dev/catools-lc.zip
   ```

Do **not** upload individual files.  
Do **not** upload the MKV.  
Do **not** upload the MP4 alone.

Windows must receive the **ZIP**.

---

# Tidy up Linux (return to stateless)
1. Delete contents of:
   ```
   ~/junk/
   ```
1. Delete contents of:
   ```
   ~/dev/catools-lc/
   ```
1. Delete:
   ```
   ~/dev/catools-lc.zip
   ```

Linux returns to a clean, stateless condition.

---

# End of Linux Exercise
This completes the Linux‑only workflow.  
The next exercise begins on Windows and handles dehydration and downstream processing.
