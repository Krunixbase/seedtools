# 📘 **SeedTools Security FAQ**

## **1. Is SeedTools safe to use offline?**
Yes. SeedTools is designed as an **offline‑first** application.  
It does not:

- connect to the internet  
- send telemetry  
- use external APIs  
- store seeds or keys  

All operations happen locally on the user’s device.

---

## **2. Does SeedTools ever transmit my seed or private keys?**
No.  
SeedTools has **no networking code**, no telemetry, and no cloud components.  
Your seed never leaves your device.

---

## **3. Does SeedTools store my seed on disk?**
No.  
SeedTools does not write:

- seed phrases  
- seed hex  
- private keys  
- derivation paths  

to disk in any mode.

All sensitive data stays in RAM and is zeroized where possible.

---

## **4. Can SeedTools be used to hack or attack other wallets?**
No.  
SeedTools does not provide:

- brute‑force tools  
- seed recovery  
- blockchain scanning  
- attack surfaces  
- offensive cryptography  

It only works deterministically on the seed **provided by the user**.

---

## **5. What happens if a malicious person uses SeedTools?**
Nothing harmful.  
A malicious user can only:

- generate addresses from **their own seed**  
- verify addresses from **their own seed**  
- scan derivation paths for **their own seed**

SeedTools does not give attackers any advantage over standard HD wallets.

---

## **6. Is SeedTools safe if my operating system is compromised?**
No.  
If the OS is infected (keylogger, screen grabber, memory scraper),  
**no application can protect your seed**.

This is an environmental risk, not an application flaw.

Recommendation:  
Use SeedTools on a **trusted, offline machine**.

---

## **7. Can clipboard hijackers steal my seed?**
No.  
SeedTools does **not** use the clipboard for seed handling.  
Clipboard‑based attacks are effectively eliminated.

---

## **8. How does SeedTools protect against supply‑chain attacks?**
Mitigations include:

- official GitHub releases  
- reproducible builds (planned)  
- pinned dependencies  
- offline packaging  
- checksums and signatures (recommended)

Users should verify downloads before use.

---

## **9. Does SeedTools validate Shamir shares?**
Yes.  
SeedTools performs:

- polynomial validation  
- threshold verification  
- share consistency checks  

This prevents recovery using corrupted or tampered shares.

---

## **10. Does SeedTools check entropy quality?**
Yes.  
SeedTools includes:

- entropy scoring  
- anomaly detection  
- pattern detection  

Weak or predictable seeds are flagged.

---

## **11. Can SeedTools fail due to hardware issues?**
Yes.  
Hardware failures (RAM instability, disk corruption, power loss)  
are outside the scope of SeedTools.

Recommendation:  
Use SeedTools on stable, trusted hardware.

---

## **12. Is Taproot (BIP86) supported securely?**
Yes.  
SeedTools validates:

- key‑path derivation  
- script‑path rules  
- bech32m encoding  

Incorrect Taproot logic is detected and rejected.

---

## **13. Does SeedTools protect me from physical access attacks?**
Partially.  
SeedTools does not store sensitive data, but:

- shoulder surfing  
- device theft  
- hardware implants  

are outside the application’s control.

Operational security is required.

---

## **14. What risks remain even with SeedTools?**
Residual risks include:

- OS‑level compromise  
- hardware keyloggers  
- malicious firmware  
- physical theft  
- supply‑chain hardware attacks  

These cannot be mitigated by software alone.

---

## **15. Is SeedTools a wallet?**
No.  
SeedTools is a **deterministic cryptographic tool**, not a wallet.  
It does not:

- hold funds  
- sign transactions  
- broadcast transactions  
- manage balances  

It is strictly a **local analysis and verification tool**.

---

## **16. Can SeedTools generate unsafe seeds?**
No.  
SeedTools uses:

- high‑quality entropy  
- deterministic generation  
- entropy validation  

Weak seeds are detected and rejected.

---

## **17. Can SeedTools be used in regulated environments?**
Yes.  
SeedTools is designed for:

- air‑gapped systems  
- compliance workflows  
- forensics  
- enterprise security environments  

It introduces no network or cloud dependencies.

---
