[![Build Status](https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL/actions/workflows/ci.yml/badge.svg)](https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL/actions)
[![Version](https://img.shields.io/badge/version-v7.4-blue.svg)](https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL/releases/tag/v7.4)
[![License](https://img.shields.io/badge/license-BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

# ERES PlayNAC VERTECA “KERNEL” Codebase v7.4

**Human Operating System (HUOS) 4D VR/AR Environment**
*Part of the ERES Institute for New Age Cybernetics ecosystem.*

Live repository: [https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL](https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL)

---

## 🚀 Overview

PlayNAC “KERNEL” v7.4 extends the base framework with:

* **HUOS Module:** Core 4D VR/AR services for immersive experiences.
* **VERTECA Integration:** Spatial gesture mapping and WebXR support.
* **Green‑Box Simulator:** Enhanced rendering, spatial audio, dynamic zones.
* **Multi‑User Orchestration:** Real‑time sessions with EP & GERP overlays.
* **Containerized Deployment:** Docker Compose & Helm charts updated for VR.
* **Updated Docs & Diagrams:** Sphinx autodocs, architecture diagrams for HUOS.

This release powers smart‑city user‑group dashboards in a VR/AR setting, enabling real‑time decision intelligence in a fully immersive environment.

---

## 🎯 Features in v7.4

1. **HUOS Module** (`src/huos/`)

   * `HUOSKernel`: Lifecycle & command routing.
   * `SpatialSceneManager`: Zone & scene definitions.
   * `UserGroupCoordinator`: Session management for multiple users.

2. **VERTECA VR/AR Adapters** (`src/nav/mandala_translator.py`)

   * Gesture‑to‑command translation.
   * Unity/Three.js demo hooks in `examples/vr_ar/`.

3. **Green‑Box Simulator** (`src/huos/render/`)

   * Rendering pipelines for WebXR & native engines.
   * Spatial audio integration and dynamic highlights.

4. **User‑Group Orchestration** (`src/kernel/context_manager.py`)

   * `UserGroupSession` abstraction for synchronized VR sessions.
   * Real‑time EP node and GERP forecast overlays.

5. **Deployment & Configuration**

   * `deploy/docker-compose.yml`: Adds `huos-service` & WebSocket gateway.
   * `deploy/helm/huos/`: Ingress rules & AR device API secrets.

6. **Documentation & Testing**

   * `docs/architecture/huos/`: Component & sequence diagrams.
   * Sphinx autodoc entries for `src/huos/`.
   * CI workflow updated to include `tests/huos/`.

---

## 📂 Directory Structure

```text
.
├── src/
│   ├── kernel/              # Core orchestrator & context manager
│   ├── huos/                # HUOS 4D VR/AR module
│   ├── nav/                 # Gesture translation adapters
│   ├── vacationomics/       # Business logic engines
│   └── ...
├── examples/vr_ar/          # Green‑Box VR/AR demo project
├── docs/architecture/huos/   # HUOS diagrams & docs
├── deploy/
│   ├── docker-compose.yml   # VR container orchestration
│   └── helm/huos/           # Helm charts for VR deployment
├── tests/huos/              # HUOS unit and integration tests
└── .github/workflows/ci.yml # CI pipeline including HUOS tests
```

---

## 🛠️ Getting Started

1. **Clone & Install**

   ```bash
   git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
   cd PlayNAC-KERNEL
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**

   ```bash
   cp .env.example .env
   # Edit .env:
   HUOS_API_KEY=your_vr_api_key
   HUOS_WS_ENDPOINT=ws://localhost:8080/huos
   ```

3. **Launch Services & Demo**

   ```bash
   docker-compose up --build
   python src/kernel/playnac_kernel.py --enable-huos
   ```

   * Open `examples/vr_ar/index.html` in a WebXR-compatible browser.

---

## 📖 Documentation & Contribution

* **Read the Docs**: `make docs` to generate HTML API docs (including HUOS).
* **Run Tests**: `pytest tests/huos/`
* **Contribute**: Fork ➔ `feature/v7.4-huos` ➔ PR

---

## 📜 License

This project is licensed under Creative Commons BY‑NC‑SA 4.0. See [LICENSE](LICENSE) for details.
