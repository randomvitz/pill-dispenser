pill‑dispenser/
├── README.md                    # high‑level overview & setup
├── docs/                        # design notes, wiring diagrams, API docs
│   └── wiring.md
├── src/                         # all application code
│   ├── __init__.py
│   ├── main.py                  # entry point, esbootstraps servic
│   ├── config.py                # loads/saves user settings & schedules
│   ├── hardware/                # low‑level drivers
│   │   ├── __init__.py
│   │   ├── pwm_servo.py         # abstraction for 6‑module controller
│   │   ├── water_pump.py        # continuous‑servo controller
│   │   └── screen.py            # display/touch interface
│   ├── gui/                     # GUI screens, widgets, event loop
│   │   ├── __init__.py
│   │   ├── screens.py
│   │   └── widgets.py
│   ├── scheduler/               # timer and dispensing logic
│   │   ├── __init__.py
│   │   ├── timer.py             # background timer service
│   │   └── dispenser.py         # coordinates motors/pump per schedule
│   └── utils/                   # helpers, logging, error handling
│       ├── __init__.py
│       └── logger.py
├── tests/                       # unit/integration tests
│   ├── test_config.py
│   ├── test_scheduler.py
│   └── test_hardware_mock.py
├── requirements.txt             # Python dependencies (e.g. RPi.GPIO, pygame)
├── scripts/                     # deployment/build helpers
│   └── install.sh
└── .gitignore