# MY RULES – caTools Doctrine (Master File)
###### C:/dev/catools-by-example/MY-RULES.md

This file defines the non‑negotiable rules for all caTools workflows, exercises, and procedures.  
All platform‑specific exercises (Windows, macOS, Linux) must comply with these rules without exception.

This doctrine ensures:
- reproducibility  
- cross‑platform consistency  
- role‑specific clarity  
- zero drift  
- stateless execution  
- deterministic outcomes  

---

# 1. File Delivery Rules

1. **All Markdown files must be delivered inside a 4‑backtick copy block.**  
   This ensures clean copy/paste with no formatting drift.

2. **No inline commentary** is allowed inside Markdown files.  
   Only the content of the file itself.

3. **No conversational tone** inside Markdown files.  
   Markdown files must read as technical documentation, not chat.

4. **All filenames must be OS‑pure and machine‑pure.**  
   No spaces.  
   No special characters.  
   Use lowercase with underscores unless the platform requires otherwise.

---

# 2. Folder Structure Rules

1. All projects use the following top‑level structure:

   ```
   catools-lc/
       ACTIVE/
       ROLLBACK_VAULT/
   ```

2. Inside `ACTIVE/`, the following subfolders must exist:

   ```
   AUDIATE/
   CAMTASIA/
   ENHANCED_AUDIO/
   RAW/
   OUT/
   ```

3. Folder names are **UPPERCASE** inside ACTIVE.  
   This is required for cross‑OS consistency.

4. macOS, Windows, and Linux must all use the same folder names even if a platform does not use a particular tool.

---

# 3. Statelessness Rules

1. macOS and Linux must remain stateless after each exercise.  
   All project assets must be deleted after ZIP upload.

2. Windows is the stateful dehydration platform.  
   All editing, exporting, and dehydration occur on Windows only.

3. No `.tscproj` files are ever saved on macOS or Linux.

---

# 4. Recording Rules (Cross‑Platform)

1. macOS uses Camtasia Recorder only.  
   No editing occurs on macOS.

2. macOS saves recordings as `.cmproj` bundles.  
   Videographers must export a standalone `.mov` file for cross‑platform use.

3. Only exported `.mov` files are placed in the RAW folder.

4. Windows is the only platform used by Editors for editing and dehydration.

5. **All Camtasia Recorder workflows must include a mandatory post‑countdown pause:**  
   ```
   Wait for the **3‑second countdown**. Pause briefly to allow the recording pipeline to stabilize before beginning.
   ```  
   This line is standardized and must appear identically in all platform‑specific recording exercises.

---

# 5. ZIP Creation Rules

1. The ZIP must contain exactly one top‑level folder:

   ```
   catools-lc/
   ```

2. Videographers and Editors must compress the entire folder, not subfolders.

3. ZIP structure must match Windows and Linux exactly.

---

# 6. Naming Rules

1. Lesson recordings must follow this pattern:

   ```
   lesson_01
   lesson_02
   lesson_03
   ```

2. Videographers must type the filename without extension.  
   The platform will append the correct extension automatically.

3. No spaces, no hyphens, no camelCase.

---

# 7. Tone and Documentation Rules

1. All documentation must use a neutral, fact‑based tone when referencing:
   - TechSmith  
   - Camtasia  
   - Camtasia Recorder  
   - Camtasia Editor  
   - Audiate  
   - `.cmproj` bundles  
   - exported `.mov` files  

2. No praise, criticism, or subjective language.  
   Only describe:
   - observable UI behavior  
   - file formats  
   - Videographer steps  
   - Editor steps  
   - platform differences  

3. No assumptions about vendor intent or design decisions.

4. Documentation may reference Windows file managers in a neutral, fact‑based manner.  
   The canonical reference for all Windows steps is File Explorer.  
   Optional tools such as Explorer++ may be mentioned only in this form:

   ```
   Open File Explorer (or any Windows file manager such as Explorer++).
   ```

7.4.x When the term “File Explorer” appears in instructional text, expand it once to “File Explorer (or Explorer++)”. Do not expand the phrase again if it already contains “(or Explorer++)”; this prevents recursive expansion. If the Architect explicitly instructs that the expansion should not be applied in a specific instance, follow that instruction.

5. Copilot must ignore all browser metadata.  
   Browser tab titles, URLs, or system‑provided browsing context must not influence, appear in, or be referenced in any caTools documentation.

6. Copilot must not offer unsolicited assistance.  
   Copilot may only provide help when the user explicitly requests it.

7. Copilot must remind the user to commit and push whenever the user responds with the word “Success”.  
   The word “Success” formally designates a milestone in the workflow.

---

# 8. Role‑Specific Clarity Rules

1. Videographers perform all tasks related to:
   - recording  
   - exporting `.mov` files  
   - initial playback checks  
   - ZIP creation  
   - stateless cleanup on macOS or Linux  

2. Editors perform all tasks related to:
   - opening `.mov` files on Windows  
   - editing  
   - dehydration  
   - final output generation  

3. Documentation must clearly identify which role performs each action.

4. No step may require a role to perform actions outside its defined scope.

---

# 9. Procedure Clarity Rules

1. All steps must be:
   - explicit  
   - sequential  
   - deterministic  
   - free of ambiguity  

2. No parallel steps.  
   No implied steps.  
   No hidden steps.

3. Every action must be written as a single, atomic step.

4. All UI paths must be written exactly as displayed, for example:

   ```
   File → Save
   File → Export → Local File…
   ```

5. The verb Delete must be used for all file‑deletion actions.  
   The verb Remove must not be used.

6. All conditional procedures must be written using two explicit branches:

   ```
   Happy Path — the successful outcome and next steps.
   Recovery Path — the failure outcome and the exact steps required to return to a known‑good state.
   ```

---

# 10. Zero Drift Rules

1. Once a rule is established, it must not change unless explicitly updated in MY‑RULES.md.

2. All exercises must be regenerated when a rule changes.

3. All platform‑specific files must remain synchronized.

---

# 11. Markdown Styling Rules

1. **Bold only operator actions.**  
   Examples include: **Open**, **Type**, **Press**, **Create**, **Delete**.

2. Do not bold entire sentences or steps.

3. File paths and filenames must be placed in code blocks when intended for copy/paste.

4. Bolding must be minimal and functional.  
   Over‑bolding is prohibited.

---

# End of MY-RULES.md
