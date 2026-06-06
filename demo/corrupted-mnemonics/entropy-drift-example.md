# Corrupted Mnemonic: Entropy Drift

## Description
Mnemonic is valid and passes checksum, but entropy does not match the original due to transcription drift.

## Example
Original (unknown):
```
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
```

Drifted:
```
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon above
```

## Symptoms
- Mnemonic imports successfully  
- Wallet shows empty balance  
- Addresses do not match  
- Drift probability > 80%  

## Tools Used
- Entropy Inspector — Drift Detection  
- Forensics Tool — Address Mismatch Analysis  
