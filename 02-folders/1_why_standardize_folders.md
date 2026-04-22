# Why Standardize Folders
###### C:/dev/caTools-by-example/02-folders\1_why_standardize_folders.md

## A uniform standard of folders and file names provides these benefits
1. This *borrows* from **DDD** the concept of **ubiquitous** names.
1. Standard folder names. If you have 100 video projects, they are organized the same way.
1. Standard file names. When you standardize file names, others can quickly understand their purpose.

As with any standard, the key is to plant your flag, pick a standard, and stick with it.  
Once the standard is set in concrete, anyone following it can lock it in and expect consistent results.

---

## IBM created HIPO in the 1960s  
**Hierarchical Input, Processing, and Output.**  
It made sense then, and it still makes sense today.

### Our Inputs are:
1. Initial video and audio files created on Windows, Mac, or Linux, using Camtasia Recorder or other editors.
1. Assets from other projects, such as intros and outros.
1. Images from outside Camtasia.

### Our Processing steps are:
1. Edits  
    1. **Destructive**  
        1. Removing parts of the timeline.  
        1. Removing hesitations (uhh’s) and long silences.  
        1. Removing “dirty” text from the video.  
    1. **Constructive**  
        1. Fixing typos from AI Speech‑to‑Text conversion.
1. Enhance audio quality  
    1. Using podcast.adobe.com/en/enhance  
        1. Hire an AI sound engineer for $10/month.
1. Add captions in various languages.
1. Add AI synthetic voices in various languages.

### Our Outputs are:
1. MP4 files with captions and dubbing in various languages.
1. Folders organized to permit dehydration, rehydration, and adding dependent or global video assets.

### Key features we want:
1. Most videos archived in Dropbox.
1. Several videos actively being edited.
1. Lockdowns so we can roll back to a prior good state.

---

# Dropbox Access to caTools

## Security
1. All folders accessible by apps such as caTools must be inside:
   ```
   /Apps/
   ```
1. Every folder **not** inside `/Apps/` is off‑limits to apps.  
   caTools cannot read, scan, or even know those folders exist.

## Productivity
1. You have better things to do than manually zip folders, name them correctly, and upload them to Dropbox.  
   caTools handles these chores quickly, efficiently, and accurately.

## Companies may standardize folders by customer
1. Each customer may have their own folder tree so all their videos stay together.
1. A real example:  
    1. An offshore company documented the SolidCP control panel.  
    1. When the staffer left, they couldn’t find any of the documentation.  
    1. They had no company‑wide **Brother‑Bill** folder.  
    1. The work lived only in the staffer’s personal folder.  
    1. When his account was deleted, the documentation was deleted with it.  
1. We do not repeat that mistake.

---

## In this course, we use simple top‑level folders

### by-hand
1. The manual, stick‑shift version.  
1. We use Dropbox via the UI — slower, but easier to see each step.  
1. We must get folder paths and filenames correct.  
1. Good for learning curve, not for production.

### by-caTools
1. The automatic transmission version.  
1. caTools handles:  
    1. Updating Dropbox directly  
    1. Zipping folders  
    1. Guiding you through C + A steps it cannot automate  
    1. Providing copy/paste‑ready folder paths and filenames  
1. caTools validates that humans are not going rogue.  
1. Fail fast, roll back to last **safe** version.

