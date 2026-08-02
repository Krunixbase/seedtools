# SeedTools Documentation Index

The `docs/` directory contains the complete documentation system for **SeedTools Suite**.  
It provides architecture, modules, security model, compliance workflows, CLI/API references, and all technical materials required for audits, enterprise onboarding, and deterministic offline usage.

Documentation in SeedTools is:

- deterministic  
- offline‑safe  
- modular  
- enterprise‑grade  
- neon‑consistent  

---

## 📁 Folder Structure

```
docs/
├── architecture/
├── api/
├── compliance/
├── recovery/        (planned)
├── ngo/             (planned)
├── roadmap/
├── security/
└── assets/
```

---

## 🧱 Architecture Documentation

Location: `/docs/architecture/`

Contains:

- `system-architecture.md`  
- `modules.md`  
- `data-flow.md`  
- `trust-boundaries.md`  
- `diagrams.md`  

Architecture docs define:

- module interactions  
- deterministic workflows  
- trust boundaries  
- internal data flow  
- system‑level design  

---

## 🛡 Security Documentation

Location: `/docs/security/`

Includes:

- `security-model.md`  
- `threat-model.md`  
- `attack-surface.md`  
- `hardened-mode.md`  
- `masking-layer.md`  

Security docs describe:

- offline‑first model  
- isolation guarantees  
- deterministic cryptography  
- hardened execution paths  
- masking and zeroization rules  

---

## 📚 Compliance Suite

Location: `/docs/compliance/`

Includes:

- Compliance Suite Architecture  
- Rules Engine  
- Compliance Diagram  
- GDPR / SOC2 / IAM / Licensing workflows  

Compliance Suite integrates with:

- NGOs  
- enterprises  
- regulated environments  
- audit workflows  

---

## 🔄 Recovery Pipeline (Planned)

Location: `/docs/recovery/` *(folder will be created later)*

Will include:

- mnemonic → entropy → seed → keys  
- deterministic path exploration  
- anomaly detection  
- offline recovery workflows  

---

## 🛡 NGO Workflows (Planned)

Location: `/docs/ngo/` *(folder will be created later)*

Will include:

- identity verification  
- document integrity checks  
- compliance evidence generation  
- NGO audit workflows  

---

## 🖥 CLI & API Documentation

Location: `/docs/api/`

Includes:

- `cli-api.md`  
- future GUI/API docs  

Roadmap:

- `/docs/roadmap/cli-roadmap.md`

---

## 🗺 Roadmap Documentation

Location: `/docs/roadmap/`

Includes:

- CLI Roadmap  
- GUI Roadmap *(future)*  
- Module Roadmap *(future)*  

---

## 🖼 Documentation Assets

Location: `/docs/assets/`

Contains:

- splash screens  
- diagrams  
- icons  
- architecture graphics  

Branding assets come from:

- [branding/](/attachments/branding/)  
- [splash/](/attachments/branding/splash/)  
- [Color Palette](/attachments/branding/colors.md)  
- [Typography Rules](/attachments/branding/typography.md)  
- [Brandbook](/attachments/branding/guidelines/brandbook.md)

---

## 🧩 Related Repository Sections

- Main README → `/README.md`  
- Attachments → `/attachments/`  
- Pitch Deck → `/attachments/pitch-deck/`  
- Branding → `/attachments/branding/`  
- Splash Screens → `/attachments/branding/splash/`  
- Color Palette → `/attachments/branding/colors.md`  
- Typography → `/attachments/branding/typography.md`  
- Brandbook → `/attachments/branding/guidelines/brandbook.md`

---

## 🛠 Contribution Rules

When adding new documentation:

- follow deterministic formatting  
- keep sections minimal and structured  
- use local links (`/docs/...`)  
- include diagrams in `/docs/assets/`  
- update this README when structure changes  
- maintain consistency with SeedTools branding  

---
