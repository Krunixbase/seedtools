# Corrupted Mnemonic: Invalid Language Word

## Description
Mnemonic contains a word that does not exist in any BIP39 wordlist.

## Example
```
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abend
```

(`abend` is not a valid BIP39 word)

## Symptoms
- Immediate rejection by wallets  
- Cannot compute entropy  
- No valid checksum  

## Tools Used
- Mnemonic Tools — Invalid Word Detector  
- Wordlist Tools — Similar Word Suggestions  
