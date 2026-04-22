# caTools‑jr Backend Plan
###### C:/dev/caTools-by-example/docs/architecture/caTools-jr-backend-plan.md

## 1. Purpose

Define the backend architecture for caTools‑jr, focusing on deterministic `.trec` dehydration, robust error handling, and a clean separation between engine and UI.

The backend will:

- accept `.trec` inputs  
- dehydrate to `.mp4` (and optionally `.wav`)  
- validate outputs  
- log all activity and failures  
- expose a stable interface for a future rich client app  

---

## 2. Technology Stack

- **Language:** C#  
- **Runtime:** .NET (cross‑platform, targeting Linux and Windows)  
- **Architecture style:** Object‑Oriented + Domain‑Driven Design + Vertical Architecture  
- **Database:** SQLite (single‑user, embedded)  
- **Data access:** Dapper  
- **External tools:** `ffmpeg`, `ffprobe`  

---

## 3. Core Design Principles

1. **Single‑instance execution**  
   Only one instance of the console app or rich client may run at a time.

2. **Deterministic behavior**  
   Same input and environment must always produce the same outcome.

3. **Happy Path + Recovery Path**  
   Every operation defines both paths explicitly.

4. **Engine first, UI later**  
   Backend is a self‑contained engine.  
   Rich client app is a thin wrapper.

5. **Structured logging**  
   All steps, decisions, and failures are logged.

6. **DRY (Do Not Repeat Yourself)**  
   All error handling, environment validation, and resource cleanup must be centralized.  
   No duplicated logic.  
   No WET code paths.

7. **YAGNI (You Aren’t Gonna Need It)**  
   The backend must implement only the features required for the current workflow.  
   No speculative abstractions.  
   No premature generalization.  
   No unused extension points.

8. **Domain‑Driven Design (DDD)**  
   The system must model the dehydration workflow as a domain with explicit concepts:  
   - `TrecFile`  
   - `ProbeResult`  
   - `DehydrationJob`  
   - `JobStatus`  
   - `EnvironmentState`  
   - `FailureCategory`  
   The domain model must remain independent of UI, storage, and infrastructure concerns.

9. **Design by Contract (DbC)**  
   All engine components must enforce explicit contracts using preconditions, postconditions, and invariants.  
   - Preconditions validate all inputs before execution.  
   - Postconditions validate all outputs and state transitions after execution.  
   - Invariants ensure domain objects remain in a valid state at all times.  
   DbC enforcement must occur at the domain layer and must be centralized to maintain DRY compliance.

10. **Railway Oriented Programming (ROP)**  
    All workflows must model success and failure as explicit result types (e.g., `Result<TSuccess, TFailure>`).  
    - Each step returns a result instead of throwing for expected failures.  
    - Happy Path is a chain of successful results.  
    - Recovery Path is a chain of failure results with structured error information.  
    ROP must be applied consistently to dehydration, probing, environment validation, and persistence operations.

11. **Vertical Architecture**  
    The codebase must be organized by feature verticals rather than technical layers.  
    - Each vertical encapsulates domain types, services, repositories, and contracts for a specific feature (e.g., Dehydration, Probing, Jobs).  
    - Cross‑vertical coupling is minimized.  
    - Shared infrastructure is limited to clearly defined, stable abstractions.  
    This structure supports incremental evolution and localized changes.

---

## 4. High‑Level Components

1. **TrecFile**  
   Validates `.trec` inputs and exposes metadata.

2. **ProbeService**  
   Wraps `ffprobe` to inspect input and output files.

3. **DehydrationService**  
   Wraps `ffmpeg` to convert `.trec` → `.mp4`.

4. **JobModel**  
   Represents a dehydration job with status and timestamps.

5. **JobRepository (SQLite + Dapper)**  
   Persists job records and logs.

6. **LogService**  
   Writes structured logs to SQLite.

7. **SingleInstanceGuard**  
   Prevents concurrent execution.

8. **EnvironmentValidator**  
   Performs pre‑flight checks for memory, disk space, permissions, and tool availability.

9. **FailureHandler**  
   Centralized component for handling all error categories, ensuring DRY compliance and integrating ROP/DbC semantics.

10. **ConsoleFrontEnd**  
    Entry point for the initial engine.

---

## 5. Dehydration Flow

### 5.1 Happy Path

1. Acquire single‑instance guard.  
2. Validate environment.  
3. Validate input file.  
4. Create job record.  
5. Probe input with `ffprobe`.  
6. Run `ffmpeg` to dehydrate.  
7. Probe output with `ffprobe`.  
8. Mark job as succeeded.

### 5.2 Recovery Path

At any failure point:

1. Capture error context.  
2. Mark job as failed.  
3. Optionally delete partial outputs.  
4. Log details.  
5. Return non‑zero exit code.

All steps must be implemented using ROP result types and DbC contracts.

---

## 6. Error Categories

- Input errors  
- Probe errors  
- Dehydration errors  
- Output validation errors  
- System errors  
- Memory pressure errors  
- Disk exhaustion errors  

Each category maps to structured results and operator‑readable messages.

---

## 7. Data Model Sketch (SQLite)

### 7.1 Jobs table

- `id`  
- `created_at`  
- `started_at`  
- `completed_at`  
- `status`  
- `input_path`  
- `output_path`  
- `input_duration`  
- `output_duration`  
- `input_codec`  
- `output_codec`  
- `error_summary`  

### 7.2 Logs table

- `id`  
- `job_id`  
- `timestamp`  
- `level`  
- `message`  
- `details`  

### 7.3 Dapper Integration

- All database operations use Dapper for parameterized queries.  
- Repository classes encapsulate SQL statements.  
- No dynamic SQL generation at runtime.  
- All queries and commands are deterministic and version‑controlled.

---

## 8. Memory Pressure Handling

### 8.1 Pre‑allocated resources

The engine pre‑allocates:

- a panic log buffer  
- a shutdown message  
- a failure JobModel  
- a SQLite connection  
- a crash log file handle  

### 8.2 Memory pressure detection

The engine monitors:

- available physical memory  
- available virtual memory  
- GC pressure  
- allocation failures  

If thresholds are exceeded:

- refuse to start new jobs  
- mark current job as failed  
- write panic log  
- exit cleanly  

### 8.3 Catastrophic memory failure

If the OS cannot allocate even a few KB:

- graceful shutdown cannot be guaranteed  
- crash recovery logic will run on next startup  
- incomplete jobs will be marked as failed  

---

## 9. Disk Exhaustion Handling

### 9.1 Pre‑flight disk checks

Before each job:

- confirm free space exceeds a minimum threshold  
- confirm output directory is writable  
- confirm temp directory is writable  

### 9.2 Mid‑job disk exhaustion

If disk space is exhausted during dehydration:

- terminate ffmpeg  
- delete partial outputs  
- mark job as failed  
- write structured error log  

### 9.3 Post‑crash recovery

On startup:

- detect partial outputs  
- detect incomplete jobs  
- clean up  
- mark jobs as failed  

---

## 10. Console Application Execution Model

The console application uses a menu‑driven event loop.  
Each menu item corresponds to a specific end‑to‑end test or operational flow.

### 10.1 Menu Structure

Menu items include:

- Full dehydration E2E test  
- Specific Sad Path tests  
- Step‑by‑step forward execution  
- Step‑by‑step reverse execution  
- Step‑by‑step random execution  
- Nightly randomized test loop  
- Log viewing utilities  
- Cleanup utilities  

### 10.2 Event Loop

The console application:

1. Displays the menu.  
2. Waits for operator input.  
3. Executes the selected test.  
4. Writes logs to a dedicated folder.  
5. Returns to the menu.  
6. Continues until the operator exits.

### 10.3 Test Isolation and Cleanup

Each test:

- cleans up artifacts from previous runs  
- initializes a new job record  
- executes the test flow  
- writes logs  
- returns to a known‑good state  

### 10.4 Randomized Execution Modes

Supported modes:

1. Forward order execution  
2. Reverse order execution  
3. Random order execution  

### 10.5 Nightly Test Mode

A dedicated menu item:

1. Randomly selects menu items.  
2. Executes them repeatedly.  
3. Logs all results.  
4. Continues until the operator deletes a designated **signal file**.

---

## 11. Evolution Path

1. **Phase 1 — Console engine**  
2. **Phase 2 — Rich client integration**  
3. **Phase 3 — Extended features**

---

## 12. Non‑Goals

- Multi‑user concurrency  
- Networked databases  
- Background services  
- Vendor‑specific integrations beyond `.trec` dehydration  

---

## 13. Summary

The caTools‑jr backend will be a single‑instance, C#/.NET, SQLite‑backed engine using Dapper for data access. It will:

- dehydrate `.trec` files into validated `.mp4` outputs  
- log all steps and failures  
- detect and handle memory pressure  
- detect and handle disk exhaustion  
- centralize all failure handling to enforce DRY  
- avoid speculative features through YAGNI  
- model the workflow using DDD  
- enforce correctness through Design by Contract  
- model success and failure explicitly using Railway Oriented Programming  
- organize code by feature using Vertical Architecture  
- provide a menu‑driven console interface for deterministic testing  
- support randomized and nightly test modes  
- form the foundation for a future Uno Platform rich client  

This document defines the initial architecture and execution model.
