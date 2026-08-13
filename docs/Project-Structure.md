



bt-l2cap-fuzzer/
├── README.md              # what, why, scope, findings
├── .gitignore             # ignore compiled binary + Python cache
├── requirements.txt       # Python dependencies
├── docs/
│   └── methodology.md     # how the fuzzer works, mutation strategy
├── src/
│   ├── harness.py         # send loop + crash detection
│   │── sequencer.py       # strategy 2: valid packets, broken order  ← NEW
│   ├── mutators.py        # packet mutation strategies
│   ├── monitor.py         # alive-check between test cases
│   └── sender/
│       ├── sender.cpp     # high-throughput C++ sender
│       └── Makefile       # builds the sender binary
│── findings/
│── .gitkeep           # keeps the empty folder in Git
├── misc/
    └── mal_audio.py

Files:

README.md
.gitignore
requirements.txt
docs/methodology.md
src/harness.py
src/mutators.py
src/monitor.py
src/sender/sender.cpp
src/sender/Makefile
findings/.gitkeep
misc/mal_audio.py