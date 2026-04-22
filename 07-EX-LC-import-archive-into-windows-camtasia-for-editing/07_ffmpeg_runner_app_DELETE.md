# ffmpeg-runner App Specification
###### C:/dev/caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing\07_ffmpeg_runner_app_DELETE.md

This document defines the **ffmpeg-runner** utility used during the LearningCurve phase.  
The purpose of this utility is to provide a **safe, deterministic, operator‑grade** method for converting Camtasia Recorder `.trec` files into `.mp4` files using the bundled `ffmpeg.exe`.

The ffmpeg-runner app is a **temporary bridge** between:
- manual LearningCurve workflows, and  
- the future automated **caTools** application.

The app must require **no shell usage**, **no typing**, and **no operator decisions**.

---

# 1. Purpose

The ffmpeg-runner app performs exactly three actions:

1. **Detect** a `.trec` file in the quarantine folder.  
2. **Convert** the `.trec` file into `.mp4` using the bundled ffmpeg.  
3. **Place** both assets into the correct RAW folder.

The app must enforce:
- stateless recording  
- metadata preservation  
- deterministic folder structure  
- zero operator drift  
- zero shell interaction  

---

# 2. Operator Workflow

The operator performs the following steps:

1. Record a lesson using Camtasia Recorder.  
2. Save the `.trec` file into:
   ```
   C:\quarantine\
   ```
3. Launch the **ffmpeg-runner** app.  
4. The app performs all required actions automatically.  
5. The operator uploads the resulting assets to Dropbox.  
6. The operator deletes all local state.

No command line.  
No PowerShell.  
No typing.  
No decisions.

---

# 3. App Behavior (Deterministic)

When launched, the app must:

## 3.1 Locate `.trec` file
Search:
```
C:\quarantine\
```

Rules:
- Exactly one `.trec` file must exist.  
- If zero or more than one exist, show an error and exit.

## 3.2 Verify ffmpeg exists
Verify:
```
C:\dev\caTools\bin\ffmpeg.exe
```

If missing:
- Show error  
- Exit  

## 3.3 Convert `.trec` → `.mp4`
Run ffmpeg with the following command:

```
ffmpeg.exe -i lesson_01.trec -c:v libx264 -preset fast -crf 18 lesson_01.mp4
```

Rules:
- Output file must be created in the same folder as the `.trec`.  
- Output filename must match the `.trec` base name.  
- No operator choices.  
- No UI for settings.

## 3.4 Move both assets into RAW folder
Move:
```
lesson_01.trec
lesson_01.mp4
```
into:
```
C:\dev\catools-lc\ACTIVE\RAW\
```

Rules:
- Create folder if missing.  
- Overwrite must not occur.  
- If file exists, show error and exit.

## 3.5 Validate assets
Confirm both files exist in RAW:
- `lesson_01.trec`
- `lesson_01.mp4`

If validation fails:
- Show error  
- Exit  

## 3.6 Success indicator
Show a **single green success screen**:

```
Conversion Complete
Both assets are ready in ACTIVE\RAW
```

No logs.  
No advanced UI.  
No extra buttons.

## 3.7 Optional: Open RAW folder
Provide a single button:

```
Open RAW Folder
```

This is optional but recommended.

---

# 4. Error Handling

The app must show **one error at a time**, with a single **OK** button.

Errors include:

- No `.trec` file found  
- Multiple `.trec` files found  
- ffmpeg missing  
- ffmpeg conversion failure  
- RAW folder write failure  
- Filename collision  
- Permission denied  

Error messages must be:

- neutral  
- technical  
- deterministic  
- non‑emotional  

Example:

```
Error: No .trec file found in C:\quarantine\
```

---

# 5. UI Requirements

The UI must be:

- single window  
- fixed size  
- no menus  
- no settings  
- no preferences  
- no advanced mode  
- no hidden features  

Layout:

```
[ Title: ffmpeg-runner ]

[ Status Box ]
Displays: "Ready to process .trec file"

[ Run Button ]
Label: "Convert Recording"

[ Optional: Open RAW Folder Button ]

[ Footer ]
Version number
```

No animations.  
No progress bars (optional).  
No multi-step wizards.

---

# 6. File Locations (Hard‑Coded)

The app must use the following fixed paths:

### Quarantine (input)
```
C:\quarantine\
```

### ffmpeg binary
```
C:\dev\caTools\bin\ffmpeg.exe
```

### RAW output folder
```
C:\dev\catools-lc\ACTIVE\RAW\
```

These paths must not be configurable.

---

# 7. Statelessness Enforcement

After successful conversion, the app must:

- leave `C:\quarantine\` empty  
- leave no temp files  
- leave no logs  
- leave no state  

The operator will later delete:
```
C:\dev\catools-lc\
```
as part of the standard stateless cleanup.

---

# 8. Future Migration Path

The ffmpeg-runner app is a **temporary** tool.  
It will be replaced by the full **caTools** application.

The migration path:

1. ffmpeg-runner (LearningCurve phase)  
2. caTools CLI (automation phase)  
3. caTools GUI (full production phase)  

All three will use the same:

- folder structure  
- naming rules  
- ffmpeg invocation  
- stateless cleanup  
- Dropbox upload rules  

---

# End of ffmpeg-runner App Specification
