 **SeedTools CLI — Roadmap**

## **Overview**

This roadmap defines the development plan for SeedTools CLI over the next 12 months.  
The focus is on deterministic recovery, batch forensics, automation, hardened offline workflows, JSON output, and deep integration with the GUI applications.

---

# **1. 3‑Month Roadmap — Foundation Phase**

- **CLI Core Engine v1** — unified command parser, offline‑first architecture, secure input handling  
- **Mnemonic Tools CLI** — validate mnemonics, convert entropy, inspect checksum  
- **Recovery Engine CLI MVP** — derive addresses, verify ownership, scan index ranges  
- **Address Scanner CLI** — single‑address and batch verification  
- **Path Explorer CLI** — derive keys for any path, validate BIP32/44/49/84/86  
- **Documentation v1** — usage examples, command reference, offline workflows  

---

# **2. 6‑Month Roadmap — Expansion Phase**

- **Batch Forensics Engine** — analyze multiple mnemonics, entropy sets, or paths at once  
- **Taproot‑Specific CLI Tools** — BIP86 path validation, Taproot address generation  
- **JSON Output Mode** — machine‑readable output for automation and scripting  
- **Wallet Presets** — Sparrow, Specter, Electrum, BTCPay‑style presets  
- **UX & Safety Enhancements** — no‑history mode, ephemeral session mode, safer prompts  
- **Export Module** — export paths, addresses, and reports in structured formats  

---

# **3. 12‑Month Roadmap — PRO Phase**

- **CLI Hardened Mode for Tails/Qubes** — memory‑safe mode, no disk writes, secure temp buffers  
- **Full Forensics Mode PRO** — entropy drift maps, anomaly scoring, corruption classification  
- **Mixed‑Type Wallet Detection** — detect wallets using multiple BIP standards  
- **Interoperability Layer** — compatibility with wallet metadata formats  
- **Integration with GUI Apps** — shared engines, shared presets, unified export formats  
- **Reproducible Builds** — deterministic builds + verification instructions  

---

# **Long‑Term Vision**

SeedTools CLI becomes the **standard offline command‑line toolkit** for Bitcoin:

- trusted by NGOs and support teams  
- used by developers for testing and automation  
- safe for high‑risk users in hostile environments  
- fully auditable and reproducible  
- maintained as a long‑term public good  

---
