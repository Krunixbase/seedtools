# **Recovery Tool — SeedTools Suite**

## **Overview**

Recovery Tool is the core application of the SeedTools Suite.
It provides **deterministic, offline, transparent HD wallet recovery** for Bitcoin users who need reliable, auditable, and secure workflows without relying on third parties.

It is designed for:

- self‑custody users,
- NGOs and support teams,
- merchants and BTCPay users,
- high‑risk users operating in hostile environments,
- educators and technical trainers.

Recovery Tool helps users safely reconstruct wallets, verify derivation paths, analyze address ownership, and prepare clean recovery plans.

---

# **Key Features**

- **Mnemonic input**
  - 12 / 15 / 18 / 21 / 24‑word BIP39
  - optional passphrase
  - raw seed hex (advanced)

- **Derivation paths**
  - BIP44 / BIP49 / BIP84 / BIP86 (Taproot)
  - custom paths
  - **deep derivation path scanning across extended index ranges**

- **Address verification**
  - confirm whether an address belongs to a given seed
  - display full derivation path
  - detect standard (e.g., BIP84, BIP86)
  - verify multiple addresses in sequence

- **Recovery workflows**
  - single‑account wallets
  - multi‑account setups
  - BTCPay‑style merchant wallets
  - hardware‑wallet‑like structures
  - non‑standard or legacy paths

- **Offline‑first architecture**
  - no telemetry
  - no analytics
  - no external API calls
  - suitable for air‑gapped devices

---

# **Typical Workflows**

## **1. Verify if an address belongs to a seed**

1. Enter mnemonic and optional passphrase.
2. Paste the address.
3. Run **Address Verification**.
4. Tool returns:
   - match: true/false
   - full derivation path
   - index
   - address type (SegWit, Taproot, etc.)

Useful for confirming ownership, checking backups, or validating wallet imports.

---

## **2. Recover a wallet after device loss**

1. Enter mnemonic + passphrase.
2. Select a standard (BIP44/49/84/86) or use **Auto‑Detect**.
3. Run **Deep Scan** across extended index ranges.
4. Export:
   - derived addresses
   - derivation paths
   - indexes
5. Import results into Sparrow, Specter, Electrum, or BTCPay‑style setups.

---

## **3. Locate funds on non‑standard indexes**

1. Enter seed.
2. Choose **Deep Scan**.
3. Set:
   - account
   - change (0/1)
   - extended index range
4. Tool generates addresses and paths for manual or node‑based balance checks.

---

# **Who This Tool Is For**

- **Self‑custody users**
  Want reliable, transparent recovery workflows.

- **NGOs and support teams**
  Assist users after device loss or confiscation.

- **Merchants / BTCPay users**
  Need deterministic, auditable wallet structures.

- **High‑risk users**
  Require offline, no‑trace recovery methods.

- **Educators**
  Demonstrate how HD wallets and derivation paths work.

---

# **Security Notes**

- Use Recovery Tool on a **trusted machine**.
- Prefer **air‑gapped** or offline environments for sensitive cases.
- Never paste mnemonics into online tools.
- Encrypt exported data if stored long‑term.
- Always verify builds using reproducible build instructions (when available).

---

# **Roadmap (Preview)**

- wallet presets (Sparrow, Specter, Electrum, BTCPay‑style)
- batch address verification
- advanced “wrong path / wrong index” diagnostics
- integration with Forensics Tool for anomaly detection
- reproducible builds and verification guide

---
