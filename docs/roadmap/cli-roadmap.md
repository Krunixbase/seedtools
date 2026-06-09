# 🧭 **SeedTools CLI — Roadmap (12‑Month Plan)**

SeedTools CLI (`seedtools_cli/`) is the deterministic command‑line engine powering all non‑GUI workflows in the SeedTools Suite.  
It is designed for:

- air‑gapped systems  
- forensics workflows  
- automation  
- scripting  
- hardened‑mode environments  
- deterministic recovery pipelines  

This roadmap defines the development plan for the next 3, 6, and 12 months.

---

# 1. 🎯 Vision

SeedTools CLI aims to be:

- **the most deterministic Bitcoin CLI toolkit available**  
- **fully hardened‑mode compatible**  
- **safe for high‑risk users and forensics teams**  
- **modular, predictable, and script‑friendly**  
- **zero‑clipboard, zero‑logging, zero‑side‑effects**  

CLI must remain:

- pure Python  
- deterministic  
- offline‑first  
- reproducible  
- dependency‑minimal  

---

# 2. 🗂 CLI Architecture Overview

- **Modules Documentation**  
- **Security Guide**  
- **Hardened Mode**  

---

# 3. 🚀 3‑Month Roadmap (Q1)

## 3.1 CLI Engine v1  
- deterministic command execution  
- unified argument parser  
- strict validation layer  
- no auto‑processing  
- no hidden state  

## 3.2 Command Router v1  
- deterministic routing  
- consistent command naming  
- predictable error handling  

## 3.3 Output Engine v1  
- deterministic formatting  
- no ANSI color in hardened mode  
- no clipboard  
- no logs  

## 3.4 Core Commands v1  
- mnemonic validate  
- mnemonic normalize  
- entropy score  
- seed derive  
- address generate  

## 3.5 Hardened Mode (CLI Layer)  
- disable shell history  
- disable clipboard  
- disable temp files  
- disable verbose errors  

## 3.6 Documentation v1  
- CLI API  
- command reference  
- usage examples  

→ **Generate CLI API**

---

# 4. 🔥 6‑Month Roadmap (Q2)

## 4.1 Forensics CLI v1  
- corrupted mnemonic detection  
- entropy anomaly detection  
- partial seed inference  
- Shamir share validation  

## 4.2 Workflow Engine v1  
- multi‑step CLI workflows  
- deterministic state machine  
- no background tasks  

## 4.3 Metadata CLI Tools  
- fingerprint extraction  
- derivation path inference  
- wallet metadata normalization  

## 4.4 Taproot CLI Tools  
- BIP86 validation  
- Taproot address generation  
- tweak inspection  

## 4.5 CLI Test Suite PRO  
- deterministic test vectors  
- hardened‑mode tests  
- cross‑platform reproducibility tests  

---

# 5. 🛡 12‑Month Roadmap (Q3–Q4)

## 5.1 Forensics CLI v2  
- corrupted entropy reconstruction  
- partial mnemonic inference  
- Shamir share forensics  
- entropy drift reconstruction  

## 5.2 Recovery CLI Engine  
- multi‑workflow recovery  
- deterministic recovery pipelines  
- reproducible recovery outputs  

## 5.3 Deterministic Export Engine  
- reproducible JSON exports  
- deterministic address lists  
- deterministic metadata dumps  

## 5.4 Multi‑Wallet Compatibility CLI  
- Electrum  
- Sparrow  
- Specter  
- BlueWallet  
- Liana (Taproot multisig)  

## 5.5 CLI Reproducible Build Pipeline  
- deterministic packaging  
- deterministic hashing  
- multi‑platform reproducibility  

→ **Reproducible Builds**

---

# 6. 🧩 Dependencies & Constraints

SeedTools CLI must remain:

- deterministic  
- offline‑first  
- hardened‑mode compatible  
- reproducible  
- dependency‑minimal  

Forbidden:

- external CLI libraries  
- OS randomness  
- floating‑point math  
- nondeterministic formatting  
- global mutable state  
- auto‑processing  

---

# 7. 📚 Related Documentation

- **Core Roadmap**  
- **GUI Roadmap**  
- **Utils Roadmap**  
- **Security Guide**  
- **Memory Model**  
- **Hardened Mode**  

---
