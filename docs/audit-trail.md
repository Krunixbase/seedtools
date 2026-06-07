```

+====================================================================+
|                        SeedTools Audit Trail                       |
+====================================================================+

[1] CONTEXT & SESSION START
+--------------------------------------------------------------------+
| - Operator identity / role (optional)                              |
| - NGO / project context                                            |
| - Date / time (local, offline)                                     |
| - Machine / environment label (air‑gapped, lab, etc.)              |
+-------------------------------+------------------------------------+
                                |
                                v
[2] INPUT CAPTURE
+--------------------------------------------------------------------+
| - What was provided:                                               |
|   • mnemonics / XPUBs / wallet files / addresses                   |
| - How it was provided (file, manual entry, etc.)                   |
| - Non‑sensitive metadata only (no raw secrets in logs)             |
+-------------------------------+------------------------------------+
                                |
                                v
[3] ACTION LOG
+--------------------------------------------------------------------+
| - Tools invoked (modules, versions)                                |
| - Parameters (ranges, paths, options)                              |
| - Sequence of steps (in order)                                     |
| - Errors / warnings / anomalies                                    |
+-------------------------------+------------------------------------+
                                |
                                v
[4] DECISION POINTS
+--------------------------------------------------------------------+
| - Operator choices (accepted / rejected candidates)                |
| - Branching (which path / wallet / derivation was followed)        |
| - Manual overrides or notes                                        |
+-------------------------------+------------------------------------+
                                |
                                v
[5] OUTPUT RECORD
+--------------------------------------------------------------------+
| - Recovery candidates produced                                     |
| - Final selected result (if any)                                   |
| - Generated reports (NGO / audit)                                  |
| - Exported artifacts (PDF, CSV, etc.)                              |
+-------------------------------+------------------------------------+
                                |
                                v
[6] AUDIT TRAIL STORAGE
+--------------------------------------------------------------------+
| - Local, offline log file / report                                 |
| - Optional cryptographic checksum / signature                      |
| - Versioned format (tool version, schema version)                  |
| - Suitable for external review / reproducibility                   |
+--------------------------------------------------------------------+

```
