<p align="center">
  <img src="docs/assets/splash-special-icon.png" width="220" alt="SeedTools Logo"/>
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

*(Folder [recovery](docs/recovery/) does not exist yet — documentation will be created later.)*

---

# 4. 🛡 NGO Workflows

SeedTools supports NGO verification and audit workflows, including:

- identity verification  
- document integrity checks  
- compliance evidence generation  

Detailed NGO workflow documentation will be added in future releases.

*(Folder [ngo](docs/ngo/) does not exist yet — documentation will be created later.)*

---

# 5. 📚 Compliance Suite

The Compliance Suite is fully documented and available here:


[compliance](docs/compliance/)


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


[modules](modules/)


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

- **[CLI API](../api/cli-api.md)**  
- **[CLI Roadmap](../roadmap/cli-roadmap.md)**  

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


[demo videos](demo/videos/)


These videos are compressed for GitHub (<25 MB each) and safe for offline environments.

---

# 13. 🛠️ **Development Workflow**

SeedTools Suite uses a structured and auditable development workflow designed for security‑critical environments, deterministic builds, and long‑term maintainability.

### **Branch Structure**

- **main** — stable, production‑ready branch.  
  Contains only reviewed and tested code. All release tags (`v1.x.x`) are created from `main`.

- **dev** — active development branch.  
  All new features, improvements, and refactors are merged here before stabilization.

- **release/v1.x** — release preparation branches.  
  Used for final QA, documentation updates, version bumps, and preparing stable releases.  
  Example: `release/v1.0`.

- **hotfix/v1.x.x** — emergency patches for production.  
  Critical fixes start from `main` and are merged back into both `main` and `dev`.

---

### **Workflow Overview**

1. Developers create feature branches from **dev**  
   (`feature/short-description`)

2. Completed features are merged into **dev** via Pull Requests

3. When preparing a release:  
   **dev → release/v1.x**

4. After stabilization and QA:  
   **release/v1.x → main**

5. A version tag is created on **main**  
   (`v1.0.0`, `v1.1.0`, etc.)

6. Hotfixes start from **main** and merge back into both **main** and **dev**

---

### **Branch Naming Conventions**

- Feature branches:  
  **feature/short-description**

- Bugfix branches:  
  **bugfix/issue-id-description**

- Release branches:  
  **release/vX.Y**

- Hotfix branches:  
  **hotfix/vX.Y.Z**

---

### **Why This Workflow?**

- Ensures deterministic, stable releases  
- Keeps production code isolated from development  
- Supports offline, auditable security workflows  
- Matches expectations of security‑focused grant programs  
- Enables clean versioning and long‑term maintenance  

---

# 14. 🛡️ Security Model

SeedTools Suite follows a strict, offline‑first security model designed for adversarial environments, high‑risk users, and deterministic cryptographic workflows.  
The model is based on four pillars: **Isolation**, **Determinism**, **Transparency**, and **Minimal Attack Surface**.

---

## **1. Isolation Model**

SeedTools is designed to operate in fully offline, air‑gapped environments.

- No network connections  
- No telemetry  
- No external API calls  
- No automatic updates  
- All operations run locally and deterministically  

This ensures that sensitive data (mnemonics, entropy, seeds, keys, compliance evidence) never leaves the device.

---

## **2. Deterministic Execution**

All cryptographic operations follow deterministic, reproducible workflows:

- BIP‑39 → entropy → seed  
- BIP‑32/44/49/84/86 derivation  
- Taproot deterministic paths  
- Deterministic forensics workflows  
- Deterministic compliance evidence generation  

This allows independent verification, reproducibility, and offline audits.

---

## **3. Trust Boundaries**

SeedTools defines clear trust boundaries across modules:

- **Core cryptography** (entropy, seed, derivation)  
- **Forensics engine** (analysis, scanning, anomaly detection)  
- **Compliance suite** (rules engine, audit trails)  
- **NGO workflows** (identity, document integrity, verification)  
- **CLI / GUI** (user interaction layer)

Each boundary is isolated to prevent cross‑module data leakage.

Full trust boundary documentation is available in:


[trust boundaries](docs/rchitecture/trust-boundaries.md)


---

## **4. Threat Model**

SeedTools assumes an adversarial environment with threats including:

- Device compromise  
- Malware / keyloggers  
- Supply‑chain attacks  
- Side‑channel attacks  
- Human error  
- Data corruption  
- Insider threats  
- Forensics tampering  

The toolkit mitigates these threats through:

- Offline execution  
- Deterministic workflows  
- No external dependencies  
- Minimal code surface  
- Reproducible builds  
- Clear audit trails  

Detailed threat model:


[threat model](docs/security/threat-model.md)


---

## **5. Attack Surface Reduction**

SeedTools minimizes attack surface by design:

- No networking stack  
- No browser engine  
- No remote calls  
- No dynamic imports  
- No background services  
- Minimal dependencies  
- Strict module boundaries  

This dramatically reduces the number of possible attack vectors.

---

## **6. Hardened Mode**

SeedTools includes a hardened mode for high‑risk users:

- Read‑only execution  
- No file writes  
- No logs  
- No caching  
- No temporary files  
- Memory‑only operations  

Documentation:


[hardened mode](docs/security/hardened-mode.md)


---

## **7. Masking Layer**

Sensitive data is masked at every stage:

- In‑memory masking  
- Zeroization of buffers  
- No plaintext persistence  
- No accidental logging  
- No stack traces with sensitive data  

Documentation:


[masking layer](docs/security/masking-layer.md)


---

## **8. Security Documentation Index**

All security documentation is located in:

```
docs/security/
 ├── security-model.md
 ├── threat-model.md
 ├── attack-surface.md
 ├── hardened-mode.md
 └── masking-layer.md
```

---

# 🌍 15. Krunixbase Manifest  
> An ecosystem built on truth.  
> Systems that do not lie.  
> Tools that never guess.

Krunixbase exists because the world needs software that is **always true** — regardless of context, device, or interpretation. This is the foundation of the entire ecosystem and the reason SeedTools Suite was created.

---

## 🔥 15.1 Core Principles

- **Truth** — results are deterministic, predictable, and verifiable.  
- **Determinism** — the same input always produces the same output.  
- **Transparency** — no hidden logic, no magic, no ambiguity.  
- **Security** — simplicity, modularity, and clarity form the basis of safety.  
- **Minimalism** — no unnecessary features, no noise, no bloat.  
- **Authenticity** — the ecosystem was built from real needs, not marketing.  
- **Freedom** — tools that empower the user, not control them.  
- **Responsibility** — if a tool can help people, it must be reliable.  
- **Human‑centric design** — technology is a means, not the goal.

---

## 📄 15.2 Full Manifest  
The complete version of the Krunixbase Manifest — describing the philosophy, mission, and values of the ecosystem — is available in the Krunixbase Ecosystem repository.

---

## 🧭 15.3 Why the Manifest Matters  
The Manifest defines the identity of the project.  
It shows that SeedTools Suite is not a random collection of utilities, but a part of a larger vision — an ecosystem built on truth, determinism, and responsibility.

---

# 16. 📄 License

MIT License.

---

# 📬 Contact

**Email:** krunixbase@gmail.com  
**Repository:** https://github.com/Krunixbase/seedtools

---

