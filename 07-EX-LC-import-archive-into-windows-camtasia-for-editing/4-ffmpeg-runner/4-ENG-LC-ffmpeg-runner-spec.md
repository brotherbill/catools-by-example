# 4‑ENG‑LC‑ffmpeg‑runner‑spec — Engineering Specification 
###### /caTools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/4-ENG-LC-ffmpeg-runner-spec.md

### *Engineering Specification — caTools LearningCurve Pipeline*  
### *Not for Operators*

---

## **1. Purpose**
`ffmpeg-runner.exe` is a deterministic, operator‑safe extraction tool used to convert Camtasia Recorder `.trec` files into stateless media assets (raw audio + raw video) while preserving all Camtasia metadata in the RAW folder.

It eliminates all operator interaction with:
- ffmpeg  
- PowerShell  
- cmd  
- command‑line parameters  
- manual extraction steps  

The app is a **safety wall** between operators and the underlying complexity.

---

## **2. Architectural Role**
`ffmpeg-runner.exe` sits between:

### **Upstream**
- Camtasia Recorder  
- Camtasia Editor’s “Export Zipped Project…”  
- The RAW folder produced by expanding `lesson_XX_RAW.zip`

### **Downstream**
- The Windows/macOS editing workflow  
- The dehydration ZIP  
- Dropbox as source of truth  
- Stateless machine reset  

The app ensures RAW becomes **canonical** immediately after ZIP expansion.

---

## **3. Operator Workflow (High‑Level)**
Operators do **not** see ffmpeg or any internal logic.

Their entire interaction is:

1. Launch `ffmpeg-runner.exe`  
2. Select the folder:
   ```
   C:\dev\catools-by-example\
   ```
3. Click **Extract**  
4. Close the app  

That is the full operator workflow.

All other behavior is internal and deterministic.

---

## **4. Folder Selection & Persistence**
### **4.1 Folder Picker**
On launch, the app opens a standard Windows folder picker.

The operator selects the **repo root**, not RAW:

```
C:\dev\catools-by-example\
```

### **4.2 Persistence**
The app stores the last selected folder in:

```
%APPDATA%\caTools\ffmpeg-runner\settings.json
```

On next launch:
- If the folder exists → auto‑load it  
- If RAW is valid → enable Extract  
- If RAW is missing → prompt again  

This reduces operator friction and prevents drift.

---

## **5. RAW Folder Detection**
After folder selection, the app recursively searches for:

```
ACTIVE\RAW\
```

### **5.1 RAW Validation Requirements**
RAW must contain:

- Exactly one `.trec` file  
- A `.tscproj` file  
- A `.tscshadervid` file  
- The dehydrated metadata ZIP (`lesson_XX_RAW.zip`)  

If any required file is missing:
- Extract is disabled  
- A clear error message is shown  

---

## **6. Extraction Logic (Internal)**
When the operator clicks **Extract**, the app:

1. Locates the `.trec` file  
2. Extracts raw audio  
3. Extracts raw video  
4. Writes outputs into RAW  
5. Logs each step in real time  
6. Displays success/failure  

### **6.1 Output Filenames**
- `lesson_XX_RAW.wav`  
- `lesson_XX_VIDEO.mp4`  

These filenames are deterministic and match the LearningCurve naming doctrine.

### **6.2 ffmpeg Invocation**
The app internally calls ffmpeg with the correct parameters.

Operators never see these commands.

---

## **7. UI Specification**
### **Window Title**
```
ffmpeg-runner
```

### **UI Elements**
- **Extract** (primary action)  
- **Cancel**  
- **Log Panel** (read‑only, scrollable)  
- **Status Bar** (Idle → Extracting → Success/Failure)  

### **Operator Interaction**
- No typing  
- No parameters  
- No command line  
- No branching  
- No decisions  

---

## **8. Error Handling**
The app must gracefully handle:

- Missing `.trec`  
- Multiple `.trec` files  
- Missing metadata files  
- Missing ffmpeg.exe  
- Locked files  
- Permission issues  
- Invalid folder selection  

Errors appear in the log panel and disable Extract.

---

## **9. Distribution**
The app is distributed as:

```
ffmpeg-runner.exe
ffmpeg.exe
ffprobe.exe (optional)
```

All files live together.  
No installer.  
No registry writes (except optional settings).  
Portable.  
Stateless.

---

## **10. Testing Strategy**
### **10.1 Engineering E2E Testing**
Before the app exists, engineers will “play computer”:

- Navigate to RAW  
- Open PowerShell  
- Run ffmpeg commands manually  
- Verify outputs  
- Continue workflow  

This validates the architecture before implementation.

### **10.2 Operator Testing**
Operators never run ffmpeg manually.  
They only run the app.

---

## **11. Out of Scope**
- Editing  
- Rendering  
- Camtasia automation  
- Dropbox upload  
- Dehydration ZIP creation  
- Linux pixel‑only workflow  
- Any operator‑visible ffmpeg commands  

---

## **12. Future Enhancements (Not in v1)**
- Progress bar  
- Batch extraction  
- Automatic lesson number detection  
- Automatic dehydration ZIP creation  
- macOS build  
- Linux integration  

---
