# 📘 **SECURITY.md — SeedTools Suite**

## **Security Policy**

SeedTools Suite is designed for **offline‑first**, **deterministic**, and **high‑security environments**.  
The application does not transmit, store, or sync sensitive data and is safe to use in air‑gapped systems.

This document describes:

- supported security guarantees  
- known limitations  
- responsible disclosure  
- operational security recommendations  

---

## **Supported Versions**

SeedTools follows a rolling‑release model.  
Only the **latest stable release** receives:

- security patches  
- cryptographic updates  
- dependency updates  

Older versions should not be used in production or regulated environments.

---

## **Security Guarantees**

SeedTools provides the following guarantees:

- **No networking** — no API calls, no telemetry, no cloud  
- **No seed storage** — mnemonics, seed hex, and keys never touch disk  
- **Deterministic execution** — same input → same output  
- **Offline‑first architecture** — safe for air‑gapped workflows  
- **No clipboard usage** — eliminates clipboard hijacking  
- **Zero‑trust design** — OS, hardware, and environment are not trusted  
- **Memory zeroization** — sensitive data cleared where possible  
- **No offensive capabilities** — cannot attack or brute‑force wallets  

For a full threat analysis, see **Threat Model**.

---

## **Security Limitations**

SeedTools cannot protect against:

- compromised operating systems  
- hardware keyloggers  
- malicious firmware  
- physical access attacks  
- supply‑chain hardware implants  

These risks require user‑side operational security.

For details, see **Security FAQ**.

---

## **Reporting a Vulnerability**

If you discover a security issue, please report it privately.

### **How to report**

Send an email to:

```
krunixbase@gmail.com
```

Include:

- description of the issue  
- steps to reproduce  
- affected version  
- potential impact  

We aim to respond within **72 hours**.

### **Do not:**

- open public GitHub issues  
- disclose vulnerabilities before coordinated release  
- share exploit details publicly  

---

## **Cryptographic Scope**

SeedTools implements:

- BIP32  
- BIP39  
- BIP44 / BIP49 / BIP84 / BIP86  
- SLIP‑44  
- Shamir Secret Sharing (SLIP‑39)  
- Taproot (BIP86)  

Cryptographic correctness is validated through:

- deterministic test vectors  
- entropy scoring  
- polynomial validation  
- hardened path enforcement  

For details, see **Cryptographic Threats**.

---

## **Operational Security Recommendations**

To ensure maximum safety:

### **Use SeedTools on a trusted device**
Avoid:

- infected systems  
- shared computers  
- cloud desktops  
- remote sessions  

### **Prefer offline / air‑gapped environments**
SeedTools is designed for:

- cold wallets  
- forensics  
- regulated environments  
- secure key generation  

### **Verify downloads**
Always verify:

- checksums  
- signatures  
- release source  

### **Never store seeds digitally**
Avoid:

- screenshots  
- notes apps  
- cloud backups  
- password managers  

### **Use strong entropy**
Weak seeds reduce security regardless of the tool.

---

## **Security Architecture Overview**

SeedTools is built on four layers:

1. **Input Controller** — validates and normalizes user input  
2. **Deterministic Core** — performs BIP derivations  
3. **Validation Layer** — entropy scoring, Shamir checks, Taproot rules  
4. **Presentation Layer** — offline rendering, no clipboard, no logs  

For a full diagram, see **DFD (Data Flow Diagram)**.

---

## **Residual Risks**

Even with SeedTools, the following risks remain:

- OS‑level compromise  
- hardware implants  
- malicious BIOS/UEFI  
- physical theft  
- user mistakes  
- weak entropy  

These are outside the scope of any offline cryptographic tool.

---

## **Final Notes**

SeedTools is designed to be:

- safe  
- deterministic  
- offline  
- transparent  
- auditable  

But **security always depends on the environment**.  
A compromised system cannot be made safe by any application.

---
