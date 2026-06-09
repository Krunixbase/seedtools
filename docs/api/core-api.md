# 🔐 **SeedTools Core API Documentation**

`src/core/` contains the deterministic cryptographic engine powering SeedTools Suite.  
It implements BIP standards, entropy tools, Bitcoin & Ethereum derivation, and deterministic workflows.

This document describes the **public API surface** of the real Core module.

---

# 1. 📦 Module Structure (Actual)

```
src/core/
 ├── bip32.py          # BIP32 derivation engine
 ├── bip39.py          # mnemonic ↔ entropy engine
 ├── bip44.py          # BIP44 account derivation
 ├── crypto_core.py    # shared crypto primitives
 ├── eth_core.py       # Ethereum derivation engine
 └── taproot.py        # Taproot key-path derivation
```

See also:

- **Core Roadmap**  
- **Security Guide**  
- **Memory Model**  

---

# 2. 🧠 `bip39.py` — Mnemonic ↔ Entropy API

## 2.1 `BIP39.mnemonic_to_entropy(mnemonic: str) -> bytes`
Converts a BIP39 mnemonic to raw entropy.

### Guarantees:
- deterministic  
- checksum‑validated  
- zeroized intermediate buffers  

---

## 2.2 `BIP39.entropy_to_mnemonic(entropy: bytes) -> str`
Converts raw entropy to a mnemonic.

---

## 2.3 `BIP39.normalize(mnemonic: str) -> str`
Normalizes whitespace, casing, formatting.

---

## 2.4 `BIP39.validate(mnemonic: str) -> None`
Validates:

- wordlist  
- length  
- checksum  

---

# 3. 🔑 `bip32.py` — BIP32 Derivation API

## 3.1 `BIP32.from_seed(seed: bytes)`
Creates a BIP32 master node.

---

## 3.2 `BIP32.derive(path: str) -> BIP32`
Derives a child key using a BIP32 path.

### Features:
- hardened path support  
- deterministic derivation  
- zeroized intermediate keys  

---

## 3.3 `BIP32.xprv() -> str`
Returns extended private key.

---

## 3.4 `BIP32.xpub() -> str`
Returns extended public key.

---

## 3.5 `BIP32.private_key() -> bytes`
Returns raw private key.

---

## 3.6 `BIP32.public_key() -> bytes`
Returns raw public key.

---

# 4. 🧭 `bip44.py` — BIP44 Account Derivation API

## 4.1 `BIP44.from_seed(seed: bytes, coin_type: int)`
Creates a BIP44 root for a specific coin.

---

## 4.2 `BIP44.account(account_index: int)`
Derives account‑level node.

---

## 4.3 `BIP44.address(index: int, change: int = 0)`
Derives address‑level private key.

---

# 5. 🏦 `crypto_core.py` — Shared Crypto Primitives

## 5.1 `CryptoCore.sha256(data: bytes) -> bytes`
Deterministic SHA‑256.

---

## 5.2 `CryptoCore.hmac_sha512(key: bytes, data: bytes) -> bytes`
Used in BIP32.

---

## 5.3 `CryptoCore.ripemd160(data: bytes) -> bytes`
Used in P2PKH.

---

## 5.4 `CryptoCore.keccak256(data: bytes) -> bytes`
Used in Ethereum address generation.

---

# 6. 🦊 `eth_core.py` — Ethereum Derivation API

## 6.1 `ETHCore.from_seed(seed: bytes)`
Creates Ethereum root from BIP32 seed.

---

## 6.2 `ETHCore.derive_private_key(path: str) -> bytes`
Derives ETH private key.

---

## 6.3 `ETHCore.private_key_to_address(privkey: bytes) -> str`
Generates Ethereum address:

- Keccak‑256  
- last 20 bytes  
- EIP‑55 checksum  

---

## 6.4 `ETHCore.derive_address(path: str) -> str`
One‑shot derivation:

```
seed → privkey → address
```

---

# 7. 🌲 `taproot.py` — Taproot (BIP86) API

## 7.1 `TaprootEngine.from_seed(seed: bytes)`
Creates Taproot master node.

---

## 7.2 `TaprootEngine.derive_key(path: str) -> bytes`
Derives Taproot private key.

---

## 7.3 `TaprootEngine.to_taproot_address(pubkey: bytes) -> str`
Generates P2TR address.

---

## 7.4 `TaprootEngine.tweak_key(privkey: bytes) -> bytes`
Applies BIP86 tweak.

---

# 8. 🛡 Security Guarantees

All Core API functions guarantee:

### ✔ Deterministic execution  
No randomness, no OS‑dependent behavior.

### ✔ No networking  
No HTTP, DNS, telemetry.

### ✔ No disk writes  
Seeds, entropy, mnemonics never touch disk.

### ✔ Zeroization  
Sensitive buffers are wiped after use.

### ✔ Hardened‑mode compatibility  
No clipboard, no logs, no temp files.

See: **Hardened Mode**.

---

# 9. 🧪 Testing & Validation

Core API includes:

- deterministic test vectors  
- cross‑wallet compatibility tests  
- Taproot test vectors  
- Ethereum derivation tests  

Run tests:

```
pytest -q
```

---

# 10. 📚 Related Documentation

- **Core Roadmap**  
- **Utils API**  
- **CLI API**  
- **Security Guide**  
- **Memory Model**  

---
