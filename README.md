# ERES PlayNAC KERNEL

**New Age Cybernetic Game Theory Core**  
**Version 7.5** · _Last updated: May 31, 2025_

---

## Table of Contents

1. [Overview](#overview)  
2. [Core Concepts](#core-concepts)  
   - [PlayNAC KERNEL](#playnac-kernel)  
   - [EarnedPath Integration](#earnedpath-integration)  
   - [Sociocratic Metadata (SOMT)](#sociocratic-metadata-somt)  
   - [BERC & GERP Connectivity](#berc--gerp-connectivity)  
3. [Features](#features)  
4. [Architecture & Modules](#architecture--modules)  
   - [Kernel Core](#kernel-core)  
   - [DQAM (Dynamic Quorum Adjustment Module)](#dqam-dynamic-quorum-adjustment-module)  
   - [MRQS (Merit‑Weighted Randomized Quest Seeder)](#mrqs-merit‑weighted-randomized-quest-seeder)  
   - [EarnedPath v2.3 Adapter](#earnedpath-v23-adapter)  
5. [Getting Started](#getting-started)  
   1. [Prerequisites](#prerequisites)  
   2. [Clone & Build](#clone--build)  
   3. [Configuration](#configuration)  
   4. [Run & Validate](#run--validate)  
6. [CLI Tools](#cli-tools)  
   - `pnctl quest:preview`  
   - `pnctl sla:simulate`  
7. [API Endpoints](#api-endpoints)  
   - QuestService  
   - SLAService  
8. [Testing & Quality Assurance](#testing--quality-assurance)  
9. [Configuration & Monitoring](#configuration--monitoring)  
   - Prometheus & Grafana  
10. [Contributing](#contributing)  
11. [License](#license)  
12. [Acknowledgments](#acknowledgments)  

---

## Overview

The **ERES PlayNAC KERNEL** is the simulation core of the ERES Institute’s New Age Cybernetic Game Theory framework. It enables real‑time, merit‑driven resource allocation, policy voting, and automated governance across multiple scales—from individual households to planetary and celestial initiatives. PlayNAC KERNEL interfaces seamlessly with:

- **EarnedPath (v2.3)** – Lifelong learning, credentialing, and EP token management  
- **BERC** (Bio‑Ecologic Ratings Codex) – Continuous environmental impact scoring  
- **GERP** (Global Earth Resource Planning) – Spatial resource forecasting  
- **GAIA** (Global Actuary Investor Authority) – Actuarial oversight of resource SLAs  

By combining sociocratic decision workflows (SOMT) with automated smart‑contract triggers, PlayNAC KERNEL ensures that every action—whether a community “quest” or an individual credential issuance—is recorded, scored, and tied to incentive mechanisms (EP tokens, Meritcoin, UBIMIA).

---

## Core Concepts

### PlayNAC KERNEL

A modular, event‑driven engine that seeds, assigns, and resolves community “quests” (tasks) aligned with ecological and social objectives. It measures participation via EP tokens and Meritcoin, adjusting resource flows and policy proposals in real time.

### EarnedPath Integration

PlayNAC KERNEL incorporates the **EarnedPath v2.3 API** to synchronize token balances, issue credentials, and trigger quests based on skill certifications. The `BulkTokenSync` endpoint dramatically reduces network overhead for large‑scale EP updates.

### Sociocratic Metadata (SOMT)

Decision‑making is conducted via SOMT’s consent‑by‑consent model. PlayNAC KERNEL provides interactive consoles for leaders to propose, discuss, and ratify SLAs, policies, and resource reallocation—automatically adjusting quorums (DQAM) in response to BERC fluctuations.

### BERC & GERP Connectivity

- **BERC**: Continuously updated environmental scores feed into quest prioritization and SLA adjustments. If BERC for a region drops below threshold, PlayNAC may auto‑spawn a “remediation” quest.  
- **GERP**: Live spatial forecasts (water, energy, migration) integrate into SLA simulations and quest impact projections. PlayNAC events update GERP’s global resource models to reflect real‑time actions.

---

## Features

- **Dynamic Quorum Adjustment (DQAM)**  
  – Predictive quorum recalibration based on real‑time vote history and BERC/EP metrics.  

- **Merit‑Weighted Randomized Quest Seeder (MRQS)**  
  – Probabilistic quest assignment balancing under‑served communities with historical EP engagement.  

- **EarnedPath v2.3 Adapter**  
  – `BulkTokenSync` for up to 1,000 User‑GROUPs per request; `CredentialWatcher` triggers PlayNAC events.  

- **Asynchronous Event Bus (Akka Streams)**  
  – Low‑latency intra‑node communication; average notification latency reduced to ~45 ms under load.  

- **HUOS Identity & MFA**  
  – TOTP + FAVORS biometric checks guard elevated operations (e.g., SLA approval).  

- **Smart‑Contract Hook Validation**  
  – Cryptographic signature checks for SLA updates; whitelist via GAIA before accepting new oracles.  

- **CLI Tooling (`pnctl`)**  
  – `quest:preview` and `sla:simulate` subcommands for pre‑deployment validation and dry‑run testing.  

- **Built‑in Monitoring & Metrics**  
  – Prometheus/Grafana dashboards for event latency, EP sync error rates, and quorum adjustment frequency.  

- **Upgradeable Contract Proxy Pattern**  
  – On‑chain logic can be upgraded (e.g., `SLA_v1` → `SLA_v2`) without losing state, following SOMT‑approved proposals.  

---

## Architecture & Modules

### Kernel Core

- **Event Bus** (`playnac-kernel/core/event`)  
  – Actor‑based, asynchronous message routing.  

- **Quest Engine V2** (`playnac-kernel/core/quest`)  
  – Handles quest definitions, assignment logic, completion workflows, and reward distribution.  

- **SLA Engine** (`playnac-kernel/core/sla`)  
  – Encodes user‑group SLA logic, oracle integrations, and automated enforcement.  

- **Oracles** (`playnac-kernel/core/oracles`)  
  – Interfaces for WaterSensor, BERC, GSSG, and custom smart‑contract event feeds.

### DQAM (Dynamic Quorum Adjustment Module)

- **Location:** `playnac-kernel/core/dqam`  
- **Components:**  
  - `QuorumPredictorService`  
  - `QuorumAdjustmentEvent`  
  - Configuration for `minQuorum`, `maxQuorum`, and volatility thresholds.

### MRQS (Merit‑Weighted Randomized Quest Seeder)

- **Location:** `playnac-kernel/core/mrqs`  
- **Components:**  
  - `MeritWeightCalculator`  
  - `QuestSeederService`  
  - Sampling algorithms to seed daily quests across regions.

### EarnedPath v2.3 Adapter

- **Location:** `playnac-kernel/adapters/earnedpath-v2-3`  
- **Components:**  
  - `EarnedPathAdapterV2_3`  
  - `BulkTokenSync` integration  
  - `CredentialWatcher` to auto‑trigger quests.  
- **Fallback:** v2.1 compatibility with retry logic (up to 5 minutes).

---

## Getting Started

### Prerequisites

- **Java 17 (OpenJDK)** or later  
- **Gradle 7.x** (wrapper included)  
- **PostgreSQL 13+** (for `quest_assignments`, `vote_records`, `sla_states` tables)  
- **Docker & Docker Compose** (for local orchestration)  
- **EarnedPath v2.3 Credentials** (clientId, clientSecret)  
- **HUOS MFA Setup** (TOTP + FAVORS biometric module)

### Clone & Build

```bash
git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
cd PlayNAC-KERNEL
./gradlew clean build -x test
