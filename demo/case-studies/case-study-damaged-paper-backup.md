# Case Study: Damaged Paper Backup

## Summary
A paper backup was partially destroyed by water.  
Several words were unreadable or ambiguous.

## Problem
- 24‑word mnemonic  
- 3 words unreadable  
- 2 words ambiguous (similar handwriting)  
- checksum mismatch  

## Approach
1. Use **Mnemonic Tools** to validate partial input.  
2. Use **Entropy Inspector** to detect drift.  
3. Use **Forensics Tool** to classify corruption type.  
4. Generate candidate sets and test against known addresses.  

## Result
- Correct mnemonic reconstructed  
- Drifted words identified  
- Wallet fully restored  

## Tools Used
- Mnemonic Tools  
- Entropy Inspector  
- Forensics Tool  
- Address Scanner  

## Related
- ../corrupted-mnemonics/missing-words.md
