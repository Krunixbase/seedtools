# 📘 Suite Launcher Architecture

## Overview

Suite Launcher is the central orchestration layer of SeedTools Suite.

Its purpose is to provide a unified entry point for all applications,
guided workflows, documentation, settings, and future cross-application integrations.

Suite Launcher does not implement recovery, forensics, scanning, or analysis logic itself.

Instead, it serves as a secure, offline-first coordination layer for the entire Suite.

---

# High-Level Architecture

```text
SeedTools Suite

Suite Launcher
│
├── Applications
│   ├── Recovery Tool
│   ├── Forensics Tool
│   ├── Address Scanner
│   ├── Entropy Inspector
│   ├── Mnemonic Tools
│   ├── Path Explorer
│   ├── SeedTools Desktop
│   └── SeedTools CLI
│
├── Guided Workflows
│   ├── Recovery Mode
│   ├── Forensics Mode
│   ├── Address Verification Mode
│   └── Entropy Diagnostics Mode
│
├── Preset Manager
│   ├── BIP32
│   ├── BIP39
│   ├── BIP44
│   ├── BIP49
│   ├── BIP84
│   ├── BIP86
│   └── Wallet Presets
│
├── Documentation Hub
│   ├── READMEs
│   ├── Architecture
│   ├── Security Docs
│   ├── Roadmaps
│   └── Manuals
│
└── Settings Layer
    ├── Theme
    ├── Language
    ├── Offline Mode
    └── Hardened Mode
```

---

# Core Components

## 1. Application Registry

The Application Registry maintains information about all SeedTools applications.

Responsibilities:

- module discovery
- module registration
- metadata management
- version awareness

Applications currently supported:

- Recovery Tool
- Forensics Tool
- Address Scanner
- Entropy Inspector
- Mnemonic Tools
- Path Explorer
- SeedTools Desktop
- SeedTools CLI

---

## 2. Guided Workflow Engine

The Guided Workflow Engine coordinates multiple applications
into deterministic step-by-step workflows.

Examples:

### Recovery Workflow

```text
Mnemonic Tools
    ↓
Recovery Tool
    ↓
Path Explorer
    ↓
Address Verification
```

### Forensics Workflow

```text
Entropy Inspector
    ↓
Forensics Tool
    ↓
Address Scanner
```

---

## 3. Preset Manager

Preset Manager provides reusable configurations.

Supported categories:

- BIP standards
- wallet presets
- BTCPay presets
- Specter presets
- Sparrow presets
- NGO presets

Presets may be shared across all applications.

---

## 4. Documentation Hub

The Documentation Hub provides offline access to:

- application READMEs
- architecture documentation
- security documentation
- financing documentation
- product documentation
- roadmaps

All documentation should remain accessible without network access.

---

## 5. Settings Layer

Centralized Suite settings:

- theme configuration
- language selection
- security profiles
- hardened mode
- offline-only mode

Settings should be shared across all Suite applications.

---

# Security Principles

Suite Launcher follows SeedTools security requirements:

- offline-first operation
- zero telemetry
- deterministic workflows
- no external API dependencies
- reproducible build compatibility

Launcher does not transmit or store private wallet information.

---

# Future Expansion

Planned features:

- Cross-App Session Sync
- Wallet Preset Auto-Detection
- Guided Recovery PRO
- Launcher Notifications
- Suite-Wide Export Module
- Cross-App Automation Engine

---

# Long-Term Vision

Suite Launcher becomes the central control plane of SeedTools Suite.

It provides:

- unified navigation
- workflow orchestration
- application discovery
- documentation access
- shared settings

while maintaining the project's offline-first,
deterministic, and security-focused philosophy.
