                   +---------------------------+
                   |       Input Sources       |
                   +---------------------------+
                   | - Mnemonics               |
                   | - XPRVs / XPUBs           |
                   | - Wallet files            |
                   | - Addresses               |
                   +-------------+-------------+
                                 |
                                 v
+---------------------------------------------------------------+
|                     Processing Engines                        |
+---------------------------------------------------------------+
|  +------------------+   +------------------+   +-------------+|
|  | Mnemonic Tools   |   | Entropy Engine   |   | Path        ||
|  | - validation     |   | - entropy checks |   | Explorer    ||
|  | - correction     |   | - scoring        |   | - BIP32/44  ||
|  | - heuristics     |   | - anomaly detect |   | - BIP49/84  ||
|  +------------------+   +------------------+   | - Taproot   ||
|                                                   +----------+|
|  +-----------------------------------------------------------+|
|  | Forensics Engine                                          ||
|  | - address scanning                                        ||
|  | - UTXO discovery                                          ||
|  | - Taproot script-path analysis (future)                   ||
|  +-----------------------------------------------------------+|
+---------------------------------------------------------------+
                                 |
                                 v
                   +---------------------------+
                   |          Outputs          |
                   +---------------------------+
                   | - Recovery candidates     |
                   | - Path suggestions        |
                   | - Reports (NGO-ready)     |
                   | - Risk assessments        |
                   +-------------+-------------+
                                 |
                                 v
                   +---------------------------+
                   |         Storage           |
                   +---------------------------+
                   | - Local encrypted files   |
                   | - Offline exports (PDF)   |
                   | - Temporary RAM-only data |
                   +---------------------------+
