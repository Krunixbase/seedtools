# 🧰 **SeedTools Utils API Documentation**

SeedTools does **not** currently include a standalone `utils/` directory.  
Instead, utility functions are implemented **inside the core modules**:

- `bip32.py`  
- `bip39.py`  
- `bip44.py`  
- `crypto_core.py`  
- `eth_core.py`  
- `taproot.py`  

These utilities provide deterministic helper functions for:

- validation  
- formatting  
- encoding  
- hashing  
- zeroization  
- byte‑level operations  

They are **pure, deterministic, side‑effect‑free**, and fully compatible with Hardened Mode and the Memory Model.

---

## 1. 📦 Scope of Utility Functions

Utility functions appear across the Core and support:

- BIP32 derivation  
- BIP39 mnemonic processing  
- BIP44 account derivation  
- Bitcoin address generation  
- Ethereum address generation  
- Taproot key‑path derivation  

Functional areas:

- validation  
- formatting  
- encoding  
- hashing  
- memory safety  

---

## 2. 🧪 Validation API

### **validate_hex**  
`validate_hex(value: str) -> None`

Checks:

- valid hex characters  
- even length  
- no invalid prefixes  

Raises: `InvalidHexError`

---

### **validate_mnemonic_words**  
`validate_mnemonic_words(words: list[str]) -> None`

Checks:

- wordlist membership  
- valid mnemonic length  

---

### **validate_bip32_path**  
`validate_bip32_path(path: str) -> None`

Checks:

- correct format  
- hardened/not hardened markers  
- index ranges  

---

### **validate_entropy**  
`validate_entropy(entropy: bytes) -> None`

Checks:

- length (128–256 bits)  
- structure  
- repetition patterns  

---

## 3. 🧹 Formatting API

### **normalize_hex**  
`normalize_hex(value: str) -> str`

Returns:

- lowercase  
- no spaces  
- no `0x` prefix  

---

### **normalize_mnemonic**  
`normalize_mnemonic(mnemonic: str) -> str`

Returns:

- single‑space separation  
- lowercase  
- no special characters  

---

### **normalize_path**  
`normalize_path(path: str) -> str`

Returns:

- deterministic BIP32 path format  
- no redundant separators  

---

## 4. 🔐 Encoding API

### **hex_to_bytes**  
`hex_to_bytes(value: str) -> bytes`

---

### **bytes_to_hex**  
`bytes_to_hex(data: bytes) -> str`

---

### **base58_encode**  
`base58_encode(data: bytes) -> str`

---

### **base58_decode**  
`base58_decode(value: str) -> bytes`

---

### **bech32_encode**  
`bech32_encode(hrp: str, data: bytes) -> str`

Used for:

- P2WPKH  
- P2TR  

---

## 5. 🔒 Hashing API

### **sha256**  
`sha256(data: bytes) -> bytes`

---

### **ripemd160**  
`ripemd160(data: bytes) -> bytes`

---

### **hash160**  
`hash160(data: bytes) -> bytes`

---

### **hmac_sha512**  
`hmac_sha512(key: bytes, data: bytes) -> bytes`

---

### **keccak256**  
`keccak256(data: bytes) -> bytes`

Used in Ethereum.

---

## 6. 🧼 Memory & Security API

### **zeroize**  
`zeroize(buffer: bytearray) -> None`

Securely overwrites a buffer with zeros.

---

### **secure_compare**  
`secure_compare(a: bytes, b: bytes) -> bool`

Constant‑time comparison.

---

### **secure_clear_list**  
`secure_clear_list(values: list) -> None`

Clears list contents in place.

---

## 7. 🧩 Utility Helpers

### **int_to_bytes**  
`int_to_bytes(value: int, length: int) -> bytes`

---

### **bytes_to_int**  
`bytes_to_int(data: bytes) -> int`

---

### **ensure_bytes**  
`ensure_bytes(value: Any) -> bytes`

Converts:

- str → bytes  
- bytearray → bytes  
- int → bytes  

---

## 8. 🛡 Security Guarantees

Utils guarantee:

- **deterministic behavior**  
- **zeroization of sensitive buffers**  
- **Hardened Mode compatibility**  
- **no side effects**  
- **no disk writes**  
- **no OS‑dependent behavior**  

See: **Hardened Mode**.

---

## 9. 🧪 Testing

Utils include:

- deterministic test vectors  
- compatibility tests  
- security tests  
- zeroization tests  

Run:

```
pytest -q
```

---

## 10. 📚 Related Documentation

- **Core API**  
- **CLI API**  
- **GUI API**  
- **Security Guide**  
- **Memory Model**  

---
