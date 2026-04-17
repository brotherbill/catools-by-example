# Project naming wizard

1. The customers may have one or more ways to name projects.
    1. A simple way would be lesson_01, lesson_02, etc.
    1. A fancier way would be c04_2c_p32_fun_with_strings, where this is for chapter 4, second section, third part, starting on page 32, with lesson "fun with strings".
1. Each Project Naming rule has versions, with the projects staying with their original versions, and automatically have names modernized to the current version.
1. Once a naming wizard is created and projects are built with it, it is locked down for that version, and and changes require a new version.
    1. Although there are safe changes that can be applied in a version, it is best to make changes to the next version, where it is obvious that changes were made.
1. There may be many ways to name projects.  In general, it is expected that there should only be a handful of ways to name projects.  If you have 50 ways of naming projects, that is likely not taking advantage of the power that the wizard has.

## Architecture of project names
1. A project name is a sequence of segments.
1. There may be no ambiguity of parsing segments.
1. A segment may be one of:
    1. literal (constant) text 
        1. "lesson" or "c" or "p"
    2. choice of several literal (constant) text
    3. separator
        1. period or dash or underbar (only one)
    4. Number
        1. Min, Max
        1. Decimal or Hexadecimal
    5. Free text
        1. Min length 
        1. Max length
        1. Choice of letters, digits, punctuation
        1. Rules for lowercase, uppercase

## For hands-on version, we will manually name files, using lesson_01 format.        