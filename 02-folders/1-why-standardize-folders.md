# Why Standardize Folders

## A uniform standard of folders and file names provides these benefits:
1. This *borrows* from **DDD** the concept of **ubiquitous** names.
1. Standard folder names.  If you have 100 video projects, they are organized the same way.
1. Standard file names. When you standardize file names, others can quickly understand their purpose.

As with any standard, the key is to plant your flag, pick some standard and stick with it.  Once the standard is set in concrete, then anyone following can follow it, lock it in, and expect standard results.

## IBM created HIPO back in the 1960's.  Hierarchical Input, Processing and Output.  This made sense then, and still makes sense today.
### Our inputs are:
1. Initial video and audio files created on Windows, Mac or Linux, with Camtasia Recorder or other editor.
1. Assets from other projects, such as intros and outros.
1. Images from outside Camtasia.

### Our Processing steps are :
1. Edits
    1. Destructive
        1. Removing parts of the time line.
        1. Removing hesitations (uhh's) and long silence durations.
        1. Removing "dirty" text from the video.
    1. Constructive
        1. Fixing typos of AI Speech to Text conversion.
1. Enhance Audio quality
    1. podcast.adobe.com/en/enhance
        1. Hire an AI Sound Engineer for $10/month.
1. Add Captions, in various languages
1. Add AI Synthetic voices in various languages

### Our Outputs are:
1. mp4 files with captions, with dubbing in various languages
1. Folders organized to permit dehydration, rehydration, adding dependent or global video assets.

Key features that we want is to:
1. Have most of our videos archived in Dropbox.
1. Have several videos that we are currently editing.
1. Lock down state so we can roll back to a prior (good) state.

---

# Dropbox access to caTools

## Security
1. All folders that can be accessed by apps such as caTools are in /Apps/ folder.
1. Every folder that doesn't start with /Apps/ is off limits to nosy apps such as caTools.  So caTools doesn't have access to your working folders.  Can't read them, can't even know that they exist.

## Productivity
1. You have better things to do with your time that manually zipping folders, properly naming them, then copying them to Dropbox.  Let caTools handle these chores, quickly, efficiently and accurately.

## Companies may standardize folders by their customers.
1. Each customer may have their own folder tree, so all their videos are naturally together.
    1. As a client, an off-shore company did some documentation of the SolidCP control panel for me.  After several attempts, they got it right.
        1. When the staffer who did the work left the company, they couldn't find any of my documentation.
        1. The off-shore company didn't have a company wide *Brother-Bill" folder, with all my work in it.
        1. It was likely only in the staffer's folder, and when he left and they trashed his account, my documentation was trashed with it.
    1. Let's not repeat that mistake.
1. In this course, we will have simple top-level folders
    1. by-hand
        1. This is the manual, or stick-shift version, where we do things by hand.
        1. We use Dropbox via the UI, which is slower, but it is easier to see each step.
        1. We have to get the folder paths right, as well as file names right.
            1. This is fine for learning curve, not good for production work.
    1. by-caTools
        1. This is where we use the automatic transmission, where caTools does a lot for us, including
            1. Updating Dropbox directly, doing the zipping, and guiding you to do steps in C+A, that it can't do.
            2. Providing folder paths and filenames, so you can copy/paste them into C+A, letting caTools get the paths and filenames right, so the human recorder/editor can focus on recording and editing, not the naming conventions, and not making typos.
        1. Have validation steps to detect if humans are going rogue and the project is off the rails.
            1. Better to fail fast, and roll back to last *safe* version.