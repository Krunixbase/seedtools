# Scenario: Wallet Structure Forensics

## Overview
Analyze a wallet with mixed or inconsistent structure (e.g., BIP44 + BIP84 mixed).

## Input
- Mnemonic  
- Exported xpubs  
- Mixed address set

## Steps (CLI)
1. Run wallet structure analyzer:
   ```
   seedtools forensics wallet --mnemonic "<mnemonic>" --addresses <addresses.txt>
   ```
2. Detect mixed BIP standards.
3. Generate structure report.

## Steps (Desktop)
- Open **Forensics Tool**
- Select **Wallet Structure Analysis**
- Import mnemonic + addresses
- Click **Analyze**

## Expected Output
- Detected BIP standards  
- Mixed‑wallet warning  
- Suggested reconstruction paths  

## Files Used
- `../case-studies/case-study-mixed-wallet-structure.md`
