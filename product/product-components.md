# **SeedTools Suite — Product Components**

SeedTools Suite is composed of a set of **modular, deterministic, offline‑first components** that work together to deliver secure Bitcoin recovery, forensics, and diagnostics.  
Each component is isolated, auditable, and reusable across the entire ecosystem.

---

# **1. High‑Level Component Map**





SeedTools Suite is built from four major component groups:

1. **Application Components**  
2. **Interface Components (GUI)**  
3. **Logic Components (Core + CLI Module)**  
4. **Utility Components (Utils)**  

Each group contains multiple sub‑components described below.

---

# **2. Application Components**

These are the **user‑facing tools** of the Suite.

## **2.1 SeedTools Desktop**
- full graphical environment  
- unified UX  
- guided workflows  
- offline‑first  
- hardened mode  

👉 **Learn more**

---

## **2.2 Suite Launcher**
- unified entry point  
- preset manager  
- workflow selector  
- cross‑app session sync  

👉 **Learn more**

---

## **2.3 SeedTools CLI**
- deterministic command‑line toolkit  
- automation workflows  
- NGO‑friendly offline mode  

👉 **Learn more**

---

## **2.4 Standalone Tools**
- **Recovery Tool**  
- **Forensics Tool**  
- **Address Scanner**  
- **Entropy Inspector**  
- **Mnemonic Tools**  
- **Path Explorer**

👉 **Explore standalone tools**

---

# **3. Interface Components (GUI)**





SeedTools GUI provides the **visual foundation** for all applications.

## **3.1 Component Library**
- buttons, inputs, dialogs  
- secure mnemonic fields  
- entropy viewers  
- path visualizers  

👉 **Component Library**

---

## **3.2 Workflow Engine UI**
- stepper  
- progress indicators  
- error/warning surfaces  

👉 **Workflow Engine**

---

## **3.3 Preset‑Aware UI**
- wallet presets  
- BIP standard presets  
- NGO presets  

👉 **Preset‑Aware UI**

---

## **3.4 Secure Input Components**
- masked fields  
- isolated buffers  
- zeroization  

👉 **Secure Inputs**

---

# **4. Logic Components (Core + CLI Module)**





These components implement the **deterministic logic** of the Suite.

---

## **4.1 SeedTools Core**

### **4.1.1 BIP Engines**
- BIP39 mnemonic engine  
- BIP32 derivation engine  
- BIP44/49/84/86 path logic  

👉 **BIP Engines**

---

### **4.1.2 Address Engine**
- P2PKH  
- P2SH‑P2WPKH  
- P2WPKH  
- P2TR  

👉 **Address Engine**

---

### **4.1.3 Entropy & Checksum Engine**
- entropy reconstruction  
- checksum validation  
- drift detection  

👉 **Entropy Engine**

---

### **4.1.4 Forensics Engine**
- corruption mapping  
- drift scoring  
- anomaly detection  

👉 **Forensics Engine**

---

## **4.2 SeedTools CLI Module**

### **4.2.1 Command Router**
- deterministic argument parsing  
- nested command groups  

👉 **Command Router**

---

### **4.2.2 Execution Layer**
- hardened mode  
- ephemeral memory  
- no‑history mode  

👉 **Secure Execution**

---

### **4.2.3 Output Layer**
- human‑readable output  
- structured output (JSON planned)  

👉 **Output Layer**

---

# **5. Utility Components (Utils)**





SeedTools Utils provides the **shared low‑level primitives** used across all modules.

---

## **5.1 Validation Utilities**
- mnemonic validation  
- entropy length checks  
- path syntax validation  
- address format checks  

👉 **Validation Utils**

---

## **5.2 Encoding & Decoding**
- Base58  
- Bech32/Bech32m  
- hex ↔ bytes  

👉 **Encoding Tools**

---

## **5.3 Cryptographic Helpers**
- hashing wrappers  
- secure random utilities  
- buffer manipulation  

👉 **Crypto Helpers**

---

## **5.4 Formatting Utilities**
- deterministic formatting  
- pretty‑printed JSON  
- structured CLI output  

👉 **Formatting Utils**

---

## **5.5 Secure Memory Helpers**
- zeroization  
- ephemeral buffers  
- hardened mode support  

👉 **Secure Memory**

---

# **6. Component Interactions**

SeedTools uses a **strict, deterministic dependency flow**:

```
Applications → GUI → Core → Utils
```

Rules:

- no circular dependencies  
- no hidden state  
- no background processes  
- no external calls  
- all components auditable  

---

# **7. Component Summary**

SeedTools Suite is built from:

- **Applications** — user‑facing tools  
- **GUI** — visual components  
- **Core** — deterministic logic  
- **CLI Module** — automation logic  
- **Utils** — shared primitives  

Together, they form a **modular, secure, deterministic ecosystem** for Bitcoin recovery and forensics.

---
