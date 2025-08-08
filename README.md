# 🔌 Dircom

[![CI](https://github.com/ncamilo/dircom/actions/workflows/python-ci.yml/badge.svg)](https://github.com/ncamilo/dircom/actions)

**Dircom** is a lightweight, cross-platform command-line utility written in Python to list available serial (COM) ports on your system, with special emphasis on USB-connected devices. Ideal for developers working with ESP32, Arduino, Raspberry Pi, sensors, and other serial peripherals.

---

## 🚀 Features

- Lists all available serial ports (COM on Windows, `/dev/tty*` on Unix-like systems)  
- Filters only USB-connected ports (`--usb-only`)  
- Tags USB ports with `[USB]`  
- Compatible with **Windows**, **Linux**, and **macOS**  
- Simple, easy-to-use CLI  
- Can be packaged as a standalone executable for Windows  

---

## 💻 Usage

```bash
dircom [options]
```

### Options

| Flag               | Description                               |
|--------------------|-------------------------------------------|
| `-u`, `--usb-only` | Show only USB-connected ports             |
| `-v`, `--version`  | Display the current Dircom version        |
| `-h`, `--help`     | Show help message and exit                |

### Examples

```bash
dircom
dircom --usb-only
dircom --version
```

---

## 🔧 Installation

### From PyPI

```bash
pip install dircom
```

---

## 🛠️ Compiling to a Windows Executable

If you want to distribute Dircom without requiring Python:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --name dircom dircom.py
   ```
3. The standalone executable will be created at:
   ```
   dist/dircom.exe
   ```

---

## 🐧 Linux / macOS

Run directly with Python:

```bash
python3 dircom.py
```

Or package with PyInstaller on the target operating system.

---

## 📂 Recommended Project Structure

```
dircom/
├── dircom.py
├── README.md
├── .gitignore
├── requirements.txt
├── setup.py
├── MANIFEST.in
├── LICENSE
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## 📦 Requirements

Ensure your `requirements.txt` contains:

```
pyserial>=3.5
```

---

## 📜 License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

---

## 📝 TODO

- [x] Fully test functionality on **Windows**  
- [ ] Test on **Linux** (various distributions)  
- [ ] Test on **macOS**  
- [ ] Add automated tests (e.g., pytest)  
- [ ] Build executables for Linux and macOS  
- [ ] Publish GitHub releases  

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or pull requests.

---

## 🔗 Author

**Nelson Almeida**  
[https://github.com/ncamilo](https://github.com/ncamilo)
