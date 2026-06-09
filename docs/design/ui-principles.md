# 🎨 **SeedTools UI Principles — Design Documentation**

SeedTools Suite uses a **deterministic, secure, minimalistic UI philosophy** designed for high‑risk environments, air‑gapped systems, and forensics workflows.  
This document defines the core UI principles that all modules, tools, and GUI components must follow.

---

## 1. 🎯 UI Philosophy

SeedTools UI is built on five pillars:

### ✔ Minimalism  
No visual noise, no unnecessary elements, no distractions.

### ✔ Determinism  
UI must behave identically across platforms and sessions.

### ✔ Security‑first  
UI must prevent leaks, avoid unsafe patterns, and isolate sensitive data.

### ✔ Predictability  
Every action must be explicit, reversible, and clearly visible.

### ✔ Accessibility  
Clear contrast, readable typography, keyboard‑friendly workflows.

See also: **UX Guidelines**.

---

## 2. 🧱 Core UI Principles

### 2.1 No Scrolling  
All critical UI modules must fit on screen without scrolling:

- Seed Input  
- Address Generation  
- Audit / Forensics  
- Entropy Tools  

Scrolling hides state and increases risk of user mistakes.

### 2.2 Modular Layout  
Each module is a **self‑contained block**:

```
+------------------+ +------------------+ +------------------+
|   Seed Input     | | Address Gen      | |   Audit Tools    |
+------------------+ +------------------+ +------------------+
```

Modules never overlap responsibilities.

### 2.3 Explicit Actions  
Every action must be triggered by a clear button:

- “Validate”  
- “Generate”  
- “Scan”  
- “Derive”  

No implicit auto‑processing.

### 2.4 No Hidden State  
UI must never:

- auto‑save  
- auto‑cache  
- auto‑restore  
- auto‑fill  

State must always be visible and user‑controlled.

---

## 3. 🔐 Security‑Driven UI Rules

### 3.1 No Clipboard  
Clipboard is disabled to prevent:

- clipboard sniffers  
- malware injection  
- accidental seed exposure  

### 3.2 Masked Sensitive Fields  
Mnemonic, entropy, seed hex, and private keys must be masked by default.

### 3.3 Zeroization on Close  
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

## 4. 🧩 Component Principles

### 4.1 Secure Input Fields  
All sensitive inputs must:

- use isolated buffers  
- avoid OS‑level rendering caches  
- support zeroization  
- never store history  

### 4.2 Deterministic Buttons  
Buttons must:

- have consistent placement  
- have consistent size  
- trigger deterministic actions  
- never depend on async background tasks  

### 4.3 Read‑Only Output Blocks  
Outputs (addresses, xpubs, diagnostics) must be:

- read‑only  
- non‑selectable in hardened mode  
- non‑copyable  
- clearly separated from inputs  

### 4.4 Clear Error States  
Errors must be:

- deterministic  
- non‑verbose  
- non‑leaking  
- visually distinct  

Example:

```
[!] Invalid mnemonic checksum
```

---

## 5. 🧭 Layout Principles

### 5.1 Three‑Column Layout (SeedTools Standard)

```
+---------------------------------------------------------------+
|  [ SEED INPUT ]   |   [ ADDRESS GENERATION ]   |  [ AUDIT ]   |
+---------------------------------------------------------------+
```

Benefits:

- no scrolling  
- clear separation  
- predictable workflow  
- easy to scale modules  

### 5.2 Fixed Width  
UI must not reflow unpredictably.  
Fixed‑width columns ensure determinism.

### 5.3 High Contrast  
Colors must support:

- dark mode  
- high contrast  
- accessibility  

No gradients, no shadows.

---

## 6. 🧪 Deterministic Rendering Rules

UI must render identically across:

- Windows  
- macOS  
- Linux  
- WSL2  
- Tails  
- Qubes  

To ensure this:

- no system fonts  
- no system themes  
- no OS‑dependent widgets  
- no GPU‑dependent effects  

---

## 7. 🛠 Developer Guidelines

### ✔ Always:
- use secure components  
- isolate sensitive fields  
- zeroize buffers  
- avoid dynamic layout changes  
- avoid animations  
- avoid auto‑processing  

### ✘ Never:
- store sensitive data in UI state  
- use clipboard  
- use system dialogs for sensitive fields  
- rely on OS rendering  
- use unpredictable layout engines  

---

## 8. 📚 Related Documentation

- **UX Guidelines**  
- **Component Documentation**  
- **Hardened Mode**  
- **Memory Model**  
- **Security Guide**  

---
