# Security Model — SeedTools Suite

SeedTools Suite is designed as an **offline‑first, deterministic, auditable Bitcoin recovery toolkit**.  
This document outlines the security assumptions, guarantees, and limitations of the project.

---

## 1. Threat Model

SeedTools is built for users operating in:

- high‑risk or authoritarian environments  
- situations involving device loss, confiscation, or corruption  
- NGO workflows requiring offline verification  
- recovery scenarios where privacy and safety are critical  

SeedTools **does not** assume a trusted network environment.  
SeedTools **does** assume the user controls their local machine.

---

## 2. Core Security Principles

### **Offline‑First Architecture**
All core recovery and forensics tools operate **without internet access**.  
No external API calls, no telemetry, no remote dependencies.

### **Deterministic Behavior**
Given the same inputs, SeedTools always produces the same outputs.  
This ensures:

- auditability  
- reproducibility  
- predictable behavior in critical scenarios  

### **No Key Storage**
SeedTools never stores:

- seeds  
- private keys  
- entropy  
- derived keys  
- scanned addresses  

All sensitive data stays in memory only for the duration of the operation.

### **User Sovereignty**
The user retains full control over:

- seed phrases  
- derivation paths  
- scanning ranges  
- output formats  

SeedTools never sends or uploads anything.

---

## 3. What SeedTools Guarantees

- no network communication in core tools  
- no telemetry or analytics  
- deterministic, reproducible operations  
- transparent, open‑source code  
- offline workflows suitable for NGOs and high‑risk users  

---

## 4. What SeedTools Does NOT Guarantee

SeedTools is **not**:

- a wallet  
- a key manager  
- a seed generator  
- a secure enclave  
- a hardware security module  

SeedTools does **not** protect against:

- compromised operating systems  
- malware on the user’s device  
- physical surveillance  
- keyloggers  
- supply‑chain attacks on Python or OS packages  

Users must operate SeedTools on a trusted machine.

---

## 5. Recommended Usage for High‑Risk Users

- run SeedTools on an **air‑gapped machine**  
- verify checksums and signatures  
- avoid copy/paste of sensitive data  
- use temporary RAM‑only environments when possible  
- clear shell history after use  

---

## 6. Reproducible Builds

SeedTools aims to provide:

- reproducible Python environments  
- pinned dependencies  
- deterministic build scripts  

This ensures that independent parties can verify that distributed binaries match the source code.

---

## 7. NGO‑Ready Workflows

SeedTools supports:

- offline verification  
- printable reports  
- deterministic audit trails  
- transparent recovery steps  

These workflows are designed for NGOs handling sensitive Bitcoin operations.

---

## 8. Future Security Improvements

Planned enhancements:

- Safe Mode (restricted offline environment)  
- reproducible builds v2  
- independent security review  
- hardened CLI workflows  
- sandboxed execution modes  

---

## 9. Contact

For security questions or responsible disclosure:

**krunixbase@gmail.com**
