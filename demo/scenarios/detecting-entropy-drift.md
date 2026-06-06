# Scenario: Detecting Entropy Drift

## Overview
Entropy drift occurs when a mnemonic is valid but does not match the original entropy due to transcription or encoding errors.

## Input
- 24‑word mnemonic  
- User suspects drift  
- No known derivation path

## Steps (CLI)
1. Run entropy inspector:
   ```
   seedtools entropy inspect --mnemonic "<mnemonic>"
   ```
2. Compare entropy checksum vs expected.
3. Run drift classifier:
   ```
   seedtools entropy drift --mnemonic "<mnemonic>"
   ```

## Steps (Desktop)
- Open **Entropy Inspector**
- Paste mnemonic
- Click **Analyze**
- Review drift probability

## Expected Output
- Drift probability score  
- Bit‑level entropy map  
- Suggested correction candidates  

## Files Used
- `../corrupted-mnemonics/entropy-drift-example.md`
