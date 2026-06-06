# Case Study: Lost 12‑Word Seed Recovery

## Summary
A user lost access to a 12‑word seed after misplacing the original backup.  
They remembered only 10 words and the approximate order.

## Problem
- 2 missing words  
- checksum unknown  
- no derivation path  
- no xpub  
- only 3 known addresses  

## Approach
1. Use **Mnemonic Tools** to generate all checksum‑valid candidates.  
2. Use **Address Scanner** to match known addresses.  
3. Use **Path Explorer** to infer the correct BIP path.  

## Result
- Correct mnemonic reconstructed  
- BIP84 path identified  
- Wallet fully recovered  

## Tools Used
- Mnemonic Recovery  
- Address Scanner  
- Path Explorer  

## Related
- ../scenarios/recovery-from-partial-mnemonic.md
