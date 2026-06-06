# Scenario: Recovering a Wallet from a Partial Mnemonic

## Overview
This scenario demonstrates how SeedTools Suite reconstructs a wallet from an incomplete mnemonic with missing words.

## Input
- 12‑word mnemonic with 2 missing words  
- Known: BIP84 wallet  
- Known: last 4 addresses

## Steps (CLI)
1. Run the mnemonic reconstruction module:
   ```
   seedtools mnemonic recover --input "abandon abandon ? ? abandon abandon abandon abandon abandon abandon abandon about"
   ```
2. Generate all valid checksum‑correct candidates.
3. Use the address scanner:
   ```
   seedtools scan addresses --path bip84 --match <known-addresses.txt>
   ```
4. Identify the correct seed.

## Steps (Desktop)
- Open **Mnemonic Tools**
- Select **Recover Missing Words**
- Paste partial mnemonic
- Select **BIP84**
- Import known addresses
- Click **Scan**

## Expected Output
- Reconstructed mnemonic  
- Derived seed  
- Matching derivation path  
- Verified addresses  

## Files Used
- `../corrupted-mnemonics/missing-words.md`
