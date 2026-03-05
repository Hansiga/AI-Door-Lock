🔐 AI-Powered Smart Door Lock System (Raspberry Pi)
🚀 Overview

An intelligent IoT-based door security system that integrates Face Recognition + OTP Verification to provide secure, multi-factor authentication for physical access control.

This project combines Artificial Intelligence, Embedded Systems, and IoT to create a real-time smart locking mechanism using Raspberry Pi.

🎯 Problem Statement

Traditional locks can be easily bypassed or keys can be duplicated. Even smart locks with single authentication methods (PIN or face recognition) are vulnerable to spoofing.

This system solves the problem by implementing:

✅ Face Recognition (AI-based identity verification)

✅ OTP-based Second Factor Authentication

✅ Hardware-level Lock Control via Relay & Solenoid

🧠 System Architecture

User registers face and mobile number.

System stores face dataset locally.

During authentication:

Face is detected using Haar Cascade.

Face is recognized using LBPH algorithm.

If matched → OTP is sent via Twilio.

If OTP verified → GPIO triggers relay.

Solenoid lock unlocks the door.

🛠️ Technologies Used
💻 Software

Python

OpenCV

Haar Cascade Classifier

LBPH Face Recognizer

Twilio API (OTP Service)

Linux (Raspberry Pi OS)

🔌 Hardware

Raspberry Pi

USB Camera

Relay Module

Solenoid Lock

18650 Battery Pack

Power Bank

🔒 Security Layers
Layer	Mechanism
1️⃣	Face Recognition
2️⃣	OTP Verification
3️⃣	Hardware Relay Activation

This ensures multi-factor authentication, increasing real-world security reliability.

📂 Project Structure
AI-Door-Lock/
│
├── register_face.py
├── unlock.py
├── dataset/
│   └── <mobile_number>/
│       ├── 1.jpg
│       ├── 2.jpg
│       ├── ...
│       └── number.txt
└── haarcascade_frontalface_default.xml
⚙️ How It Works
🔹 Step 1: Face Registration

Run:

python3 register_face.py

Captures 20 grayscale face images

Stores mobile number

Creates dataset folder

🔹 Step 2: Unlock Process

Run:

python3 unlock.py

Trains LBPH model

Detects and recognizes face

Sends OTP

Unlocks solenoid upon verification
