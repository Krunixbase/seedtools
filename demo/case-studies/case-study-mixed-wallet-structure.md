# Case Study: Mixed Wallet Structure

## Summary
A user unknowingly used multiple wallets over time, mixing BIP44 and BIP84 structures.

## Problem
- valid mnemonic  
- mixed address sets  
- inconsistent balances  
- multiple xpubs  
- unknown original wallet  

## Approach
1. Use **Wallet Structure Analyzer** to detect mixed BIP standards.  
2. Map addresses to their respective paths.  
3. Reconstruct each sub‑wallet deterministically.  

## Result
- Mixed structure identified  
- BIP44 and BIP84 separated  
- Full wallet reconstructed  
- User educated on wallet hygiene  

## Tools Used
- Forensics Tool  
- Path Explorer  
- Address Scanner  

## Related
- ../scenarios/wallet-structure-forensics.md
