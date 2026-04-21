# Exercise – Create Project Scaffolding (Windows Version)
###### C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/1-EX-LC-windows/1-EX-LC-create-project-scaffolding-windows.md

This exercise defines the required folder structure for Windows‑based editing in the caTools workflow. All steps must be followed exactly to ensure cross‑platform consistency and deterministic behavior.

---

## Prepare quarantine folder (Windows)

1. **Open** File Explorer (or any Windows file manager such as Explorer++).
2. **Type**:
   ```
   C:\dev\
   ```
   into the Address bar, then **Press** Enter.

### Happy Path — `quarantine` folder does not exist

3. **Create** a folder named:
   ```
   quarantine
   ```
4. Use this folder to store unverified or untrusted content before it is inspected.

### Recovery Path — `quarantine` folder already exists

3. **Open**:
   ```
   C:\dev\quarantine
   ```
   in File Explorer (or any Windows file manager such as Explorer++).
4. Inside the `quarantine` folder, **Delete** all files and folders until the folder is empty.
5. Continue using this folder to store unverified or untrusted content before it is inspected.

---

## Parent folder

1. **Open** File Explorer (or any Windows file manager such as Explorer++).
1. **Type**:
   ```
   C:\dev\catools-lc
   ```
   into the Address bar, then **Press** Enter.
1. Inside the `catools-lc` folder, **Create** the following folders:
   ```
   ACTIVE
   ROLLBACK_VAULT
   ```

---

## ACTIVE subfolders

1. **Open**:
   ```
   C:\dev\catools-lc\ACTIVE
   ```
   in File Explorer (or any Windows file manager such as Explorer++).
2. Inside `ACTIVE`, **Create** the following folders:
   ```
   AUDIATE
   CAMTASIA
   ENHANCED_AUDIO
   RAW
   OUT
   ```

---

# End of Windows Scaffolding Exercise

