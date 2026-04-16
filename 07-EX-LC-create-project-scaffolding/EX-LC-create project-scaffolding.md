# Exercise - Create Project Scaffolding

When creating videos, there are many assets (files) that comprise the videos and enhancements.
At the top, there is a parent folder that contains the folders and files for a single project.

As we are in the learning curve, we will do this manually, explaining each step.

## Parent folder
1. The parent folder is the root of all of the video editing projects.
1. Each video editing projects has these top folders
    1. ACTIVE - Actively editing this video
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


    2. ROLLBACK_VAULT - The safe versions locked down, so you can roll back to them after breaking the ACTIVE video.
        - Mission: Protect dehydrated states. Insurance for ACTIVE/.
        - Do not edit, rename, or delete anything.
        - Do not open vault files in Camtasia or Audiate.
        - Operator performs rehydration manually in Phase 1.
        - Operator deposits new states manually in Phase 1.
        - Any modification breaks rollback integrity.
        - Treat this folder as untouchable.