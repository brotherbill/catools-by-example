# Create Project

## What is a Project?
1. A project is all the assets needed to record, edit and publish a *single* video.
    1. This includes Locked-downs restore points, one or more recordings (clips)
    1. This may support captions and dubbing in many languages
    1. This may include global intro or outro.
    1. This may include a private sub-project to add in a missing part of a video.
1. A Project is in a path, with a parent folder.

## Where does a project live?
1. During creation, recording and editing, it lives in the local file system, with backups on Dropbox.
1. After the project is "completed", for a while, it lives on Dropbox, with local file folders deleted.
1. The parent folder of all projects in this course 

## Parent folder
1. The parent folder is the root of all of the video editing projects.
    1. For the Learning Curve part of this course, we will have parent folder be C:\dev\catools-lc
        1. catools means Camtasia + Audiate + caTools
        2. lc means learning curve
    - Parent folder for learning curve.
    - Mirrors caTools workflow manually.
    - Not used for production nor automation.
    - Training ground for operator discipline.

1. Each video editing projects has these top folders
    1. **ACTIVE** - Actively editing this video
        - This is the only folder used for editing.
        - Camtasia and Audiate read and write here.
        - All editing happens inside ACTIVE/.
        - Do not copy timelines into other locations.
        - Do not rename files inside ACTIVE/.
        - Do not move files out of ACTIVE/.
        - Do not import files from ROLLBACK_VAULT/.
        - Do not mix assets from other lessons.
        - Keep only files required for this lesson.
        - Keep the folder clean. No duplicates. No clutter.
        - If corruption occurs, stop editing immediately.
        - Rehydrate from ROLLBACK_VAULT/ if needed.
        - ACTIVE/ must always reflect the current working state.
        - Treat this folder as volatile. It can break.
        1. Subfolders are: 
            1. RAW
                - Holds original camera, microphone and screen recordings.
                - Source of truth for the lesson.
                - Never edited, renamed, modified or deleted.
            2. ENHANCED_AUDIO
                - Holds cleaned and improved audio.
                - Vendor-agnostic enhancement workspace.
                - Only processed audio lives here.            
            3. AUDIATE
                - Holds Audiate project files and transcripts.
                - Used for alignment and text edits only.
                - Audiate reads and writes here.                
            4. CAMTASIA
                - Holds Camtasia project files and timeline assets.
                - Camtasia reads and writes here.
                - Active editing workspace.
            5. OUT
                - Holds final rendered outputs.
                - Only completed lesson assets go here.
                - Must stay clean for automation.

    2. **ROLLBACK_VAULT** - The safe versions locked down, so you can roll back to them after breaking the **ACTIVE** video.
        - Mission: Protect dehydrated states. Insurance for ACTIVE/.
        - Do not edit, rename, or delete anything.
        - Do not open vault files in Camtasia or Audiate.
        - Operator performs rehydration manually in Phase 1.
        - Operator deposits new states manually in Phase 1.
        - Any modification breaks rollback integrity.
        - Treat this folder as untouchable.
