# ffmpeg-runner Implementation Blueprint  
###### C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/ffmpeg_runner_implementation_blueprint.md

## Purpose
This blueprint defines the internal architecture of `ffmpeg-runner` so that the implementation is deterministic, testable, and fully aligned with the frozen validation doctrine (v1.0).

This document does not contain code.  
It defines structure, flow, and boundaries only.

---

# 1. File Layout

```
ffmpeg-runner/
    runner.py
    cli/
        __init__.py
        parser.py
    state/
        __init__.py
        model.py
    logging/
        __init__.py
        logger.py
    validation/
        __init__.py
        file_exists.py
        metadata.py
        duration.py
        resolution.py
        color.py
```

### Requirements
- Each validator is an atomic module.
- No module performs work outside its defined scope.
- No cross‑module side effects.
- All output is written to stdout only.

---

# 2. Internal State Model

The internal state must contain exactly the following fields:

```
State:
    filename: str
    duration: float
    width: int
    height: int
    rgb: (int, int, int)
```

### Rules
- No optional fields.
- No dynamic attributes.
- State is populated strictly in doctrine order.
- No mutation after a field is set.

---

# 3. Deterministic Flow (State Machine)

```
START
  ↓
FILE_EXISTS_CHECK
  ↓
METADATA_EXTRACTION
  ↓
DURATION_VALIDATION
  ↓
RESOLUTION_VALIDATION
  ↓
COLOR_VALIDATION
  ↓
SUCCESS_EXIT
```

### Failure Path
At any step:

```
FAIL → WRITE ERROR → EXIT WITH CODE → STOP
```

No logs after failure.  
No cleanup.  
No additional actions.

---

# 4. Function Boundaries

## file_exists.py
```
validate_file_exists(state) -> None
```

## metadata.py
```
extract_metadata(state) -> None
```

## duration.py
```
validate_duration(state) -> None
```

## resolution.py
```
validate_resolution(state) -> None
```

## color.py
```
validate_color(state) -> None
```

## logger.py
```
log_ok(step_name: str, filename: str) -> None
log_error(message: str) -> None
```

## runner.py
```
run(filename: str) -> int
```

---

# 5. Error‑Handling Architecture

All validators raise a `ValidationError`.

```
ValidationError:
    exit_code: int
    message: str
```

### Rules
- runner.py catches the exception.
- Writes the deterministic error message.
- Exits with the exact exit code.
- Performs no additional actions.

---

# 6. Logging Architecture

### Format
```
[OK] <step-name>: <filename>
```

### Required step-names (in order)
1. file-exists  
2. metadata-extracted  
3. duration-valid  
4. resolution-valid  
5. color-valid  

### Rules
- No timestamps.
- No file output.
- No logs after failure.
- No logs after exit code is determined.

---

# 7. CLI Architecture

## parser.py
```
parse_args() -> str
```

## runner.py
```
def main():
    filename = parse_args()
    exit(run(filename))
```

### Rules
- Single input file.
- No flags.
- No options.
- Deterministic behavior only.

---

# 8. Implementation Guarantees

This blueprint guarantees:

- deterministic execution  
- deterministic logs  
- deterministic exit codes  
- deterministic error messages  
- deterministic state transitions  
- deterministic ffprobe/ffmpeg calls  
- cross‑platform consistency  
- zero drift from doctrine  

---

# End of ffmpeg_runner_implementation_blueprint.md
