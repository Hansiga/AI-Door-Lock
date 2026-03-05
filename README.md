# 🔐 AI-Powered Smart Door Lock System (Raspberry Pi)

An intelligent IoT-based security system that combines **Face Recognition + OTP Verification** to provide secure multi-factor authentication for physical access control.

---

## 🚀 Overview

This project enhances traditional door locking systems by integrating Artificial Intelligence and IoT.  
It uses real-time face recognition along with OTP-based second-factor authentication to prevent unauthorized access.

---

## 🎯 Problem Statement

Traditional locks can be bypassed or keys duplicated.  
Even smart locks with a single authentication method are vulnerable to spoofing.

This system improves security by implementing:

- ✅ AI-Based Face Recognition  
- ✅ OTP-Based Second Factor Authentication  
- ✅ Hardware-Level Relay Controlled Lock  

---

## 🧠 System Architecture

1. User registers face and mobile number  
2. Face dataset is stored locally  
3. During authentication:
   - Face detected using Haar Cascade  
   - Face recognized using LBPH algorithm  
   - If matched → OTP sent  
   - If OTP verified → GPIO triggers relay  
   - Solenoid lock unlocks  

---

## 🛠️ Technologies Used

### 💻 Software
- Python  
- OpenCV  
- Haar Cascade Classifier  
- LBPH Face Recognizer  
- Twilio API (OTP Service)  
- Raspberry Pi OS  

### 🔌 Hardware
- Raspberry Pi  
- USB Camera  
- Relay Module  
- Solenoid Lock  
- 18650 Battery Pack  

---

## 🔒 Security Layers

| Layer | Mechanism |
|-------|------------|
| 1️⃣ | Face Recognition |
| 2️⃣ | OTP Verification |
| 3️⃣ | Hardware Relay Activation |

Multi-layer authentication increases real-world security reliability.

---

## 📂 Project Structure

```bash
AI-Door-Lock/
│
├── register_face.py
├── unlock.py
├── dataset/
│   └── <mobile_number>/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── number.txt
│
├── haarcascade_frontalface_default.xml
└── README.md
```

---

## ⚙️ How to Run

### Step 1: Install Dependencies
```bash
pip install opencv-python
```

### Step 2: Register Face
```bash
python3 register_face.py
```

### Step 3: Unlock System
```bash
python3 unlock.py
```

---

## 📸 Project Model

![AI Door Lock Model](model%20image.jpg)

---

## 🙏 Thank You

Thank you for exploring this project.  
