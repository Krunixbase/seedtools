# **SeedTools Desktop — SeedTools Suite**

## **Overview**

SeedTools Desktop is the **full graphical desktop application** that unifies all SeedTools modules into a single, offline‑first environment.  
It provides a secure, consistent, and user‑friendly interface for:

- deterministic wallet recovery,  
- mnemonic and entropy diagnostics,  
- derivation path exploration,  
- address scanning and verification,  
- forensic analysis for NGOs and high‑risk users,  
- guided workflows across the entire Suite.

It is designed for:

- self‑custody users,  
- NGOs and support teams,  
- high‑risk users in hostile environments,  
- developers and auditors,  
- educators teaching Bitcoin security.

SeedTools Desktop is **fully offline**, **deterministic**, and **auditable**.

---

# **Key Capabilities**

- **Unified Desktop Interface**  
  - all SeedTools apps in one place  
  - consistent UX across modules  
  - fast navigation and shared components  

- **Guided Workflows**  
  - Recovery Mode  
  - Forensics Mode  
  - Address Verification Mode  
  - Entropy/Mnemonic Diagnostics  

- **Integrated Tools**  
  - Recovery Tool  
  - Forensics Tool  
  - Address Scanner  
  - Entropy Inspector  
  - Mnemonic Tools  
  - Path Explorer  
  - SeedTools CLI (embedded terminal)  

- **Preset Manager**  
  - wallet presets (Sparrow, Specter, Electrum, BTCPay)  
  - BIP standard presets  
  - NGO‑friendly presets  

- **Security Modes**  
  - Offline‑Only Mode  
  - Hardened Mode (no disk writes, secure memory, ephemeral sessions)  

- **Documentation Hub**  
  - offline manuals  
  - printable guides  
  - app READMEs  

---

# **Typical Workflows**

## **1. Full wallet recovery**

1. Open SeedTools Desktop.  
2. Select **Recovery Mode**.  
3. Enter:
   - mnemonic  
   - passphrase (optional)  
   - wallet type  
4. Desktop automatically:
   - validates mnemonic  
   - scans derivation paths  
   - verifies addresses  
   - generates a recovery report  

---

## **2. Diagnose a corrupted mnemonic**

1. Open **Forensics Mode**.  
2. Paste mnemonic.  
3. Desktop performs:
   - checksum validation  
   - entropy drift detection  
   - invalid‑word detection  
4. Output includes:
   - corruption map  
   - drift indicators  
   - recoverability hints  

---

## **3. Explore derivation paths**

1. Open **Path Explorer**.  
2. Select BIP standard or enter custom path.  
3. Desktop displays:
   - full path structure  
   - hardened segments  
   - derived keys and addresses  

---

## **4. Verify multiple addresses**

1. Open **Address Scanner**.  
2. Paste a list of addresses.  
3. Desktop:
   - checks ownership  
   - extracts paths  
   - groups results by BIP standard  

---

# **Who This Tool Is For**

- **Self‑custody users**  
  Safe, offline wallet recovery and diagnostics.

- **NGOs & support teams**  
  Field‑ready workflows, minimal metadata, hardened mode.

- **High‑risk users**  
  No telemetry, no external calls, secure memory handling.

- **Developers**  
  Unified environment for testing BIP32/39/44/49/84/86.

- **Educators**  
  Clean interface for teaching Bitcoin security fundamentals.

---

# **Security Notes**

- Always run SeedTools Desktop on a **trusted machine**.  
- Hardened Mode disables:
  - disk writes  
  - logs  
  - caching  
- No telemetry or analytics are ever used.  
- All operations are deterministic and offline.  
- Verify builds using reproducible build instructions.

---

# **Roadmap (Preview)**

- **Hardened Mode PRO**  
- **Cross‑App Automation Engine**  
- **Wallet Preset Auto‑Detection**  
- **Multi‑App Session Sync**  
- **Suite‑Wide Export Module**  
- **Reproducible Builds**  

---
