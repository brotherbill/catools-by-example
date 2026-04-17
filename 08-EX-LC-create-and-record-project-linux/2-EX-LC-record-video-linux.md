# Exercise – Record Video on Linux (OBS Studio)
###### /caTools/LearningCurve/2-EX-LC-record-video-linux.md

This exercise covers the **Linux‑only** portion of the workflow.  
It ends after uploading the project ZIP to Dropbox and returning the Linux machine to a **stateless** condition.

Windows dehydration is handled in a separate exercise.

---

# Important Note About Recording Format
This workflow **currently supports `.mkv` as the required RAW recording format**.

If the recording format changes in the future (e.g., `.mov`, `.webm`, `.mp4`),  
**update the “Recording Format” section below — the filename of this MD file does not change.**

The workflow remains the same; only the format line changes.

---

# Goals
1. **Prepare for recording**  
1. **Record the video**  
1. **Perform a VLC sanity check**  
1. **Move assets into project scaffolding**  
1. **Create a deterministic ZIP (GUI‑only)**  
1. **Upload to Dropbox (browser only)**  
1. **Return Linux to stateless**

---

# Remove COSMIC Media Player (one‑time)
1. COSMIC Media Player starts muted and cannot be trusted for sanity checks.  
   Remove it:
   ```bash
   sudo apt remove cosmic-media-player
   ```

---

# Configure OBS Studio (one‑time setup, but verify every session)

## **Output Settings (Critical for Windows Compatibility)**

1. **Settings → Output → Output Mode**
   ```
   Advanced
   ```

1. **Settings → Output → Recording**
   - **Type**
     ```
     Standard
     ```
   - **Recording Format**
     ```
     mkv
     ```
   - **Video Encoder**
     ```
     x264 (software)
     ```
     *Do NOT use VAAPI, NVENC, AMF, AV1, or any hardware encoder.*
   - **Audio Encoder**
     ```
     AAC
     ```
   - **Rate Control**
     ```
     CBR
     ```
   - **Bitrate**
     ```
     20000
     ```
     *(You may increase to 30000 if needed.)*
   - **Keyframe Interval**
     ```
     2
     ```
   - **CPU Usage Preset**
     ```
     veryfast
     ```
   - **Profile**
     ```
     high
     ```

These settings guarantee:
- **Constant Frame Rate (CFR)**  
- **Camtasia‑compatible H.264**  
- **No ragged edges, no blockiness, no jitter**  
- **Perfect Windows decoding**

---

## **Video Settings**

1. **Settings → Video**
   - **Base (Canvas) Resolution**
     ```
     1920x1080
     ```
   - **Output (Scaled) Resolution**
     ```
     1920x1080
     ```
   - **Common FPS Values**
     ```
     30
     ```

This ensures:
- No fractional framerates  
- No scaling artifacts  
- No decoding drift on Windows  

---

## **Audio Settings**

1. **Settings → Audio**
   - **Sample Rate**
     ```
     48 kHz
     ```
   - **Channels**
     ```
     Stereo
     ```
   - **Global Audio Devices**
     - Disable everything except your microphone.

---

# Prepare for recording
1. **Open OBS Studio**

1. **Verify capture source**
   - Must use **one**:
     ```
     Screen Capture (PipeWire)
     ```
   - Must point to the **exact monitor** you are using.

1. **Verify microphone**
   - Correct mic selected  
   - System audio disabled

1. **Microphone sanity check**
   - Speak into mic  
   - Meter must move

---

# Record the video and audio
1. Click **Start Recording**  
1. Perform your presentation  
1. Click **Stop Recording**  
1. OBS saves to:
   ```
   ~/junk/
   ```
1. **Rename**:
   ```
   lesson_01.mkv
   ```

---

# Playback sanity check (Linux)
1. Right‑click:
   ```
   ~/junk/lesson_01.mkv
   ```
1. Open With → **VLC Media Player**

Confirm:
- Video exists  
- Audio exists  
- Mic correct  
- Screen correct  
- No corruption  

If audio is missing → re‑record.

---

# Move assets into project scaffolding

### **Ensure full project scaffolding exists**
Linux must create the **same folder structure** that Windows expects.

Create (or verify) the following folders:

```
~/dev/catools-lc/ACTIVE/RAW/
~/dev/catools-lc/ACTIVE/CAMTASIA/
~/dev/catools-lc/ACTIVE/AUDIATE/
~/dev/catools-lc/ACTIVE/OUT/
```

> Even though Linux never uses CAMTASIA,  
> **it must exist** so the Windows workflow is deterministic.

### **Move the RAW MKV**
1. **Cut**:
   ```
   ~/junk/lesson_01.mkv
   ```
1. **Paste** into:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ```

---

# Create ZIP for Dropbox (GUI‑only, deterministic)

> **Critical doctrine:**  
> The ZIP must contain **exactly one top‑level folder named `catools-lc`**.  
> No nested `catools-lc/catools-lc/`.  
> No missing folder.  
> No extra levels.

### **Correct zipping procedure**
1. Open **Files**  
1. Navigate to:
   ```
   ~/dev/
   ```
1. **Right‑click the folder**:
   ```
   catools-lc
   ```
   *(Do NOT enter the folder before compressing it.)*
1. Choose:
   ```
   Compress…
   ```
1. Set **File name** to:
   ```
   catools-lc
   ```
   *(Do NOT type “.zip” — the system adds it.)*

This guarantees the ZIP root is:

```
catools-lc/
    ACTIVE/
        RAW/
        CAMTASIA/
        AUDIATE/
        OUT/
```

---

# Upload to Dropbox (Linux side only)

Linux uses **Dropbox in the browser**.  
No filesystem‑mounted Dropbox.  
No terminal uploads.

### Steps
1. Open browser → https://www.dropbox.com  
1. **Construct the full Dropbox path if missing**:
   ```
   /caTools/LearningCurve/lesson_01/
   ```
   - Create `caTools` if missing  
   - Create `LearningCurve` if missing  
   - Create `lesson_01` if missing  

1. Enter:
   ```
   /caTools/LearningCurve/lesson_01/
   ```

1. **Drag‑and‑drop upload**  
   Drag:
   ```
   ~/dev/catools-lc.zip
   ```
   into the Dropbox window **while inside the correct folder**.

---

# Tidy up the Linux recording machine
1. Delete contents of:
   ```
   ~/junk/
   ```
1. Delete contents of:
   ```
   ~/dev/catools-lc/
   ```
1. Linux machine returns to **stateless**.

---

# End of Linux Exercise
This completes the Linux‑only workflow.  
The next exercise begins on Windows and handles dehydration and downstream processing.
