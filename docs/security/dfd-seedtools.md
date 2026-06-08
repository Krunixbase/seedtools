### 📘 Data Flow Diagram (DFD) — SeedTools Suite

---

## 1. Context level (Level 0)

**External Entity: User**  
**System: SeedTools Suite (offline, local)**

**Main flows:**

- **User → SeedTools:**  
  - mnemonic / seed phrase  
  - derivation paths  
  - configuration choices (coin, account, index ranges, modes)  

- **SeedTools → User:**  
  - derived addresses  
  - derivation paths  
  - validation results  
  - warnings / errors / entropy scores  

No external services, no network, no cloud.

---

## 2. Level 1 — Main processes

### 2.1 Process P1 — Input Controller

**Inputs:**

- seed phrase / seed hex  
- derivation path  
- Shamir shares (optional)  
- configuration (coin, network, index ranges, mode)

**Operations:**

- validate format (BIP39, hex, path syntax)  
- normalize input  
- reject malformed data  

**Outputs:**

- normalized seed / shares / paths → to P2, P3, P4  
- validation errors → to User  

---

### 2.2 Process P2 — Deterministic Core (Derivation Engine)

**Inputs:**

- normalized seed / seed hex (from P1)  
- derivation paths (from P1)  
- coin/network parameters

**Operations:**

- BIP32/BIP39/BIP44/BIP49/BIP84/BIP86 derivation  
- hardened / non‑hardened path handling  
- key and address generation

**Outputs:**

- derived keys (in memory only)  
- derived addresses  
- derivation metadata  

**Data Stores:**

- **D1: Ephemeral Memory (Sensitive)**  
  - seed  
  - intermediate keys  
  - derived keys  
  - cleared/zeroized after use  

---

### 2.3 Process P3 — Validation & Analysis

**Inputs:**

- derived addresses / keys / paths (from P2)  
- user‑provided reference data (optional)  
- Shamir shares (from P1, if used)  

**Operations:**

- address/path consistency checks  
- Shamir share validation (threshold, polynomial consistency)  
- entropy scoring / anomaly detection  
- Taproot rules validation  

**Outputs:**

- validation results  
- warnings / errors  
- analysis reports (local, in memory)  

---

### 2.4 Process P4 — UI / Presentation Layer

**Inputs:**

- results from P2 (addresses, paths)  
- results from P3 (validation, warnings, scores)  

**Operations:**

- render tables / lists / reports  
- highlight warnings / errors  
- present deterministic outputs to the user  

**Outputs:**

- visual output to User  
- optional export (if enabled: local file only, no network)

**Data Stores (optional, non‑sensitive):**

- **D2: Local Config / Settings**  
  - UI preferences  
  - last used coin/network  
  - non‑sensitive options  

No seeds, no keys, no mnemonics stored here.

---

## 3. Data stores overview

- **D1 — Ephemeral Sensitive Memory**  
  - seed, keys, shares, intermediate values  
  - lives only in RAM  
  - zeroized where possible  

- **D2 — Local Configuration (Non‑Sensitive)**  
  - UI settings  
  - app preferences  
  - no secrets  

No:

- database  
- cloud storage  
- remote logs  

---

## 4. External entities

### 4.1 User

**Provides:**

- seed / mnemonic / shares  
- derivation paths  
- configuration  

**Receives:**

- derived addresses  
- validation results  
- warnings / entropy scores  

### 4.2 (Optional) Local Filesystem

Only if export is enabled:

- **Output:** reports, address lists, analysis results  
- No seeds or private keys written by default.

---

## 5. Security notes tied to DFD

- All sensitive flows are **User ↔ P1 ↔ P2 ↔ P3 ↔ P4 (in RAM only)**  
- No data leaves the device  
- No network flows exist  
- Sensitive data is never written to D2  
- D1 is ephemeral and should be treated as high‑sensitivity memory

---
