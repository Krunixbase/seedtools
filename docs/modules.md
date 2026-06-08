# 🧩 SeedTools Suite — Module Documentation

This document provides a complete overview of all modules in the SeedTools Suite.  
Each module is deterministic, offline‑safe, auditable, and designed for high‑risk environments.

---

# 🔐 SeedTools Core

SeedTools Core is the **foundational cryptographic engine** of the entire Suite.

## Overview
It provides deterministic, offline‑safe primitives used by all applications:

- Recovery Tool
- Forensics Tool
- Address Scanner
- Entropy Inspector
- Mnemonic Tools
- Path Explorer
- SeedTools Desktop
- SeedTools CLI

## Responsibilities
- BIP39 mnemonic ↔ entropy
- BIP32 hardened/non‑hardened derivation
- BIP44/49/84/86 path logic
- Address generation (P2PKH, P2SH‑P2WPKH, P2WPKH, P2TR)
- Entropy drift & checksum tools
- Secure memory handling

## Architecture
- Mnemonic Module  
- Entropy Module  
- Derivation Module  
- Path Module  
- Address Module  
- Utils Module  

## Typical Workflows
- mnemonic → entropy  
- seed → path → derived key  
- derived key → address  
- path validation  

## Security
- no network operations  
- ephemeral memory  
- hardened mode  
- deterministic cryptography  

---

# 🧰 SeedTools Utils

SeedTools Utils is the **shared utility layer** used across all modules.

## Overview
It provides foundational helpers, cryptographic wrappers, validation tools, and formatting utilities.

## Responsibilities
- Validation utilities (mnemonics, entropy, paths, addresses)
- Cryptographic helpers (SHA‑256, HMAC‑SHA512, secure buffers)
- Encoding/decoding (Base58, Bech32, hex)
- Formatting utilities
- Unified error framework
- Secure memory helpers

## Architecture
- Validation Layer  
- Crypto Layer  
- Formatting Layer  
- Error Layer  
- Integration Layer  

## Typical Workflows
- mnemonic validation  
- address encoding  
- CLI output formatting  
- zeroizing sensitive data  

## Security
- no external crypto dependencies  
- zeroization  
- ephemeral buffers  
- deterministic behavior  

---

# 🖥 SeedTools GUI

SeedTools GUI is the **shared graphical interface layer** for all visual applications.

## Overview
It provides reusable UI components, secure input widgets, workflow engines, and preset‑aware interfaces.

## Responsibilities
- unified component library  
- secure input components  
- workflow engine UI  
- preset‑aware UI  
- offline‑first rendering  

## Architecture
- Core UI Layer  
- Component Layer  
- Secure Components Layer  
- Workflow Layer  
- Integration Layer  

## Typical Workflows
- building new screens  
- creating guided workflows  
- implementing preset‑aware screens  

## Security
- no external fonts or assets  
- masked fields  
- isolated buffers  
- hardened UI mode  

---

# 🖥‍💻 SeedTools CLI Module

SeedTools CLI Module is the **internal engine** behind all CLI‑based operations.

## Overview
It powers the SeedTools CLI binary, automation workflows, embedded terminals, and NGO field tools.

## Responsibilities
- command router  
- mnemonic tools CLI  
- entropy inspector CLI  
- recovery engine CLI  
- address scanner CLI  
- path explorer CLI  
- forensics mode engine  
- secure execution layer  

## Architecture
- Command Layer  
- Execution Layer  
- Integration Layer  
- Output Layer  

## Typical Workflows
- mnemonic validation  
- recovery scans  
- forensics analysis  

## Security
- no telemetry  
- ephemeral memory  
- hardened mode  
- deterministic execution  

---

# 🔗 Cross‑Module Relationships

```
SeedTools Core  ← used by ←  Utils
SeedTools Core  ← used by ←  CLI
SeedTools Core  ← used by ←  GUI

Utils ← used by ← Core, CLI, GUI
GUI  ← used by ← Desktop, Tools
CLI  ← used by ← Desktop, Automation
```

---

# 🛡 Shared Security Principles

All modules follow:

- offline‑first architecture  
- deterministic operations  
- no network calls  
- no telemetry  
- ephemeral memory  
- hardened mode  
- reproducible builds  

---

# 🌍 Target Users

- developers  
- auditors  
- wallet maintainers  
- NGOs & support teams  
- high‑risk users  

---

# 📘 Versioning

This documentation reflects the current state of:

- SeedTools Core  
- SeedTools Utils  
- SeedTools GUI  
- SeedTools CLI Module  

Future modules will be added as the Suite expands.

---
