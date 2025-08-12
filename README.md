# File-Intergrity-Checker

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CT04DZ1482

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH





##  File Integrity Monitoring Script (Python)

This project is a lightweight Python tool designed to monitor file integrity using SHA-256 hashing.  

---

###  What It Does

- Calculates the SHA-256 hash of a target file.
- Compares the current hash with a previously stored value.
- Alerts the user if the file has been modified.
- Waits for manual input to re-check the file, making it interactive and easy to test.

---

###  Sample Output

```
Initial hash for Day4 moving object.txt: 462e677eb919590ac1b5f371d830466969c3c958b081c7c9ec80252b613cf430
Press Enter to check again...
```

This confirms the file’s initial hash and prompts the user to re-run the check. If the file changes, the script will notify you immediately.

---

###  How It Works

The script is divided into three main components:

1. **Hash Calculation Function**  
   Reads the file in binary mode and processes it in chunks to generate a SHA-256 hash. Efficient and memory-safe.

2. **Monitoring Function**  
   Compares the current hash with the stored one. If they differ, it flags the modification and prints both hashes.

3. **Main Loop**  
   Continuously monitors the file, waiting for user input between checks. Great for manual integrity verification.

---

###  Use Cases

- Detect tampering in sensitive files
- Monitor config files or logs
- Learn core cybersecurity concepts
- Build your own intrusion detection tools

---

###  Future Enhancements

- Logging changes to a `.txt` or `.csv` file
- Sending alerts via email or Discord
- Monitoring multiple files simultaneously
- Adding a GUI for easier interaction

---

###  File Monitored in Demo

`Day4 moving object.txt` — used here as a sample target file. You can replace it with any file path you want to monitor.

---

###  Why It Matters

File integrity monitoring is a foundational skill in cybersecurity. This script offers a hands-on way to understand hashing, file verification, and change detection—all in under 50 lines of Python.

---

Feel free to fork, modify, or expand this project. Contributions are welcome!

---

