# bt-l2cap-fuzzer

A Python and C++ Bluetooth L2CAP fuzzer for security research — built to find denial-of-service conditions in consumer Bluetooth firmware.

> **Scope:** for use on devices the operator owns or is explicitly authorised to test. Sending disruptive traffic to any other device is likely an offence under laws such as the UK Computer Misuse Act 1990 and the US CFAA (18 U.S.C. § 1030).

---

## Why two languages

The interesting part of this project is the split, so it's worth stating plainly:

- **Python** drives the research logic — mutation strategies, liveness checking, logging, orchestration. A research tool has to be auditable, and Python keeps the methodology readable.
- **C++** takes over for high-throughput sending via raw sockets, where Scapy's overhead becomes the bottleneck under flood conditions.

The point isn't "used two languages" — it's knowing *where* the handoff belongs and *why*: Python for expressiveness, C++ when throughput is the variable under test.

---

## Approach

The full write-up lives in [docs/methodology.md](docs/methodology.md). The short version: baseline the target's normal behaviour, send mutated traffic, check responsiveness after each case, and on failure capture the input and confirm it reproduces. Where a failure is reproducible, the aim is to trace it back to the relevant stack code and understand the root cause.


---

## Setup

Linux, Python 3, and a g++ toolchain (C++20). Build dependencies:

```bash
sudo apt install bluetooth bluez bluez-tools python3-dev libbluetooth-dev g++
```

---

## Structure

```
bt-l2cap-fuzzer/
├── src/
│   ├── harness.py        # send loop and crash detection
│   ├── mutators.py       # mutation strategies
│   ├── monitor.py        # liveness check between cases
│   └── sender/           # high-throughput C++ sender
├── docs/methodology.md   # how and why it works
└── findings/             # write-ups (repro + analysis)
```

The Python harness calls the compiled C++ sender as a subprocess for flood tests, keeping the layers separate.

---

## Findings

| ID | Description | Status |
|----|-------------|--------|
| — | No findings published yet | In progress |

---

## References

- [BlueZ source](https://git.kernel.org/pub/scm/bluetooth/bluez.git)
- [Scapy Bluetooth layer](https://scapy.readthedocs.io/en/latest/layers/bluetooth.html)
- Background reading: KNOB (CVE-2019-9506), BLUFFS (CVE-2023-24023)
- https://github.com/ArmisSecurity/blueborne
- https://francozappa.github.io/publication/2023/bluffs/
- https://knobattack.com/