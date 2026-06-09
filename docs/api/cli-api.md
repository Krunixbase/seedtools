# 🖥️ **SeedTools CLI API Documentation (Planned Interface)**

SeedTools currently does **not** include a standalone CLI module.  
This document defines the **planned public API surface** for the upcoming `seedtools_cli` package, based on:

- the Core module capabilities  
- the CLI Roadmap  
- deterministic and hardened‑mode design principles  

The CLI will provide a secure, deterministic command‑line interface for:

- mnemonic validation  
- entropy tools  
- Bitcoin key derivation  
- Ethereum key derivation  
- address generation  
- forensics workflows (future)  

This API specification defines **what the CLI will expose**, once implemented.

---

# 1. 🎯 CLI Vision

The SeedTools CLI will be:

- deterministic  
- offline‑first  
- hardened‑mode compatible  
- safe for air‑gapped and forensics environments  
- script‑friendly  
- reproducible across platforms  

The CLI will serve as a thin, deterministic wrapper around the Core module.

---

# 2. 🚀 Planned CLI Entry Point

The CLI will be installed as:

```
seedtools
```

or via Python:

```
python -m seedtools
```

All commands will follow the structure:

```
seedtools <command> [options]
```

---

# 3. 🧠 Mnemonic Commands (Planned)

### **mnemonic validate**  
Validates a BIP39 mnemonic.

```
seedtools mnemonic validate "<mnemonic>"
```

---

### **mnemonic normalize**  
Normalizes a mnemonic to deterministic format.

```
seedtools mnemonic normalize "<mnemonic>"
```

---

### **mnemonic to-entropy**  
Converts mnemonic → entropy.

```
seedtools mnemonic to-entropy "<mnemonic>"
```

---

### **mnemonic from-entropy**  
Converts entropy → mnemonic.

```
seedtools mnemonic from-entropy "<hex_entropy>"
```

---

# 4. 🔑 Seed & Key Derivation Commands (Planned)

### **seed derive**  
Derives a BIP32 seed from a mnemonic.

```
seedtools seed derive "<mnemonic>" --passphrase "<optional>"
```

---

### **bip32 derive**  
Derives a key using a BIP32 path.

```
seedtools bip32 derive "<seed_hex>" --path "m/84'/0'/0'/0/0"
```

---

### **bip44 address**  
Derives a BIP44 address.

```
seedtools bip44 address "<seed_hex>" --index 0 --change 0
```

---

# 5. 🏦 Bitcoin Address Commands (Planned)

### **address p2pkh**  
```
seedtools address p2pkh "<pubkey_hex>"
```

---

### **address p2wpkh**  
```
seedtools address p2wpkh "<pubkey_hex>"
```

---

### **address p2sh-p2wpkh**  
```
seedtools address p2sh-p2wpkh "<pubkey_hex>"
```

---

### **address p2tr**  
```
seedtools address p2tr "<pubkey_hex>"
```

---

# 6. 🦊 Ethereum Commands (Planned)

### **eth derive**  
```
seedtools eth derive "<seed_hex>" --path "m/44'/60'/0'/0/0"
```

---

### **eth address**  
```
seedtools eth address "<privkey_hex>"
```

---

### **eth from-seed**  
One‑shot derivation:

```
seed → private key → address
```

---

# 7. 🔍 Entropy Tools (Planned)

### **entropy score**  
```
seedtools entropy score "<hex_entropy>"
```

---

### **entropy validate**  
```
seedtools entropy validate "<hex_entropy>"
```

---

# 8. 🧪 Forensics Commands (Future)

These commands are defined in the roadmap and will be implemented later:

- **mnemonic recover**  
- **entropy detect-drift**  
- **seed infer**  
- **shamir validate**  

See: **CLI Roadmap**.

---

# 9. 📤 Output Format (Planned)

CLI output will be:

- deterministic  
- plain text  
- stable across platforms  
- hardened‑mode safe  
- without ANSI colors (in hardened mode)  
- without logs  
- without clipboard usage  

---

# 10. 🛡 Security Guarantees

The CLI will guarantee:

- deterministic execution  
- no randomness  
- no networking  
- no disk writes  
- zeroization of sensitive buffers  
- hardened‑mode compatibility  
- reproducible output  

See: **Hardened Mode**.

---

# 11. 🧪 Testing (Planned)

The CLI test suite will include:

- deterministic command tests  
- hardened‑mode tests  
- reproducibility tests  
- cross‑platform tests  

---

# 12. 📚 Related Documentation

- **Core API**  
- **Utils API**  
- **GUI API**  
- **CLI Roadmap**  
- **Security Guide**  

---

- **docs/api/index.md** (API table of contents)

Daj tylko sygnał.
