# 📘 **SeedTools Suite — Contributor Guide**

SeedTools Suite is an offline‑first, deterministic, security‑focused toolkit used by developers, auditors, NGOs, and high‑risk users.  
This guide explains how to contribute safely, effectively, and consistently with the project’s architecture and security model.

---

## 1. 🎯 Contribution Philosophy

SeedTools follows strict principles:

- **deterministic behavior**  
- **offline‑first architecture**  
- **no telemetry, no networking**  
- **auditable and reproducible code**  
- **security over convenience**  
- **modular, testable components**

All contributions must respect these principles.

---

## 2. 🧩 Ways You Can Contribute

You can contribute in many areas:

- **Code contributions**  
- **Documentation improvements**  
- **Security reviews**  
- **Testing & reproducibility**  
- **GUI/UX improvements**  
- **CLI enhancements**  
- **Architecture & module design**  

Non‑code contributions are equally valuable.

---

## 3. ⚙️ Development Environment Setup

### 3.1 Clone the repository

```bash
git clone https://github.com/Krunixbase/seedtools.git
cd seedtools
```

### 3.2 Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3.3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. 📦 Project Structure

SeedTools Suite is organized into modular packages

See also:

- **Module Documentation**  
- **Architecture Diagram**  
- **Data Flow Diagram**  

---

## 5. 🛡 Security Requirements (Mandatory)

All contributions must follow SeedTools security rules:

### ✔ No networking  
No HTTP, DNS, sockets, telemetry, analytics, or remote assets.

### ✔ Deterministic behavior  
No randomness except cryptographic entropy from Core.

### ✔ Ephemeral memory  
Sensitive data must be stored only in temporary buffers.

### ✔ Zeroization  
Buffers must be wiped after use.

### ✔ Hardened Mode compatibility  
Your code must not break hardened mode.

### ✔ Reproducibility  
Builds must remain deterministic.

See: **Security Guide**.

---

## 6. 🧪 Testing Requirements

Every PR must include:

- deterministic test vectors  
- reproducible test cases  
- no network dependencies  
- cross‑platform compatibility  

Run tests:

```bash
pytest -q
```

---

## 7. 🔄 Contribution Workflow

### 7.1 Fork the repository

Click **Fork** on GitHub.

### 7.2 Create a feature branch

```bash
git checkout -b feature/my-improvement
```

### 7.3 Make your changes  
Follow deterministic and offline‑first principles.

### 7.4 Add tests  
Every new feature must include tests.

### 7.5 Commit your changes

```bash
git commit -m "Add: description of your change"
```

### 7.6 Push and open a Pull Request

```bash
git push origin feature/my-improvement
```

Then open a PR to the main repository.

---

## 8. 🧭 Code Style & Guidelines

### ✔ Python style  
- PEP8  
- type hints required  
- no wildcard imports  
- no unused dependencies  

### ✔ Deterministic logic  
- no time‑based randomness  
- no OS‑dependent behavior  
- no floating‑point nondeterminism  

### ✔ Error handling  
Use unified error types from Utils.

### ✔ Logging  
No logs in hardened mode.

---

## 9. 🧩 Module‑Specific Rules

### **Core**
- must remain deterministic  
- no external crypto libraries  
- strict validation rules  

### **Utils**
- must remain dependency‑free  
- must be deterministic  
- must support zeroization  

### **GUI**
- no external fonts or assets  
- secure input components only  
- deterministic rendering  

### **CLI**
- deterministic argument parsing  
- no shell history in hardened mode  
- structured output  

---

## 10. 📫 Reporting Security Issues

Do **not** open a public GitHub issue.

Report privately to:

```
krunixbase@gmail.com
```

Include:

- description  
- reproduction steps  
- affected version  
- potential impact  

---

## 11. ❤️ Thank You

SeedTools exists because of contributors like you.  
Your work strengthens a public‑good toolkit used by NGOs, journalists, activists, and high‑risk communities worldwide.

---
