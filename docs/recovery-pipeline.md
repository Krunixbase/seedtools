```

+-------------------------------------------------------------+
|                   SeedTools Recovery Pipeline               |
+-------------------------------------------------------------+

[1] INPUT COLLECTION
+-------------------------------------------------------------+
| - Mnemonics (full / partial)                               |
| - XPRVs / XPUBs                                             |
| - Wallet files (backups, exports)                           |
| - Addresses / known outputs                                 |
+-------------------------------+-----------------------------+
                                |
                                v
[2] PRE-PROCESSING
+-------------------------------------------------------------+
| - Format normalization                                      |
| - Checksum validation (BIP39 etc.)                          |
| - Entropy inspection                                        |
| - Corruption / anomaly detection                            |
+-------------------------------+-----------------------------+
                                |
                                v
[3] ANALYSIS
+-------------------------------------------------------------+
| - Path Explorer (BIP32/44/49/84/86, Taproot)                |
| - Forensics Engine (address / UTXO scanning)                |
| - Entropy Engine (quality, patterns, red flags)             |
+-------------------------------+-----------------------------+
                                |
                                v
[4] CANDIDATE GENERATION
+-------------------------------------------------------------+
| - Deterministic derivation of candidate wallets             |
| - Address/path matching against known data                  |
| - Ranking / scoring of recovery candidates                  |
+-------------------------------+-----------------------------+
                                |
                                v
[5] OUTPUT & REPORTING
+-------------------------------------------------------------+
| - Recovery candidate list                                   |
| - Recommended derivation paths                              |
| - NGO / audit‑ready reports (planned)                       |
| - Risk and integrity assessment                             |
+-------------------------------------------------------------+

```
