# **SeedTools 2.0 — Integration Plan for BTCPay Server**

## **1. Overview**

SeedTools 2.0 is an offline, open‑source toolkit designed to help BTCPay merchants recover wallets, verify derivation paths, analyze corrupted backups, and validate addresses without exposing private data.

This document outlines the integration plan between SeedTools and BTCPay Server, focusing on deterministic wallet compatibility, merchant workflows, and security improvements.

---

# **2. Integration Goals**

## **2.1 Improve Merchant Recovery Workflows**
BTCPay merchants often rely on:

- BIP84 (native SegWit)
- BIP86 (Taproot)
- custom derivation paths
- hardware wallet backups
- multisig setups

SeedTools provides deterministic scanning and verification for all these cases.

## **2.2 Provide BTCPay‑Specific Presets**
SeedTools will include:

- BTCPay derivation path presets
- BTCPay wallet structure templates
- BTCPay address verification logic

This ensures merchants can recover wallets without guessing paths.

## **2.3 Strengthen Backup Reliability**
SeedTools helps merchants detect:

- corrupted mnemonics
- wrong passphrases
- mismatched derivation paths
- misconfigured wallet setups

This reduces support load and prevents permanent fund loss.

---

# **3. Technical Integration Plan**

## **3.1 BTCPay Derivation Path Presets**
SeedTools will ship with presets for:

- `m/84'/0'/0'` (SegWit)
- `m/86'/0'/0'` (Taproot)
- BTCPay multisig templates
- merchant‑specific account structures

These presets will be selectable in the UI and CLI.

---

## **3.2 Deterministic Address Verification**
SeedTools will implement:

- address generation matching BTCPay wallet logic
- gap‑limit scanning
- deep path scanning (0 → X)
- Taproot verification

This ensures merchants can confirm wallet ownership and recover funds safely.

---

## **3.3 Forensics Mode for BTCPay**
For merchants with compromised or misconfigured setups:

- mnemonic integrity checks
- entropy drift detection
- derivation path mismatch detection
- address exposure analysis
- forensic reports

This helps diagnose issues without exposing sensitive data.

---

## **3.4 CLI Integration for Tails/Qubes**
SeedTools CLI will support:

- offline merchant recovery
- deterministic scanning
- BTCPay presets
- reproducible builds

Ideal for high‑risk merchants and NGOs.

---

# **4. Documentation Deliverables**

SeedTools will provide:

- BTCPay merchant recovery guide
- BTCPay derivation path documentation
- BTCPay multisig compatibility notes
- step‑by‑step recovery workflows
- troubleshooting guide for corrupted backups

All documentation will be open‑source.

---

# **5. Testing Plan**

SeedTools will include:

- BTCPay wallet test vectors
- corrupted mnemonic datasets
- path scanning tests
- multisig compatibility tests
- Taproot merchant tests

This ensures reliability across all merchant setups.

---

# **6. Timeline**

| Month | Deliverable |
|-------|-------------|
| 1–2 | BTCPay presets, Recovery Mode MVP |
| 3–4 | Forensics Mode MVP, address verification |
| 5–6 | Taproot support, Safe Mode |
| 7–9 | Installer, UX, documentation |
| 10–12 | Forensics PRO, merchant integrations |

---

# **7. Benefits for BTCPay Ecosystem**

SeedTools improves:

- merchant safety
- wallet reliability
- backup integrity
- recovery workflows
- operational security

It reduces support burden and strengthens self‑custody for BTCPay users.

---

