# SeedTools Suite — Demo

The `demo/` directory contains practical examples, real‑world scenarios, corrupted mnemonic samples, and case studies demonstrating how SeedTools Suite works in practice.

This folder is designed for:
- reviewers evaluating the project,
- developers exploring the toolkit,
- NGOs and support teams learning workflows,
- users testing recovery and forensics features.

---

## 📁 Folder Structure

```
demo/
├── scenarios/            # step‑by‑step usage scenarios
├── corrupted-mnemonics/  # real-world corrupted seed examples
├── case-studies/         # full analyses of real recovery cases
└── README.md             # this file
```

---

## 🧪 Scenarios (`scenarios/`)

This folder contains **guided, step‑by‑step scenarios** showing how to use SeedTools Suite in real situations.

Examples include:
- recovering a wallet from a partial mnemonic,
- detecting entropy drift,
- analyzing BIP32/44/49/84/86 derivation paths,
- performing wallet structure forensics,
- verifying addresses in batch mode.

Browse scenarios here:  
[`./scenarios/`](./scenarios/)

---

## ⚠️ Corrupted Mnemonics (`corrupted-mnemonics/`)

This folder contains **realistic corrupted seed examples**, including:
- missing words,
- swapped words,
- checksum failures,
- entropy drift,
- mixed wordlists,
- invalid language cases.

These samples are used for:
- testing,
- forensics,
- demonstrations,
- reproducible examples.

Browse corrupted mnemonics here:  
[`./corrupted-mnemonics/`](./corrupted-mnemonics/)

---

## 📚 Case Studies (`case-studies/`)

This folder contains **full, narrative-style analyses** of real recovery situations.

Each case study includes:
- the problem,
- the analysis steps,
- the tools used,
- the final outcome,
- lessons learned.

Examples include:
- lost 12‑word seed recovery,
- unknown derivation path analysis,
- damaged paper backup reconstruction,
- confiscated device recovery,
- mixed-wallet structure forensics.

Browse case studies here:  
[`./case-studies/`](./case-studies/)

---

## 🧰 How to Use the Demo

### 1. Try scenarios first  
They show how to use the tools step by step.

### 2. Test corrupted mnemonics  
Use them to validate recovery and forensics modules.

### 3. Study real cases  
Understand how SeedTools solves real‑world problems.

### 4. Use CLI or Desktop App  
Each scenario includes instructions for both interfaces.

---

## 🛠 Requirements

- SeedTools CLI or Desktop App  
- Offline environment recommended  
- No internet connection required  
- All examples are deterministic and reproducible  

---

## 📄 License

All demo materials are provided under the MIT License, unless stated otherwise.

---
