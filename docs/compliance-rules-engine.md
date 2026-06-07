```

+====================================================================+
|                     SeedTools Compliance Rules Engine              |
+====================================================================+

[1] INPUT LAYERS
+--------------------------------------------------------------------+
| - Technical evidence (addresses, UTXOs, paths, reports)            |
| - NGO policy definitions (internal rules, thresholds)              |
| - Donor constraints (earmarks, allowed regions, purposes)          |
| - Regulatory / sanctions lists (offline datasets)                  |
+-------------------------------+------------------------------------+
                                |
                                v
[2] NORMALIZATION & MAPPING
+--------------------------------------------------------------------+
| - Normalize formats (amounts, currencies, labels)                  |
| - Map evidence to entities (project, donor, wallet)                |
| - Align data with rule domains (risk, geography, usage)            |
+-------------------------------+------------------------------------+
                                |
                                v
[3] RULE SETS
+--------------------------------------------------------------------+
| - NGO Policy Rules                                                 |
|   • spending limits, project scope, approval chains                |
| - Donor Rules                                                      |
|   • earmarks, restricted uses, reporting requirements              |
| - Security Rules                                                   |
|   • offline operation, key‑handling, environment constraints       |
| - Jurisdiction / Sanctions Rules                                   |
|   • blocked regions, entities, addresses                           |
+-------------------------------+------------------------------------+
                                |
                                v
[4] EVALUATION ENGINE
+--------------------------------------------------------------------+
| - Apply rule sets to normalized evidence                           |
| - Compute compliance status per rule group                         |
| - Aggregate results: compliant / review / blocked                  |
| - Attach reasons and rule references                               |
+-------------------------------+------------------------------------+
                                |
                                v
[5] OUTPUT & INTEGRATION
+--------------------------------------------------------------------+
| - Compliance decision (per donation / flow)                        |
| - Detailed rule evaluation report                                  |
| - Remediation suggestions (extra evidence, clarifications)         |
| - Feed into NGO reports and audit trail                            |
+--------------------------------------------------------------------+

```
