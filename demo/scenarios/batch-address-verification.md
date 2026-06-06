# Scenario: Batch Address Verification

## Overview
Verify a large set of addresses against a mnemonic or xpub.

## Input
- 200+ addresses  
- Known: BIP49 wallet  
- Mnemonic or xpub

## Steps (CLI)
1. Run batch verification:
   ```
   seedtools scan addresses --bip49 --input addresses.txt --mnemonic "<mnemonic>"
   ```

## Steps (Desktop)
- Open **Address Scanner**
- Select **Batch Verification**
- Import address list
- Click **Verify**

## Expected Output
- Verified addresses  
- Path inference  
- Mismatch report  

## Files Used
- `../scenarios/address-scanner-batch-verification.md`
