#  SHA-256 Hash Cracker (Wordlist & CSV)

A simple Python-based **SHA-256 hash cracking tool** that attempts to recover plaintext passwords using a wordlist.  
The script supports **single-hash cracking** (interactive mode) and **bulk cracking from a CSV file**.

>  This tool is intended for **educational and ethical security research only**.

---

##  Features

- Crack **SHA-256 hashes**
- Wordlist-based brute force
- Optional **CSV mode** for cracking multiple hashes
- Colorized terminal output using `colorama`
- Timestamped start and end messages
- ASCII banner branding

---

##  Requirements

- `colorama`

Install dependencies:
```bash
pip install colorama
