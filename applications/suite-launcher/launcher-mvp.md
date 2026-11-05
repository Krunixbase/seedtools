# 📘 Suite Launcher MVP

## Overview

This document defines the Minimum Viable Product (MVP) for Suite Launcher.

The MVP focuses on providing a unified entry point to SeedTools Suite while keeping implementation simple, deterministic, and offline-first.

The goal is to validate the launcher concept before introducing advanced features such as cross-app automation, workflow synchronization, and session management.

---

# MVP Objectives

Suite Launcher MVP should:

- provide a single entry point to all Suite applications
- simplify navigation across the ecosystem
- provide access to documentation
- support guided workflows
- operate entirely offline
- remain deterministic and transparent

---

# Scope

## Included In The MVP

### Application Launcher

Display and launch:

```text
Recovery Tool
Forensics Tool
Entropy Inspector
Mnemonic Tools
Path Explorer
Address Scanner
SeedTools Desktop
SeedTools CLI
```

Users should be able to select any application from a centralized interface.

---

### Workflow Launcher

Display available workflows:

```text
Recovery Mode
Forensics Mode
Address Verification Mode
Entropy Diagnostics Mode
```

The MVP does not automate workflows.

It only presents them and explains which applications are involved.

---

### Documentation Hub

Provide access to:

```text
Application READMEs
Architecture Documentation
Security Documentation
Product Documentation
Financing Documentation
Roadmaps
```

Documentation should be accessible offline.

---

### Suite Settings

Provide centralized settings:

```text
Theme
Language
Offline Mode
```

Settings should be stored locally.

---

### Module Registry

Maintain metadata about available modules.

Example:

```text
Recovery Tool
Forensics Tool
Entropy Inspector
Mnemonic Tools
Path Explorer
Address Scanner
SeedTools CLI
SeedTools Desktop
```

The registry enables application discovery.

---

# Excluded From MVP

The following features are intentionally postponed:

```text
Cross-App Session Sync
Wallet Preset Auto-Detection
Launcher Notifications
Automation Engine
Export Center
Workflow Marketplace
Cloud Features
Online Updates
Analytics
Telemetry
```

These capabilities belong to future versions.

---

# User Interface

## Main Screen

```text
SeedTools Suite Launcher

Applications
------------
Recovery Tool
Forensics Tool
Entropy Inspector
Mnemonic Tools
Path Explorer
Address Scanner
SeedTools Desktop
SeedTools CLI

Workflows
---------
Recovery Mode
Forensics Mode
Address Verification Mode
Entropy Diagnostics Mode

Documentation
-------------
Documentation Hub

Settings
--------
Theme
Language
Offline Mode
```

---

# Startup Sequence

```text
Launcher Start
        ↓
Module Registry Load
        ↓
Documentation Index Load
        ↓
Settings Load
        ↓
Main Screen
```

---

# Navigation Model

```text
Suite Launcher
│
├── Applications
│
├── Workflows
│
├── Documentation
│
└── Settings
```

Every section should be reachable within a single interaction.

---

# Security Requirements

The MVP must comply with SeedTools security principles:

- offline-first operation
- no telemetry
- no analytics
- no cloud dependencies
- deterministic behavior
- transparent workflows

Launcher must never transmit recovery-related information.

---

# Architecture Dependencies

The MVP depends on:

```text
launcher-architecture.md
launcher-modules.md
launcher-workflows.md
```

These documents define the architecture and behavior of the system.

---

# Success Criteria

The MVP is considered complete when:

- all Suite applications are discoverable
- workflows are visible
- documentation is accessible
- settings are configurable
- launcher operates offline
- launcher remains deterministic

---

# Future Evolution

After MVP completion, future milestones include:

## Phase 2

```text
Cross-App Session Sync
Preset Manager
Wallet Detection
Notifications
```

## Phase 3

```text
Automation Engine
Advanced Workflow Chaining
Export Center
Reporting Center
```

## Phase 4

```text
Launcher PRO Dashboard
Workflow Marketplace
Advanced NGO Features
```

---

# Long-Term Vision

Suite Launcher becomes the primary control plane of SeedTools Suite.

It provides:

- unified navigation
- application discovery
- workflow orchestration
- documentation access
- shared Suite configuration

while preserving the SeedTools principles of:

- transparency
- determinism
- reproducibility
- privacy
- user sovereignty
