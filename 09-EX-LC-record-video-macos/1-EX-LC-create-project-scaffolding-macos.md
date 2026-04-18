# Exercise – Create Project Scaffolding (Mac Version)
###### /caTools/LearningCurve/09-EX-LC-record-video-macos/1-EX-LC-create-project-scaffolding-macos.md

When creating videos, there are many assets (files) that comprise the videos and enhancements.  
At the top, there is a parent folder that contains the folders and files for a single project.

As we are in the learning curve, we will do this manually, explaining each step.

---

## Prepare junk folder (Mac)

1. **Create junk folder** (Terminal or Finder):

   **Terminal:**
   ```bash
   mkdir -p ~/junk/
   ```

   **Finder:**
   - Open **Finder**
   - In the menu bar, click:
     ```
     Go → Home
     ```
   - Create a new folder named:
     ```
     junk
     ```

   - This is your **safe holding area** for *suspected* or *unverified* content.  
   - Nothing in this folder is trusted until it passes sanity checks.

---

## Parent folder

1. **Create parent folder**:

   **Terminal:**
   ```bash
   mkdir -p ~/dev/catools-lc/
   ```

   **Finder:**
   - From **Home**, create:
     ```
     dev
     ```
   - Inside `dev`, create:
     ```
     catools-lc
     ```

1. **cd into it** (Terminal):
   ```bash
   cd ~/dev/catools-lc/
   ```

1. **Create subfolders**:
   ```bash
   mkdir -p ACTIVE ROLLBACK_VAULT
   ```

---

## ACTIVE/ subfolders

1. **cd into ACTIVE** (Terminal):
   ```bash
   cd ~/dev/catools-lc/ACTIVE
   ```

1. **Create folders**:
   ```bash
   mkdir -p AUDIATE CAMTASIA ENHANCED_AUDIO RAW OUT
   ```

Folder layout:

```
~/dev/catools-lc/ACTIVE/AUDIATE/
~/dev/catools-lc/ACTIVE/CAMTASIA/
~/dev/catools-lc/ACTIVE/ENHANCED_AUDIO/
~/dev/catools-lc/ACTIVE/RAW/
~/dev/catools-lc/ACTIVE/OUT/
```

---

# End of Mac Scaffolding Exercise
This completes the Mac‑only project scaffolding setup.  
Recording, exporting, and ZIP creation are handled in the next exercises.
