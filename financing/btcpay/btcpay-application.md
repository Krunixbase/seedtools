# **BTCPay Server Grant Application**
**Project: SeedTools 2.0 — Offline HD Wallet Recovery & Forensics Toolkit**
**Applicant: Andrzej (Krunixbase)**
**License: MIT**

---

# **1. Project Summary**

SeedTools 2.0 is an **offline, open‑source toolkit** for recovering Bitcoin HD wallets, analyzing corrupted mnemonics, scanning derivation paths, and verifying addresses.
It is designed for users who rely on self‑custody — including merchants using BTCPay Server — and need secure, private, air‑gapped recovery workflows.

SeedTools strengthens the Bitcoin ecosystem by reducing permanent loss of funds and improving wallet interoperability.

---

# **2. Why This Matters for BTCPay Server**

Merchants using BTCPay rely heavily on:

- secure backups
- deterministic wallet structures
- correct derivation paths
- reliable recovery workflows

SeedTools directly supports BTCPay users by providing:

### **Deterministic recovery of merchant wallets**
Merchants often use:

- BIP84 (native SegWit)
- BIP86 (Taproot)
- custom derivation paths

SeedTools scans all relevant paths and verifies addresses deterministically.

### **Forensics for compromised or misconfigured setups**
If a merchant:

- loses access to a device
- misconfigures a wallet
- corrupts a backup
- forgets a passphrase

SeedTools provides safe, offline recovery.

### **Offline workflows for high‑risk merchants**
Some merchants operate in:

- high‑risk regions
- censorship‑prone environments
- unstable political climates

SeedTools enables recovery without exposing private data.

---

# **3. Project Goals (12 months)**

### **Core Development**
- Recovery Mode PRO
- Forensics Mode PRO
- Taproot (BIP86) support
- deterministic engine improvements
- CLI for Tails/Qubes

### **Merchant‑Focused Features**
- BTCPay‑compatible derivation path presets
- address verification for merchant wallets
- recovery workflows tailored to BTCPay setups
- documentation for BTCPay users

### **Security & Reliability**
- reproducible builds
- external security review
- corrupted mnemonic datasets

---

# **4. Deliverables**

### **Within 3 months**
- Recovery Mode MVP
- Forensics Mode MVP
- CLI v1
- BTCPay derivation path presets
- documentation v1

### **Within 6 months**
- Taproot support
- Safe Mode
- installer (.exe)
- reproducible builds

### **Within 12 months**
- full forensic suite
- merchant‑focused recovery guides
- integrations with Sparrow/Specter

---

# **5. Budget Request**

**Requested amount: 10 000 USD**

Breakdown:

| Category | Amount | Description |
|---------|--------|-------------|
| Development | **7 000** | Recovery, Forensics, Taproot, BTCPay presets |
| Documentation | **1 500** | Merchant guides, recovery workflows |
| Testing | **1 500** | BTCPay wallet compatibility tests |

---

# **6. How Funds Will Be Used**

- development of BTCPay‑specific features
- deterministic engine improvements
- documentation for merchants
- testing with BTCPay wallet setups
- reproducible builds

---

# **7. Project Status**

SeedTools is already in active development:

- deterministic engine working
- GUI prototype
- CLI prototype
- architecture documented
- roadmap prepared
- demo pack ready
- MIT license added
- repo structured

The project is ready for expansion with BTCPay support.

---

# **8. Links**

- GitHub: [https://github.com/Krunixbase/seedtools](https://github.com/Krunixbase/seedtools)
- Documentation: `/product/`
- Roadmap: `/roadmap/`
- Demo Pack: `/demo/`

---

# **9. Why BTCPay Support Matters**

SeedTools helps merchants:

- recover funds safely
- avoid permanent loss
- verify wallet integrity
- operate securely in high‑risk environments

This aligns directly with BTCPay’s mission of empowering merchants with open‑source, self‑custodial tools.

---

