# Project Naming Wizard
###### C:/dev/caTools-by-example/05-project-naming-wizard\1_project_naming_wizard.md

## Project naming wizard
1. Customers may have one or more ways to name projects.
1. A simple naming pattern might be:
   ```
   lesson_01, lesson_02, lesson_03
   ```
1. A more expressive pattern might be:
   ```
   c04_2c_p32_fun_with_strings
   ```
   - Chapter 4  
   - Second section  
   - Third part  
   - Starting on page 32  
   - Lesson title: “fun with strings”

1. Each Project Naming Rule has **versions**.  
   - Projects stay with their original version.  
   - Names may be automatically modernized to the current version.  

1. Once a naming wizard is created and projects are built with it, that version is **locked down**.  
   - Changes require a **new version**.  
   - Safe changes may exist, but it is best to apply them to the next version so the change is explicit.

1. There may be many ways to name projects, but in practice there should be only a handful.  
   - If you have 50 naming patterns, you are not leveraging the power of the wizard.

---

## Architecture of project names
1. A project name is a **sequence of segments**.
1. There must be **no ambiguity** when parsing segments.
1. A segment may be one of:

   1. **Literal text**  
      - Examples: `"lesson"`, `"c"`, `"p"`

   1. **Choice of literal text**  
      - A fixed set of allowed constants

   1. **Separator**  
      - One of: period (`.`), dash (`-`), underbar (`_`)

   1. **Number**  
      - Min / Max  
      - Decimal or Hexadecimal

   1. **Free text**  
      - Min length  
      - Max length  
      - Allowed characters (letters, digits, punctuation)  
      - Rules for lowercase / uppercase

---

## Hands‑on version
1. For the learning curve, we will manually name files using the simple format:
   ```
   lesson_01
   ```
