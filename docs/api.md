# 📘 **SeedTools Suite — API Documentation**

This API documentation describes the **public interfaces**, **data structures**, and **deterministic workflows** exposed by the SeedTools Suite modules:

- **Core API**  
- **Utils API**  
- **CLI API**  
- **GUI API**  

All APIs are:

- **offline‑safe**  
- **deterministic**  
- **cryptographically correct**  
- **auditable**  
- **modular**  

---

# 🔐 **1. SeedTools Core — API**

SeedTools Core exposes deterministic cryptographic primitives.

---

## **1.1 Mnemonic API**

### **`mnemonic_to_entropy(mnemonic: str) -> bytes`**

Converts a BIP39 mnemonic to raw entropy.

**Returns:**

- entropy bytes  
- raises deterministic validation errors  

### **`entropy_to_mnemonic(entropy: bytes) -> str`**

Converts entropy to a valid BIP39 mnemonic.

### **`validate_mnemonic(mnemonic: str) -> ValidationResult`**

Checks:

- wordlist conformity  
- checksum correctness  
- word count  

---

## **1.2 BIP32 Derivation API**

### **`derive_xprv(seed: bytes, path: str) -> XPrv`**

Derives an extended private key.

### **`derive_xpub(xprv: XPrv) -> XPub`**

Returns the corresponding extended public key.

### **`derive_child(key: XKey, index: int, hardened: bool) -> XKey`**

Deterministic child derivation.

---

## **1.3 Path API**

### **`parse_path(path: str) -> Path`**

Validates:

- hardened markers  
- segment ranges  
- BIP44/49/84/86 conformity  

### **`validate_path(path: str) -> PathValidationResult`**

Returns structured metadata.

---

## **1.4 Address API**

### **`encode_p2pkh(pubkey: bytes) -> str`**  
### **`encode_p2wpkh(pubkey: bytes) -> str`**  
### **`encode_p2sh_p2wpkh(pubkey: bytes) -> str`**  
### **`encode_p2tr(pubkey: bytes) -> str`**

Deterministic address generation.

---

## **1.5 Entropy & Checksum API**

### **`entropy_checksum(entropy: bytes) -> int`**

Returns checksum bits.

### **`detect_entropy_drift(entropy: bytes) -> DriftReport`**

Detects bit‑level corruption.

---

# 🧰 **2. SeedTools Utils — API**

Utils provides shared helpers for all modules.

---

## **2.1 Validation API**

### **`validate_entropy(entropy: bytes) -> bool`**  
### **`validate_path_syntax(path: str) -> bool`**  
### **`validate_address(address: str) -> bool`**

---

## **2.2 Encoding API**

### **`base58_encode(data: bytes) -> str`**  
### **`base58_decode(text: str) -> bytes`**  
### **`bech32_encode(hrp: str, data: bytes) -> str`**  
### **`hex_to_bytes(hexstr: str) -> bytes`**

---

## **2.3 Crypto Helpers API**

### **`sha256(data: bytes) -> bytes`**  
### **`hmac_sha512(key: bytes, data: bytes) -> bytes`**  
### **`secure_random(n: int) -> bytes`**

---

## **2.4 Secure Memory API**

### **`zeroize(buffer: bytearray)`**

Overwrites memory in place.

### **`ephemeral_buffer(size: int)`**

Context manager for temporary secure buffers.

---

## **2.5 Formatting API**

### **`format_json(data: dict) -> str`**  
### **`format_table(rows: list) -> str`**

---

# 🖥‍💻 **3. SeedTools CLI Module — API**

This is the **internal engine** behind the CLI.

---

## **3.1 Command Router API**

### **`register_command(name: str, handler: Callable)`**  
### **`dispatch(argv: list[str]) -> int`**

Deterministic argument parsing.

---

## **3.2 CLI Engines**

### **Mnemonic Engine**
- `cli_mnemonic_validate(mnemonic: str)`  
- `cli_mnemonic_entropy(mnemonic: str)`  

### **Entropy Inspector**
- `cli_entropy_analyze(file: Path)`  

### **Recovery Engine**
- `cli_recover(mnemonic: str, bip: str, index_range: tuple)`  

### **Address Scanner**
- `cli_scan_address(address: str)`  

### **Path Explorer**
- `cli_path_validate(path: str)`  
- `cli_path_derive(seed: bytes, path: str)`  

---

## **3.3 Output API**

### **`print_human(data: dict)`**  
### **`print_json(data: dict)`** *(future)*

---

# 🖥 **4. SeedTools GUI — API**

GUI exposes reusable UI components and secure widgets.

---

## **4.1 Component API**

### **`Button(label: str, on_click: Callable)`**  
### **`InputField(masked: bool = False)`**  
### **`Dialog(title: str, content: Component)`**

---

## **4.2 Secure Components API**

### **`MnemonicField(masked: bool = True)`**  
### **`EntropyViewer(entropy: bytes)`**  
### **`PassphraseField()`**

All secure components use:

- isolated buffers  
- zeroization  
- deterministic rendering  

---

## **4.3 Workflow Engine API**

### **`Workflow(steps: list[WorkflowStep])`**  
### **`WorkflowStep(id: str, handler: Callable)`**

---

## **4.4 Preset‑Aware UI API**

### **`apply_preset(preset: Preset)`**  
### **`load_wallet_preset(name: str)`**

---

# 📡 **5. Cross‑Module Data Models**

### **MnemonicResult**  
### **EntropyReport**  
### **PathValidationResult**  
### **DriftReport**  
### **AddressInfo**  
### **CLIExecutionContext**  

---
