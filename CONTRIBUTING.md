# Contributing to SeedTools Suite

Thank you for your interest in contributing to **SeedTools Suite** — a deterministic, offline‑first toolkit for Bitcoin recovery, forensics, entropy diagnostics, and wallet structure analysis.

This project is built as a **public good**, and contributions of all kinds are welcome:
code, documentation, testing, UX, security review, and research.

---

## 🧭 Project Structure

```
seedtools/
├── financing/          # grant documents & applications
├── applications/       # mini‑grants (OpenSats, HRF, BTCPay, Spiral)
├── product/            # architecture, modules, features
├── roadmap/            # roadmap PRO + milestones
├── demo/               # scenarios, corrupted mnemonics, case studies
├── branding/           # logo, colors, typography
├── modules/            # core engines, GUI, CLI, utils
└── README.md
```

---

## 🛠 How to Contribute

### 1. Fork the repository
Click **Fork** on GitHub and clone your fork locally:

```bash
git clone https://github.com/<your-username>/seedtools.git
cd seedtools
```

### 2. Create a feature branch

```bash
git checkout -b feature/my-improvement
```

### 3. Make your changes
Follow the coding guidelines below.

### 4. Commit your work

```bash
git commit -m "Add: description of your change"
```

### 5. Push and open a Pull Request

```bash
git push origin feature/my-improvement
```

Then open a PR to the main repository.

---

## 🧩 Coding Guidelines

### Deterministic by design
All modules must follow deterministic principles:

- reproducible outputs  
- no randomness  
- no network calls  
- no telemetry  
- no external dependencies that break determinism  

### Offline‑first
SeedTools **must always work offline**.

### Security‑focused
- no logging sensitive data  
- no clipboard usage  
- memory‑safe patterns  
- avoid unnecessary allocations  

### Modular architecture
Each module should be isolated and testable independently.

---

## 🧪 Testing

All contributions must include:

- deterministic test vectors  
- reproducible test cases  
- cross‑module validation where applicable  

Tests must run offline and produce identical results across environments.

---

## 📚 Documentation

Every new feature must include:

- a short description in `product/modules.md`  
- usage examples (CLI or Desktop)  
- test vectors if applicable  

Documentation is as important as code.

---

## 🛡 Security Contributions

Security‑related contributions are highly valued.

If you discover a vulnerability:

1. **Do NOT open a public issue.**
2. Contact the maintainer privately at:  
   **security@seedtools.org** (placeholder — replace when ready)
3. Provide a reproducible test case if possible.

---

## 🧱 Pull Request Requirements

A PR must include:

- clear description of the change  
- reference to related issue (if exists)  
- tests for new functionality  
- documentation updates  
- confirmation that code runs offline  

PRs that break determinism or offline‑first principles will be rejected.

---

## 🤝 Ways to Contribute (Non‑Code)

You can help even without writing code:

- improve documentation  
- create demo scenarios  
- add corrupted mnemonic examples  
- help with UX flows  
- review grant documents  
- translate documentation  
- test modules on different platforms  

All contributions matter.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the **MIT License**, the same as the main project.

---

## ❤️ Thank You

SeedTools Suite exists because of contributors like you.  
Your help strengthens a public good used by individuals, NGOs, and high‑risk communities worldwide.

---
