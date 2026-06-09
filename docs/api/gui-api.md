# 🎛️ **SeedTools GUI API Documentation (Planned Interface)**

SeedTools currently does **not** include a GUI module.  
This document defines the **planned public API surface** for the upcoming `seedtools_gui` package, based on:

- the GUI Roadmap  
- UX & UI guidelines  
- Component Library specification  
- Hardened Mode requirements  
- deterministic rendering principles  

The GUI will provide a secure, deterministic, offline‑first graphical interface for all SeedTools workflows.

This API specification defines **what the GUI will expose once implemented**.

---

# 1. 🎯 GUI Vision

The SeedTools GUI will be:

- deterministic  
- minimalistic  
- security‑first  
- offline‑only  
- hardened‑mode compatible  
- predictable across platforms  
- safe for high‑risk users and forensics workflows  

The GUI will serve as a thin, deterministic layer on top of the Core module.

See: **UX Guidelines** and **UI Principles**.

---

# 2. 🧱 Planned Module Structure

The final structure will look like:

```
seedtools_gui/
 ├── components/      # secure UI components
 ├── workflow/        # deterministic workflow engine
 ├── secure/          # hardened-mode logic
 ├── themes/          # deterministic styling
 └── app.py           # main GUI entry point
```

But **this structure does not exist yet** — it is defined here for future implementation.

See: **GUI Roadmap**.

---

# 3. 🚀 GUI Entry Point (Planned)

## 3.1 `seedtools_gui.app.run()`
Starts the GUI application.

### Planned guarantees:
- deterministic startup  
- no network access  
- no external assets  
- hardened‑mode auto‑detection  
- zero clipboard usage  

---

# 4. 🧩 Component API (Planned)

The GUI will expose a deterministic component library.

Below is the planned public API surface.

---

## 4.1 Secure Input Components

### **MnemonicField**  
```
MnemonicField(masked: bool = True)
```

### **EntropyField**  
```
EntropyField()
```

### **SeedHexField**  
```
SeedHexField()
```

### **SecureNumberField**  
```
SecureNumberField(min: int, max: int)
```

All secure fields guarantee:

- masked sensitive data  
- no clipboard  
- no auto‑completion  
- zeroization on close  
- isolated memory buffers  

---

## 4.2 Action Components

### **PrimaryButton**  
```
PrimaryButton(label: str, on_click: Callable)
```

### **SecondaryButton**  
```
SecondaryButton(label: str, on_click: Callable)
```

### **DangerButton**  
```
DangerButton(label: str, on_click: Callable)
```

All buttons guarantee:

- deterministic behavior  
- no async tasks  
- no animations in hardened mode  

---

## 4.3 Output Components

### **ReadOnlyOutput**  
```
ReadOnlyOutput(value: str)
```

### **AddressList**  
```
AddressList(addresses: list[str])
```

### **DiagnosticBlock**  
```
DiagnosticBlock(messages: list[str])
```

Output components guarantee:

- deterministic formatting  
- no clipboard in hardened mode  
- no auto‑refresh  

---

# 5. 🔄 Workflow Engine API (Planned)

The GUI will include a deterministic workflow engine.

---

## 5.1 `WorkflowPanel`
```
WorkflowPanel(steps: list[WorkflowStep])
```

### Guarantees:
- no hidden state  
- no auto‑progression  
- deterministic transitions  

---

## 5.2 `WorkflowStep`
```
WorkflowStep(id: str, title: str, render: Callable)
```

---

## 5.3 `StepIndicator`
```
StepIndicator(current: int, total: int)
```

---

# 6. 🔐 Hardened Mode API (Planned)

The GUI will include a hardened‑mode subsystem.

---

## 6.1 `HardenedMode.enable()`
Enforces:

- no clipboard  
- no animations  
- no caching  
- no logs  
- no external dialogs  

---

## 6.2 `HardenedMode.is_enabled() -> bool`
Returns hardened‑mode status.

---

## 6.3 `HardenedMode.wrap(component)`
Wraps a component with hardened‑mode restrictions.

---

# 7. 🎨 Theme & Layout API (Planned)

## 7.1 `Theme.load(name: str)`
Loads a deterministic theme.

---

## 7.2 `ColumnLayout`
```
ColumnLayout(left, center, right)
```

Guarantees:

- fixed width  
- no scrolling  
- deterministic spacing  

---

## 7.3 `Section`
```
Section(title: str, content: Component)
```

---

# 8. 🛡 Security Guarantees

The GUI will guarantee:

### ✔ Deterministic rendering  
No dynamic layout changes.

### ✔ No external assets  
No fonts, images, scripts, CDNs.

### ✔ Zeroization  
All sensitive fields are wiped on:

- close  
- module switch  
- workflow reset  

### ✔ Hardened‑mode compatibility  
No clipboard, no animations, no logs.

### ✔ Offline‑only  
No networking, no telemetry.

See: **Security Guide**.

---

# 9. 🧪 Testing (Planned)

The GUI test suite will include:

- deterministic rendering tests  
- hardened‑mode tests  
- zeroization tests  
- cross‑platform layout tests  

---

# 10. 📚 Related Documentation

- **GUI Roadmap**  
- **UX Guidelines**  
- **UI Principles**  
- **Component Documentation**  
- **Core API**  
- **Utils API**  

---
