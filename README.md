# 🌐 ROVSKY Network Toolkit

> A modern Python CLI toolkit for learning networking and cybersecurity.

ROVSKY Network Toolkit is an open-source Python project designed to help beginners and enthusiasts learn networking concepts, system information, DNS analysis, HTTP inspection, and other cybersecurity fundamentals through a modular command-line interface.

---

## 🚧 Project Status

**Current Version:** `v0.1.0`

This project is currently under active development. New features and improvements will be added incrementally.

---

## ✨ Planned Features

### 🌍 Network Information

* Display Local IP Address
* Display Public IP Address
* Display Hostname
* Display Operating System
* Display Python Version

### 🌐 DNS Tools

* DNS Lookup
* Reverse DNS Lookup
* DNS Record Viewer (A, AAAA, MX, NS, TXT)

### 🌎 HTTP Tools

* HTTP Header Viewer
* Website Status Checker
* Response Information

### 🔒 SSL Information

* SSL Certificate Details
* Certificate Expiration
* Issuer Information

### 📄 Report Generator

* Export Results to TXT
* Export Results to JSON
* Export Results to Markdown

---

## 📁 Project Structure

```text
rovsky-network-toolkit/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── main.py
│
├── modules/
│   ├── network.py
│   ├── dns.py
│   ├── http.py
│   ├── sslinfo.py
│   └── report.py
│
├── utils/
│   ├── banner.py
│   ├── colors.py
│   ├── logger.py
│   └── helper.py
│
├── reports/
├── assets/
├── screenshots/
└── tests/
```

---

## 🐍 Requirements

* Python 3.13+
* pip

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/rovsky-commits/moong-network-toolkit.git
```

Move into the project directory:

```bash
cd moong-network-toolkit
```

Create a virtual environment:

```bash
py -3.13 -m venv .venv
```

Activate the virtual environment (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py 
```

---

## 🎯 Learning Goals

This project is built to improve skills in:

* Python Programming
* Modular Programming
* Networking Fundamentals
* Cybersecurity Fundamentals
* Command Line Interface (CLI)
* Git & GitHub
* Software Project Structure

---

## 🛣️ Roadmap

* [x] Create project structure
* [x] Create README
* [x] CLI Banner
* [x] Main Menu
* [x] Network Information Module
* [ ] DNS Module
* [ ] HTTP Module
* [ ] SSL Module
* [ ] Report Generator
* [ ] Documentation
* [ ] Release v1.0.0

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project will be released under the MIT License.

---

## 👨‍💻 Author

**ROVSKY MOONG**

Learning Python • Networking • Cybersecurity
