# Case Study: Confiscated Device Recovery

## Summary
An NGO worker had their phone confiscated at a border crossing.  
They later recovered a mnemonic from memory, but suspected tampering.

## Problem
- mnemonic recalled under stress  
- possible word swaps  
- possible drift  
- unknown derivation path  
- high‑risk environment  

## Approach
1. Validate mnemonic using **Checksum Inspector**.  
2. Run **Entropy Drift Detection**.  
3. Use **Forensics Tool** to detect swapped words.  
4. Use **Suite Launcher** to run full recovery workflow.  

## Result
- Drift detected and corrected  
- Swapped words identified  
- Wallet reconstructed offline  
- NGO‑safe workflow preserved  

## Tools Used
- Mnemonic Tools  
- Entropy Inspector  
- Forensics Tool  
- Suite Launcher  

## Related
- ../scenarios/suite-launcher-cross-tool-workflow.md
