# **📸 Extra Demo — Advanced Test Cases (SeedTools 2.0)**

This extended demo demonstrates SeedTools 2.0 in advanced scenarios:

high indexes, unusual paths, full scans, Taproot, BIP84/BIP86, and address verification in extreme cases.

--

## **1. BIP84 — Verify True at High Index**
Shows:

- Index = 9000
- BIP84 address generation
- Verify → **Match: True**
- correct address binding to the seed
- deterministic operation even with very large indexes

---

## **2. BIP84 — Scan Paths for Index 9000**
- Verify → False (expected)
- Scan Paths → **True**, found:
- `m/84'/0'/0'/0/9000`
- standard: BIP84
- index: 9000

**Conclusion:**
SeedTools can scan paths in large ranges (e.g., 100500) and correctly find addresses at high indices.

--

## **3. BIP86 — Taproot at a High Index**
Shows:

- Taproot address generation (BIP86)
- Verify → False (because index ≠ 0)
- Scan Paths → True
- Correct detection of the address type: **p2tr**

**Conclusion:**
Taroot support works correctly even with extreme indexes.

--

## **4. Multi‑Path Stress Test**
Shows:

- Various BTC/ETH addresses
- Various BIP standards
- Various indexes (0, 1, 9000)
- Correct Verify and Scan results
- Correct address types (p2pkh, p2sh, bech32, bech32m, p2tr)

**Conclusion:**
SeedTools maintains full determinism and consistency even with extreme input data.

---

