# 📘 Suite Launcher Module Registry

## Overview

This document defines all modules available through Suite Launcher.

Suite Launcher acts as the central access layer of SeedTools Suite and provides unified access to all applications, workflows, documentation, and shared services.

The Launcher does not implement recovery, forensics, scanning, or analysis functionality directly.

Instead, it discovers, organizes, launches, and coordinates SeedTools Suite modules.

---

# Module Categories

Suite Launcher organizes modules into the following categories:

- Recovery
- Forensics
- Analysis
- Navigation
- Interface
- Documentation
- Shared Services

---

# Recovery Modules

## Recovery Tool

Location:

```text
applications/recovery-tool/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- deterministic wallet recovery
- seed reconstruction workflows
- recovery diagnostics
- restoration validation

Launch Methods:

- Launcher
- Desktop
- CLI

---

# Forensics Modules

## Forensics Tool

Location:

```text
applications/forensics-tool/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- recovery investigations
- wallet structure analysis
- backup analysis
- forensic verification

Launch Methods:

- Launcher
- Desktop

---

# Analysis Modules

## Entropy Inspector

Location:

```text
applications/entropy-inspector/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- entropy analysis
- randomness diagnostics
- entropy scoring
- anomaly detection

Launch Methods:

- Launcher
- Desktop

---

## Mnemonic Tools

Location:

```text
applications/mnemonic-tools/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- mnemonic validation
- checksum verification
- mnemonic diagnostics
- BIP39 operations

Launch Methods:

- Launcher
- Desktop

---

## Path Explorer

Location:

```text
applications/path-explorer/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- derivation path analysis
- BIP traversal
- path discovery
- address derivation verification

Launch Methods:

- Launcher
- Desktop

---

## Address Scanner

Location:

```text
applications/address-scanner/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- address discovery
- address verification
- scanning workflows
- reporting support

Launch Methods:

- Launcher
- Desktop

---

# Interface Modules

## SeedTools Desktop

Location:

```text
applications/seedtools-desktop/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- graphical user interface
- guided interactions
- visual workflows
- primary desktop experience

Launch Methods:

- Launcher

---

## SeedTools CLI

Location:

```text
applications/seedtools-cli/
```

Documentation:

```text
README.md
roadmap.md
```

Responsibilities:

- command-line operations
- scripting support
- automation workflows
- advanced user access

Launch Methods:

- Launcher
- Terminal

---

# Launcher Module

## Suite Launcher

Location:

```text
applications/suite-launcher/
```

Documentation:

```text
README.md
roadmap.md
launcher-architecture.md
launcher-modules.md
```

Responsibilities:

- application discovery
- module registry
- navigation
- workflow orchestration
- documentation access
- suite-wide settings

This module acts as the central entry point for the entire SeedTools Suite.

---

# Guided Workflow Registry

## Recovery Mode

Workflow:

```text
Mnemonic Tools
    ↓
Recovery Tool
    ↓
Path Explorer
    ↓
Address Verification
```

---

## Forensics Mode

Workflow:

```text
Entropy Inspector
    ↓
Forensics Tool
    ↓
Address Scanner
```

---

## Address Verification Mode

Workflow:

```text
Path Explorer
    ↓
Address Scanner
```

---

## Entropy Diagnostics Mode

Workflow:

```text
Entropy Inspector
    ↓
Mnemonic Tools
```

---

# Documentation Modules

Suite Launcher provides centralized access to:

## Architecture

- System Architecture
- Trust Boundaries
- Data Flow
- DFD Documentation

## Security

- Threat Model
- Security Model
- Attack Surface
- Hardened Mode
- Memory Model
- Reproducible Builds

## Product

- Product Overview
- Product Architecture
- Product Components
- Product Specification

## Financing

- OpenSats
- HRF
- BTCPay
- Spiral
- FUTO

---

# Shared Services

## Preset Manager

Provides:

- BIP presets
- wallet presets
- NGO presets
- recovery profiles

---

## Documentation Hub

Provides:

- offline documentation
- manuals
- guides
- release notes

---

## Settings Manager

Provides:

- theme configuration
- language selection
- offline mode
- hardened mode

---

# Future Modules

Potential future modules:

- Reporting Center
- Export Center
- Automation Engine
- Session Manager
- Cross-App Sync Layer
- Workflow Marketplace

---

# Registry Principles

All Suite modules should be:

- deterministic
- offline-first
- discoverable
- independently maintainable
- version-aware

Suite Launcher serves as the unified access layer while keeping all functional modules isolated and modular.

---

# Long-Term Vision

Suite Launcher evolves into the central control plane of SeedTools Suite.

It provides:

- unified navigation
- workflow orchestration
- application discovery
- documentation access
- shared settings
- future automation capabilities

while maintaining the SeedTools philosophy of transparency, determinism, privacy, and reproducibility.
