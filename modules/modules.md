# 🧩 **SeedTools Suite — Module Documentation**  

---

## 🔐 **SeedTools Core** — Deterministic Cryptographic Engine

SeedTools Core is the **foundational engine** of the entire Suite.

> “SeedTools Core is the **foundational engine** of the entire SeedTools Suite.”  

### **Purpose**
It provides deterministic, offline‑safe cryptographic primitives used by all applications:

- Recovery Tool  
- Forensics Tool  
- Address Scanner  
- Entropy Inspector  
- Mnemonic Tools  
- Path Explorer  
- Desktop & CLI  

### **Key Capabilities**
- BIP39 mnemonic ↔ entropy  
- BIP32 hardened/non‑hardened derivation  
- BIP44/49/84/86 path logic  
- Address generation (P2PKH, P2SH‑P2WPKH, P2WPKH, P2TR)  
- Entropy drift & checksum tools  
- Secure memory handling  

> “It is designed to be modular, deterministic, offline‑first, auditable, secure.”

### **Architecture**
- Mnemonic Module  
- Entropy Module  
- Derivation Module  
- Path Module  
- Address Module  
- Utils Module  

### **Typical Workflows**
- mnemonic → entropy  
- seed → path → derived key  
- derived key → address  
- path validation  

---

## 🧰 **SeedTools Utils** — Shared Utility Layer

SeedTools Utils is the **shared utility library** used across all modules.

> “SeedTools Utils is the **shared utility library** used across all modules and applications.”

### **Key Capabilities**
- Validation utilities (mnemonics, entropy, paths, addresses)  
- Cryptographic helpers (SHA‑256, HMAC‑SHA512, secure buffers)  
- Encoding/decoding (Base58, Bech32, hex)  
- Formatting utilities  
- Unified error framework  
- Secure memory helpers  

### **Architecture**
- Validation Layer  
- Crypto Layer  
- Formatting Layer  
- Error Layer  
- Integration Layer  

> “It is the **glue layer** that keeps the entire Suite coherent and maintainable.”

### **Typical Workflows**
- mnemonic validation  
- address encoding  
- CLI output formatting  
- zeroizing sensitive data  

---

## 🖥 **SeedTools GUI** — Secure UI Framework

SeedTools GUI is the **shared graphical interface layer** for all visual applications.

> “SeedTools GUI is the **shared graphical interface layer** used across all SeedTools applications.”

### **Key Capabilities**
- Unified component library  
- Secure input components (masked mnemonic fields, zeroized buffers)  
- Workflow engine UI  
- Preset‑aware UI  
- Offline‑first rendering  

### **Architecture**
- Core UI Layer  
- Component Layer  
- Secure Components Layer  
- Workflow Layer  
- Integration Layer  

### **Typical Workflows**
- building new screens  
- creating guided workflows  
- implementing preset‑aware screens  

> “It is the **visual foundation** of the SeedTools ecosystem.”

---

## 🖥‍💻 **SeedTools CLI Module** — Deterministic CLI Engine

SeedTools CLI Module powers the entire command‑line interface.

> “SeedTools CLI Module provides the **programmatic and internal engine** behind the SeedTools command‑line interface.”

### **Key Capabilities**
- Command router  
- Mnemonic Tools CLI  
- Entropy Inspector CLI  
- Recovery Engine CLI  
- Address Scanner CLI  
- Path Explorer CLI  
- Forensics Mode Engine  
- Secure execution layer  

### **Architecture**
- Command Layer  
- Execution Layer  
- Integration Layer  
- Output Layer  

### **Typical Workflows**
- mnemonic validation  
- recovery scans  
- forensics analysis  

> “It is the **engine** behind all CLI‑based operations in the Suite.”

---

# 🔗 **Module Interactions**

```
SeedTools Core  ← used by ←  Utils
SeedTools Core  ← used by ←  CLI
SeedTools Core  ← used by ←  GUI

Utils ← used by ← Core, CLI, GUI
GUI  ← used by ← Desktop, Tools
CLI  ← used by ← Desktop, Automation
```

---
