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
    1. Play mp4 video (*at least 5 - 10 seconds*) for sanity check that video and audio look and sound right.

### Close Windows Camtasia
1. In Camtasia, **File > Exit**
1. When prompted to: ** Save changes to the project file Untitled Project.tscproj**, click the **No** button.
    1. Resist the urge to save changes in Windows Camtasia.
    1. Windows Camtasia closes quietly.

### Zip and save to Dropbox
1. Zip all files in C:\dev\caTools-lc\ to C:\dev\caTools-lc\catools-lc_lesson_01_2026-04-17T071916.zip
2. Drag C:\dev\caTools-lc\catools-lc_lesson_01_2026-04-17T071916.zip to Dropbox location caTools/LearningCurve/lesson_01/catools-lc_lesson_01_2026-04-17T071916.zip

### Backup C:\dev\caTools-lc\ to C:\junk
1. Ensure C:\junk\ doesn't contain caTools-lc.
1. This is a good time to delete contents of C:\junk\
1. Copy C:\dev\caTools-lc\ to C:\junk

### Delete contents of C:\dev\caTools-lc\
1. Delete contents of C:\dev\caTools-lc\
    1. Now you are ready for next recording.

### Summary
1. For the 99.9% of you that have used Windows Camtasia Recorder before, you have noticed a different flow.
1. Am I mad, or paranoid, or just doing best-can-do?
    1. I am not mad, nor even angry.
    1. As Andy Grove wrote: "Only the paranoid survive".  (*He is a Holocaust surviver*)
    1. Yes, I am paranoid.  
        1. Computers do what they are told.  
        1. When Audiate synchronizes with Camtasia, but Camtasia doesn't synchronize with Audiate, that is an accident waiting to happen.
        1. When your microphone is plugged into a different machine, your audio will be 100% silent.
    1. This is the best can do.
        1. Standard folder names.
        1. Standard file names.
        1. Saving to Dropbox.
    1. During the Mercury, Gemini and Apollo NASA missions, where each mission was by definition **experimental**, every mission took off and returned safely to Earth.  The Apollo 1 mission ended with three deaths due to an on-board fire in 100% Oxygen environment during a training exercise, where the hatch could not be opened in an emergency.
        1. There is a joke that when Neil Armstrong landed on the Moon, NASA informed him that every single part in the mission was made by the lowest bidder.
        1. In fact, each vendor made sure that every part they shipped was the **best** that current technology could produce.  There was pride in workmanship.
    1. For Apollo 11, there had never been a requirement that the command module be powered down during flight and re-powered on for the return, where the command module would be literally frozen.
        1. The astronauts were concerned that any toggle switch could fail under these harsh and untested conditions.
        1. It would take only a single failure of a single toggle switch to doom the return mission.
        1. Every toggle switch did its job and the astronauts returned safely to Earth.