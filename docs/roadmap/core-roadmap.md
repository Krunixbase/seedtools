# 🧭 **SeedTools Core — Roadmap (12‑Month Plan)**

SeedTools Core is the deterministic cryptographic engine powering the entire SeedTools Suite.  
It implements BIP standards, entropy tools, address generation, validation logic, and deterministic workflows used across CLI, GUI, and forensics modules.

This roadmap defines the development plan for the next 3, 6, and 12 months.

---

# 1. 🎯 Vision

SeedTools Core aims to be:

- **the most deterministic Bitcoin derivation engine available**  
- **fully auditable and reproducible**  
- **offline‑first and hardened‑mode compatible**  
- **modular and dependency‑minimal**  
- **safe for high‑risk users and forensics workflows**  

Core must remain:

- pure Python  
- deterministic  
- reproducible  
- zero‑trust  
- zero‑side‑effects  

---

# 2. 🗂 Core Architecture Overview

- **[Architecture Diagrams](../architecture/diagrams.md)**  
- **[Module Documentation](../modules.md)**  
- **[Security Guide](../guides/security.md)**  

---

# 3. 🚀 3‑Month Roadmap (Q1)

## 3.1 Core Engine v1 Stabilization  
- finalize deterministic BIP32 engine  
- finalize BIP39 → entropy → seed pipeline  
- finalize BIP44/49/84/86 derivation logic  
- unify error types across modules  
- remove all nondeterministic code paths  

## 3.2 Entropy & Checksum Module  
- entropy scoring v1  
- checksum validation v1  
- wordlist validation  
- formatting normalization  

## 3.3 Address Generation Engine  
- P2PKH  
- P2WPKH  
- P2SH‑wrapped SegWit  
- Taproot (BIP86) basic support  

## 3.4 Path Logic v1  
- strict path validation  
- hardened path enforcement  
- deterministic path parsing  

## 3.5 Secure Memory Layer  
- ephemeral buffers  
- zeroization utilities  
- deterministic bytearray handling  

## 3.6 Documentation v1  
- Core API  
- entropy docs  
- derivation docs  

→ **Generate Core API**

---

# 4. 🔥 6‑Month Roadmap (Q2)

## 4.1 Taproot Derivation Engine (Advanced)  
- full BIP86 compliance  
- tweak logic  
- scriptless scripts support (non‑interactive)  
- deterministic keypath rules  

## 4.2 Entropy Drift Engine  
- entropy drift detection  
- entropy anomaly scoring  
- multi‑source entropy comparison  
- Shamir share entropy validation  

## 4.3 SLIP‑39 (Shamir Secret Sharing)  
- polynomial validation  
- share reconstruction  
- threshold enforcement  
- deterministic share ordering  

## 4.4 Wallet Metadata Interop Layer  
- xpub/xprv normalization  
- fingerprint validation  
- derivation path inference  
- wallet compatibility matrix  

## 4.5 Performance Optimizations  
- bytearray‑based operations  
- optimized hashing  
- reduced allocations  
- deterministic caching (in‑memory only)  

## 4.6 Core Test Suite PRO  
- 100% deterministic test vectors  
- cross‑wallet compatibility tests  
- entropy drift tests  
- Taproot test vectors  

---

# 5. 🛡 12‑Month Roadmap (Q3–Q4)

## 5.1 Full Cryptographic Auditability  
- reproducible test vectors  
- deterministic build verification  
- cross‑platform reproducibility tests  

## 5.2 Advanced Forensics Engine  
- corrupted mnemonic recovery  
- entropy reconstruction  
- partial seed inference  
- Shamir share forensics  

## 5.3 Multi‑Wallet Compatibility Layer  
- Electrum  
- Sparrow  
- Specter  
- BlueWallet  
- Liana (Taproot multisig)  

## 5.4 Deterministic Export Engine  
- reproducible JSON exports  
- deterministic address lists  
- deterministic metadata dumps  

## 5.5 Zero‑Knowledge Validation (Exploratory)  
- checksum proofs  
- entropy proofs  
- derivation path proofs  

## 5.6 Full Reproducible Build Pipeline  
- deterministic packaging  
- deterministic hashing  
- multi‑platform reproducibility  

→ **Reproducible Builds**

---

# 6. 🧩 Dependencies & Constraints

SeedTools Core must remain:

- dependency‑minimal  
- pure Python  
- deterministic  
- offline‑first  
- hardened‑mode compatible  
- reproducible across OSes  

Forbidden:

- external crypto libraries  
- OS randomness  
- floating‑point math  
- nondeterministic hashing  
- global mutable state  

---

# 7. 📚 Related Documentation

- **[Security Guide](../guides/security.md)**  
- **[Memory Model](../security/memory-model.md)**  
- **[Hardened Mode](../security/hardened-mode.md)**  
- **[Modules Documentation](../modules.md)**  
- **[CLI Roadmap](../roadmap/cli-roadmap.md)**  
- **[Utils Roadmap](../roadmap/utils-roadmap.md)**  
- **[GUI Roadmap](../roadmap/gui-roadmap.md)**  

---
