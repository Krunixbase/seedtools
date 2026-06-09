# 🔁 **Reproducible Builds — SeedTools Security Documentation**

Reproducible builds ensure that **anyone can verify** that the distributed SeedTools binaries were built from the exact same source code published in the repository.

This is essential for:

- high‑risk users  
- NGOs and field teams  
- forensics workflows  
- regulated environments  
- supply‑chain integrity  
- trust minimization  

This document explains how reproducible builds work in SeedTools Suite, how to verify them, and how developers must maintain determinism.

---

## 1. 🎯 Purpose of Reproducible Builds

Reproducible builds allow users to:

- verify that binaries match the source code  
- detect tampering or supply‑chain attacks  
- ensure deterministic behavior across platforms  
- trust the build process without trusting the builder  

SeedTools treats reproducibility as a **security requirement**, not a convenience feature.

---

## 2. 🔐 Reproducibility Guarantees

SeedTools guarantees:

- deterministic build steps  
- deterministic dependency resolution  
- deterministic file ordering  
- deterministic hashing  
- no timestamps in artifacts  
- no OS‑dependent behavior  
- no environment‑dependent output  

These guarantees apply to:

- CLI  
- GUI  
- Core  
- Utils  
- all tools and modules  

See also: **Memory Model** and **Hardened Mode**.

---

## 3. 🧱 Sources of Non‑Determinism (and how SeedTools avoids them)

### 3.1 Timestamps  
Forbidden in:

- build artifacts  
- logs  
- metadata  
- compiled files  

### 3.2 Randomness  
Only cryptographic entropy from Core is allowed.  
No OS randomness, no time‑based randomness.

### 3.3 File ordering  
All build steps must use:

- sorted file lists  
- deterministic directory traversal  

### 3.4 Environment variables  
Build must not depend on:

- locale  
- timezone  
- OS version  
- CPU architecture  
- Python minor version  

### 3.5 Floating‑point operations  
Forbidden — nondeterministic across platforms.

---

## 4. 🧪 Reproducible Build Process

SeedTools uses a deterministic build pipeline:

### Step 1 — Clean environment  
Use a minimal, isolated environment:

- Python virtualenv  
- no global packages  
- no system‑level overrides  

### Step 2 — Install dependencies deterministically  
Dependencies must be pinned:

```
package==version
```

No wildcard versions.

### Step 3 — Build artifacts  
Artifacts must be:

- byte‑for‑byte identical  
- free of timestamps  
- free of OS metadata  

### Step 4 — Hash artifacts  
Use deterministic hashing:

```
sha256sum seedtools-*.whl
sha256sum seedtools-*.tar.gz
```

### Step 5 — Verify reproducibility  
Two independent builds must produce identical hashes.

---

## 5. 🧬 Developer Requirements

All contributors must ensure:

### ✔ No nondeterministic code  
Avoid:

- random  
- time  
- OS‑dependent paths  
- concurrency  
- floating‑point math  

### ✔ No global state  
Global state breaks reproducibility.

### ✔ No environment‑dependent behavior  
Locale, timezone, or OS must not affect output.

### ✔ Deterministic formatting  
Formatting functions must produce identical output across platforms.

### ✔ Deterministic tests  
Tests must not rely on:

- timing  
- OS behavior  
- randomness  

---

## 6. 🛠 How to Verify a Reproducible Build

### 6.1 Build locally

```bash
python -m build
```

### 6.2 Hash the artifacts

```bash
sha256sum dist/*
```

### 6.3 Compare with published hashes  
Hashes must match the official release.

### 6.4 Optional: Build in a second environment  
For example:

- Linux  
- macOS  
- Windows  
- WSL2  
- Tails  
- Qubes  

Hashes must still match.

---

## 7. 🧱 Trust Boundary Alignment

Reproducible builds protect against:

- supply‑chain attacks  
- tampered binaries  
- compromised build servers  
- malicious maintainers  
- corrupted dependencies  

They **do not** protect against:

- compromised OS  
- hardware implants  
- BIOS/UEFI malware  
- physical access attacks  

See: **Security Guide**.

---

## 8. 📚 Related Documentation

- **Hardened Mode**  
- **Memory Model**  
- **Security Guide**  
- **Architecture Diagram**  
- **Data Flow Diagram**  

---

