# **Address Scanner — SeedTools Suite**

## **Overview**

Address Scanner is the SeedTools Suite application designed for **deep, deterministic scanning of derivation paths and indexes** to identify where a specific Bitcoin address originates within a seed.

It is built for:

- users verifying ownership of an address,
- support teams diagnosing wallet issues,
- merchants using BTCPay‑style structures,
- high‑risk users validating backups offline,
- developers testing derivation logic.

Address Scanner performs **extended‑range scanning**, supports all major BIP standards, and works fully **offline**.

---

# **Key Capabilities**

- **Deep Derivation Path Scanning**
  - extended index ranges
  - multi‑account scanning
  - change 0/1 detection

- **Address Ownership Verification**
  - confirm whether an address belongs to a seed
  - extract full derivation path
  - detect address type (SegWit, Taproot, Legacy)

- **BIP Standard Detection**
  - BIP44 / BIP49 / BIP84 / BIP86
  - custom paths
  - wallet‑specific patterns

- **Multi‑Address Scanning**
  - verify multiple addresses in sequence
  - detect mixed‑type wallets
  - identify non‑standard index usage

- **Offline‑First Architecture**
  - no telemetry
  - no external API calls
  - safe for air‑gapped devices

---

# **Typical Workflows**

## **1. Find the derivation path of a known address**

1. Enter mnemonic + optional passphrase.
2. Paste the address.
3. Select:
   - BIP standard
   - account
   - change
   - extended index range
4. Run **Scan**.
5. Tool returns:
   - match: true/false
   - full derivation path
   - index
   - address type

---

## **2. Scan for addresses across extended index ranges**

Useful for:

- wallets with non‑standard index usage,
- migrated wallets,
- BTCPay merchant setups,
- users unsure which index range was used.

1. Enter seed.
2. Choose **Deep Scan**.
3. Set:
   - account
   - change
   - extended index range
4. Tool generates:
   - all matching addresses
   - their paths
   - their indexes

---

## **3. Verify multiple addresses at once**

1. Enter seed.
2. Paste a list of addresses.
3. Run **Batch Scan**.
4. Tool:
   - checks each address
   - extracts paths
   - identifies mismatches
   - groups results by BIP standard

---

# **Who This Tool Is For**

- **Self‑custody users**
  Confirm address ownership and validate backups.

- **Merchants / BTCPay users**
  Recover or audit merchant wallets with extended index usage.

- **NGOs & support teams**
  Diagnose user issues without exposing sensitive data.

- **High‑risk users**
  Validate addresses offline after device loss or confiscation.

- **Developers**
  Test derivation logic and wallet compatibility.

---

# **Security Notes**

- Always run Address Scanner on a **trusted machine**.
- Prefer **air‑gapped** environments for sensitive seeds.
- Never paste mnemonics into online tools.
- Exported results (paths, addresses) may be sensitive — store securely.
- Verify builds using reproducible build instructions (when available).

---

# **Roadmap (Preview)**

- **Multi‑Account Auto‑Detection**
- **Taproot‑specific Scanning Improvements**
- **Batch Verification PRO**
- **Wallet Presets (Sparrow, Specter, BTCPay)**
- **Integration with Recovery Tool**
- **Reproducible Builds**

---

