# Defensive Auth System v2.0

A modular, defensive user authentication system built with Python. Designed as a proof-of-concept for secure credential handling, password salting, and persistent data storage.

## Features
- **Salted Password Hashing:** Uses `SHA-256` combined with a unique, cryptographically random salt (`os.urandom`) per user to prevent Rainbow Table attacks.
- **Hidden Password Input:** Implements `getpass` for terminal-level password masking to prevent shoulder surfing.
- **Persistent JSON Storage:** Saves user credentials securely in a structured `users.json` database.
- **Cross-Platform Pathing:** Uses `pathlib` for reliable, dynamic file paths across systems.
- **Input Sanitization:** Strips whitespace and enforces case-insensitivity on usernames.
- **Modular Architecture:** Clean separation of concerns between cryptography logic (`auth.py`) and command-line user interface (`login.py`).

## Tech Stack
- **Language:** Python 3.14+
- **Modules:** `hashlib`, `json`, `os`, `getpass`, `pathlib`

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/AxelGabrielOlarte/python-secure-login-system.git](https://github.com/AxelGabrielOlarte/python-secure-login-system.git)
   cd python-secure-login-system
