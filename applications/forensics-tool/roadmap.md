# **Forensics Tool — Roadmap**

## **Overview**

This roadmap defines the development plan for the Forensics Tool over the next 12 months.
The focus is on mnemonic integrity analysis, entropy diagnostics, derivation‑path forensics, Taproot‑specific checks, NGO‑friendly reporting, and deep integration with the Recovery Tool.

---

# **1. 3‑Month Roadmap — Foundation Phase**

- **Mnemonic Integrity Engine v1** — checksum validation, wordlist conformity, invalid‑word detection
- **Entropy Inspector MVP** — entropy length checks, mismatch detection, drift preview
- **Path Forensics MVP** — detect wrong purpose/coin/account, identify non‑standard patterns
- **Address Ownership Diagnostics** — detect mismatch between seed and address type
- **Forensic Report v1** — structured offline‑safe report export
- **Documentation v1** — architecture, workflows, examples

---

# **2. 6‑Month Roadmap — Expansion Phase**

- **Advanced Entropy Drift Detection** — detect subtle entropy inconsistencies
- **Partial Mnemonic Reconstruction** — assist users with missing or corrupted words
- **Taproot Forensics** — BIP86‑specific checks, mismatch detection, path validation
- **Wallet Metadata Analyzer** — analyze wallet files (Sparrow, Specter, Electrum) for path inconsistencies
- **Deep Path Forensics Engine** — extended index ranges, multi‑account anomaly detection
- **UX Enhancements** — clearer warnings, risk indicators, guided explanations

---

# **3. 12‑Month Roadmap — PRO Phase**

- **Forensics Mode PRO** — full corruption analysis, entropy drift maps, anomaly scoring
- **Compromised Device Workflow** — safe workflows for confiscated or tampered devices
- **NGO‑Friendly Forensic Reports** — printable, field‑safe, minimal‑metadata reports
- **Interoperability Layer** — compatibility with wallet metadata formats
- **Integration with Recovery Tool** — automatic anomaly detection during recovery
- **Reproducible Builds** — deterministic builds + verification instructions

---

# **Long‑Term Vision**

Forensics Tool becomes the **standard offline diagnostic toolkit** for Bitcoin:

- trusted by NGOs and support teams
- used by wallet developers to validate derivation logic
- safe for high‑risk users
- fully auditable and reproducible
- a long‑term public good for the Bitcoin ecosystem

---

