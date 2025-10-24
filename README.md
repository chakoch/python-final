# 🐍 System Monitoring Application in Python

> A terminal-based tool to monitor CPU, memory, and disk usage – built with object-oriented Python and a DevOps-inspired architecture.

---

## 👤 Project Information
**Name:** Sam Jaudat  
**Class:** DOE25 (Chas Academy)  
**Date:** October 24, 2025  
**GitHub:** [chakoch/python-final](https://github.com/chakoch/python-final)

---

## 🎓 Chas Academy Python Final Project
**Monitoring CPU / Memory / Disk Application**

---

### 🐧 Setup for Linux / macOS

**Create a virtual environment:**
```bash
python3 -m venv venv
```

**Activate the environment:**
```bash
source venv/bin/activate
```

**Install required packages:**
```bash
pip install -r requirements.txt
```

**Run the program:**
```bash
python main.py
```

---

### 🪟 Setup for Windows

**Create a virtual environment:**
```bash
python -m venv venv
```

**Activate the environment:**
```bash
venv\Scripts\activate
```

**Install required packages:**
```bash
pip install -r requirements.txt
```

**Run the program:**
```bash
python main.py
```

---

## 📘 1. Introduction
This application displays real-time CPU, memory, and disk usage directly in the terminal.  
It allows users to start or stop monitoring, create and delete alarms, and run an automated monitoring mode that triggers alerts when resource usage exceeds defined thresholds.  
The goal is to demonstrate object-oriented programming, file handling, and exception management in Python – applied in a small but structured DevOps-inspired utility.

---

## 🧩 2. Planning and Design
The project follows the **CRUD principle** (Create, Read, Update, Delete) to maintain a clear and realistic structure, similar to how resources are managed through APIs in DevOps workflows.  
This approach made the logic easy to follow, with each class having a well-defined responsibility within the overall architecture.

---

## 🏗️ 3. Program Structure

| File | Purpose |
|------|----------|
| `main.py` | Main menu and program flow |
| `monitor.py` | Retrieves system data using `psutil` |
| `alarm.py` | Handles creation and control of alarms |
| `storage.py` | Saves and loads alarms from JSON file |
| `logger.py` | Logs program events |
| `helpers.py` | Contains reusable helper functions (DRY principle) |
| `constants.py` | Stores constants to prevent data duplication |

Communication between modules occurs through objects passed as arguments (e.g., `AlarmManager`, `SystemMonitor`, `Logger`, `AlarmStorage`).

---

## ⚙️ 4. Key Functions and Classes

1. **`SystemMonitor.get_current_stats()`** – Returns real-time CPU, RAM, and disk usage using `psutil`.  
2. **`AlarmManager.check_alarms(stats)`** – Compares live stats with thresholds and triggers alarms if limits are exceeded.  
3. **`helpers.py`** – Contains shared utility functions (`print_section()`, `format_stats()`, `get_int_input()` etc.) following the **DRY principle**.

---

## 🧰 5. Libraries and Tools

| Library | Usage |
|----------|-------|
| `psutil` | Retrieves system statistics (CPU, memory, disk) |
| `os` | File handling and terminal operations |
| `json` | Saves and loads alarms from file |
| `sys`, `tty`, `termios`, `msvcrt` | Handles key presses without requiring Enter |
| `time` | Loops and pauses in monitoring mode |

Version control handled via **Git and GitHub**.

---

## 🧪 6. Testing and Debugging
- Each menu option was tested manually.  
- Alarm triggers were validated using various threshold values.  
- Input errors are handled with `try/except`.  
- The JSON file was tested for both adding and deleting alarms.  

### Identified and Fixed Bugs:
1. **Logger attribute:** incorrect attribute name fixed to `self.log_file`.  
2. **Boolean call:** `is_monitoring()` changed to variable reference.  
3. **macOS issue:** `psutil` installation required a proper virtual environment (`venv`).  
4. **UX improvement:** `wait_for_key()` rewritten for cross-platform compatibility (Windows/macOS/Linux).

After these fixes, the program ran stably across environments, with cleaner, more modular code following DRY principles.

---

## 🧾 7. Results
✅ Monitoring can be started and stopped  
✅ Alarms can be created, listed, deleted, and triggered  
✅ Data is stored persistently in a JSON file  
✅ Interface is consistent and user-friendly  

---

## 🚀 8. Future Improvements
Possible enhancements:
- 📬 Add email or Slack notifications when alarms trigger  
- 🧩 Implement unit tests using `pytest`  
- 🕓 Extend the logger with timestamps and log levels  

---

## 🧠 9. Summary
The project demonstrates how Python can be used to build a robust, modular, and well-structured system monitoring tool.  
It applies OOP, JSON storage, exception handling, the DRY principle, and Git-based version control – resulting in a portable, maintainable, and DevOps-inspired application.

---

📎 **Repository:** [https://github.com/chakoch/python-final](https://github.com/chakoch/python-final)
