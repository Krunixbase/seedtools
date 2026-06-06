# **Forensics Tool — SeedTools Suite**

## **Overview**

Forensics Tool is the analytical engine of the SeedTools Suite.
It provides **deep, offline forensic analysis** of mnemonics, entropy, derivation paths, and wallet structures.
Its purpose is to help users, NGOs, support teams, and high‑risk individuals understand *why* a wallet fails, *where* corruption occurred, and *how* to safely reconstruct or validate a seed.

Forensics Tool does **not** attempt brute‑force or guessing.
It focuses on **deterministic, explainable, auditable diagnostics**.

---

# **Key Capabilities**

- **Mnemonic Integrity Analysis**
  - checksum validation
  - wordlist conformity
  - detection of invalid or out‑of‑range words
  - entropy reconstruction preview

- **Entropy Inspection**
  - entropy bit‑length validation
  - drift detection
  - mismatch between mnemonic and entropy

- **Derivation Path Forensics**
  - detect wrong purpose/coin/account
  - detect wrong change/index
  - analyze extended index ranges
  - identify non‑standard wallet patterns

- **Address Ownership Diagnostics**
  - confirm whether an address *should* belong to a seed
  - detect mismatch between seed and address type
  - identify Taproot/SegWit inconsistencies

- **Forensic Reports**
  - structured, offline‑safe reports
  - exportable summaries for NGOs/support teams
  - reproducible, auditable results

---

# **Typical Workflows**

## **1. Diagnose a corrupted mnemonic**

1. Paste the mnemonic.
2. Tool performs:
   - checksum validation
   - wordlist conformity
   - entropy reconstruction
3. Output includes:
   - which word(s) are invalid
   - which bits of entropy are inconsistent
   - whether corruption is recoverable

---

## **2. Detect wrong derivation path**

1. Enter mnemonic + optional passphrase.
2. Paste an address that *should* belong to the wallet.
3. Tool checks:
   - purpose mismatch (44/49/84/86)
   - coin type mismatch
   - account mismatch
   - change/index mismatch
4. Output:
   - expected path
   - actual path
   - recommended correction

---

## **3. Analyze a suspicious or compromised setup**

1. Enter seed or mnemonic.
2. Run **Full Forensics Scan**.
3. Tool checks:
   - entropy integrity
   - path anomalies
   - address inconsistencies
   - Taproot/SegWit mismatch
4. Output:
   - forensic summary
   - risk indicators
   - recommended next steps

---

# **Who This Tool Is For**

- **NGOs & support teams**
  Diagnose user issues without exposing sensitive data.

- **High‑risk users**
  Validate backups after device confiscation or compromise.

- **Self‑custody users**
  Understand why a wallet import fails.

- **Developers & wallet maintainers**
  Test derivation path correctness and entropy handling.

- **Educators**
  Demonstrate how mnemonics, entropy, and BIP paths work.

---

# **Security Notes**

- Forensics Tool is **offline‑first** and safe for air‑gapped use.
- No telemetry, analytics, or external API calls.
- Forensic reports contain sensitive metadata — store them securely.
- Always verify builds using reproducible build instructions (when available).

---

# **Roadmap (Preview)**

- **Partial Mnemonic Reconstruction**
- **Advanced Entropy Drift Detection**
- **Taproot‑specific Forensics**
- **Wallet Metadata Analyzer**
- **NGO‑friendly Forensic Reports**
- **Integration with Recovery Tool**

---

