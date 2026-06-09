# 📘 **Modules Architecture — SeedTools Suite**

SeedTools Suite is built as a modular, deterministic, offline‑first system.  
Each module has a **single responsibility**, strict **trust boundaries**, and **no external dependencies**.

The modules are grouped into four categories:

1. **Core Modules**  
2. **Application Modules**  
3. **Security Modules**  
4. **System Modules**

---

# **1. Core Modules**

Core modules implement deterministic, low‑level cryptographic logic.  
They are the **most trusted** part of the system.

---

## **1.1 Crypto Core**  
**Expand Crypto Core**

Responsibilities:
- BIP32/39/44/49/84/86 derivation  
- hardened / non‑hardened path logic  
- key generation  
- Taproot key‑path logic  

Guarantees:
- deterministic output  
- no external entropy  
- reproducible results  

---

## **1.2 Entropy Engine**  
**Expand Entropy Engine**

Responsibilities:
- entropy scoring  
- anomaly detection  
- randomness validation  

Guarantees:
- detection of weak or predictable entropy  
- deterministic scoring  

---

## **1.3 Forensics Core**  
**Expand Forensics Core**

Responsibilities:
- Taproot script‑path analysis  
- multi‑wallet scanning logic  
- UTXO interpretation  

Guarantees:
- deterministic forensic output  
- reproducible analysis  

---

## **1.4 Storage Engine**  
**Expand Storage Engine**

Responsibilities:
- local‑only storage  
- deterministic serialization  
- integrity checks  

Guarantees:
- no cloud  
- no telemetry  
- no external writes  

---

# **2. Application Modules**

Application modules implement workflows and user‑facing logic.  
They are **semi‑trusted** and isolated from cryptographic primitives.

---

## **2.1 Mnemonic Tools**  
**Expand Mnemonic Tools**

Responsibilities:
- mnemonic validation  
- correction heuristics  
- checksum verification  

---

## **2.2 Entropy Tools**  
**Expand Entropy Tools**

Responsibilities:
- entropy scoring UI  
- anomaly reporting  
- entropy visualization  

---

## **2.3 Path Explorer**  
**Expand Path Explorer**

Responsibilities:
- BIP path exploration  
- hardened / non‑hardened navigation  
- Taproot derivation preview  

---

## **2.4 Scanner**  
**Expand Scanner**

Responsibilities:
- address scanning  
- UTXO discovery  
- multi‑wallet analysis  

---

## **2.5 Forensics Engine**  
**Expand Forensics Engine**

Responsibilities:
- forensic workflows  
- Taproot analysis  
- multi‑wallet correlation  

---

## **2.6 Reports Module (planned)**  
**Expand Reports Module**

Responsibilities:
- NGO‑ready reports  
- compliance‑grade summaries  
- deterministic export  

---

# **3. Security Modules**

Security modules enforce isolation, masking, and deterministic behavior.

---

## **3.1 Isolation Layer**  
**Expand Isolation Layer**

Responsibilities:
- sandboxed buffers  
- strict module separation  
- no shared memory  

---

## **3.2 Masking Layer**  
**Expand Masking Layer**

Responsibilities:
- field‑level masking  
- zeroization  
- ephemeral memory  

---

## **3.3 Hardened Mode**  
**Expand Hardened Mode**

Responsibilities:
- no animations  
- no caching  
- no disk writes  
- deterministic rendering  

---

# **4. System Modules**

System modules provide foundational services.

---

## **4.1 Logging Service**  
**Expand Logging Service**

Responsibilities:
- local‑only logs  
- deterministic metadata  
- forensic‑grade audit trail  

---

## **4.2 Configuration Manager**  
**Expand Configuration Manager**

Responsibilities:
- deterministic config loading  
- no dynamic assets  
- reproducible environment  

---

## **4.3 Dependency Resolver**  
**Expand Dependency Resolver**

Responsibilities:
- offline dependency management  
- reproducible builds (planned)  

---

## **4.4 Environment Manager**  
**Expand Environment Manager**

Responsibilities:
- reproducible runtime  
- deterministic environment setup  
- offline packaging  

---

# **5. Module Interaction Model**

Modules interact through **strict, one‑directional flows**:

```
UI → Controllers → Application Modules → Core Modules → System Modules
```

No module can bypass its layer.

---

# **6. Trust Levels**

| Module Category       | Trust Level |
|-----------------------|-------------|
| Core Modules          | High        |
| Security Modules      | High        |
| Application Modules   | Medium      |
| System Modules        | Medium      |
| UI                    | Low         |

---

# **7. Design Principles**

- single responsibility  
- deterministic behavior  
- strict isolation  
- no external dependencies  
- reproducible outputs  

---

