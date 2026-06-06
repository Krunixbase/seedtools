# **Spiral Grant Application**
**Project:** SeedTools 2.0 — Offline HD Wallet Recovery & Forensics Toolkit
**Applicant:** Andrzej (Krunixbase)
**License:** MIT (FOSS)

---

## 1. Project overview

**SeedTools 2.0** is an **offline, open‑source toolkit** for:

- recovering Bitcoin HD wallets,
- analyzing corrupted or incomplete mnemonics,
- scanning derivation paths (including Taproot),
- verifying addresses and wallet structures,
- performing basic forensics on compromised setups.

It is built for **self‑custody users, activists, NGOs, and merchants** who need **deterministic, transparent, air‑gapped recovery workflows**.

SeedTools aims to become the **standard offline recovery and forensics toolkit** in the Bitcoin ecosystem.

---

## 2. Problem statement

Bitcoin self‑custody is powerful, but fragile in practice. Users lose access to funds because of:

- wrong or unknown derivation paths,
- corrupted or partially remembered mnemonics,
- missing or mis‑typed passphrases,
- incompatible wallet formats,
- misconfigured setups (e.g. multisig, custom paths),
- compromised or confiscated devices,
- lack of safe offline tools for recovery.

Today, the ecosystem has:

- fragmented tools,
- outdated or unmaintained projects,
- online services that require trust,
- very few options suitable for high‑risk users.

There is **no unified, offline‑first, well‑maintained toolkit** that provides deterministic recovery and forensic analysis in a way that is:

- auditable,
- reproducible,
- safe for activists and NGOs,
- friendly enough for support teams and educators.

SeedTools is designed to fill exactly this gap.

---

## 3. Proposed solution

SeedTools 2.0 provides a **modular toolkit** with:

- **Core deterministic engine**
  - BIP32/39/44/49/84/86
  - deep derivation path scanning (0 → X)
  - deterministic address generation and verification

- **Recovery Mode**
  - guided recovery workflows
  - passphrase handling
  - multi‑wallet compatibility (Sparrow, Electrum, Specter, BTCPay‑style setups)
  - address verification and balance checks (via user‑provided node / tools, never via third‑party APIs)

- **Forensics Mode**
  - corrupted mnemonic analysis
  - checksum and entropy validation
  - derivation path mismatch detection
  - basic forensic reports for support/NGO teams

- **Safe Mode for high‑risk users**
  - offline‑only workflows
  - optional no‑disk‑write mode
  - minimal logs, clear threat‑model documentation

- **CLI + GUI**
  - CLI for Tails/Qubes and advanced users
  - GUI for support teams, NGOs, educators

All of this is **offline‑first**, with **no telemetry, no analytics, no external API calls**.

---

## 4. Why this matters for Bitcoin

SeedTools strengthens **Bitcoin’s self‑custody layer** by:

- reducing permanent loss of funds,
- enabling safe recovery without trusted third parties,
- improving interoperability between wallets,
- giving NGOs and support teams a standard toolkit,
- making recovery workflows transparent and auditable,
- supporting high‑risk users in authoritarian environments.

From Spiral’s perspective, SeedTools:

- reinforces the **infrastructure of self‑custody**,
- supports **education and operational security**,
- provides a **public good** that any wallet, NGO, or project can rely on,
- is fully aligned with **open‑source, long‑term ecosystem building**.

---

## 5. Project goals (12–18 months)

### 5.1 Core technical goals

- stabilize and extend the deterministic engine,
- implement Recovery Mode PRO,
- implement Forensics Mode PRO,
- add full Taproot (BIP86) support,
- improve CLI for Tails/Qubes workflows,
- implement Safe Mode for high‑risk users,
- add reproducible builds and verification instructions.

### 5.2 Ecosystem & UX goals

- provide wallet‑specific presets (Sparrow, Specter, BTCPay‑style, common hardware wallet patterns),
- create high‑quality documentation and tutorials,
- prepare NGO‑oriented guides and training materials,
- design a clean, minimal, accessible GUI,
- publish demo packs and example workflows.

---

## 6. Deliverables

### Within 3 months

- deterministic engine v1 stabilized,
- Recovery Mode MVP (GUI + CLI),
- Forensics Mode MVP (basic mnemonic checks, path scanning),
- documentation v1 (architecture + basic guides),
- initial demo pack.

### Within 6 months

- Taproot (BIP86) support,
- Safe Mode for activists (offline‑only, minimal traces),
- improved GUI (onboarding, error handling),
- Windows installer (.exe) and packaging improvements,
- initial reproducible build pipeline.

### Within 12 months

- Forensics Mode PRO (advanced corruption analysis, partial mnemonic workflows, reports),
- wallet presets and compatibility docs (Sparrow, Specter, BTCPay‑style, common hardware wallets),
- NGO and support‑team training materials,
- multi‑language support (starting with EN/PL, then more where it makes sense),
- public security review and hardened build process.

### Within 18 months (stretch / long‑term)

- deeper integrations with wallet projects (where appropriate),
- extended forensic tooling (more datasets, more patterns),
- community‑driven presets and contributions,
- continuous maintenance and support.

---

## 7. Funding request

**Requested amount:**
**60 000–80 000 USD** (depending on Spiral’s preferred structure; can be split into milestones)

### High‑level breakdown (for 70 000 USD midpoint)

- **Core development:** 40 000
  - deterministic engine, Recovery Mode PRO, Forensics Mode PRO, Taproot, Safe Mode, CLI/GUI work

- **Security & reliability:** 10 000
  - external review, reproducible builds, hardened packaging

- **Documentation & education:** 10 000
  - NGO guides, wallet presets docs, tutorials, demo packs, multi‑language basics

- **Long‑term maintenance & community work:** 10 000
  - issue triage, contributions review, ongoing improvements, support for integrations

The exact structure (lump sum vs milestones) can be adapted to Spiral’s preferences.

---

## 8. How funds will be used

Funds will support:

- full‑time focus on SeedTools for a sustained period,
- implementation of the roadmap above,
- security review and reproducible builds,
- creation of high‑quality documentation and training materials,
- long‑term maintenance and responsiveness to ecosystem needs.

No funds will be used for:

- marketing,
- closed‑source components,
- token/altcoin integrations.

All work remains **FOSS under MIT**.

---

## 9. Current status

SeedTools is already in active development:

- deterministic engine prototype working,
- GUI and CLI prototypes,
- architecture and roadmap drafted,
- initial demo pack concept,
- repository structured under Krunixbase,
- MIT license in place.

The Spiral grant would move the project from **prototype → robust, widely usable toolkit**.

---

## 10. Links

- **GitHub:** `https://github.com/Krunixbase/seedtools`
- **Roadmap & docs:** stored in the repo (`/roadmap/`, `/product/`, `/financing/`)
- Additional materials (demo packs, examples) will be published in‑repo as they mature.

---

## 11. About the maintainer

**Andrzej** — independent developer and maintainer of SeedTools.
Background in:

- automation and backend integrations,
- API workflows and infrastructure,
- secure offline tooling,
- practical, product‑oriented engineering.

The goal is to treat SeedTools as a **long‑term public good** for the Bitcoin ecosystem, not a short‑lived side project.

---

## 12. Why Spiral

Spiral focuses on:

- long‑term open‑source infrastructure,
- tools that strengthen Bitcoin’s foundations,
- projects that are public goods,
- maintainers who can own a domain deeply.

SeedTools fits this vision:

- it is infrastructure for self‑custody and recovery,
- it is fully open‑source and offline‑first,
- it directly benefits wallets, NGOs, merchants, and users,
- it has a clear, long‑term roadmap and ownership.

---
