# 📘 Suite Launcher Module Discovery

## Overview

This document defines the module discovery mechanism used by Suite Launcher.

The discovery process is responsible for identifying available SeedTools Suite modules, validating their structure, loading metadata, and registering them in the launcher registry.

Module discovery allows Suite Launcher to remain modular, extensible, and automatically aware of available applications.

---

# Objectives

Module Discovery should:

- detect available modules
- validate module structure
- load module metadata
- build launcher registry
- support future module expansion
- remain fully offline

---

# Discovery Scope

The launcher scans the following directory:

```text
applications/
```

Expected structure:

```text
applications/

├── recovery-tool/
├── forensics-tool/
├── entropy-inspector/
├── mnemonic-tools/
├── path-explorer/
├── address-scanner/
├── seedtools-desktop/
├── seedtools-cli/
└── suite-launcher/
```

Every subdirectory is treated as a candidate module.

---

# Discovery Process

```text
Launcher Start
        ↓
Scan applications/
        ↓
Identify candidate modules
        ↓
Validate module structure
        ↓
Load metadata
        ↓
Create registry entries
        ↓
Build Launcher Registry
        ↓
Display Modules
```

---

# Discovery Lifecycle

## Step 1 — Scan

The launcher scans:

```text
applications/*
```

and collects all directories.

Example:

```text
recovery-tool
forensics-tool
entropy-inspector
```

---

## Step 2 — Validation

Each discovered directory is validated.

Required files:

```text
README.md
roadmap.md
```

Future requirement:

```text
module.json
```

Validation determines whether the module can be registered.

---

## Step 3 — Metadata Loading

If validation succeeds, metadata is loaded.

Source:

```text
module.json
```

or future registry-compatible metadata files.

Loaded information:

```text
module_id
name
version
category
status
launch methods
workflows
```

---

## Step 4 — Registry Entry Creation

A registry record is created.

Example:

```text
Recovery Tool
Category: Recovery
Status: Available
```

This information becomes available to Suite Launcher.

---

## Step 5 — Registry Build

All validated entries are combined into:

```text
registry.json
```

or an equivalent in-memory registry.

---

# Validation Rules

## Required Files

Current MVP:

```text
README.md
roadmap.md
```

Future:

```text
module.json
```

---

## Directory Validation

Valid:

```text
applications/recovery-tool/

README.md
roadmap.md
module.json
```

Invalid:

```text
applications/recovery-tool/

README.md
```

Reason:

```text
Missing roadmap.md
```

---

# Discovery States

## Available

```text
All required files present.
```

---

## Experimental

```text
Module exists but metadata is incomplete.
```

---

## Planned

```text
Module registered but not implemented.
```

---

## Deprecated

```text
Module retained for compatibility.
```

---

# Registry Integration

Discovery populates:

```text
registry.json
```

Example:

```text
Module Discovery
        ↓
Metadata Collection
        ↓
Registry Build
        ↓
Launcher UI
```

---

# Error Handling

## Missing Documentation

Example:

```text
README.md missing
```

Action:

```text
Mark module invalid.
```

---

## Missing Metadata

Example:

```text
module.json missing
```

Action:

```text
Register as experimental.
```

---

## Duplicate Module ID

Example:

```text
recovery-tool
recovery-tool
```

Action:

```text
Reject duplicate registration.
```

---

## Invalid Category

Example:

```text
Unknown Category
```

Action:

```text
Fallback: Experimental
```

---

# Discovery Output

The discovery process produces:

```text
Detected Modules
Validated Modules
Registry Entries
Errors
Warnings
```

Example:

```text
Modules Found: 9
Valid Modules: 9
Errors: 0
Warnings: 0
```

---

# MVP Discovery Requirements

The MVP discovery system supports:

```text
Directory Scanning
File Validation
Metadata Loading
Registry Building
```

The MVP discovery system does not support:

```text
Remote Repositories
Cloud Discovery
Online Registries
Network Metadata
Plugin Downloads
```

---

# Security Requirements

Discovery must remain:

- offline-first
- deterministic
- reproducible
- local-only

Discovery must never:

- upload metadata
- download metadata
- contact external services

---

# Future Enhancements

Future phases may add:

```text
Automatic module registration
Capability validation
Dependency graph generation
Workflow compatibility checks
Version compatibility checks
```

---

# Long-Term Vision

Module Discovery becomes the foundation of Launcher automation.

The launcher should be capable of:

- discovering new modules
- validating module structure
- building registries automatically
- exposing modules to workflows

while preserving SeedTools principles:

- transparency
- determinism
- reproducibility
- offline-first operation
- modular architecture
