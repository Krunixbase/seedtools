# **Mnemonic Tools — SeedTools Suite**

## **Overview**

Mnemonic Tools is the SeedTools Suite application focused on **creating, validating, transforming, and analyzing BIP39 mnemonics**.  
It provides a safe, offline environment for generating high‑quality seeds, validating existing backups, converting between formats, and inspecting mnemonic structure.

It is designed for:

- self‑custody users generating secure backups,  
- NGOs and support teams assisting users in the field,  
- high‑risk users who require offline‑only workflows,  
- developers testing BIP39 implementations,  
- educators teaching how mnemonics and entropy work.





Mnemonic Tools does **not** store, transmit, or sync any mnemonic data.  
Everything runs locally and offline.

---

# **Key Capabilities**

- **Mnemonic Generation**  
  - 12 / 15 / 18 / 21 / 24‑word BIP39  
  - high‑quality entropy  
  - offline‑safe generation  

- **Mnemonic Validation**  
  - checksum verification  
  - wordlist conformity  
  - invalid‑word detection  

- **Entropy Conversion**  
  - mnemonic → entropy  
  - entropy → mnemonic  
  - checksum reconstruction  

- **Passphrase Tools**  
  - validate passphrase usage  
  - detect common mistakes  
  - show seed changes with/without passphrase  

- **Wordlist Tools**  
  - search BIP39 wordlist  
  - detect similar‑looking words  
  - highlight common transcription errors  

- **Offline‑First Architecture**  
  - no telemetry  
  - no external API calls  
  - safe for air‑gapped devices  

---

# **Typical Workflows**

## **1. Generate a new secure mnemonic**

1. Choose word count (12–24).  
2. Click **Generate**.  
3. Tool displays:
   - mnemonic  
   - entropy  
   - checksum bits  
4. User writes it down offline.





---

## **2. Validate an existing mnemonic**

1. Paste mnemonic.  
2. Tool performs:
   - checksum validation  
   - wordlist conformity  
   - entropy reconstruction  
3. Output includes:
   - valid/invalid  
   - incorrect words  
   - checksum mismatch  
   - drift indicators  

---

## **3. Convert mnemonic ↔ entropy**

1. Enter mnemonic or entropy hex.  
2. Tool displays:
   - raw entropy  
   - checksum bits  
   - mnemonic mapping  
3. Useful for:
   - debugging  
   - education  
   - verifying wallet implementations  

---

## **4. Analyze passphrase usage**

1. Enter mnemonic.  
2. Enter optional passphrase.  
3. Tool shows:
   - seed with passphrase  
   - seed without passphrase  
   - difference indicators  
4. Helps detect:
   - forgotten passphrases  
   - incorrect passphrases  
   - accidental passphrase usage  

---

# **Who This Tool Is For**

- **Self‑custody users**  
  Generate and validate backups safely.

- **NGOs & support teams**  
  Diagnose mnemonic issues offline.

- **High‑risk users**  
  Create secure backups without touching the internet.

- **Developers**  
  Test BIP39 implementations and entropy handling.

- **Educators**  
  Demonstrate how mnemonics, entropy, and checksum interact.

---

# **Security Notes**

- Always generate mnemonics on a **trusted, offline machine**.  
- Never store mnemonics digitally unless encrypted.  
- Never paste mnemonics into online tools.  
- Passphrases must be written down separately and securely.  
- Verify builds using reproducible build instructions (when available).

---

# **Roadmap (Preview)**

- **Mnemonic Reconstruction Assistant**  
- **Advanced Similar‑Word Detection**  
- **Entropy Drift Visualizer**  
- **Taproot‑specific Mnemonic Checks**  
- **Integration with Entropy Inspector**  
- **Reproducible Builds**  

---
