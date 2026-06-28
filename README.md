# Data Integrity Checker (SHA-256 Demo)

A lightweight Python script that demonstrates the core cybersecurity concept of **Data Integrity** (the "I" in the CIA Triad). Using the **SHA-256** cryptographic hashing algorithm, this project visually explains how even a minor, single-character alteration in data completely changes its hash, making unauthorized modifications instantly detectable.

---

## 🚀 How It Works

The script simulates a 3-stage workflow to test and verify data integrity:

1. **Original Data:** Generates a SHA-256 hash for a secure baseline message.
2. **Data Manipulation:** Simulates a tamper event or accidental modification by changing just one character (changing a capital `T` to a lowercase `t`).
3. **Integrity Control:** Compares both hashes. Since the hashes do not match, the system flags that the data integrity has been compromised.

---

## 🛠️ Features

* **Zero Dependencies:** Uses Python's built-in `hashlib` library.
* **Cryptographic Demonstration:** Implements secure **SHA-256** hashing.
* **Educational Value:** Clear console outputs showcasing how hashing secures data transmission.

---

## 📦 Prerequisites & Installation

No external packages are required! You only need **Python 3.x** installed on your machine.
