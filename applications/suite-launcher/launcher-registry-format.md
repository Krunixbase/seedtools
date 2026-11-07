
# 📘 Suite Launcher Registry Format

## Overview

This document defines the registry format used by Suite Launcher.

The registry acts as the authoritative source of information about all modules available within SeedTools Suite.

Its purpose is to provide:

- module discovery
- module metadata
- module categorization
- launch configuration
- documentation integration
- future workflow integration

The registry is designed to remain simple, deterministic, and human-readable.

---

# Design Goals

The registry must be:

- offline-first
- deterministic
- version-aware
- human-readable
- extensible
- platform-independent

The registry should not require any network access.

---

# Registry Responsibilities

The registry manages:

```text
Application Discovery
Module Metadata
Launch Configuration
Documentation Mapping
Workflow Integration
Version Tracking
```

The Launcher uses the registry to build its interface dynamically.

---

# Registry Architecture

```text
Suite Launcher
        │
        ▼
Module Registry
        │
        ├── Recovery Tool
        ├── Forensics Tool
        ├── Entropy Inspector
        ├── Mnemonic Tools
        ├── Path Explorer
        ├── Address Scanner
        ├── SeedTools Desktop
        └── SeedTools CLI
```

---

# Registry File

Initial MVP implementation:

```text
registry.json
```

Example location:

```text
applications/suite-launcher/registry.json
```

---

# Module Schema

Every module registered in the launcher should follow the same schema.

Example:

```json
{
  "module_id": "recovery-tool",
  "name": "Recovery Tool",
  "version": "1.0",
  "category": "Recovery",
  "status": "available",
  "launch_methods": [
    "desktop",
    "cli"
  ]
}
```

---

# Required Fields

## module_id

Unique identifier.

Example:

```text
recovery-tool
forensics-tool
entropy-inspector
```

Rules:

- lowercase
- unique
- immutable

---

## name

Human-readable module name.

Example:

```text
Recovery Tool
Forensics Tool
Entropy Inspector
```

---

## version

Registered module version.

Example:

```text
1.0
1.1
2.0
```

---

## category

Module category.

Allowed values:

```text
Recovery
Forensics
Entropy
Analysis
Interface
Launcher
Documentation
```

---

## status

Current module status.

Allowed values:

```text
available
experimental
planned
deprecated
```

---

# Optional Fields

## description

Example:

```json
"description": "Deterministic wallet recovery workflows."
```

---

## documentation

Associated documentation.

Example:

```json
"documentation": [
  "README.md",
  "roadmap.md"
]
```

---

## workflows

Associated workflows.

Example:

```json
"workflows": [
  "Recovery Mode",
  "Address Verification Mode"
]
```

---

## entrypoints

Registered launch entry points.

Example:

```json
"entrypoints": {
  "desktop": "desktop.exe",
  "cli": "cli.py"
}
```

---

# Module Categories

## Recovery

```text
Recovery Tool
```

---

## Forensics

```text
Forensics Tool
```

---

## Entropy

```text
Entropy Inspector
```

---

## Analysis

```text
Mnemonic Tools
Path Explorer
Address Scanner
```

---

## Interface

```text
SeedTools Desktop
SeedTools CLI
```

---

## Launcher

```text
Suite Launcher
```

---

# Registry Example

```json
{
  "modules": [
    {
      "module_id": "recovery-tool",
      "name": "Recovery Tool",
      "version": "1.0",
      "category": "Recovery",
      "status": "available",
      "description": "Deterministic wallet recovery workflows.",
      "documentation": [
        "README.md",
        "roadmap.md"
      ]
    },
    {
      "module_id": "forensics-tool",
      "name": "Forensics Tool",
      "version": "1.0",
      "category": "Forensics",
      "status": "available"
    }
  ]
}
```

---

# Registry Lifecycle

## Registration

A new module is registered when:

- folder exists
- documentation exists
- metadata exists

---

## Update

A module entry is updated when:

- version changes
- status changes
- metadata changes

---

## Removal

A module should not be physically removed.

Deprecated modules should use:

```json
"status": "deprecated"
```

to preserve historical compatibility.

---

# MVP Scope

The MVP registry supports:

```text
Module Listing
Metadata Storage
Version Awareness
Category Classification
Documentation Mapping
```

The MVP registry does not support:

```text
Automatic Updates
Cloud Synchronization
Online Registries
Remote Modules
```

---

# Security Principles

The registry must remain:

- local
- offline
- deterministic
- reproducible

The registry should never contain:

- wallet data
- mnemonics
- recovery artifacts
- user secrets

---

# Future Expansion

Potential future additions:

```text
Workflow Metadata
Preset Metadata
Module Dependencies
Capability Tracking
Security Profiles
```

---

# Long-Term Vision

The registry becomes the foundation of Launcher operation.

All user interface components, workflows, settings, and application discovery mechanisms should rely on the registry as the single source of truth.

This guarantees consistency, transparency, and deterministic behavior across SeedTools Suite.
