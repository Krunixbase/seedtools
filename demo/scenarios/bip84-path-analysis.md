# Scenario: BIP84 Path Analysis

## Overview
This scenario demonstrates how SeedTools analyzes BIP84 derivation paths and detects inconsistencies.

## Input
- Valid mnemonic  
- Unknown derivation path  
- 3 known addresses

## Steps (CLI)
1. Run path explorer:
   ```
   seedtools path explore --mnemonic "<mnemonic>" --match <addresses.txt>
   ```
2. Scan BIP84 paths:
   ```
   seedtools path scan --bip84
   ```

## Steps (Desktop)
- Open **Path Explorer**
- Select **BIP84**
- Import known addresses
- Click **Scan**

## Expected Output
- Correct derivation path  
- Address match confidence  
- Path depth analysis  

## Files Used
- `../case-studies/case-study-unknown-derivation-path.md`
