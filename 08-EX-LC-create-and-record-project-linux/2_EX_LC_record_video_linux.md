# Exercise – Record Video on Linux
###### C:/dev/caTools-by-example/08-EX-LC-create-and-record-project-linux\2_EX_LC_record_video_linux.md

This exercise covers the **Linux‑only** portion of the workflow.  
It ends after uploading the **project ZIP** (containing all project folders and files, including the remuxed `.mp4`) to Dropbox and returning the Linux machine to a **stateless** condition.

Windows dehydration is handled in a separate exercise.

---

# Important Note About Recording Format
Linux records in:
```
.mkv
```
because MKV is crash‑proof and safe.

Immediately after recording, Linux performs a **lossless remux** to:
```
.mp4
```
using OBS Studio.

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
COSMIC Media Player starts muted and cannot be trusted for sanity checks.

1. Open **Pop!\_Shop** (or your distro’s software center).  
2. Search for:
   ```
   COSMIC Media Player
   ```
3. Click **Remove**.  
4. Confirm removal.

---

# Configure OBS Studio (one‑time setup, verify every session)

## Output Settings
1. Open **OBS Studio**.  
2. Click:
   ```
   Settings → Output
   ```
3. Set:
   - Output Mode:
     ```
     Advanced
     ```
   - Recording → Type:
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
2. Disable all global audio devices except the microphone.

---

# Prepare for recording
1. Open **OBS Studio**.  
2. In the **Sources** panel, verify:
   ```
   Screen Capture (PipeWire)
   ```
3. Verify the correct monitor is selected.  
4. Verify the correct microphone is selected.  
5. Speak into the mic — the meter must move.

---

# Record the video
1. Click **Start Recording**.  
2. Perform the presentation.  
3. Click **Stop Recording**.  
4. OBS saves the file into your **Videos** folder by default.

5. Open the **Files** app.  
6. Navigate to:
   ```
   Home → Videos
   ```
7. Locate the newest `.mkv` file.  
8. Right‑click → **Rename**:
   ```
   lesson_01.mkv
   ```
9. Move it into:
   ```
   Home → quarantine
   ```

---

# Playback sanity check (Linux)
1. In **Files**, open:
   ```
   Home → quarantine
   ```
2. Right‑click `lesson_01.mkv` → **Open With → VLC Media Player**.  
3. Confirm:
   - Video exists  
   - Audio exists  
   - Mic correct  
   - Screen correct  
   - No corruption  

If audio is missing → re‑record.

---

# Move MKV into project scaffolding
1. In **Files**, open:
   ```
   Home/dev/catools-lc/ACTIVE/RAW/
   ```
2. Drag:
   ```
   lesson_01.mkv
   ```
   from:
   ```
   Home/quarantine
   ```
   into:
   ```
   ACTIVE/RAW
   ```

---

# Remux MKV → MP4 (Linux side, lossless)
1. Open **OBS Studio**.  
2. Click:
   ```
   File → Remux Recordings
   ```
3. Click **…** and select:
   ```
   Home/dev/catools-lc/ACTIVE/RAW/lesson_01.mkv
   ```
4. OBS automatically sets the MP4 output path:
   ```
   lesson_01.mp4
   ```
5. Click **Remux**.  
6. Wait for:
   ```
   Remuxing finished.
   ```
7. Click **Close**.

The `.mp4` is bit‑for‑bit identical to the `.mkv`.

---

# Create deterministic ZIP (GUI‑only)
The ZIP must contain **exactly one top‑level folder named `catools-lc`**.

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
   Compress...
   ```
5. In the dialog:
   - Name:
     ```
     catools-lc
     ```
     *(Do NOT type `.zip` — the system adds it.)*
   - Click **Create**.

This produces:
```
~/dev/catools-lc.zip
```

---

# Upload ZIP to Dropbox – Videographer

1. Open a browser and go to:
   ```
   https://www.dropbox.com
   ```
1. In Dropbox, navigate to:
   ```
   /caTools/LearningCurve/lesson_01
   ```
1. Upload:
   ```
   ~/dev/catools-lc.zip
   ```

---

# Tidy up Linux (return to stateless)
1. In **Files**, delete all contents of:
   ```
   Home/quarantine
   ```
2. Delete all contents of:
   ```
   Home/dev/catools-lc
   ```
3. Delete:
   ```
   Home/dev/catools-lc.zip
   ```

Linux returns to a clean, stateless condition.

---

# End of Linux Exercise
This completes the Linux‑only workflow.  
The next exercise begins on Windows and handles dehydration and downstream processing.
