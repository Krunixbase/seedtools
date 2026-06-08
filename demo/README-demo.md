> 📎 **Related:**  
> For advanced test cases (high indexes, Taproot, extreme scans), see  
> **[Extra Demo — Advanced Test Cases](README-seedtools-extra-demo.md)**.

# **SeedTools 2.0 — Demo Pack**
Real-world testing of the SeedTools 2.0 application.
Screenshots show address generation, verification, BIP path scanning, and address validation.

--

## **1. Demo 1 — Seed → Seed Hex → BTC/ETH Addresses**
File: `seedtools-demo-01.png`

Shows:

- mnemonic entry
- conversion to seed_hex
- **Seed OK** status
- address generation:
- BTC BIP44
- BTC BIP49
- BTC BIP84
- BTC BIP86
- ETH BIP44
- Index = 0
- full deterministic address set

**Conclusion:**
SeedTools generates valid addresses for all major BIP standards.

---

## **2. Demo 2 — ETH BIP44 Address Verification**
File: `seedtools-demo-02.png`

Shows:

- generated ETH address
- pasting it into the Verify section
- result: **Match: True, Info: seed_hex:ETH_BIP44**

**Conclusion:**
SeedTools can associate an ETH address with a specific seed and standard.

--

## **3. Demo 3 — BTC BIP86, Index 0**
File: `seedtools-demo-03.png`

Shows:

- Taproot address generation (BIP86)
- Verify → **Match: True**
- Validate Address → **Valid: True**

**Conclusion:**
Taproot support is working correctly.

---

## **4. Demo 4 - BTC BIP86, Index 1 + Scan Paths**
File: `seedtools-demo-04.png`

Shows:

- Index = 1
- Verify → **False** (expected)
- Scan Paths → **True**, found:
- path: `m/86'/0'/0'/0/1`
- index: 1
- standard: BTC BIP86

**Conclusion:**
- Verify only checks the current index
- Scan Paths searches the entire path
- This behavior is identical to professional forensics tools

---

## **5. Demo 5 — Multi-Seed Tests**
File: `seedtools-demo-05.png`

Shows:

- different mnemonics
- different seed_hex
- different BTC/ETH addresses
- correct Verify and Scan results
- correct address types (p2pkh, p2sh, bech32, bech32m)

**Conclusion:**
SeedTools works deterministically for multiple seeds and multiple standards.

---

## Related Documentation

- **[Standard Demo Pack](README-demo.md)** — basic deterministic tests, BTC/ETH generation, verification, scanning  
- **[Extra Demo Pack](README-seedtools-extra-demo.md)** — advanced scenarios, high indexes, Taproot, extreme path scans

---
