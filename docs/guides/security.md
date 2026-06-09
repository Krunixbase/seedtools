# 🛡️ **SeedTools Suite — Security Guide**

SeedTools Suite is designed for **offline‑first**, **deterministic**, and **high‑security environments**.  
This guide explains how SeedTools protects users, what guarantees it provides, what limitations exist, and how to operate it safely.

This document complements the root‑level **SECURITY.md** file and expands it into a full security guide.

---

# 1. 🔐 Security Guarantees

SeedTools provides strong, verifiable guarantees:

- **No networking** — no API calls, no telemetry, no cloud  
- **No seed storage** — mnemonics, entropy, and keys never touch disk  
- **Deterministic execution** — same input → same output  
- **Offline‑first architecture** — safe for air‑gapped workflows  
- **No clipboard usage** — prevents clipboard hijacking  
- **Zero‑trust design** — OS, hardware, and environment are not trusted  
- **Memory zeroization** — sensitive data cleared where possible  
- **No offensive capabilities** — cannot brute‑force or attack wallets  

For module‑level details, see **Module Documentation**.

---

# 2. ⚠️ Security Limitations

SeedTools cannot protect against:

- compromised operating systems  
- hardware keyloggers  
- malicious firmware  
- BIOS/UEFI implants  
- physical access attacks  
- supply‑chain tampering  

These threats require user‑side operational security.

See also: **Security FAQ**.

---

# 3. 🧱 Trust Boundaries

SeedTools defines strict trust boundaries:

```
+---------------------------+
|  Trusted Zone (Core)      |
|  - BIP32/39/44/86         |
|  - entropy tools          |
|  - address generation     |
+-------------+-------------+
              |
              v
+---------------------------+
|  Semi‑Trusted Zone        |
|  - Utils                  |
|  - CLI Engine             |
|  - GUI Secure Components  |
+-------------+-------------+
              |
              v
+---------------------------+
|  Untrusted Input Zone     |
|  - user mnemonics         |
|  - entropy files          |
|  - disk images (forensics)|
+---------------------------+
```

Rules:

- Core never accepts unvalidated input  
- Utils sanitizes all external data  
- GUI isolates sensitive fields  
- CLI never logs sensitive data  

See also: **Architecture Diagram**.

---

# 4. 🧠 Memory Security Model

SeedTools uses a strict memory model:

### ✔ Ephemeral memory  
Sensitive data is stored only in temporary buffers.

### ✔ Zeroization  
Buffers are wiped immediately after use.

### ✔ No disk writes  
Sensitive data never persists unless explicitly exported.

### ✔ No caching  
No OS‑level or application‑level caching.

### ✔ No logs  
Sensitive operations produce **no logs**.

### ✔ No shell history (CLI)  
Hardened mode disables shell history entirely.

See: **Memory Model Docs**.

---

# 5. 🧱 Hardened Mode

Hardened Mode is designed for:

- Tails  
- Qubes  
- air‑gapped laptops  
- NGO field operations  
- hostile environments  

### Hardened Mode disables:

- disk writes  
- caching  
- logs  
- animations (GUI)  
- shell history (CLI)  
- clipboard access (optional)  

### Hardened Mode enforces:

- deterministic execution  
- ephemeral buffers  
- zero‑trace rendering  
- strict input validation  

See: **Hardened Mode Docs**.

---

# 6. 🔐 Cryptographic Scope

SeedTools implements:

- BIP32  
- BIP39  
- BIP44 / BIP49 / BIP84 / BIP86  
- SLIP‑44  
- SLIP‑39 (Shamir Secret Sharing)  
- Taproot (BIP86)  

Cryptographic correctness is validated through:

- deterministic test vectors  
- entropy scoring  
- polynomial validation  
- hardened path enforcement  

See: **Core API**.

---

# 7. 🧪 Deterministic Execution

SeedTools guarantees:

- no time‑based randomness  
- no OS‑dependent behavior  
- no floating‑point nondeterminism  
- no external entropy sources  
- no race conditions  

This is essential for:

- audits  
- reproducible builds  
- forensics  
- recovery workflows  

See: **Reproducible Builds Docs**.

---

# 8. 🛠 Operational Security Recommendations

### ✔ Use SeedTools on a trusted device  
Avoid infected systems, shared computers, cloud desktops.

### ✔ Prefer offline / air‑gapped environments  
SeedTools is designed for cold wallets and forensics.

### ✔ Verify downloads  
Always check signatures and checksums.

### ✔ Never store seeds digitally  
Avoid screenshots, cloud backups, password managers.

### ✔ Use strong entropy  
Weak seeds reduce security regardless of the tool.

---

# 9. 🧬 Residual Risks

Even with SeedTools, the following risks remain:

- OS‑level compromise  
- hardware implants  
- malicious BIOS/UEFI  
- physical theft  
- user mistakes  
- weak entropy  

These are outside the scope of any offline cryptographic tool.

---

# 10. 📫 Reporting a Vulnerability

Do **not** open a public GitHub issue.

Report privately to:

```
krunixbase@gmail.com
```

Include:

- description  
- reproduction steps  
- affected version  
- potential impact  

Response target: **72 hours**.

---

# 11. 📚 Related Documentation

- **Onboarding Guide**  
- **Contributor Guide**  
- **Module Documentation**  
- **Data Flow Diagram**  

---
