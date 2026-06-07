# Attack Surface — SeedTools Suite

SeedTools Suite minimizes attack vectors through strict offline-first architecture and deterministic execution.

---

## 1. Eliminated Attack Vectors

### 1.1 Network-Based Attacks
- no internet  
- no API calls  
- no telemetry  
- no remote assets  

### 1.2 Browser Engine Exploits
- no WebView  
- no HTML rendering  
- no JavaScript execution  

### 1.3 Cloud Compromise
- no cloud storage  
- no remote logs  
- no external dependencies  

---

## 2. Reduced Attack Vectors

### 2.1 User Input Manipulation
Mitigated by:
- controllers  
- deterministic validation  
- strict parsing  

### 2.2 Supply-Chain Attacks
Mitigated by:
- offline packaging  
- reproducible builds (planned)  

### 2.3 Weak Entropy
Mitigated by:
- entropy scoring  
- anomaly detection  

---

## 3. Remaining Attack Vectors

### 3.1 OS-Level Compromise
- kernel malware  
- rootkits  
- memory scrapers  

### 3.2 Physical Access
- stolen device  
- shoulder surfing  

### 3.3 Hardware Implants
- malicious USB  
- hardware keyloggers  

---

## 4. Attack Surface Diagram (ASCII)

```
Eliminated → Network, Cloud, Browser
Reduced    → Input, Entropy, Supply Chain
Remaining  → OS, Physical, Hardware
```

---

## 5. Related Docs
- **Threat Model**  
- **Security Model**  
- **Hardened Mode**  

---
