# **Path Explorer — SeedTools Suite**

## **Overview**

Path Explorer is the SeedTools Suite application designed for **interactive exploration, validation, and analysis of BIP32/BIP44/BIP49/BIP84/BIP86 derivation paths**.  
It allows users to inspect how HD wallets derive keys, visualize path structures, test custom paths, and generate addresses across extended index ranges.

It is built for:

- developers testing wallet implementations,  
- self‑custody users validating their wallet structure,  
- NGOs and support teams diagnosing path‑related issues,  
- educators teaching how hierarchical deterministic wallets work,  
- high‑risk users verifying paths offline.

Path Explorer is fully **offline‑first**, deterministic, and transparent.

---

# **Key Capabilities**

- **BIP Standard Exploration**  
  - BIP32 / BIP44 / BIP49 / BIP84 / BIP86  
  - visualize path structure  
  - inspect hardened vs non‑hardened segments  

- **Custom Path Builder**  
  - build any derivation path interactively  
  - validate syntax  
  - detect invalid or unsupported segments  

- **Deep Index Scanning**  
  - extended index ranges  
  - change 0/1  
  - multi‑account scanning  

- **Address Generation**  
  - generate addresses for any path  
  - detect address type (Legacy, SegWit, Taproot)  
  - export derived addresses  

- **Path Validation**  
  - detect incorrect purpose/coin/account  
  - identify non‑standard wallet patterns  
  - highlight path mismatches  

- **Offline‑First Architecture**  
  - no telemetry  
  - no external API calls  
  - safe for air‑gapped devices  

---

# **Typical Workflows**

## **1. Explore a standard BIP path**

1. Select a BIP standard (44/49/84/86).  
2. Choose:
   - account  
   - change  
   - index  
3. Tool displays:
   - full derivation path  
   - key hierarchy  
   - generated address  

---

## **2. Build and test a custom derivation path**

1. Enter a custom path (e.g., `m/84'/0'/3'/1/57`).  
2. Tool validates:
   - syntax  
   - hardened markers  
   - segment ranges  
3. Tool generates:
   - derived public key  
   - derived address  
   - path metadata  

---

## **3. Scan extended index ranges**

Useful for:

- wallets using non‑standard indexes,  
- migrated wallets,  
- merchant setups,  
- users unsure which index range was used.

1. Enter seed.  
2. Choose **Deep Scan**.  
3. Set:
   - account  
   - change  
   - extended index range  
4. Tool outputs:
   - all derived addresses  
   - their paths  
   - their indexes  

---

## **4. Validate a wallet’s structure**

1. Enter mnemonic + optional passphrase.  
2. Select a BIP standard.  
3. Tool checks:
   - purpose/coin/account correctness  
   - change/index structure  
   - path consistency  
4. Output includes:
   - expected vs actual path  
   - mismatch indicators  
   - recommended corrections  

---

# **Who This Tool Is For**

- **Developers**  
  Test and debug derivation logic.

- **Self‑custody users**  
  Validate wallet structure and ensure correct paths.

- **NGOs & support teams**  
  Diagnose path‑related issues offline.

- **High‑risk users**  
  Verify paths safely without internet access.

- **Educators**  
  Demonstrate how HD wallets derive keys and addresses.

---

# **Security Notes**

- Always use Path Explorer on a **trusted machine**.  
- Prefer **air‑gapped** environments for sensitive seeds.  
- Never paste mnemonics into online tools.  
- Exported paths and addresses may be sensitive — store securely.  
- Verify builds using reproducible build instructions (when available).

---

# **Roadmap (Preview)**

- **Multi‑Account Auto‑Detection**  
- **Taproot‑specific Path Analysis**  
- **Path Visualization Graph**  
- **Wallet Presets (Sparrow, Specter, BTCPay)**  
- **Integration with Address Scanner**  
- **Reproducible Builds**  

---
