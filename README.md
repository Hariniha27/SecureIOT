# 🔒 Secure IoT Communication with Lightweight Encryption  
### 🌐 Aligning with **SDG 9 (Industry, Innovation & Infrastructure)** and **SDG 11 (Sustainable Cities & Communities)**  

---

## 📘 Overview
This project demonstrates a **Secure IoT Communication System** using **Lightweight Encryption** techniques for efficient and safe data exchange between IoT devices and a central server.  

It simulates an IoT device that sends encrypted telemetry data (temperature, humidity, battery) to a server using a **combination of asymmetric (X25519)** and **symmetric (AES-GCM)** cryptography.  
The system ensures **end-to-end confidentiality, integrity, and authentication** while being suitable for low-resource IoT environments.

---

## 🧭 Sustainable Development Goals (SDG) Alignment

### 🌱 **SDG 9 — Industry, Innovation & Infrastructure**
- Promotes **innovation** in lightweight cryptography for IoT.
- Strengthens **digital infrastructure** for industrial applications.
- Supports **Industry 4.0** through secure device communication.
- Encourages **research and development** in efficient encryption models.

### 🏙 **SDG 11 — Sustainable Cities & Communities**
- Enables **secure smart city communication** systems.
- Protects **sensor data integrity** for traffic, pollution, or utility monitoring.
- Reduces **power and bandwidth usage** via lightweight encryption.
- Builds **trustworthy IoT networks** for safer, smarter, and more sustainable urban life.

---

## ⚙️ Features
✅ Lightweight end-to-end encryption  
✅ Secure key exchange using X25519 (Elliptic Curve Diffie-Hellman)  
✅ Symmetric encryption using AES-GCM (authenticated encryption)  
✅ Real-time telemetry simulation (temperature, humidity, battery)  
✅ Multi-device server handling using threads  
✅ Energy-efficient and scalable for IoT environments  

---

## 🖥️ Requirements

- **Python 3.8+**
- Install dependencies:
  ```bash
  pip install cryptography
  ```
  
🚀 How to Run
 ```bash
🖧 Step 1: Start the Server
python server.py
Output:
Server running on 0.0.0.0:9000
```

📱 Step 2: Run the IoT Device
 ```bash
Open another terminal window and run:
python device.py
```
🧩 Step 3: Observe Secure Communication
 ```bash
Device Output:
ACK: {"status": "ok", "received": "telemetry"}
ACK: {"status": "ok", "received": "telemetry"}
```
Server Output:
 ```bash
Server running on 0.0.0.0:9000
[('127.0.0.1', 53324)] received: {'type': 'telemetry', 'device_id': 'device-001', 'ts': 1730569221, 'temperature': 26.4, 'humidity': 52.3, 'battery': 86.2}
Closed: ('127.0.0.1', 53324)
 ```
