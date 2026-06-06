 **SeedTools CLI — SeedTools Suite**

## **Overview**

SeedTools CLI is the **command‑line interface** for the entire SeedTools Suite.  
It provides a fast, scriptable, offline‑first toolkit for:

- deterministic wallet recovery,  
- mnemonic and entropy analysis,  
- derivation path exploration,  
- address scanning and verification,  
- forensics workflows for NGOs and high‑risk users.

The CLI is designed for:

- power users,  
- developers,  
- Tails/Qubes/air‑gapped environments,  
- automated workflows,  
- support teams operating in the field.

It mirrors the functionality of the GUI applications, but in a **lightweight, automation‑friendly** form.

---

# **Key Capabilities**

- **Mnemonic Tools**  
  - validate mnemonics  
  - convert mnemonic ↔ entropy  
  - inspect checksum and structure  

- **Entropy Inspector**  
  - entropy validation  
  - drift detection  
  - checksum mismatch analysis  

- **Recovery Engine**  
  - derive addresses  
  - verify ownership  
  - scan extended index ranges  

- **Address Scanner**  
  - batch address verification  
  - deep path scanning  
  - multi‑account scanning  

- **Path Explorer**  
  - test custom derivation paths  
  - generate addresses for any path  
  - validate BIP32/44/49/84/86  

- **Forensics Mode**  
  - detect corrupted mnemonics  
  - analyze entropy drift  
  - identify path mismatches  

- **Offline‑first architecture**  
  - no telemetry  
  - no external API calls  
  - safe for air‑gapped systems  

---

# **Installation**

SeedTools CLI is distributed as:

- a standalone Python package,  
- a portable binary for Linux/macOS/Windows,  
- a Tails/Qubes‑friendly offline bundle.

(Installation instructions go into the main documentation repo.)

---

# **Basic Usage**

## **Validate a mnemonic**

```
seedtools mnemonic validate "abandon abandon abandon ..."
```

## **Convert mnemonic → entropy**

```
seedtools mnemonic to-entropy "abandon abandon abandon ..."
```

## **Scan for an address**

```
seedtools scan --seed "..." --address bc1qxyz...
```

## **Explore a derivation path**

```
seedtools path derive --seed "..." --path "m/84'/0'/0'/0/5"
```

## **Run full forensics**

```
seedtools forensics --mnemonic "..." 
```

---

# **Typical Workflows**

## **1. Offline wallet recovery**

1. Boot Tails/Qubes.  
2. Run:
   ```
   seedtools recover --mnemonic "..." --bip84 --scan-range 0-500
   ```
3. Export addresses and paths.  
4. Import into Sparrow/Specter.

---

## **2. Batch address verification**

```
seedtools scan batch --seed "..." --file addresses.txt
```

Outputs:

- match / no match  
- full derivation path  
- index  
- address type  

---

## **3. Diagnose a corrupted mnemonic**

```
seedtools forensics --mnemonic "..."
```

CLI returns:

- invalid words  
- checksum mismatch  
- entropy drift map  
- recoverability hints  

---

# **Who This Tool Is For**

- **Developers** — scripting, automation, testing.  
- **Power users** — fast, deterministic workflows.  
- **NGOs & support teams** — field‑safe, offline diagnostics.  
- **High‑risk users** — no GUI, no telemetry, no traces.  
- **Educators** — demonstrate BIP32/39/44/84/86.  

---

# **Security Notes**

- Always run CLI on a **trusted machine**.  
- Prefer **air‑gapped** environments for sensitive seeds.  
- Never store mnemonics in shell history.  
- Use `--no-history` or ephemeral shells when possible.  
- Verify builds using reproducible build instructions.

---

# **Roadmap (Preview)**

- **Tails/Qubes hardened mode**  
- **Batch forensics**  
- **Taproot‑specific CLI tools**  
- **JSON output mode**  
- **Integration with GUI apps**  
- **Reproducible builds**  

---
