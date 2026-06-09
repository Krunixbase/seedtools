# 🧠 **SeedTools Memory Model — Security Documentation**

SeedTools Suite uses a strict, deterministic, zero‑trust memory model designed for high‑risk environments, including air‑gapped systems, NGO field operations, forensics, and cold‑wallet workflows.

This document explains:

- how memory is allocated  
- how sensitive data is handled  
- how zeroization works  
- what developers must follow  
- how modules must behave in hardened environments  

---

## 1. 🎯 Memory Model Goals

SeedTools memory handling is designed to:

- eliminate residual data  
- prevent OS‑level leakage  
- avoid caching  
- ensure deterministic behavior  
- protect mnemonics, entropy, seeds, and keys  
- support hardened mode and forensics workflows  

The model assumes **zero trust** in:

- the operating system  
- the hardware  
- the environment  

---

## 2. 🔐 Core Principles

SeedTools memory model is based on five principles:

### ✔ Ephemeral memory  
Sensitive data lives only in short‑lived buffers.

### ✔ Zeroization  
Buffers are wiped immediately after use.

### ✔ No persistence  
No disk writes, no temp files, no caching.

### ✔ Deterministic allocation  
Memory usage must not depend on OS‑specific behavior.

### ✔ Isolation  
Sensitive data must not mix with UI state, logs, or CLI output.

See also: **Hardened Mode**.

---

## 3. 🧩 Memory Zones in SeedTools

SeedTools defines three memory zones:

```
+---------------------------+
|  Zone 1: Sensitive Data   |
|  - mnemonics              |
|  - entropy                |
|  - seeds                  |
|  - private keys           |
|  - Shamir shares          |
+---------------------------+
              |
              v
+---------------------------+
|  Zone 2: Derived Data     |
|  - xprv/xpub              |
|  - addresses              |
|  - entropy scores         |
|  - validation results     |
+---------------------------+
              |
              v
+---------------------------+
|  Zone 3: Presentation     |
|  - UI components          |
|  - CLI output             |
|  - logs (disabled)        |
+---------------------------+
```

### Rules:

- Zone 1 must always be ephemeral and zeroized.  
- Zone 2 may exist briefly but must not persist.  
- Zone 3 must never contain sensitive data.

---

## 4. 🔒 Sensitive Data Handling

### 4.1 Mnemonics  
Stored only in:

- isolated buffers  
- masked GUI fields  
- CLI ephemeral variables  

Never stored in:

- logs  
- clipboard  
- disk  
- global state  

### 4.2 Entropy  
Entropy is:

- validated  
- scored  
- zeroized  

Entropy buffers must be overwritten after use.

### 4.3 Seeds (BIP32)  
Seeds must:

- never touch disk  
- never be cached  
- never be logged  
- be zeroized immediately after derivation  

### 4.4 Private Keys  
Private keys must:

- exist only in Zone 1  
- be zeroized after address generation  
- never be returned to UI unless explicitly required  

---

## 5. 🧼 Zeroization Rules

Zeroization must occur:

- after every sensitive operation  
- after every derivation  
- after every validation  
- before returning from functions  
- before freeing buffers  

### Allowed zeroization methods:

- overwriting bytearrays  
- overwriting lists  
- overwriting memoryviews  
- explicit del + GC trigger (fallback only)

### Forbidden:

- relying on Python garbage collector  
- relying on OS memory cleanup  
- leaving sensitive data in exceptions  

---

## 6. 🧪 Deterministic Memory Behavior

SeedTools must avoid:

- OS‑dependent memory allocation  
- nondeterministic buffer sizes  
- floating‑point operations  
- time‑based randomness  
- concurrency that affects memory layout  

Memory behavior must be identical across:

- Linux  
- macOS  
- Windows  
- WSL2  
- Tails  
- Qubes  

See: **Reproducible Builds**.

---

## 7. 🧱 Module‑Level Requirements

### 7.1 Core (seedtools_core)
Core must:

- use only deterministic buffers  
- avoid global state  
- zeroize all sensitive data  
- avoid Python objects that cannot be zeroized  

### 7.2 Utils (seedtools_utils)
Utils must:

- sanitize all external input  
- avoid caching  
- avoid OS‑dependent behavior  

### 7.3 CLI (seedtools_cli)
CLI must:

- avoid printing sensitive data  
- avoid storing data in shell history  
- avoid temp files  

### 7.4 GUI (seedtools_gui)
GUI must:

- isolate sensitive fields  
- zeroize input fields on close  
- avoid OS‑level rendering caches  

---

## 8. 🛠 Developer Guidelines

When writing code that handles sensitive data:

### ✔ Always:
- use bytearrays for sensitive data  
- zeroize buffers explicitly  
- isolate sensitive variables  
- avoid global state  
- avoid exceptions leaking secrets  

### ✔ Never:
- store sensitive data in strings  
- store sensitive data in logs  
- store sensitive data in UI state  
- rely on garbage collection  
- use clipboard  

---

## 9. 🧬 Threat Model Alignment

Memory model mitigates:

- clipboard sniffers  
- temp‑file malware  
- memory scraping  
- accidental leaks  
- nondeterministic behavior  
- OS caching  

It **cannot** mitigate:

- compromised OS  
- hardware implants  
- BIOS/UEFI malware  
- physical access attacks  

See: **Security Guide**.

---

## 10. 📚 Related Documentation

- **Hardened Mode**  
- **Security Guide**  
- **Reproducible Builds**  
- **Architecture Diagram**  
- **Data Flow Diagram**  

---
