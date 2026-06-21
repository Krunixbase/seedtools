<p align="center">
  <img src="docs/assets/seedtools-logo.png" width="220" alt="SeedTools Logo"/>
</p>

<h1 align="center">SeedTools Suite</h1>

<p align="center">
  Offline • Deterministic • Secure • Forensics & Compliance Toolkit
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" />
  <img src="https://img.shields.io/badge/security-offline%20first-blue" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" />
  <img src="https://img.shields.io/badge/python-3.10%2B-yellow" />
  <a href="DONATE.md">
    <img src="https://img.shields.io/badge/Donate-BTC-black?logo=bitcoin&logoColor=white" />
  </a>
  <a href="https://mempool.space/address/bc1qj2gwhsraad4stznukpp9my764nggmkjea84hd2">
    <img src="https://img.shields.io/badge/Explorer-mempool.space-orange?logo=bitcoin&logoColor=white" />
  </a>
</p>

---

SeedTools Suite is an offline, deterministic security toolkit for:

- Bitcoin seed recovery  
- entropy analysis  
- crypto forensics  
- NGO verification workflows  
- compliance automation  

Designed for high‑risk users, journalists, activists, and organizations operating in adversarial environments.

---

# 1. ⭐ Features Overview

- deterministic seed recovery  
- entropy analysis & anomaly detection  
- BIP32/44/49/84/86/Taproot path exploration  
- address & UTXO scanning  
- NGO verification workflows  
- compliance automation (GDPR, SOC2, IAM, Licensing)  
- offline audit trail generation  

---

# 2. 🏗 Architecture

SeedTools Suite includes a complete architecture documentation set covering:

- System Architecture  
- Module Map  
- Data Flow Diagram  
- Trust Boundaries  
- Architecture Diagrams  

All architecture documentation is located in:

```
docs/architecture/
 ├── system-architecture.md
 ├── modules.md
 ├── data-flow.md
 ├── trust-boundaries.md
 └── diagrams.md
```

---

# 3. 🔄 Recovery Pipeline

SeedTools includes a deterministic recovery pipeline for:

- mnemonic → entropy → seed → keys  
- path exploration  
- anomaly detection  

Full recovery workflow documentation will be added in future releases.

*(Folder `docs/recovery/` does not exist yet — documentation will be created later.)*

---

# 4. 🛡 NGO Workflows

SeedTools supports NGO verification and audit workflows, including:

- identity verification  
- document integrity checks  
- compliance evidence generation  

Detailed NGO workflow documentation will be added in future releases.

*(Folder `docs/ngo/` does not exist yet — documentation will be created later.)*

---

# 5. 📚 Compliance Suite

The Compliance Suite is fully documented and available here:

```
docs/compliance/
```

It includes:

- Compliance Suite Architecture  
- Rules Engine  
- Compliance Diagram  
- GDPR / SOC2 / IAM / Licensing workflows  

---

# 6. 🧩 Modules

SeedTools Suite consists of the following modules:

- **Mnemonic Tools**  
- **Entropy Tools**  
- **Path Explorer**  
- **Scanner**  
- **Forensics Engine**  
- **Compliance Suite**  
- **Reporting Engine**  

Module documentation is located in:

```
modules/
```

---

# 7. 🛠 Installation

```
git clone https://github.com/Krunixbase/seedtools
cd seedtools
pip install -r requirements.txt
```

---

# 8. 🖥 Usage (CLI)

```
python seedtools.py --help
```

The CLI module is planned and documented here:

- **CLI API**  
- **CLI Roadmap**  

---

# 9. 🗺 Roadmap

- Desktop GUI  
- Shamir Tools  
- Taproot forensics  
- NGO reporting engine  
- Full compliance automation  

Full roadmap is available here:

- **SeedTools PRO Roadmap**  

---

# 10. 💛 Donate

If you find SeedTools useful and want to support its development, security research, and maintenance, you can donate BTC.

**Bitcoin (BTC):**

```
bc1qj2gwhsraad4stznukpp9my764nggmkjea84hd2
```

Your support helps fund:

- ongoing development of SeedTools Suite  
- security audits and cryptographic reviews  
- documentation and research  
- maintenance of offline and air‑gapped workflows  

Thank you for supporting open‑source security tools.

---

# 11. **Why SeedTools?**

SeedTools Suite was designed as a **next generation of security tools**, combining:

- deterministic cryptographic operations  
- entropy analysis and forensics  
- NGO verification workflows  
- compliance automation  
- modular enterprise architecture  

Why SeedTools?

- **Offline-first** — works in air-gapped environments  
- **Auditable** — every step is repeatable and verifiable  
- **Modular** — easily extensible and integrated  
- **Secure** — zero telemetry, zero network, zero API  
- **Practical** — real-world use cases for NGOs, security, and compliance  
- **Professional** — documentation, whitepaper, demo, roadmap  

SeedTools Suite is not just another "seed tool."  
It's a **security platform**.

---

# 12. 🚀 Demo

SeedTools includes deterministic, offline‑safe demos illustrating how the toolkit works in practice.

### Available demos

— core examples covering mnemonic → entropy → seed → address derivation.  
— extended workflows including Taproot, Ethereum, and multi‑path derivations.

Demo files:

```
demo/
 ├── README-demo.md
 └── README-seedtools-extra-demo.md
```

These demos are deterministic, reproducible, and safe for air‑gapped environments.

---

# 12.1 🎥 Demo Videos

SeedTools Suite includes three short demonstration videos showing deterministic, offline‑safe workflows using **official BIP‑39 test vectors** (12, 18 and 24 words).  
All seeds come from the public BIP‑39 specification and **have no financial value**.

### ▶️ Available demo videos

- **12‑word demo** — deterministic seed → seed and seed → xprv verification  
- **18‑word demo** — demonstration on a longer seed with deterministic output validation  
- **24‑word demo** — full deterministic demonstration using the longest test vector  

Video files are stored in the repository:

```
seedtools/demo/videos/
```

These videos are compressed for GitHub (<25 MB each) and safe for offline environments.

---

# 13. 📄 License

MIT License.

---

# 📬 Contact

**Email:** krunixbase@gmail.com  
**Repository:** [https://github.com/Krunixbase/seedtools](https://github.com/Krunixbase/seedtools)  

---

