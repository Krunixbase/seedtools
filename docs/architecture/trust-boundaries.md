# Trust Boundaries — SeedTools Suite

SeedTools Suite enforces strict trust boundaries between layers to minimize attack surface and ensure deterministic behavior.

---

## 1. Trust Levels Overview

### Architecture Mapping

UI:
- SeedTools CLI
- SeedTools Desktop
- SeedTools Launcher

Application Modules:
- Recovery Tool
- Mnemonic Tools
- Entropy Tools
- Path Explorer
- Scanner
- Forensics Engine

Core Layer:
- Crypto Core
- Entropy Engine
- Forensics Core
- Storage Engine
- Utils Layer

System Services:
- Logging
- Configuration Manager
- Dependency Resolver
- Reproducible Environment Manager

---

## 2. Boundary Definitions

### 2.1 UI → Controllers
- UI is untrusted
- Controllers validate all input
- No sensitive data stored in UI

### 2.2 Controllers → Application Modules
- Controllers enforce deterministic flow
- Modules cannot bypass controllers

### 2.3 Application Modules → Core Layer
- Modules cannot access cryptographic primitives directly
- Core Layer is isolated and trusted

### 2.4 Core Layer → System Services
- Only deterministic, validated operations
- No external dependencies

---

## 3. Security Guarantees

- No cross-layer memory sharing
- No implicit trust between modules
- All boundaries enforce validation
- Core Layer remains isolated

---

## 4. ASCII Diagram

```
[UI] → [Controllers] → [Application Modules] → [Core Layer] → [System Services]
```

---

## 5. Related Docs

- **Security Model**
- **Attack Surface**
- **System Architecture**

---
