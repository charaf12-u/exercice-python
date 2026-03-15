# 🐍 Python Exercises & Projects Collection

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)

Welcome to the **Python Exercises & Projects** repository! This workspace contains a diverse collection of Python applications, ranging from fundamental programming exercises to advanced information security tools with Graphical User Interfaces (GUIs). 

Whether you are looking to learn Python basics, explore cryptography concepts, or see practical Tkinter GUI implementations, this repository serves as a comprehensive reference guide.

---

## 📑 Table of Contents
- [About The Repository](#-about-the-repository)
- [Project Structure](#-project-structure)
- [Key Features & Modules](#-key-features--modules)
  - [Python Security Tools](#python-security-tools)
- [Technologies Used](#%EF%B8%8F-technologies-used)
- [Getting Started](#-getting-started)
- [Usage Examples](#-usage-examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About The Repository

This repository was meticulously organized to store, categorize, and track various Python coding endeavors. It acts as both a personal learning portfolio and a centralized hub for handy, reusable Python scripts. From simple algorithmic challenges to complex Hash and Caesar Cipher generators, the codebase reflects a continuous programming journey.

**SEO Keywords**: Python projects, Python exercises, Tkinter GUI tutorial, Hash MD5 generator Python, Caesar cipher Python implementation, Learn Python programming, Information security scripting.

---

## 📂 Project Structure

The repository is modularly divided into several specialized directories to ensure code maintainability and logical separation of concerns:

```text
📁 PycharmProjects/
├── 📁 charaf_scripts/      # Personal custom utility scripts and automation tools
├── 📁 exercise_2/          # Second module of targeted programming exercises
├── 📁 main_project/        # The core primary project application
├── 📁 python_security/     # 🔐 Cryptography, hashing, and security algorithm GUIs
├── 📁 revision_materials/  # Code snippets and notes for exam/concept revisions
├── 📁 scratchpad/          # Temporary playground for testing out new Python ideas
└── 📁 secondary_project/   # Auxiliary applications and side projects
```

---

## 🚀 Key Features & Modules

### 🔐 Python Security Tools (`/python_security`)
This subset of the repository is dedicated to information security, primarily focusing on encryption and hashing techniques:
* **MD5 Hash Generator GUI (`hash_gui.py`)**: A fully functional Tkinter application that takes text input, generates its MD5 hash equivalent, and permanently stores records in a local text file.
* **Caesar Cipher GUI (`caesar_cipher_gui.py`)**: An interactive application to encrypt and decrypt sensitive messages using the historic Caesar Cipher shift text technique.
* **Security Utilities**: Reusable OOP classes for file reading (`file_reader.py`) and cipher operations (`caesar_utility.py`, `hash_utility.py`).

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Standard Libraries:** `hashlib` (Cryptography), `tkinter` (Desktop GUIs)
- **Concepts Applied:** Object-Oriented Programming (OOP), Event-Driven UI, File I/O operations, String manipulation.

---

## 🏁 Getting Started

To get a local copy up and running on your machine, follow these simple steps.

### Prerequisites
Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
No heavy external dependencies are required for the standard scripts as they mostly utilize Python's built-in libraries.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/charaf12-u/exercice-python.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd exercice-python
   ```
3. *(Optional)* **Create a Virtual Environment** to keep things clean:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On MacOS/Linux
   source venv/bin/activate
   ```

---

## 💻 Usage Examples

To run the Graphical Hash Generator:
```bash
cd python_security
python hash_gui.py
```
A desktop window will appear allowing you to input text and generate secure MD5 hashes instantly.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Maintained with ❤️ for the love of Python programming and cyber security.*
