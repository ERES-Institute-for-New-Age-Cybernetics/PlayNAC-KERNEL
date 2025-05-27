# PlayNAC “KERNEL” Codebase

**Empirical Realtime Education System × Human‑Centered Skill Development Platform**

## Overview

PlayNAC “KERNEL” is the orchestration layer for the ERES Institute’s New Age Cybernetics ecosystem. It powers multi‑modal ingestion, context‑aware Q\&A, time‑budget simulations (Vacationomics), and integrations with EarnedPath, GiantERP, BERC, and more.

This repository provides:

* **Pluggable adapters** for content ingestion (ResearchGate, Medium, GitHub)
* **Stateful context management** across user sessions
* **Vacationomics engine** to simulate UBI vs. merit time‑budget tradeoffs
* **Resilient error handling**, observability, and structured logging
* **CI/CD pipelines** for quality gates, testing, and coverage
* **Docker & Kubernetes** deployment scaffolding

## Key Features (v7.3)

1. **Ingestion & Sync**

   * Real OAuth clients for ResearchGate, Medium, GitHub
   * Rate‑limit handling, retry logic, response caching
2. **Context Manager**

   * Session/user‑scoped state store in `src/kernel/context_manager.py`
   * Supports multi‑turn intent chaining and EP node linkage
3. **Vacationomics Engine**

   * `src/vacationomics/simulation.py` for time‑budget and GCF tradeoff calculations
   * Configurable α/β parameters for the Graceful Contribution Formula
4. **Error Handling & Observability**

   * Domain‑specific exceptions in `src/utils/exceptions.py`
   * Structured logging with request/session IDs (`src/utils/logger.py`)
   * Prometheus‑compatible metrics stub (`src/utils/metrics.py`)
5. **Tests & CI/CD**

   * Unit tests for ingestion & vacationomics modules
   * GitHub Actions workflow: linting, type‑checking (mypy), pytest, security scan (Bandit), coverage badges
6. **Type Safety & Documentation**

   * Full Python type hints across modules
   * Sphinx autodoc setup in `docs/` with Google‑style docstrings
   * Architecture diagrams in `docs/architecture/`
7. **Configuration & Deployment**

   * Docker Compose for local orchestration
   * Helm chart skeleton in `deploy/helm/` for Kubernetes
8. **Real‑World Integrations**

   * AuraScanner adapters (Muse/OpenBCI) in `src/bee/`
   * Three.js stub in `examples/greenbox/`
   * ASR/TTS adapters (Google, Azure, Whisper) in `src/nav/`
9. **Performance & Scalability**

   * Async I/O with `asyncio` in ingestion and GERP modules
   * Batching & caching via `aiocache`/Redis
   * Benchmark scripts in `bench/` measuring simulation latency

## Getting Started

### Prerequisites

* Python 3.10+
* Docker & Docker Compose
* (Optional) Access tokens for ResearchGate, Medium, GitHub

### Installation

```bash
git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
cd PlayNAC-KERNEL
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and fill in:

```ini
RESEARCHGATE_TOKEN=\<your-token\>
MEDIUM_TOKEN=\<your-token\>
GITHUB_TOKEN=\<your-token\>
REDIS_URL=redis://localhost:6379/0
GCF_ALPHA=10
GCF_BETA=0.1
```

### Running Locally

```bash
docker-compose up --build
```

The Kernel API will be available at `http://localhost:8000`.

### Running Tests & Coverage

```bash
pytest --cov=src
```

## Architecture

![Architecture Diagram](docs/architecture/playnac-kernel-overview.png)

## Directory Structure

```
.
├── src/
│   ├── kernel/
│   │   ├── config.py
│   │   ├── context_manager.py
│   │   └── playnac_kernel.py
│   ├── utils/
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   ├── metrics.py
│   │   └── ingestion/
│   │       ├── researchgate.py
│   │       ├── medium.py
│   │       └── github_sync.py
│   ├── vacationomics/
│   │   └── simulation.py
│   ├── bee/
│   ├── berc/
│   ├── nav/
│   └── ...
├── tests/
│   ├── ingestion/
│   ├── vacationomics/
│   └── kernel/
├── docs/
│   ├── architecture/
│   └── api/
├── deploy/
│   ├── docker-compose.yml
│   └── helm/
├── bench/
├── examples/
│   └── greenbox/
└── .github/
    └── workflows/ci.yml
```

## Contributing

We welcome contributions! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -m 'Add foo feature'`)
4. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the [MIT License](LICENSE).
