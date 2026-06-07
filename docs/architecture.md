# **🧩 SeedTools Architecture (High‑Level)**

Below is a clear ASCII diagram showing how SeedTools is organized internally — from the GUI layer down to the cryptographic core.

```text
+------------------------------------------------------------+
|                        SeedTools Suite                     |
+-----------------------------+------------------------------+
|         GUI LAYER           |          INTERFACES          |
|-----------------------------+------------------------------|
| - Desktop App (planned)     | - CLI tools                  |
| - Wizards / presets         | - Demo workflows             |
+-----------------------------+------------------------------+

+------------------------------------------------------------+
|                     APPLICATION LAYER                      |
+------------------------------------------------------------+
| - SeedService            | deterministic recovery engine   |
| - EntropyService         | entropy checks & diagnostics    |
| - PathExplorer           | BIP32/44/49/84/86/Taproot       |
| - Scanner                | address / UTXO scanning         |
| - Reports                | NGO / audit reports (planned)   |
+------------------------------------------------------------+

+------------------------------------------------------------+
|                         CORE LAYER                         |
+------------------------------------------------------------+
| - Crypto Core            | key derivation, BIP logic       |
| - Entropy Engine         | randomness analysis             |
| - Forensics Core         | Taproot, multi‑wallet (future)  |
| - Storage Engine*        | offline local data handling     |
+------------------------------------------------------------+
```

---
