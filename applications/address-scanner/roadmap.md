# **Address Scanner — Roadmap**

## **Overview**

This roadmap defines the development plan for the Address Scanner over the next 12 months.
The focus is on deep derivation‑path scanning, multi‑address verification, wallet interoperability, Taproot improvements, and integration with the Recovery Tool.

---

# **1. 3‑Month Roadmap — Foundation Phase**

- **Deep Scan Engine v1** — extended index scanning, change 0/1 detection, multi‑account basics
- **Address Verification Engine** — match detection, path extraction, address‑type identification
- **Batch Scan MVP** — verify multiple addresses sequentially
- **BIP Standard Detection** — detect BIP44/49/84/86 and common wallet patterns
- **Documentation v1** — workflows, examples, architecture

---

# **2. 6‑Month Roadmap — Expansion Phase**

- **Multi‑Account Auto‑Detection** — detect multiple accounts automatically
- **Taproot Scanning Improvements** — BIP86‑specific path detection, mismatch diagnostics
- **Wallet Presets** — Sparrow, Specter, Electrum, BTCPay‑style, hardware‑wallet‑like patterns
- **Batch Verification PRO** — parallelized scanning, grouped results, anomaly detection
- **UX Enhancements** — progress indicators, clearer warnings, better error handling
- **Export Module** — export paths, addresses, indexes for external wallets

---

# **3. 12‑Month Roadmap — PRO Phase**

- **Deep Scan Engine PRO** — extended index ranges, multi‑account scanning, performance optimization
- **Mixed‑Type Wallet Detection** — detect wallets using multiple BIP standards
- **High‑Risk Safe Mode** — offline‑only, no‑disk‑write, secure memory handling
- **Interoperability Layer** — compatibility with wallet metadata formats
- **Integration with Recovery Tool** — automatic path extraction during recovery
- **Reproducible Builds** — deterministic builds + verification instructions

---

# **Long‑Term Vision**

Address Scanner becomes the **standard offline derivation‑path scanner** for Bitcoin:

- trusted by NGOs and support teams
- used by merchants and BTCPay users
- compatible with all major wallets
- safe for high‑risk users
- fully auditable and reproducible
- maintained as a long‑term public good

---

