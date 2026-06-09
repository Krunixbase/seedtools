# 🛡️ **Hardened Mode — SeedTools Security Documentation**

Hardened Mode is the highest‑security execution mode in SeedTools Suite.  
It is designed for **air‑gapped systems**, **NGO field operations**, **forensics**, **cold wallets**, and **high‑risk environments** where the host OS cannot be trusted.

This document describes:

- what Hardened Mode is  
- what it disables  
- what it enforces  
- how modules must behave  
- how developers should implement hardened‑safe features  

---

## 1. 🎯 Purpose of Hardened Mode

Hardened Mode exists to:

- eliminate all persistent traces  
- prevent accidental data leakage  
- reduce OS‑level attack surface  
- enforce deterministic, offline‑only execution  
- protect high‑risk users from compromised environments  

It is **not optional** for:

- forensics workflows  
- NGO emergency recovery  
- air‑gapped key generation  
- regulated environments  

---

## 2. 🔒 Hardened Mode Guarantees

When Hardened Mode is active, SeedTools guarantees:

- **no disk writes**  
- **no logs**  
- **no caching**  
- **no clipboard usage**  
- **no shell history (CLI)**  
- **no temporary files**  
- **no external assets**  
- **no network operations**  
- **deterministic execution**  
- **ephemeral memory only**  
- **zeroization of sensitive buffers**  

See also: **Security Guide**.

---

## 3. 🚫 What Hardened Mode Disables

### 3.1 Disk Writes  
All modules must avoid:

- writing to disk  
- creating temp files  
- using OS‑level caches  
- writing logs  

### 3.2 Clipboard  
Clipboard access is disabled to prevent:

- clipboard sniffers  
- malware injection  
- accidental seed exposure  

### 3.3 Logging  
No logs are written, even sanitized ones.

### 3.4 Shell History (CLI)  
CLI commands are not recorded in:

- `.bash_history`  
- `.zsh_history`  
- PowerShell history  

### 3.5 GUI Animations  
Animations are disabled to:

- reduce side‑channel timing noise  
- improve determinism  
- avoid GPU‑based leaks  

### 3.6 External Assets  
Forbidden:

- fonts  
- images  
- scripts  
- remote resources  

---

## 4. ✔️ What Hardened Mode Enforces

### 4.1 Deterministic Execution  
Same input → same output, across all platforms.

### 4.2 Ephemeral Memory  
Sensitive data must live only in:

- stack variables  
- short‑lived buffers  
- zeroized bytearrays  

### 4.3 Zero‑Trace Rendering (GUI)  
GUI components must:

- avoid caching  
- avoid persistent state  
- avoid OS‑level rendering buffers  

### 4.4 Strict Input Validation  
All user input must be validated before:

- parsing  
- derivation  
- entropy scoring  
- address generation  

### 4.5 No Background Tasks  
No async tasks unless deterministic and memory‑safe.

---

## 5. 🧱 Module‑Level Requirements

### 5.1 Core (seedtools_core)
Core must:

- never write to disk  
- never use randomness except cryptographic entropy  
- zeroize all sensitive buffers  
- avoid global state  
- remain deterministic  

See: **Core API**.

---

### 5.2 Utils (seedtools_utils)
Utils must:

- avoid OS‑dependent behavior  
- avoid caching  
- avoid non‑deterministic formatting  
- sanitize all external data  

See: **Utils API**.

---

### 5.3 CLI (seedtools_cli)
CLI must:

- disable shell history  
- avoid printing sensitive data  
- avoid logs  
- avoid temp files  
- avoid interactive prompts that leak state  

See: **CLI API**.

---

### 5.4 GUI (seedtools_gui)
GUI must:

- disable animations  
- disable clipboard  
- use isolated secure components  
- avoid OS‑level rendering caches  
- zeroize input fields  

See: **GUI API**.

---

## 6. 🧪 Testing Hardened Mode

Every module must include hardened‑mode tests:

- no disk writes  
- no logs  
- no clipboard calls  
- no nondeterministic behavior  
- no OS‑dependent output  
- no persistent state  

Example test categories:

- hardened‑mode CLI execution  
- hardened GUI rendering  
- zeroization tests  
- deterministic output tests  

---

## 7. 🧬 Threat Model Alignment

Hardened Mode mitigates:

- clipboard sniffers  
- malware reading temp files  
- shell history leaks  
- OS‑level caching  
- accidental seed exposure  
- timing‑based UI leaks  

It **cannot** mitigate:

- compromised OS  
- hardware keyloggers  
- BIOS/UEFI implants  
- physical access attacks  

See: **Security Guide**.

---

## 8. 🛠 Developer Guidelines

When writing hardened‑safe code:

### ✔ Avoid:
- global state  
- caching  
- temp files  
- OS‑dependent behavior  
- nondeterministic functions  
- background threads  

### ✔ Use:
- ephemeral buffers  
- deterministic algorithms  
- explicit zeroization  
- pure functions  
- strict validation  

### ✔ Always test:
- deterministic output  
- memory cleanup  
- no side effects  

---

## 9. 📚 Related Documentation

- **Security Guide**  
- **Memory Model**  
- **Reproducible Builds**  
- **Architecture Diagram**  
- **Data Flow Diagram**  

---

