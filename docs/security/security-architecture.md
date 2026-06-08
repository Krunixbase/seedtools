# 🔐 **SeedTools — Security Architecture Diagram**

## **1. High‑Level Architecture Overview**

SeedTools Suite is built as a **four‑layer offline security architecture**, designed to minimize attack surface and isolate sensitive operations.

```
+===============================================================+
|                        SeedTools Suite                        |
+===============================================================+

                     [ 1. Input Validation Layer ]
+---------------------------------------------------------------+
| - Mnemonic validator                                          |
| - Seed hex validator                                          |
| - BIP32/44/49/84/86 path parser                               |
| - Shamir share validator                                      |
| - Entropy pre-checks                                          |
+---------------------------------------------------------------+
                                |
                                v
                     [ 2. Deterministic Core Layer ]
+---------------------------------------------------------------+
| - BIP32 key derivation engine                                 |
| - BIP39 seed generator                                        |
| - BIP44/49/84/86 path engine                                  |
| - Taproot (BIP86) derivation                                  |
| - SLIP-39 Shamir engine                                       |
| - Ephemeral sensitive memory (zeroized)                       |
+---------------------------------------------------------------+
                                |
                                v
                     [ 3. Validation & Security Layer ]
+---------------------------------------------------------------+
| - Entropy scoring & anomaly detection                         |
| - Shamir polynomial validation                                |
| - Taproot script/key-path validation                          |
| - Address consistency checks                                  |
| - Hardened-mode protections                                   |
+---------------------------------------------------------------+
                                |
                                v
                     [ 4. Presentation & Output Layer ]
+---------------------------------------------------------------+
| - Offline rendering                                            |
| - No clipboard usage                                           |
| - No network calls                                             |
| - Local-only export (optional)                                |
| - Warnings, errors, reports                                   |
+---------------------------------------------------------------+
```

---

# **2. Layer-by-Layer Security Description**

## **1. Input Validation Layer**
Ensures all user-provided data is safe, correct, and normalized.

### Responsibilities:
- Validate mnemonic (BIP39 wordlist, checksum)
- Validate seed hex format
- Validate derivation paths (syntax + hardened rules)
- Validate Shamir shares (format, threshold)
- Pre-check entropy quality

### Security Controls:
- Reject malformed input
- Reject dangerous or ambiguous paths
- Reject invalid Shamir fragments
- Normalize all input before processing

---

## **2. Deterministic Core Layer**
The cryptographic heart of SeedTools.

### Responsibilities:
- BIP32 key derivation
- BIP39 seed generation
- BIP44/49/84/86 path derivation
- Taproot (BIP86) key-path derivation
- SLIP-39 Shamir reconstruction

### Security Controls:
- Sensitive data stored only in **ephemeral RAM**
- Zeroization after use
- No disk writes
- No clipboard usage
- No network stack

This layer is the **highest sensitivity zone**.

---

## **3. Validation & Security Layer**
Ensures correctness, safety, and cryptographic integrity.

### Responsibilities:
- Entropy scoring & anomaly detection
- Shamir polynomial validation
- Taproot script/key-path validation
- Address consistency checks
- Hardened-mode protections

### Security Controls:
- Detect weak entropy
- Detect tampered Shamir shares
- Detect invalid derivation logic
- Detect Taproot inconsistencies
- Enforce deterministic behavior

---

## **4. Presentation & Output Layer**
Displays results safely and offline.

### Responsibilities:
- Render addresses, paths, warnings, reports
- Provide local-only export (optional)
- Highlight security issues

### Security Controls:
- No clipboard usage
- No network calls
- No telemetry
- No external dependencies
- No browser engine

---

# **3. Data Stores & Sensitivity Zones**

## **D1 — Ephemeral Sensitive Memory (High Sensitivity)**
Contains:
- seed phrase  
- seed hex  
- private keys  
- Shamir shares  
- intermediate derivation values  

Cleared after use.

## **D2 — Local Configuration (Low Sensitivity)**
Contains:
- UI preferences  
- last used coin/network  
- non-sensitive settings  

Never contains seeds or keys.

---

# **4. Security Boundaries**

```
+------------------------------+
|  Security Boundary SB-1      |
|  Input Validation Layer      |
+------------------------------+

+------------------------------+
|  Security Boundary SB-2      |
|  Deterministic Core Layer    |
|  (High Sensitivity Zone)     |
+------------------------------+

+------------------------------+
|  Security Boundary SB-3      |
|  Validation & Security Layer |
+------------------------------+

+------------------------------+
|  Security Boundary SB-4      |
|  Presentation Layer          |
+------------------------------+
```

SB‑2 is the **critical boundary** — no data escapes this layer except deterministic, non-sensitive outputs.

---

# **5. Attack Surface Reduction**

SeedTools eliminates entire classes of attacks:

- No network  
- No cloud  
- No telemetry  
- No browser engine  
- No clipboard  
- No persistent storage of sensitive data  
- No external entropy sources  

Remaining risks are environmental (OS, hardware, physical access).

---

# **6. Security Architecture Summary**

SeedTools is designed to be:

- **offline**
- **deterministic**
- **non-custodial**
- **zero-trust**
- **cryptographically correct**
- **minimal attack surface**

The architecture ensures that even if a malicious user runs SeedTools, they gain **no offensive capabilities** and cannot attack other wallets.

---
