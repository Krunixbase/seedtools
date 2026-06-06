# **SeedTools CLI Module — SeedTools Suite**

## **Overview**

SeedTools CLI Module provides the **programmatic and internal engine** behind the SeedTools command‑line interface.  
While the *application* `seedtools-cli` exposes commands to users, this module contains the **core logic**, **command routing**, **argument parsing**, and **integration layer** that powers:

- SeedTools CLI binary  
- embedded CLI inside SeedTools Desktop  
- automation workflows  
- scripting interfaces  
- NGO field‑tool bundles  
- Tails/Qubes hardened CLI mode  

This module ensures that the CLI is:

- **deterministic**  
- **offline‑first**  
- **secure**  
- **modular**  
- **reproducible**  

It is the **engine** behind all CLI‑based operations in the Suite.

---

# **Key Capabilities**

- **Command Router**  
  - maps commands to internal handlers  
  - supports nested command groups  
  - deterministic argument parsing  

- **Mnemonic Tools CLI Engine**  
  - validate mnemonics  
  - convert mnemonic ↔ entropy  
  - inspect checksum and structure  

- **Entropy Inspector CLI Engine**  
  - entropy validation  
  - drift detection  
  - corruption mapping  

- **Recovery Engine CLI**  
  - derive addresses  
  - scan index ranges  
  - verify ownership  

- **Address Scanner CLI Engine**  
  - batch verification  
  - deep path scanning  
  - multi‑account scanning  

- **Path Explorer CLI Engine**  
  - validate derivation paths  
  - derive keys for any path  
  - generate addresses  

- **Forensics Mode Engine**  
  - detect corrupted mnemonics  
  - analyze entropy drift  
  - identify path mismatches  

- **Secure Execution Layer**  
  - ephemeral memory  
  - no shell history (optional)  
  - hardened mode support  

---

# **Architecture**

SeedTools CLI Module is structured into:

- **Command Layer**  
  - command definitions  
  - argument parsing  
  - routing  

- **Execution Layer**  
  - secure execution context  
  - hardened mode  
  - ephemeral buffers  

- **Integration Layer**  
  - bridges to SeedTools Core  
  - bridges to SeedTools Utils  
  - bridges to Desktop embedded terminal  

- **Output Layer**  
  - human‑readable output  
  - structured output (JSON planned)  
  - export‑friendly formatting  

---

# **Typical Workflows**

## **1. Running a mnemonic validation command**

1. CLI receives command:  
   ```
   seedtools mnemonic validate "..."
   ```
2. Command Router maps to Mnemonic Engine.  
3. Engine validates mnemonic using Core.  
4. Output Layer prints deterministic result.

---

## **2. Running a recovery scan**

1. CLI receives:  
   ```
   seedtools recover --mnemonic "..." --bip84
   ```
2. Router → Recovery Engine.  
3. Engine derives keys using Core.  
4. Engine scans index ranges.  
5. Output Layer prints results.

---

## **3. Running a forensics analysis**

1. CLI receives:  
   ```
   seedtools forensics --mnemonic "..."
   ```
2. Router → Forensics Engine.  
3. Engine analyzes entropy drift, checksum, corruption.  
4. Output Layer prints structured diagnostics.

---

# **Who This Module Is For**

- **Developers**  
  Building CLI features or extending commands.

- **Automation engineers**  
  Integrating SeedTools into scripts and pipelines.

- **NGOs & support teams**  
  Using CLI in field‑ready offline environments.

- **High‑risk users**  
  Running CLI in hardened, no‑trace modes.

- **Auditors**  
  Reviewing deterministic command execution.

---

# **Security Notes**

- No telemetry, no external calls.  
- Sensitive data is stored only in **ephemeral memory**.  
- Hardened Mode disables:
  - shell history  
  - disk writes  
  - caching  
- All operations are deterministic and offline.  
- Builds must be verified using reproducible build instructions.

---

# **Roadmap (Preview)**

- **JSON Output Mode**  
- **Batch Forensics Engine**  
- **Taproot‑Specific CLI Tools**  
- **Hardened Mode PRO**  
- **Automation API**  
- **Reproducible Builds**  

---
