# 📘 **SeedTools Suite — Developer Onboarding Guide**

Welcome to the **SeedTools Suite** — a deterministic, offline‑safe toolkit for Bitcoin recovery, forensics, entropy analysis, and secure workflows.

This guide will help you get started quickly and safely.

---

# 1. 🎯 What SeedTools Is

SeedTools is a modular ecosystem consisting of:

- **SeedTools Core** — deterministic cryptographic engine  
- **SeedTools Utils** — shared utility layer  
- **SeedTools GUI** — secure UI framework  
- **SeedTools CLI Module** — deterministic command‑line engine  
- Desktop apps, recovery tools, forensics tools, scanners, inspectors  

Everything is:

- offline‑first  
- deterministic  
- auditable  
- reproducible  
- hardened for high‑risk environments  

---

# 2. ⚙️ Setting Up Your Development Environment

## 2.1 Requirements

- Python 3.10+  
- Git  
- Virtual environment (`venv`)  
- Optional: WSL2 (recommended for Windows)  

## 2.2 Clone the repository

```bash
git clone https://github.com/seedtools/seedtools.git
cd seedtools
```

## 2.3 Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## 2.4 Install dependencies

```bash
pip install -r requirements.txt
```

---

# 3. 🧩 Understanding the Architecture

SeedTools is built around **modular, deterministic layers**:

```
Core  ←  Utils  ←  CLI / GUI  ←  Tools / Desktop
```

See:

- **Architecture Diagram**  
- **Data Flow Diagram**  

---

# 4. 🔐 Working With SeedTools Core

Core provides:

- BIP39  
- BIP32  
- BIP44/49/84/86  
- Address generation  
- Entropy & checksum tools  

### Example: Convert mnemonic → entropy

```python
from seedtools.core import mnemonic_to_entropy

entropy = mnemonic_to_entropy("abandon abandon ...")
```

### Example: Derive a key

```python
from seedtools.core import derive_xprv

xprv = derive_xprv(seed, "m/84'/0'/0'/0/5")
```

---

# 5. 🧰 Working With SeedTools Utils

Utils provides:

- validation  
- encoding/decoding  
- hashing  
- secure buffers  
- formatting  

### Example: Validate a path

```python
from seedtools.utils import validate_path_syntax

validate_path_syntax("m/84'/0'/0'/0/5")
```

---

# 6. 🖥 Working With SeedTools GUI

GUI provides:

- secure input components  
- workflow engine  
- preset‑aware UI  
- deterministic rendering  

### Example: Create a secure mnemonic field

```python
MnemonicField(masked=True)
```

---

# 7. 🖥‍💻 Working With SeedTools CLI Module

CLI Module powers:

- mnemonic tools  
- entropy inspector  
- recovery engine  
- forensics mode  
- address scanner  

### Example: Run a CLI command

```bash
seedtools mnemonic validate "abandon abandon ..."
```

---

# 8. 🛡 Security & Hardened Mode

SeedTools is designed for adversarial environments.

### Hardened Mode disables:

- disk writes  
- caching  
- logs  
- shell history  
- animations (GUI)  

### Sensitive data is always:

- stored in ephemeral memory  
- zeroized after use  
- never sent over the network  

---

# 9. 🧪 Testing & Validation

SeedTools uses:

- deterministic test vectors  
- reproducible workflows  
- cross‑wallet compatibility tests  

Run tests:

```bash
pytest -q
```

---

# 10. 🤝 Contributing

We welcome contributions from:

- developers  
- auditors  
- security researchers  
- NGO tech teams  

### Steps:

1. Fork the repo  
2. Create a feature branch  
3. Follow deterministic coding standards  
4. Add tests  
5. Submit a PR  

---

# 11. 📦 Project Structure

```
seedtools/
 ├── core/        # cryptographic engine
 ├── utils/       # shared utilities
 ├── gui/         # UI framework
 ├── cli/         # CLI engine
 ├── tools/       # apps (recovery, forensics, etc.)
 ├── docs/        # documentation
 └── tests/       # test suite
```

---

# 12. 📚 Recommended Next Steps

- Read **Module Documentation**  
- Explore **API Documentation**  
- Review **Core workflows**  
- Run the CLI tools  
- Build your first module  

---

# 13. 🚀 You're Ready

You now understand:

- the architecture  
- the modules  
- the workflows  
- the security model  
- how to build and extend SeedTools  

Welcome to the SeedTools ecosystem.

---
