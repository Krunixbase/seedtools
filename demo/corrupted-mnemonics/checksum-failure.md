# Corrupted Mnemonic: Checksum Failure

## Description
Mnemonic contains only valid BIP39 words, but checksum is incorrect.

## Example
```
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon
```

## Symptoms
- Wallet rejects mnemonic  
- Entropy reconstruction fails  
- No valid seed can be derived  

## Tools Used
- Mnemonic Tools — Checksum Inspector  
- Entropy Inspector — Bit‑Level Analysis  
