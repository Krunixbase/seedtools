```

+====================================================================+
|                     FULL NGO COMPLIANCE PIPELINE                  |
|                         (SeedTools Suite)                          |
+====================================================================+

[1] DONATION EVENT
+--------------------------------------------------------------------+
| - BTC donation received (on-chain)                                 |
| - NGO receives TXID / address                                      |
| - Donor may provide XPUB / metadata                                |
| - Initial compliance flag: "Funds received"                        |
+-------------------------------+------------------------------------+
                                |
                                v
[2] EVIDENCE COLLECTION (OFFLINE)
+--------------------------------------------------------------------+
| - Import addresses / XPUBs                                         |
| - Load wallet backups (if any)                                     |
| - Add NGO metadata (project, purpose, restrictions)                |
| - No internet required                                             |
+-------------------------------+------------------------------------+
                                |
                                v
[3] TECHNICAL VERIFICATION (SEEDTOOLS)
+--------------------------------------------------------------------+
| - Address ownership verification                                   |
| - UTXO discovery (offline)                                         |
| - Path analysis (BIP32/44/49/84/86/Taproot)                        |
| - Entropy checks (if seed involved)                                |
| - Integrity validation (no tampering)                              |
+-------------------------------+------------------------------------+
                                |
                                v
[4] COMPLIANCE VALIDATION
+--------------------------------------------------------------------+
| - NGO internal rules (project scope, spending limits)              |
| - Donor restrictions (earmarks, region constraints)                |
| - Sanctions / jurisdiction filters (offline lists)                 |
| - Operational security rules (air‑gapped, no key export)           |
| - Classification: compliant / review / blocked                     |
+-------------------------------+------------------------------------+
                                |
                                v
[5] DECISION & REMEDIATION
+--------------------------------------------------------------------+
| - If compliant → proceed                                           |
| - If review → request more evidence                                |
| - If blocked → freeze workflow                                     |
| - Document reasons and rule references                             |
+-------------------------------+------------------------------------+
                                |
                                v
[6] NGO REPORT GENERATION
+--------------------------------------------------------------------+
| - Donation verification summary                                    |
| - Path derivation evidence                                         |
| - Compliance rule evaluation                                       |
| - Risk assessment                                                  |
| - Deterministic audit trail                                        |
| - Printable offline report (PDF)                                   |
+-------------------------------+------------------------------------+
                                |
                                v
[7] AUDIT TRAIL STORAGE
+--------------------------------------------------------------------+
| - Local encrypted storage                                          |
| - Versioned schema (tool version, rule version)                    |
| - Optional cryptographic checksum                                  |
| - Suitable for donors / auditors                                   |
+-------------------------------+------------------------------------+
                                |
                                v
[8] DONOR / AUDITOR REVIEW
+--------------------------------------------------------------------+
| - Donor receives compliance package                                |
| - Auditor verifies deterministic trail                             |
| - NGO receives approval / feedback                                 |
+--------------------------------------------------------------------+

```
