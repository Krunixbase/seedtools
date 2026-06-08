# 📘 **Threat Model — SeedTools Suite**

SeedTools Suite operates in high‑risk, regulated, and offline environments.  
The threat model assumes adversaries with significant capabilities, including malware, physical access, and supply‑chain compromise.

The model is built on four pillars:

- **External Threats**  
- **Internal Threats**  
- **Environmental Threats**  
- **Cryptographic Threats**

---

## **1. Threat Modeling Approach**

SeedTools uses a hybrid methodology combining:

- **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)  
- **LINDDUN** (Privacy threat modeling)  
- **Zero‑Trust assumptions**  
- **Offline‑first constraints**

The system assumes **no trust** in:

- the operating system  
- the user environment  
- external devices  
- external entropy sources  

---

## **2. External Threats**

Threats originating outside the user’s device.

### **2.1 Malware**
- keyloggers  
- clipboard hijackers  
- screen capture tools  
- memory scrapers  

### **2.2 Supply‑Chain Attacks**
- compromised libraries  
- malicious dependencies  
- tampered binaries  

### **2.3 Hardware Implants**
- malicious USB devices  
- hardware keyloggers  
- BIOS/UEFI compromise  

### **2.4 Social Engineering**
- phishing  
- fake recovery instructions  
- manipulated seed input  

---

## **3. Internal Threats**

Threats caused by user mistakes or misconfigurations.

### **3.1 User Errors**
- incorrect mnemonic entry  
- wrong derivation path  
- mixing wallets  
- misconfigured backups  

### **3.2 Weak Entropy**
- predictable randomness  
- repeated patterns  
- low‑entropy seeds  

### **3.3 Corrupted Shamir Shares**
- invalid shares  
- mismatched thresholds  
- tampered fragments  

---

## **4. Environmental Threats**

Threats related to the physical or system environment.

### **4.1 Physical Access**
- stolen device  
- shoulder surfing  
- unauthorized observation  

### **4.2 OS‑Level Compromise**
- rootkits  
- kernel‑level malware  
- compromised system libraries  

### **4.3 Hardware Failure**
- disk corruption  
- RAM instability  
- power loss during critical operations  

---

## **5. Cryptographic Threats**

Threats targeting cryptographic correctness.

### **5.1 Predictable Entropy**
- weak randomness  
- reused entropy sources  

### **5.2 Incorrect Derivation**
- wrong BIP32/39/44/49/84/86 logic  
- incorrect hardened paths  

### **5.3 Invalid Shamir Polynomials**
- incorrect polynomial generation  
- mismatched shares  
- threshold inconsistencies  

### **5.4 Taproot‑Specific Threats**
- script‑path misinterpretation  
- incorrect key‑path validation  

---

## **6. Attack Vectors**

SeedTools eliminates entire classes of attacks by design:

### **Eliminated**
- network attacks  
- cloud compromise  
- API hijacking  
- telemetry leakage  
- browser‑engine exploits  

### **Remaining**
- user input manipulation  
- OS compromise  
- physical access  
- hardware implants  

---

## **7. Threat Scenarios**

### **Scenario A — Compromised OS**
Attacker controls the OS and attempts to read memory.  
**Mitigation:** hardened mode, masking layer, zeroization.

### **Scenario B — Clipboard Hijacking**
Attacker replaces copied addresses.  
**Mitigation:** no clipboard usage, offline rendering.

### **Scenario C — Corrupted Shamir Shares**
User attempts recovery with tampered shares.  
**Mitigation:** polynomial validation, threshold verification.

### **Scenario D — Weak Entropy Seed**
User generates a seed with insufficient randomness.  
**Mitigation:** entropy scoring, anomaly detection.

### **Scenario E — Supply‑Chain Attack**
Malicious dependency injected into the build.  
**Mitigation:** reproducible builds (planned), offline packaging.

---

## **8. Risk Levels**

| Threat Category        | Risk Level | Notes |
|------------------------|-----------|-------|
| OS‑level compromise    | High      | Outside SeedTools control |
| Hardware implants      | High      | Requires physical mitigation |
| User mistakes          | Medium    | Mitigated by controllers |
| Weak entropy           | Medium    | Mitigated by entropy engine |
| Supply‑chain attacks   | Medium    | Mitigated by reproducible builds |
| Clipboard hijacking    | Low       | Clipboard not used |
| Network attacks        | Eliminated | No networking |

---

## **9. Mitigation Mapping**

| Threat | Mitigation |
|--------|------------|
| Malware | Isolation Layer, Masking Layer |
| Weak entropy | Entropy Engine |
| Corrupted shares | Shamir validation |
| OS compromise | Hardened Mode |
| Supply‑chain | Reproducible builds (planned) |
| Physical access | Offline workflows, no cloud |
| Incorrect derivation | Deterministic Core Layer |

---

## **10. Residual Risks**

SeedTools cannot mitigate:

- OS‑level compromise  
- hardware keyloggers  
- malicious firmware  
- physical theft  
- supply‑chain hardware attacks  

These require **operational security** on the user’s side.

---

