# 🔄 **SeedTools Suite — Data Flow Diagram (ASCII)**

```
                           +----------------------+
                           |     Input Sources    |
                           +----------+-----------+
                                      |
                                      v
                     +--------------------------------------+
                     |        SeedTools Core Engine         |
                     | (BIP32/39/44/49/84/86, entropy, etc.)|
                     +-----------------+--------------------+
                                       |
                                       v
        +------------------------------+------------------------------+
        |                              |                              |
        v                              v                              v
+---------------+            +----------------+             +------------------+
| Mnemonic      |            | Entropy Engine |             | Path & Derivation|
| Tools Engine  |            | (drift, checks)|             | Engine           |
+-------+-------+            +--------+-------+             +---------+--------+
        |                             |                               |
        +-------------+---------------+---------------+---------------+
                      |                               |
                      v                               v
             +----------------+               +------------------+
             | Recovery Engine|               | Forensics Engine |
             | (keys, seeds)  |               | (scan, detect)   |
             +--------+-------+               +---------+--------+
                      |                               |
                      +---------------+---------------+
                                      |
                                      v
                         +-----------------------------+
                         |     Address Generation      |
                         | (P2PKH / P2WPKH / P2TR)     |
                         +--------------+--------------+
                                        |
                                        v
                         +-----------------------------+
                         |           Outputs           |
                         +-----------------------------+
                         | - Derived keys              |
                         | - Addresses                 |
                         | - Recovery candidates       |
                         | - Forensics reports         |
                         | - Entropy diagnostics       |
                         +--------------+--------------+
                                        |
                                        v
                         +-----------------------------+
                         |     Storage / Export        |
                         +-----------------------------+
                         | - Local encrypted files     |
                         | - Offline exports (JSON/PDF)|
                         | - RAM-only temp data        |
                         +-----------------------------+
```

---

### **1. Input Sources**
- mnemonics  
- entropy  
- seeds  
- wallet metadata  
- disk images (forensics)  

### **2. Core Engine**
Wszystkie dane przechodzą przez deterministyczny silnik Core.

### **3. Processing Engines**
- Mnemonic Tools  
- Entropy Engine  
- Path & Derivation Engine  
- Recovery Engine  
- Forensics Engine  

### **4. Address Generation**
Deterministyczne kodowanie adresów.

### **5. Outputs**
- keys  
- addresses  
- reports  
- diagnostics  

---

- **Module Map Diagram**
