<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=🛠️+Multi-Utility+Toolkit;Python+Module+Powerhouse;Built+for+Developers+%F0%9F%9A%80" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/HarshalVora86/Moduler-Packager?style=for-the-badge&logo=github&color=yellow)](https://github.com/HarshalVora86/Moduler-Packager)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge&logo=github)](https://github.com/HarshalVora86/Moduler-Packager/issues)

<br/>

> **A powerful, menu-driven Python toolkit** that bundles datetime handling, math operations, random data generation, UUID creation, and custom file I/O — all in one clean, modular package. 🎯

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700"/>

</div>

---

## 📖 Table of Contents

- [⚡ What It Does](#-what-it-does)
- [🗂️ Project Structure](#️-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🛠️ Modules Overview](#️-modules-overview)
- [📸 Screenshots](#-screenshots)
- [📌 Key Concepts Used](#-key-concepts-used)
- [🤝 Contributing](#-contributing)

---

## ⚡ What It Does

<div align="center">

![datetime](https://img.shields.io/badge/📅_Datetime-Current_Time_•_Date_Diff_•_Stopwatch_•_Countdown-E6F1FB?style=for-the-badge&labelColor=185FA5&color=E6F1FB)

![math](https://img.shields.io/badge/➗_Math-Factorial_•_Compound_Interest_•_Trig_•_Area-EEEDFE?style=for-the-badge&labelColor=534AB7&color=EEEDFE)

![random](https://img.shields.io/badge/🎲_Random-Numbers_•_Lists_•_Password_Gen_•_OTP-FAEEDA?style=for-the-badge&labelColor=854F0B&color=FAEEDA)

![uuid](https://img.shields.io/badge/🔑_UUID-Single_UUID_•_Bulk_Generation-FBEAF0?style=for-the-badge&labelColor=993556&color=FBEAF0)

![fileops](https://img.shields.io/badge/📁_File_Ops-Create_•_Write_•_Read_•_Append-FAECE7?style=for-the-badge&labelColor=993C1D&color=FAECE7)

![module](https://img.shields.io/badge/🔍_Module_Explorer-dir()_•_\_\_import\_\_()_Dynamic_Load-EAF3DE?style=for-the-badge&labelColor=3B6D11&color=EAF3DE)

</div>

## 🗂️ Project Structure

```
Moduler-Packager/
│
├── 📄 PR_7.py               # Main entry point — interactive menu system
├── 📦 file_operations.py    # Custom module for file I/O operations
└── 📘 README.md             # You're reading it!
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10+** (uses `match`/`case` syntax)
- No external libraries needed — pure standard library! 🎉

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/HarshalVora86/Moduler-Packager.git

# 2. Navigate to the project folder
cd Moduler-Packager

# 3. Run the toolkit
python PR_7.py
```

> ✅ That's it! No `pip install` needed.

---

## 🛠️ Modules Overview

### 🔵 `PR_7.py` — Main Controller

The brain of the toolkit. Uses Python's **`match`/`case`** (structural pattern matching) to route user choices to the right sub-menu.

```python
match choice:
    case 1: # Datetime operations
    case 2: # Math operations
    case 3: # Random data generation
    case 4: # UUID generation
    case 5: # File operations
    case 6: # Module explorer
    case 7: # Exit
```

**Standard libraries used:**
`math` · `datetime` · `time` · `random` · `string` · `uuid`

---

### 🟢 `file_operations.py` — Custom Module

A hand-crafted Python module demonstrating **modular programming** and clean separation of concerns.

```python
import file_operations

file_operations.create_file("notes.txt")
file_operations.write_file("notes.txt", "Hello, World!")
file_operations.read_file("notes.txt")
file_operations.append_file("notes.txt", "\nMore data")
```

| Function | Description |
|----------|-------------|
| `create_file(filename)` | Creates an empty file |
| `write_file(filename, data)` | Writes (overwrites) content to a file |
| `read_file(filename)` | Reads and prints file content |
| `append_file(filename, data)` | Appends data without overwriting |

---

## 📸 Screenshots

<div align="center">

**🏠 Main Menu**

![Main Menu](S1.png)

**📅 Datetime Operations — Date Difference**

![Date Diff](S2.png)

**➗ Math — Area of Circle**

![Math](S3.png)

**🎲 Random Password Generator**

![Password](S4.png)

**🔑 UUID Bulk Generator**

![UUID](S5.png)

**📁 File Operations — Read File**

![File Ops](S6.png)

**🔍 Module Explorer (dir())**

![Module Explorer](S7.png)

</div>

---

## 📌 Key Concepts Used

```python
✅ Modular Programming       — Custom module (file_operations.py)
✅ match / case              — Python 3.10+ structural pattern matching
✅ Standard Library Mastery  — math, datetime, time, random, string, uuid
✅ File Handling             — read, write, append, create
✅ OOP-style Design          — Clean separation of concerns
✅ Real-time I/O             — Stopwatch & countdown timer with time.sleep()
✅ Module Introspection      — dir() + __import__() for dynamic exploration
```

---

## 🤝 Contributing

Contributions, ideas, and bug reports are welcome! 🙌

```bash
# Fork → Clone → Create Branch → Commit → Push → Pull Request
git checkout -b feature/your-feature-name
git commit -m "✨ Add: your feature description"
git push origin feature/your-feature-name
```

---

<div align="center">

⭐ **If you found this useful, drop a star on the repo!** ⭐

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400"/>

*Built with ❤️ and Python*

<img src="https://komarev.com/ghpvc/?username=HarshalVara86&label=Profile+Views&color=0e75b6&style=flat" alt="profile views" />

</div>
