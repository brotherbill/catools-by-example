# Record video with Windows Camtasia Recorder
> This is the same whether the Camtasia Recorder is on this Windows machine or another Windows machine.

1. **Open Camtasia Recorder**.  
    1. It opens with title **Camtasia Editor Recorder**.
    1. Ignore the *Editor* part.  (*The Camtasia Editor Recorder doesn't have Editing capabilities*)
1. Ensure that you are recording the **correct screen**, and **correct microphone** and whether you want **System Audio** (*I don't*)
1. **Speak** into your microphone.  If you don't see your voice light up under the Microphone card, close and re-open Camtasia Recorder.  
    1. The microphone may be connected to another computer.  (*This happens to me all the time*)
    1. Camtasia will gladly record your video without a connected and working microphone.
    1. There are many times that I recorded a video and on play back, there was no sound

1. Start the recording.  **Click** the big red **rec** button 
1. **Wait** for the three second countdown, then do your Show and Tell presentation.
1. **Click** the **Stop** button.
1. **Save Recording** to **C:\junk\ ** (*Create it if it doesn't exist*), with filename: lesson_01.trec, and click Save button.
    1. This will open up Camtasia Rev app.
    1. Click the **Open in Editor** button, which opens up Camtasia Editor - Untitled Project.
        1. **STOP**.  Do not Save or start editing.  Take your hands off the keyboard and off the mouse, and nobody gets hurt.

1. **File > Export > Zipped Project...**
    1. **Change folder path** to **C:\junk\ **  (*Don't click Save button*)
    1. **Change filename** to **lesson_01_RAW.zip**  
    1. **Click** **Save** button
1. **File > Exit** (*to close Camtasia Editor*)
    1. Dialog box asks: **Save changes to the project file Untitled Project.tscproj?**
    1. **Click** the **No** button.
        1. Fight the urge to save the changes.  **No** is the only correct choice.
1. Camtasia Editor closes.  **C:\junk\** has **lesson_01.trec** and **lesson_01_RAW.zip** files.
1. Cut **C:\junk\lesson_01_RAW.**zip, then paste to **C:\dev\catools-lc\ACTIVE\RAW\**
1. **Expand C:\dev\catools-lc\ACTIVE\RAW\ ** to the same target folder of **C:\dev\catools-lc\ACTIVE\RAW\ **
     1. On my machine this results in these 4 files in C:\dev\catools-lc\ACTIVE\RAW
         1. ACTIVE/RAW/dots.tscshadervid (*harmless file, leave it alone*)
         1. ACTIVE/RAW/lesson_01.trec (*Techsmith RECording.  Contains the recorded audio and video*)
         1. ACTIVE/RAW/lesson_01_RAW.tscproj (*harmless file, leave it alone*)
         1. ACTIVE/RAW/lesson_01_RAW.zip (*dehydrated files containing other extracted files*)

1. **Open Windows Camtasia**, then STOP.  (*If it wants to install an update, allow that*)
1. **Click** New Project**, then STOP.  (*This brings up Camtasia Editor - Untitled Project*)
1. **Drag** **C:\dev\catools-lc\ACTIVE\RAW\lesson_01.trec** to Camtasia Editor | Media Bin
1. **Right-click** on **lesson_01.trec** from Media Bin, then choose: **Add to Timeline at Playhead**.
1. **Right-click** on **lesson_01.trec** on **Track 1**, then choose: **Separate Audio and Video**.
1. **Rename Track 1** to **Video**
1. **Rename Track 2** to **Audio**

### Export audio track to ACTIVE\RAW
1. **Export > Export Audio Only...**.  In "Save Audio Dialog", 
    1. **Folder Path** is: **C:\dev\catools-lc\ACTIVE\RAW\ **
    1. **File name** is: **lesson_01_RAW.wav**
    1. **Click Save** button

### Export video as MP4 (*in Camtasia*)
1. **Export > Local File...**
    1. **File name**: **lesson_01_VIDEO.mp4**
    1. **File Type**: **MP4 (*Recommended*)**
    1. **Save Location**: **C:\dev\catools-lc\ACTIVE\RAW\ **
    1. **Click: Export** button
    1. **Exporter dialog** comes up.  
        1. **Click: Open File Location** button
            1. Confirm that **path** is: **C:\dev\catools-lc\ACTIVE\RAW**
            1. Confirm that file with **filename**: **lesson_01_VIDEO.mp4** exists there.

### Close Windows Camtasia
1. In Camtasia, **File > Exit**
1. When prompted to: ** Save changes to the project file Untitled Project.tscproj, click the **No** button.
    1. Resist the urge to save changes in Windows Camtasia.
    1. Windows Camtasia closes quietly.

### Zip and save to Dropbox
1. Zip all files in C:\dev\caTools-lc\ to C:\dev\caTools-lc\catools-lc_lesson_01_2026-04-17T071916.zip
2. Drag C:\dev\caTools-lc\catools-lc_lesson_01_2026-04-17T071916.zip to Dropbox location caTools/LearningCurve/lesson_01/catools-lc_lesson_01_2026-04-17T071916.zip