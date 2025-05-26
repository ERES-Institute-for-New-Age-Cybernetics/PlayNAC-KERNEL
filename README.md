ERES PlayNAC “KERNEL” Codebase (v6.2)

Empirical Realtime Education System × New Age Cybernetic Game Theory

The PlayNAC "KERNEL" is the core engine powering:

EarnedPath (EP): Merit‑based learning and progression

GiantERP (GERP): Planetary resource planning

Bio‑Energetic Economy (BEE): EEG‑driven proof‑of‑work

BERC: Bio‑Electric Ratings consensus

Media Processor: Real‑time adaptive media styling

HFVN (Mandala-VERTECA): Hands‑free voice & gesture navigation

Persistence & Ingestion: On‑disk chain storage, context, and external content sync

This README covers setup, structure, and usage of the PlayNAC v6.2 skeleton.

📂 Repository Structure

src/
├── kernel/
│   ├── config.py           # ConfigManager loads .env files
│   ├── models.py           # Block data classes
│   ├── storage.py          # SQLite-backed Storage
│   ├── context_manager.py  # Session state manager
│   └── playnac_kernel.py   # Core orchestrator, mining loop
├── earnedpath/             # Simulation engine, EP graph, merit calc
├── gianterp/               # GiantERP client & models
├── bee/                    # AuraScanner & BioPoW algorithms
├── berc/                   # JASConsensus, MediaTask, JASLink
├── media/                  # MediaProcessor and filter pipeline
├── nav/                    # ASR/TTS, IntentParser, HFVN, MandalaTranslator
└── utils/                  # Helpers: ingestion stubs, retry/cache

tests/
└── *.py                    # pytest suite for core components

.env                        # Example environment variables
CHANGELOG.md                # Version history
LICENSE                     # CC BY‑NC‑SA 4.0


⚙️ Installation

Clone and enter:

git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
cd PlayNAC-KERNEL

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt

Configure environment:
Copy .env.example to .env and set values:

WEB3_RPC_URL=https://your-node
BEE_SECRET_KEY=your-secret
DB_PATH=playnac.db

Run tests:

pytest tests/ --maxfail=1 --disable-warnings -q

🚀 Quickstart Demo

export DB_PATH=playnac.db
python -m src.kernel.playnac_kernel

This will:

Load persisted chain (if any).

Submit a sample MediaTask.

Mine a block (BioPoW + media processing).

Persist and print block summary.

🔧 Configuration

Variable

Description

Example

WEB3_RPC_URL

Blockchain node for GCF interactions

https://gracechain-node.example

BEE_SECRET_KEY

Secret key for BioPoW entropy calibration

abc123

DB_PATH

SQLite database file for block storage

/data/playnac.db

📐 Architecture Overview

ConfigManager — loads multiple .env files, validates keys.

Storage — SQLite schema for blocks table; save_block & load_blocks API.

PlayNACKernel —

Initializes engines (BioPoW, SimulationEngine, MediaProcessor, JASConsensus)

Loads persisted blocks and rebuilds chain

Exposes submit_media_task() and mine_block() with adaptive difficulty

Persists new blocks and links consensus graph

ContextManager — session‑scoped state for HowWay queries.

Ingestion stubs — external content sync for ResearchGate, Medium, GitHub.

Refer to docs/architecture/ for UML and sequence diagrams.

🧪 Testing & CI

pytest: Core unit/integration tests under tests/ (coverage ≥ 90%).

GitHub Actions: runs lint (flake8), type‑check (mypy), pytest, bandit security scan.

Add new tests as you extend modules:

pytest tests/YourNewModule_test.py

📝 Contributing

Fork the repo → git checkout -b feature/YourFeature

Implement with type hints, docstrings, and tests

Submit PR to main branch

CI will validate and merge after review

Please follow our CONTRIBUTING.md guidelines.

📜 License

This code is released under the Creative Commons BY‑NC‑SA 4.0 license.
See LICENSE for details.
