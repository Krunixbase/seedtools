# 🎛️ **SeedTools UX Guidelines — Design Documentation**

SeedTools Suite uses a **deterministic, minimalistic, security‑first UX model** designed for high‑risk environments, air‑gapped systems, and forensics workflows.  
This document defines the UX rules that ensure consistency, safety, predictability, and clarity across all SeedTools modules.

---

## 1. 🎯 UX Philosophy

SeedTools UX is built on four core principles:

### ✔ Predictability  
Every action must behave the same way every time.

### ✔ Clarity  
No hidden state, no ambiguous actions, no visual noise.

### ✔ Security  
UX must prevent leaks, reduce attack surface, and guide users safely.

### ✔ Determinism  
UX must behave identically across platforms and sessions.

See also: **UI Principles**.

---

## 2. 🧱 Core UX Rules

### 2.1 No Auto‑Processing  
SeedTools never processes data automatically.  
Users must explicitly trigger actions such as:

- “Validate”  
- “Generate”  
- “Scan”  
- “Derive”  

This prevents accidental leaks and unintended operations.

---

### 2.2 No Hidden State  
SeedTools must never:

- auto‑save  
- auto‑restore  
- auto‑cache  
- auto‑fill  
- remember previous inputs  

All state must be visible and user‑controlled.

---

### 2.3 No Scrolling in Critical Workflows  
Critical workflows must fit on screen:

- seed input  
- entropy tools  
- address generation  
- forensics scans  

Scrolling hides state and increases risk of user mistakes.

---

### 2.4 Clear Separation of Responsibilities  
Each module must be self‑contained:

```
[ Input ] → [ Processing ] → [ Output ]
```

No module should mix responsibilities.

---

## 3. 🔐 Security‑Driven UX Rules

### 3.1 No Clipboard  
Clipboard is disabled to prevent:

- clipboard sniffers  
- malware injection  
- accidental seed exposure  

### 3.2 Masked Sensitive Fields  
Mnemonic, entropy, seed hex, and private keys must be masked by default.

### 3.3 Zeroization on Exit  
All sensitive fields must be cleared when:

- switching modules  
- closing dialogs  
- exiting the app  

### 3.4 No External Assets  
Forbidden:

- remote fonts  
- remote images  
- remote scripts  
- CDN resources  

### 3.5 No Animations in Hardened Mode  
Animations create timing noise and side‑channel risk.

See: **Hardened Mode**.

---

## 4. 🧩 Interaction Model

### 4.1 Explicit, Confirmed Actions  
Every critical action must require:

- a clear button  
- a clear label  
- no hidden triggers  

### 4.2 Deterministic Feedback  
Feedback must be:

- immediate  
- consistent  
- non‑verbose  
- non‑leaking  

Example:

```
[!] Invalid mnemonic checksum
```

### 4.3 No Background Tasks  
Background tasks introduce nondeterminism.  
All operations must be synchronous unless explicitly justified.

---

## 5. 🧭 Layout & Navigation

### 5.1 Three‑Column Layout (SeedTools Standard)

```
+---------------------------------------------------------------+
|  [ SEED INPUT ]   |   [ ADDRESS GENERATION ]   |  [ AUDIT ]   |
+---------------------------------------------------------------+
```

Benefits:

- no scrolling  
- predictable workflow  
- clear separation  
- deterministic rendering  

---

### 5.2 Fixed Layout  
UI must not reflow unpredictably.  
Fixed‑width columns ensure determinism.

---

### 5.3 High Contrast  
Colors must support:

- dark mode  
- high contrast  
- accessibility  

No gradients, no shadows, no transparency.

---

## 6. 🧪 Error Handling & Validation

### 6.1 Deterministic Errors  
Errors must:

- be consistent  
- never leak sensitive data  
- never include stack traces  
- never include OS‑level messages  

### 6.2 Inline Validation  
Validation must occur:

- only when triggered  
- only on explicit user action  
- never automatically  

### 6.3 Clear Error Zones  
Errors must be visually separated from:

- input fields  
- output fields  
- action buttons  

---

## 7. 🛠 Developer UX Guidelines

### ✔ Always:
- use explicit actions  
- isolate sensitive fields  
- avoid auto‑processing  
- avoid dynamic layout changes  
- avoid animations  
- avoid hidden state  

### ✘ Never:
- store sensitive data in UI state  
- use clipboard  
- rely on OS rendering  
- use unpredictable layout engines  
- auto‑trigger actions  

---

## 8. 🧬 UX in Hardened Mode

Hardened Mode enforces:

- no animations  
- no clipboard  
- no caching  
- no logs  
- no background tasks  
- zero‑trace rendering  

UX must adapt automatically without changing layout or behavior.

See: **Memory Model**.

---

## 9. 📚 Related Documentation

- **UI Principles**  
- **Component Documentation**  
- **Hardened Mode**  
- **Security Guide**  
- **Architecture Diagram**  

---
