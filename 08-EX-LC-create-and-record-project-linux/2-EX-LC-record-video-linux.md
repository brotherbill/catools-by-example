# Record video with Linux OBS Studio

## Goals
1. **Prepare for recording**  
   - For those of you who watch Food Network, *mise en place* (“everything in its place”) applies here too.  
   - Ensure OBS Studio is installed, the microphone is plugged into **this** recording computer, and the environment is ready.

1. **Record the video**  
   - Audio is captured automatically along with the screen recording.

1. **Save recording assets**  
   - Store them using standardized folders and standardized file names.

1. **Transfer assets to Windows**  
   - Windows performs dehydration, audio extraction, MP4 export, and all downstream processing.

1. **Save to Dropbox**  
   - This becomes the single source of truth for editing.

1. **Tidy up the recording machine**  
   - Return it to a clean, stateless condition so it’s ready for the next fresh recording.

---

## Prepare for recording
1. **Open OBS Studio**  
   - OBS opens with your Scenes and Sources visible.  
   - Ensure your “Screen Capture” and “Microphone” sources exist.

1. **Verify your inputs**  
   1. Confirm you are recording the **correct screen**.  
   1. Confirm the **correct microphone** is selected.  
   1. Decide whether to record **System Audio** (I do not).

1. **Perform a microphone sanity check**  
   1. **Speak** into your microphone.  
   1. Watch the **Audio Mixer** → your mic meter must move.  
   1. If it does not, **close and re‑open OBS Studio**.  
   1. The microphone may be connected to another machine. *(This happens to me all the time.)*  
   1. OBS will happily record video **with no audio**, and it will not warn you.  
   1. This check prevents silent‑audio failures.

---

## Record the video and audio
1. **Start the recording**  
   - Click **Start Recording** in OBS Studio.

1. **Perform your Show and Tell** presentation.  
   - OBS has **no countdown** — begin when ready.

1. **Stop the recording**  
   - Click **Stop Recording**.

1. OBS automatically saves the recording to your configured **Recording Path**.  
   - Set this path ahead of time to:  
     ```
     ~/junk/
     ```

1. Your recording will appear as:  
   ```
   lesson_01.mkv
   ```
   *(OBS uses `.mkv` by default — this is correct and preferred.)*

   1. No, this is **not** a typo — saving to `~/junk/` is correct.  
      - This is a safe holding area for *suspected* or *unverified* content.

---

## Move assets into project scaffolding
1. **Cut**  
   ```
   ~/junk/lesson_01.mkv
   ```
   then **paste** it into:  
   ```
   ~/dev/catools-lc/ACTIVE/RAW/
   ```

1. Confirm the folder now contains:  
   - `lesson_01.mkv`

---

## Transfer to Windows for dehydration
1. **Copy**  
   ```
   ~/dev/catools-lc/
   ```
   to your Windows machine using your preferred method:  
   - Dropbox  
   - USB drive  
   - Network share  
   - WSL shared folder  
   - SCP (advanced users)

1. On Windows, continue with the **Windows Dehydration Workflow**.

---

## Tidy up the Linux recording machine
1. **Delete all contents of**:  
   ```
   ~/junk/
   ```
   *(This folder must be empty before the next recording.)*

1. **Delete all contents of**:  
   ```
   ~/dev/catools-lc/
   ```
   *(Linux machine must remain stateless.)*

1. You are now ready for the **next fresh recording**.

---

## Summary
1. Linux uses **OBS Studio**, not Camtasia Recorder.  
1. Linux produces **.mkv**, not `.trec`.  
1. Linux does **zero** dehydration — Windows does all heavy lifting.  
1. Linux must remain **stateless**, just like the Windows recording machine.  
1. This workflow ensures cross‑platform consistency and prevents silent failures.  
