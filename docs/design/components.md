# 🧩 **SeedTools Component Library — Design Documentation**

SeedTools Suite provides a **deterministic, secure, minimalistic component library** used across all GUI modules.  
This document defines every component category, its rules, security constraints, and usage guidelines.

SeedTools components are designed for:

- air‑gapped systems  
- high‑risk users  
- forensics workflows  
- deterministic rendering  
- hardened mode environments  

---

## 1. 🎯 Component Philosophy

SeedTools components follow four core principles:

### ✔ Deterministic  
Same input → same rendering → same behavior.

### ✔ Secure  
No clipboard, no caching, no external assets, no hidden state.

### ✔ Minimalistic  
Only essential UI elements, no visual noise.

### ✔ Predictable  
Consistent layout, consistent actions, consistent feedback.

See also: **UI Principles** and **UX Guidelines**.

---

# 2. 🔐 Component Categories

SeedTools GUI components are grouped into:

1. **Secure Input Components**  
2. **Action Components (Buttons)**  
3. **Output Components**  
4. **Diagnostic Components**  
5. **Workflow Components**  
6. **Layout Components**

Each category has strict security and determinism rules.

---

# 3. 🛡 Secure Input Components

Secure input components handle sensitive data such as:

- mnemonics  
- entropy  
- seed hex  
- private keys  
- Shamir shares  

These components must follow the **Memory Model** and **Hardened Mode** rules.

---

## 3.1 MnemonicField

A masked, isolated input field for BIP39 mnemonics.

### Requirements:

- masked by default  
- no clipboard  
- no auto‑completion  
- zeroized on close  
- isolated buffer  
- deterministic validation  

### Example:

```
MnemonicField(masked=True)
```

---

## 3.2 EntropyField

Used for raw entropy input.

### Requirements:

- byte‑level validation  
- no auto‑formatting  
- no clipboard  
- zeroization after scoring  

---

## 3.3 SeedHexField

Used for BIP32 seed hex.

### Requirements:

- strict hex validation  
- no auto‑uppercase  
- no auto‑spacing  
- zeroization after derivation  

---

## 3.4 SecureNumberField

Used for:

- derivation paths  
- index values  
- Shamir parameters  

### Requirements:

- no scroll‑wheel increment  
- no auto‑correction  
- deterministic formatting  

---

# 4. ⚡ Action Components (Buttons)

Buttons must be:

- deterministic  
- consistent in size  
- consistent in placement  
- explicit (no auto‑processing)  

---

## 4.1 PrimaryButton

Used for critical actions:

- Validate  
- Generate  
- Derive  
- Scan  

### Requirements:

- no async behavior  
- no background tasks  
- no animations in hardened mode  

---

## 4.2 SecondaryButton

Used for non‑critical actions:

- Clear  
- Reset  
- Export (if allowed)  

---

## 4.3 DangerButton

Used for destructive actions:

- Clear All  
- Zeroize  
- Reset Workflow  

### Requirements:

- must require confirmation  
- must be visually distinct  

---

# 5. 📤 Output Components

Output components must **never** contain sensitive data unless explicitly required.

---

## 5.1 ReadOnlyOutput

Used for:

- addresses  
- xpubs  
- diagnostics  
- entropy scores  

### Requirements:

- read‑only  
- non‑copyable in hardened mode  
- deterministic formatting  

---

## 5.2 AddressList

Displays derived addresses.

### Requirements:

- fixed column width  
- deterministic ordering  
- no scrolling (pagination instead)  

---

## 5.3 DiagnosticBlock

Used for:

- entropy scoring  
- checksum validation  
- Shamir diagnostics  
- Taproot rules  

### Requirements:

- no sensitive data  
- deterministic messages  
- clear error states  

---

# 6. 🔍 Diagnostic Components

Diagnostic components must be:

- deterministic  
- non‑verbose  
- non‑leaking  
- safe for hardened mode  

---

## 6.1 EntropyScoreBlock

Displays entropy score and warnings.

### Requirements:

- no raw entropy displayed  
- no clipboard  
- deterministic scoring  

---

## 6.2 MnemonicCheckBlock

Displays:

- checksum validity  
- wordlist validation  
- formatting issues  

---

## 6.3 ShamirInspector

Displays:

- share validity  
- polynomial consistency  
- threshold rules  

### Requirements:

- never display reconstructed secret  

---

# 7. 🔄 Workflow Components

Workflow components orchestrate multi‑step processes.

---

## 7.1 WorkflowPanel

Used for:

- recovery workflows  
- forensics workflows  
- multi‑step derivations  

### Requirements:

- no hidden state  
- no auto‑progression  
- explicit “Next” and “Back”  

---

## 7.2 StepIndicator

Shows current step.

### Requirements:

- deterministic  
- no animations  
- no transitions  

---

# 8. 📐 Layout Components

Layout components ensure deterministic rendering.

---

## 8.1 ColumnLayout (3‑column standard)

```
+---------------------------------------------------------------+
|  [ INPUT ]   |   [ PROCESSING ]   |   [ OUTPUT ]              |
+---------------------------------------------------------------+
```

### Requirements:

- fixed width  
- no scrolling  
- no dynamic resizing  

---

## 8.2 Section

Used to group related components.

### Requirements:

- clear header  
- consistent spacing  
- no collapsible sections  

---

## 8.3 Divider

Used to separate logical blocks.

### Requirements:

- deterministic spacing  
- no animations  

---

# 9. 🛠 Developer Rules for Components

### ✔ Always:
- use secure components for sensitive data  
- isolate buffers  
- zeroize on close  
- avoid dynamic layout changes  
- avoid animations  
- avoid auto‑processing  

### ✘ Never:
- store sensitive data in UI state  
- use clipboard  
- rely on OS rendering  
- use unpredictable layout engines  
- auto‑trigger actions  

---

# 10. 📚 Related Documentation

- **UI Principles**  
- **UX Guidelines**  
- **Hardened Mode**  
- **Memory Model**  
- **Security Guide**  

---
