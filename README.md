# Secure IoT Communication with Lightweight Encryption

## Project Overview
This project demonstrates secure communication between simulated IoT devices and a central server using **lightweight encryption**. It is designed for resource-constrained IoT devices where heavy encryption algorithms are impractical.  

**SDG Goals:**
- **SDG 9 (Industry, Innovation, and Infrastructure):** Promotes innovative and secure technology solutions.
- **SDG 11 (Sustainable Cities and Communities):** Secures IoT devices in smart city applications, ensuring safe and reliable urban infrastructure.

---

## Folder Structure
```bash
SecureIoT/
├── client.py # Simulated IoT device sending encrypted messages
├── server.py # Central server receiving and decrypting messages
├── encryption.py # Lightweight XOR encryption algorithm
├── test_encryption.py # Test script for encryption/decryption
├── requirements.txt # Python dependencies (empty for this project)
└── README.md
```
---

## Features
- Simulated IoT communication between client and server
- Lightweight XOR encryption for securing messages
- Server decrypts messages in real-time
- Can be extended to TinyAES or other lightweight encryption algorithms
- Demonstrates secure communication in smart city applications

---

## Requirements
- Python 3.x
- No additional libraries required

---

## How to Run

### 1. Run the Server
Open a terminal and navigate to the project folder:
```bash
python server.py
You should see:
Server listening on 127.0.0.1 : 65432
```
### 2.Run the Client
```bash
Open another terminal in the same folder and run:
python client.py
You will see the encrypted messages being sent on the client terminal, and the decrypted messages on the server terminal:
Received decrypted: Temperature:25C
Received decrypted: Humidity:60%
Received decrypted: Traffic:High
```
### How It Works
```bash
Client (client.py): Simulates IoT devices sending sensor data. Data is encrypted using a lightweight XOR cipher.
Encryption (encryption.py): Contains the xor_encrypt_decrypt function for both encryption and decryption.
Server (server.py): Listens for incoming connections, receives encrypted messages, decrypts them, and prints them in real-time.
```
