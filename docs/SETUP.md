# Setup & Running

---
## Requirements

**Operating system:** Linux (the raw Bluetooth sockets this relies on are Linux-only — `libbluetooth` / BlueZ). Windows and macOS are not supported for the send path.

**Hardware:**

- A Bluetooth adapter (onboard or a USB dongle) - CSR8510 USB Bluetooth adapter
- A target device **you own** — see the scope statement in the README

**Software:**

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.x | Fuzzing logic, orchestration |
| g++ | C++20 capable | Compiles the high-throughput sender |
| BlueZ | system default | Linux Bluetooth stack |

---

## Install dependencies

**System packages (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install bluetooth bluez bluez-tools python3-dev libbluetooth-dev g++
```

**Python packages:**

```bash
pip install -r requirements.txt
```

---

## Build the C++ sender

The sender is compiled separately, once (rebuild it whenever `sender.cpp` changes):

```bash
cd src/sender
make
```

This produces the sender binary that the Python harness calls for flood tests.

---

## Run the fuzzer

From the project root:

```bash
python src/harness.py
```

Raw Bluetooth sockets need elevated privileges, so if you hit a permissions error, run with `sudo` — or grant the capability once so you don't need sudo each time:

```bash
sudo setcap 'cap_net_raw,cap_net_admin+eip' $(which python3)
```



---

## Troubleshooting

| Symptom | Likely cause |
|---------|--------------|
| `Permission denied` on the socket | Needs `sudo` or the `setcap` capability above |
| `No such device` | Bluetooth adapter not found — check `hciconfig` |
| Sender binary not found | Run `make` in `src/sender` first |
| Target not responding at baseline | Pair/connect the device before testing |