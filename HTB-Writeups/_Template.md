
# [Machine Name] - [OS] - [Difficulty]

## 🎯 Information
- **Date:** `YYYY-MM-DD`
- **Platform:** HackTheBox
- **Difficulty:** [Easy/Medium/Hard]
- **Points:** 0
- **IP:** 10.10.10.x

## 🧭 Methodology

### 1. Reconnaissance
#### Nmap Scan
```bash
nmap -sC -sV -oN nmap/initial 10.10.10.x
```
*Key findings:*
- Port 22: SSH
- Port 80: HTTP

#### Web Enumeration
- Tools: Gobuster, Nikto, Wappalyzer

### 2. Initial Access
- Description of the vulnerability found (e.g., SQLi, RCE).
- **Proof of Concept:**
```python
# Exploit snippet
```

### 3. Privilege Escalation
#### User -> Root
- Enumeration using `linpeas.sh`
- Exploit used for root access.

## 🔧 Tools Used
- [ ] Nmap
- [ ] Burp Suite
- [ ] Metasploit
- [ ] Python

## 📝 Notes & Learnings
- **Key Takeaway:** Always check for SUID binaries.
- **Mistakes to Avoid:** Don't forget to run a full port scan.

## 🔗 References
- [HackTheBox - Machine Name](https://app.hackthebox.com/machines/...)
