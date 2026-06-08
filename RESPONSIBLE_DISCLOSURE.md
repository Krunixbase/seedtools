# 📘 **Responsible Disclosure Policy — SeedTools Suite**

## **1. Introduction**

SeedTools Suite is designed for offline, deterministic, and high‑security environments.  
We take security seriously and appreciate responsible reports from the community.

This policy explains how to report vulnerabilities **privately and safely**, without exposing users to risk.

---

## **2. Reporting Security Vulnerabilities**

If you discover a security issue, please report it **privately** via email:

```
krunixbase@gmail.com
```

Include the following information:

- clear description of the issue  
- steps to reproduce  
- affected version or commit  
- potential impact  
- proof‑of‑concept (if available)  

We will acknowledge your report within **72 hours**.

---

## **3. Coordinated Disclosure**

To protect users, we ask that you:

- **do not** publish the vulnerability before we release a fix  
- **do not** open public GitHub issues  
- **do not** share exploit details publicly  
- **do not** contact developers directly outside the official channel  

We follow a **coordinated disclosure** model:

1. Researcher reports privately  
2. We investigate and confirm  
3. We develop and test a fix  
4. We release a patched version  
5. We publish a security advisory  
6. Researcher may publish details after patch release  

---

## **4. Scope**

### **In Scope**
- cryptographic correctness  
- derivation logic (BIP32/39/44/49/84/86)  
- Shamir Secret Sharing (SLIP‑39)  
- entropy generation and validation  
- memory handling and zeroization  
- offline security boundaries  
- supply‑chain vulnerabilities  
- local privilege escalation within the app  

### **Out of Scope**
These issues are **environmental** and cannot be mitigated by SeedTools:

- compromised operating systems  
- hardware keyloggers  
- malicious firmware  
- BIOS/UEFI implants  
- physical access attacks  
- malware on the user’s device  

---

## **5. What We Do Not Accept**

The following are **not** considered vulnerabilities:

- feature requests  
- UI/UX issues  
- missing functionality  
- weak user passwords  
- user mistakes (wrong seed, wrong path, etc.)  
- issues caused by malware on the user’s machine  
- issues caused by modified or unofficial builds  

---

## **6. Legal Safe Harbor**

We support good‑faith security research.

If you follow this policy:

- we will not pursue legal action  
- we will not report you to authorities  
- we will treat your research respectfully  
- we will credit you (optional) in advisories  

Actions performed **outside** this policy may violate law.

---

## **7. How We Handle Reports**

Our process:

1. **Triage** — confirm severity and reproducibility  
2. **Assessment** — evaluate cryptographic and architectural impact  
3. **Fix** — patch, test, and verify  
4. **Release** — publish a secure update  
5. **Advisory** — publish CVE (if applicable)  
6. **Credit** — acknowledge the researcher (optional)  

---

## **8. Final Notes**

SeedTools is designed to minimize attack surface:

- no networking  
- no telemetry  
- no cloud  
- no seed storage  
- offline‑first  
- deterministic core  

However, **no software can protect users on a compromised system**.  
We appreciate responsible researchers who help us keep SeedTools secure.

---
