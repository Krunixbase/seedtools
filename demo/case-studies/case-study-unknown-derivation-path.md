# Case Study: Unknown Derivation Path

## Summary
A user imported a valid mnemonic into multiple wallets and saw different balances.  
The original derivation path was unknown.

## Problem
- valid mnemonic  
- multiple possible BIP standards  
- inconsistent address sets  
- no xpub  

## Approach
1. Use **Path Explorer** to scan BIP32/44/49/84/86.  
2. Import known addresses for matching.  
3. Generate path confidence scores.  

## Result
- Correct path identified: `m/84'/0'/0'`  
- Address mismatch explained  
- Wallet reconstructed deterministically  

## Tools Used
- Path Explorer  
- Address Scanner  

## Related
- ../scenarios/bip84-path-analysis.md
