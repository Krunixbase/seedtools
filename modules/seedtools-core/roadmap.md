# **SeedTools Core — Roadmap**

## **Overview**

SeedTools Core is the cryptographic and deterministic engine powering the entire SeedTools Suite.  
This roadmap defines its evolution over the next 12 months, focusing on security, determinism, performance, interoperability, and reproducibility.

---

# **1. 3‑Month Roadmap — Foundation Phase**

- **Core Engine v1** — stable BIP32/39/44/49/84/86 implementation, deterministic primitives, strict validation  
- **Entropy & Checksum Module** — entropy reconstruction, checksum verification, drift detection basics  
- **Address Generation Engine** — P2PKH, P2SH‑P2WPKH, P2WPKH, P2TR  
- **Path Logic v1** — parsing, validation, hardened markers, standard path rules  
- **Secure Memory Layer** — zeroization, ephemeral buffers, hardened mode support  
- **Documentation v1** — architecture, module structure, API reference  

---

# **2. 6‑Month Roadmap — Expansion Phase**

- **Taproot Derivation Engine** — BIP86 derivation, x-only keys, tweak logic  
- **Entropy Drift Engine** — bit‑level drift mapping, corruption scoring  
- **Wallet Metadata Interop Layer** — compatibility with Sparrow, Specter, Electrum, BTCPay metadata  
- **Performance Optimizations** — faster derivation, reduced allocations, optimized hashing  
- **Core Test Suite PRO** — deterministic vectors, fuzzing, cross‑wallet compatibility tests  
- **Core Export Module** — structured output for Desktop, CLI, and Suite Launcher  

---

# **3. 12‑Month Roadmap — PRO Phase**

- **Hardened Memory Engine PRO** — secure enclaves, locked memory pages, zero‑trace mode  
- **Mixed‑Wallet Detection Engine** — detect hybrid BIP44/49/84/86 wallets  
- **Cross‑Module Interoperability Layer** — unified data models for all apps  
- **Advanced Entropy Forensics** — corruption classification, entropy anomaly signatures  
- **Core PRO API** — stable API for external integrations and advanced tooling  
- **Reproducible Builds** — deterministic builds + verification instructions  

---

# **Long‑Term Vision**

SeedTools Core becomes the **industry‑standard deterministic engine** for Bitcoin recovery, forensics, and wallet diagnostics:

- trusted by NGOs and support teams  
- used by developers and wallet maintainers  
- safe for high‑risk users  
- fully offline and auditable  
- reproducible and verifiable  
- the cryptographic backbone of the entire SeedTools ecosystem  

---
