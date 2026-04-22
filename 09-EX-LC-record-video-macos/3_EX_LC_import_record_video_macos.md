# Exercise – Import and Record Video on macOS (Camtasia Recorder Only)
###### C:/dev/caTools-by-example/09-EX-LC-record-video-macos\3_EX_LC_import_record_video_macos.md

This exercise covers the **macOS‑only** portion of the workflow.  
macOS is used **only** for recording with Camtasia Recorder and preparing the project ZIP.  
No editing is performed on macOS.  
No `.tscproj` files are created or saved.  
macOS must remain **stateless** after each session.

---

# Goals
1. Prepare macOS for recording  
1. Launch Camtasia **Recorder Only**  
1. Record the lesson (`lesson_01.trec`)  
1. Perform VLC sanity checks  
1. Place the `.trec` file into the project scaffolding  
1. Create the project ZIP (Mac‑exact doctrine)  
1. Upload ZIP to Dropbox (browser only)  
1. Return macOS to a stateless condition  

---

# Prepare macOS for Recording

1. Close all unnecessary applications.  
1. Ensure only the target monitor is active (no virtual displays).  
1. Confirm microphone input is active in macOS Sound settings.  
1. Ensure Camtasia **Recorder Only** will be used (not the Editor).

---

# Launch Camtasia Recorder

1. Open **Camtasia** from Applications.  
1. In the top menu bar, click:
   ```
   Camtasia → Preferences…
   ```
1. Select:
   ```
   Recording
   ```
1. Ensure:
   - **Record Screen**: enabled  
   - **Record Microphone**: enabled  
   - **Record System Audio**: disabled (unless explicitly required)

1. Close Preferences.  
1. In the main Camtasia window, click:
   ```
   New Recording
   ```

This opens **Camtasia Recorder**, which is the only tool used on macOS.

---

# Configure Recording Region

1. In the Recorder window, click:
   ```
   Screen: Full
   ```
1. Select the **exact monitor** you intend to capture.  
1. Confirm the green bounding box matches the intended display.

---

# Configure Audio Input

1. In the Recorder window, click:
   ```
   Audio: On
   ```
1. Select the correct microphone.  
1. Speak a few words and confirm the input meter moves.

---

# Start Recording

1. Position all windows exactly as they should appear in the video.  
1. In the Recorder window, click:
   ```
   Start Recording
   ```
1. Wait for the countdown.  
1. Perform the lesson normally.

---

# Stop Recording

1. Press:
   ```
   Command + Shift + 2
   ```
   or click the **Stop** button in the Recorder control bar.

Camtasia Recorder automatically opens a save dialog.

---

# Save the Recording to the RAW Folder

1. In the save dialog, set the **file name**:
   ```
   lesson_01.trec
   ```
1. Set the **path**:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ```
1. Click:
   ```
   Save
   ```

---

# Sanity Check the Recording (VLC Only)

1. Open **Finder** and navigate to:
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ```
1. **Right‑click**:
   ```
   lesson_01.trec
   ```
1. Choose:
   ```
   Open With → VLC
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

# Create the Project ZIP (Mac‑Exact Doctrine)

The ZIP must contain **exactly one top‑level folder named `catools-lc`**, matching Linux and Windows.

1. Open **Finder**.  
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
   Compress 2 Items
   ```
1. Rename the resulting ZIP:
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

# Tidy Up macOS (Stateless Doctrine)

1. Delete:
   ```
   ~/dev/catools-lc/
   ```
1. Delete:
   ```
   ~/dev/catools-lc.zip
   ```

macOS returns to **stateless**.

---

# End of macOS Recording Exercise
This completes the macOS‑only recording workflow.  
Dehydration and editing occur on Windows in the next exercise.
