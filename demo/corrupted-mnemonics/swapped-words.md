# Corrupted Mnemonic: Swapped Words

## Description
Two valid BIP39 words were swapped during transcription.

## Example
Original (unknown to user):
```
abandon ability able about above absent absorb abstract absurd abuse access accident
```

Corrupted:
```
abandon ability able about above absent absorb abstract absurd abuse accident access
```

## Symptoms
- Mnemonic appears valid  
- Checksum fails  
- Wallet derives wrong addresses  

## Tools Used
- Mnemonic Tools — Checksum Validator  
- Forensics Tool — Corruption Classifier  
