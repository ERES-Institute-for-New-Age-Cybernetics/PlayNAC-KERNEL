# PlayNAC KERNEL

**Version:** v1.7 (Last updated: 2025-06-08)

The **PlayNAC KERNEL** is the core cybernetic game-theory engine of the ERES Institute’s New Age Cybernetics framework. It provides the computational substrate for simulation, decision support, and real-time feedback across integrated systems such as EarnedPath, GERP, BERC, and related modules.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Concepts & Acronyms](#key-concepts--acronyms)
3. [Features](#features)
4. [Architecture](#architecture)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Directory Structure](#directory-structure)
8. [Development & Contribution](#development--contribution)
9. [License](#license)
10. [Contact & Support](#contact--support)

---

## Project Overview

PlayNAC KERNEL is designed to model socio-economic and ecological processes using an adaptive, non-punitive remediation game-theory approach. It underpins applications such as:

* **EarnedPath (EP):** Tokenized ledger for individual and community contributions
* **GiantERP (GERP):** Global resource planning and allocation
* **Bio-Electric Ratings Codex (BERC):** Real-time ecological and health metrics
* **Vacationomics:** Incentive-driven time-allocation for well-being and productivity

This engine ingests multidimensional metadata, runs iterative simulation cycles, and outputs heuristic scores and policy recommendations.

---

## Key Concepts & Acronyms

| Acronym | Definition                                            |
| ------- | ----------------------------------------------------- |
| EP      | EarnedPath – Contribution tracking token system       |
| GERP    | GiantERP – Earth Resource Planner                     |
| BERC    | Bio-Electric Ratings Codex                            |
| UBIMIA  | Universal Basic Income + Merit × Investments ± Awards |
| THOW    | Tiny Homes On Wheels                                  |
| FDRV    | Fly & Dive RV (Spaceship Futures)                     |
| HFVN    | Hands-Free Voice Navigation                           |
| GSSG    | Green Solar-Sand Glass                                |
| CARE    | Constant @EP #ERES ^GERP \*Vacationomic %Manage       |
| SOMT    | Sociocratic Overlay Metadata Tapestry                 |
| NAC     | New Age Cybernetics                                   |

---

## Features

* **Modular Simulation Engine**: Encapsulate custom rulesets and game-theory logic
* **Real-Time Feedback**: Adaptive AI loops with transparency and equity credits
* **Multi-Layer Data Ingestion**: Support for biometric (BEST), environmental, and social metrics
* **Blockchain Integration**: Tokenization via EarnedPath and Meritcoin
* **Extensible API**: Python and REST endpoints for integration with third‑party systems

---

## Architecture

```
[Input] → [Data Layer: JSON / Blockchain] → [Simulation Engine: PlayNAC KERNEL] → [AI Feedback Module] → [Output: Dashboard / API]
```

1. **Data Layer**: Collates EP transactions, BERC sensor feeds, GERP resource logs
2. **Kernel Core**: Executes iterative play cycles, scoring heuristics, and collision-avoidance math
3. **AI Feedback**: Applies adaptive weighting (Λ·Φ) and policy penalty functions (Γ·C\_t)
4. **Output Services**: Provides REST API and Python SDK for dashboards, reports, and real‑time control

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
   cd PlayNAC-KERNEL
   ```
2. Create a virtual environment (Python 3.10+ recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Set environment variables for blockchain endpoints and API keys.

---

## Usage

### Running Simulations

```bash
python run_simulation.py --config configs/default.yaml
```

### Python SDK

```python
from playnac import Kernel
kernel = Kernel(config="configs/default.yaml")
results = kernel.run_cycle()
print(results.summary())
```

### REST API

Start the API server:

```bash
uvicorn api:app --reload
```

Access endpoints:

* `GET /status` – Kernel health
* `POST /simulate` – Run a simulation cycle
* `GET /results` – Fetch latest scores and metrics

---

## Directory Structure

```
PlayNAC-KERNEL/
├── api/                   # REST API implementation
├── configs/               # YAML configuration files
├── docs/                  # Design docs and whitepapers
├── playnac/               # Core kernel package
│   ├── engine.py
│   ├── feedback.py
│   └── utils.py
├── scripts/               # Utility and maintenance scripts
├── tests/                 # Unit and integration tests
├── requirements.txt       # Python dependencies
├── run_simulation.py      # Main entry point for simulations
└── README.md              # (This file)
```

---

## Development & Contribution

We welcome contributions to enhance simulation rules, add new modules, and improve performance:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/awesome-update`
3. Implement your changes and add tests.
4. Run tests:

   ```bash
   pytest --cov=playnac
   ```
5. Commit and push, then open a pull request.

Please adhere to our [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contact & Support

* **Issues & Bugs**: [https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL/issues](https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL/issues)
* **Discussion Forum**: [https://forum.eresinstitute.org](https://forum.eresinstitute.org)
* **Lead Maintainer**: Joseph A. Sprute ([eresmaestro@gmail.com](mailto:eresmaestro@gmail.com))

Thank you for engaging with the PlayNAC KERNEL—driving the future of New Age Cybernetics!
