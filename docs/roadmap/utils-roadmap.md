# 🧭 **SeedTools Utils — Roadmap (12‑Month Plan)**

SeedTools Utils is the shared deterministic utility layer used across Core, CLI, GUI, and all SeedTools tools.  
It provides validation, encoding, formatting, hashing, error handling, and deterministic helper functions.

This roadmap defines the development plan for the next 3, 6, and 12 months.

---

# 1. 🎯 Vision

SeedTools Utils aims to be:

- **the deterministic backbone** of all SeedTools modules  
- **dependency‑minimal and reproducible**  
- **security‑first and hardened‑mode compatible**  
- **fully deterministic across OSes**  
- **safe for high‑risk and air‑gapped environments**  

Utils must remain:

- pure Python  
- deterministic  
- offline‑first  
- zero‑trust  
- zero‑side‑effects  

---

# 2. 🗂 Utils Architecture Overview

- **Modules Documentation**  
- **Security Guide**  
- **Memory Model**  

---

# 3. 🚀 3‑Month Roadmap (Q1)

## 3.1 Validation Engine v1  
- strict derivation path validation  
- mnemonic formatting validation  
- entropy formatting validation  
- address format validation  
- deterministic error messages  

## 3.2 Encoding Layer v1  
- deterministic hex encoding/decoding  
- deterministic base58/base32 encoding  
- no OS‑dependent behavior  
- no floating‑point operations  

## 3.3 Crypto Utils v1  
- deterministic hashing wrappers  
- HMAC utilities  
- bytearray‑based operations  
- zeroization helpers  

## 3.4 Formatting Engine v1  
- deterministic whitespace normalization  
- deterministic mnemonic normalization  
- deterministic path normalization  

## 3.5 Unified Error Layer  
- deterministic error types  
- non‑verbose, non‑leaking messages  
- hardened‑mode safe  

## 3.6 Documentation v1  
- Utils API  
- validation docs  
- formatting docs  

→ **Generate Utils API**

---

# 4. 🔥 6‑Month Roadmap (Q2)

## 4.1 Validation Engine v2  
- Shamir share validation  
- Taproot keypath validation  
- entropy drift validation  
- wallet metadata validation  

## 4.2 Encoding Layer v2  
- deterministic SLIP‑39 encoding  
- deterministic Shamir polynomial encoding  
- deterministic metadata encoding  

## 4.3 Crypto Utils v2  
- optimized hashing  
- deterministic multi‑hash engine  
- entropy drift hashing  
- deterministic fingerprinting  

## 4.4 Formatting Engine v2  
- deterministic address formatting  
- deterministic metadata formatting  
- deterministic Shamir formatting  

## 4.5 Forensics Utilities v1  
- corrupted mnemonic detection  
- entropy anomaly detection  
- partial seed inference helpers  

## 4.6 Utils Test Suite PRO  
- deterministic test vectors  
- cross‑wallet compatibility tests  
- entropy drift tests  
- Shamir validation tests  

---

# 5. 🛡 12‑Month Roadmap (Q3–Q4)

## 5.1 Forensics Utilities v2  
- corrupted entropy reconstruction  
- partial mnemonic inference  
- Shamir share forensics  
- entropy drift reconstruction  

## 5.2 Metadata Inference Engine  
- wallet fingerprint inference  
- derivation path inference  
- address type inference  
- Taproot metadata inference  

## 5.3 Deterministic Export Engine  
- reproducible JSON exports  
- deterministic metadata dumps  
- deterministic address lists  

## 5.4 Reproducible Formatting Engine  
- byte‑for‑byte deterministic formatting  
- cross‑platform reproducibility  
- hardened‑mode formatting rules  

## 5.5 Utils Reproducible Build Pipeline  
- deterministic packaging  
- deterministic hashing  
- multi‑platform reproducibility  

→ **Reproducible Builds**

---

# 6. 🧩 Dependencies & Constraints

SeedTools Utils must remain:

- deterministic  
- offline‑first  
- hardened‑mode compatible  
- reproducible  
- dependency‑minimal  

Forbidden:

- external crypto libraries  
- OS randomness  
- floating‑point math  
- nondeterministic hashing  
- global mutable state  
- auto‑formatting that changes output unpredictably  

---

# 7. 📚 Related Documentation

- **Core Roadmap**  
- **GUI Roadmap**  
- **CLI Roadmap**  
- **Security Guide**  
- **Memory Model**  
- **Hardened Mode**  

---
