```

+====================================================================+
|                     NGO Bitcoin Workflow (SeedTools)               |
+====================================================================+

[1] DONATION RECEIVED
+--------------------------------------------------------------------+
| - BTC donation arrives (on-chain)                                  |
| - NGO receives TXID / address info                                 |
| - Optional: donor provides XPUB or proof                           |
+-------------------------------+------------------------------------+
                                |
                                v
[2] DATA COLLECTION (OFFLINE)
+--------------------------------------------------------------------+
| - Import addresses / XPUBs                                         |
| - Load wallet backups (if any)                                     |
| - Enter known metadata (timestamps, labels)                        |
| - No internet required                                             |
+-------------------------------+------------------------------------+
                                |
                                v
[3] VERIFICATION & FORENSICS
+--------------------------------------------------------------------+
| - Address ownership verification                                   |
| - UTXO discovery (offline scanning via known data)                 |
| - Path analysis (BIP32/44/49/84/86/Taproot)                        |
| - Entropy checks (if seed involved)                                |
+-------------------------------+------------------------------------+
                                |
                                v
[4] RECOVERY / ACCESS WORKFLOW
+--------------------------------------------------------------------+
| - Deterministic derivation of keys/paths                           |
| - Candidate wallet reconstruction                                  |
| - Multi-path exploration                                           |
| - Taproot script-path analysis (future)                            |
+-------------------------------+------------------------------------+
                                |
                                v
[5] NGO REPORT GENERATION
+--------------------------------------------------------------------+
| - Printable offline report                                         |
| - Donation verification summary                                    |
| - Path derivation evidence                                         |
| - Risk assessment                                                  |
| - Audit trail (deterministic)                                      |
+-------------------------------+------------------------------------+
                                |
                                v
[6] SECURE STORAGE / EXPORT
+--------------------------------------------------------------------+
| - Local encrypted storage                                          |
| - Offline PDF export                                               |
| - RAM-only temporary data                                          |
| - Optional: air‑gapped archive                                     |
+--------------------------------------------------------------------+

```
