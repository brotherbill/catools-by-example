### Goals of using Camtasia + Audiate + caTools
1. Use the power of C + A, while avoiding breaking your projects.
    1. If we break projects, let's detect that quickly and roll back to last safe state.
    1. When breaking is cheap, experimentation is encouraged.
1. Lock down success states, so there is something to roll back to.
    1. Track who did what, when and why, and even throw in how and where.
1. Use computerized linters to detect failures quit, and roll back.
1. Use caTools to make it easy to put assets in the right folder, with the right name.
   1. Humans are notoriously bad at acting like machines.  Computers are excellent at that.
   1. use caTools at the *pain points*, editing quickly where you know the do's and don'ts, so you do the do's, avoid the don'ts, and fearlessly and rapidly edit.
   1. use caTools to maintain state, and let caTools let you copy/paste folder paths and file names that are perfect for where you are.  No typos, no off by one errors.  Machine level perfection.
   1. Lock down progress, so when you do make mistakes, you can discard them, and roll back to last good state.
   1. Let caTools work with Dropbox API to save lock downs effortlessly.

### Current flaws in C + A (*as of April 2026*)
1. Audiate synchronizes its changes with Camtasia, but Camtasia doesn't recipricate synchronizing its changes with Audiate.  This results in *drift*, where there are *multiple sources of truth*.
    1. This results in breakage with corrupt files.
    1. The worst part is that these errors may not be immediately obvious.
    1. It typically *bites you* three months from now, when you rehydrate the files.  Lo and behold, Audiate doesn't have the last changes, so it is out of step with Camtasia.
    1. You now have what is known in the trade as **garbage**.  Garbage has one purpose.  Throw it out.
        1. Now that 15 minute edit has grown to be a 4 hour edit, with all that rework.
        1. That is why you bought Audiate in the first place, to have high productivity.
    1. At this point, many C+A subscribers give up on Audiate as it isn't trustworthy.
1. After *Edit in Audiate*, a simple ripple-delete in Camtasia can break synchronization.

### How caTools keeps you out of C+A *pain points*?
1. It guides you with **do's** and **don'ts** that remind you not to do "ripple-deletes" in Camtasia.
1. It provides the folder path and file names that follow best practices.
1. It locks down the folders and files that allow roll backs in the future, so you can easily roll back.

### What if Techsmith fixes their *pain points*?  Will caTools still be useful?
1.  It depends on what changes Techsmith does.
    1. If they recommend using caTools, while they leave the *pain points" unchanged, then caTools will remain a valuable tool so you can get the best out of C+A, as it is today.
    1. If they prevent "ripple-deletes" in dangerous spots in Camtasia after "Edit in Audiate", good for them.
    1. If they provide the standard folder structure, and put in the "right" choices, then less need for caTools.
    1. If they provide lockdowns, and validate the folder paths and file names, and add other validations, and also automate Dropdown updates, then caTools will finally be incorporated into Camtasia and Audiate.
    1. If they incorporate caTools into C+A, then caTools will have served well, and not be needed anymore.