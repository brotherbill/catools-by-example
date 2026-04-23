# Canonical /src Folder Structure
###### docs/architecture/src_folder_structure.md

## Overview

This document defines the canonical folder structure for the `/src` directory of the caTools backend. The structure reflects the pure hexagonal monolith architecture and establishes the required boundaries for domain logic, ports, and adapters. All future backend development must conform to this structure.

## Top‑Level Structure

The `/src` directory contains a single application composed of three primary layers:

```
src/
    domain/
    ports/
    adapters/
    app/
```

### domain/

The `domain` folder contains all pure logic. This layer has no dependencies on infrastructure or external libraries other than the language runtime. All invariants, rules, and computations reside here.

### ports/

The `ports` folder defines all interfaces required by the domain. These interfaces describe interactions with external systems such as storage, file systems, or external services. No implementation code is placed in this folder.

### adapters/

The `adapters` folder contains all implementations of the ports. These implementations may depend on infrastructure, external libraries, or operating system features. This folder provides the concrete behavior required by the domain.

### app/

The `app` folder composes the domain, ports, and adapters into a single executable unit. This folder contains dependency injection configuration, application startup code, and any orchestration required to run the system.

## Dependency Direction

The dependency direction is strictly enforced:

```
domain → ports → adapters → app
```

- The domain depends only on itself.
- The domain may reference ports.
- Adapters implement ports but do not reference domain internals.
- The app layer composes all components and performs wiring.

## Naming Requirements

All folder and file names inside `/src` must follow these rules:

- lowercase
- underscores for separators
- no spaces
- no hyphens
- OS‑pure and machine‑pure

## Example Layout

```
src/
    domain/
        rules/
        invariants/
        value_objects/
        services/

    ports/
        storage_port.cs
        filesystem_port.cs

    adapters/
        filesystem/
            filesystem_adapter.cs
        storage/
            storage_adapter.cs

    app/
        program.cs
        composition_root.cs
```

## Status

Accepted.

## Summary

This structure defines the canonical layout for the caTools backend under the pure hexagonal monolith architecture. All future development must adhere to this structure to maintain consistency, correctness, and deterministic behavior.

