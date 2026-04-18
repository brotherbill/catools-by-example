# Create Project
###### /caTools/LearningCurve/06-create-project/1-create_project.md

## What is a Project?
1. A project is all the assets needed to record, edit, and publish a *single* video.
1. This includes lockdown restore points and one or more recordings (clips).
1. This may support captions and dubbing in many languages.
1. This may include global intros or outros.
1. This may include a private sub‑project to add a missing part of a video.
1. A project exists inside a path with a parent folder.

---

## Where does a project live?
1. During creation, recording, and editing, it lives in the **local file system**, with backups on Dropbox.
1. After the project is completed, it lives on **Dropbox**, and local folders are deleted.
1. The parent folder for all projects in this course is defined below.

---

## Parent folder
1. The parent folder is the root of all video editing projects.
1. For the Learning Curve portion of this course, the parent folder is:
   ```
   C:\dev\catools-lc
   ```
   - `catools` = Camtasia + Audiate + caTools  
   - `lc` = learning curve  
   - Mirrors caTools workflow manually  
   - Not used for production or automation  
   - Training ground for operator discipline  

---

## Each video editing project has these top folders

### **ACTIVE** — Actively editing this video
- This is the **only** folder used for editing.  
- Camtasia and Audiate read and write here.  
- All editing happens inside `ACTIVE/`.  
- Do **not** copy timelines into other locations.  
- Do **not** rename files inside `ACTIVE/`.  
- Do **not** move files out of `ACTIVE/`.  
- Do **not** import files from `ROLLBACK_VAULT/`.  
- Do **not** mix assets from other lessons.  
- Keep only files required for this lesson.  
- Keep the folder clean — no duplicates, no clutter.  
- If corruption occurs, stop editing immediately.  
- Rehydrate from `ROLLBACK_VAULT/` if needed.  
- `ACTIVE/` must always reflect the current working state.  
- Treat this folder as **volatile** — it can break.

#### Subfolders inside ACTIVE/
1. **RAW**  
   - Holds original camera, microphone, and screen recordings.  
   - Source of truth for the lesson.  
   - Never edited, renamed, modified, or deleted.

1. **ENHANCED_AUDIO**  
   - Holds cleaned and improved audio.  
   - Vendor‑agnostic enhancement workspace.  
   - Only processed audio lives here.

1. **AUDIATE**  
   - Holds Audiate project files and transcripts.  
   - Used for alignment and text edits only.  
   - Audiate reads and writes here.

1. **CAMTASIA**  
   - Holds Camtasia project files and timeline assets.  
   - Camtasia reads and writes here.  
   - Active editing workspace.

1. **OUT**  
   - Holds final rendered outputs.  
   - Only completed lesson assets go here.  
   - Must stay clean for automation.

---

### **ROLLBACK_VAULT** — Safe versions for recovery
- Mission: Protect dehydrated states.  
- Insurance for `ACTIVE/`.  
- Do **not** edit, rename, or delete anything.  
- Do **not** open vault files in Camtasia or Audiate.  
- Operator performs rehydration manually in Phase 1.  
- Operator deposits new states manually in Phase 1.  
- Any modification breaks rollback integrity.  
- Treat this folder as **untouchable**.

