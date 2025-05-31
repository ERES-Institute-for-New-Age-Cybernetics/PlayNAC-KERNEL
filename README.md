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
Configuration
application.yaml (under src/main/resources):

yaml
Copy
Edit
playnac:
  dqam:
    enabled: true
    minQuorum: 0.6
    maxQuorum: 0.9

earnedpath:
  apiVersion: v2.3
  baseUrl: https://api.earnedpath.example.org
  credentials:
    clientId: <YOUR_CLIENT_ID>
    clientSecret: <YOUR_CLIENT_SECRET>

huos:
  mfa:
    enabled: true
    methods: ["TOTP", "FAVORS"]

database:
  url: jdbc:postgresql://localhost:5432/playnac
  username: playnac
  password: <YOUR_DB_PASSWORD>
Flyway Migrations (automatically applied on boot):

V7_5__dqam_schema.sql

V7_5__earnedpath_v2_3_adapter.sql

Prometheus & Grafana (files in docs/monitoring/):

Copy playnac_prometheus_rules.yaml into your Prometheus rules/ folder.

Import Grafana dashboard JSONs (located under docs/monitoring/grafana_dashboards/) into Grafana to visualize key metrics.

Run & Validate
bash
Copy
Edit
docker-compose down
docker-compose up -d --build
Health Check (after ~2 minutes):

bash
Copy
Edit
curl http://localhost:8080/health
Expected response:

json
Copy
Edit
{
  "status": "UP",
  "services": {
    "dqam": "UP",
    "earnedpath": "UP",
    "prometheus": "UP"
  }
}
Bulk Token Sync Log:

pgsql
Copy
Edit
INFO [EarnedPathAdapterV2_3] - BulkTokenSync successful for 500 groups in 12.4 seconds.
CLI Tools
pnctl quest:preview [quest_id]
Description: Preview a quest’s full details before assignment.

Usage:

bash
Copy
Edit
pnctl quest:preview 3f9a5b21-8d4c-4e21-b3a1-053fcd2ace05
Output: JSON with fields:

epTokensAwarded

meritcoinAwarded

bercDelta

gerpForecastImpact

pnctl sla:simulate [sla_id] --durationHours=<integer>
Description: Dry‑run SLA performance over a specified number of hours.

Usage:

bash
Copy
Edit
pnctl sla:simulate 7e4b1c34-dd3a-4f60-9a2e-aa531c789b12 --durationHours=24
Output: JSON report including:

Projected quota usage

Penalties issued

BERC trajectory

API Endpoints
QuestService
Seed Quests

bash
Copy
Edit
POST /api/v7/quest/seed
Request Body:

json
Copy
Edit
{
  "regionId": "string",
  "seedDate": "YYYY-MM-DDTHH:MM:SSZ"
}
Response: List of seeded quests with estimated EP & Meritcoin rewards.

Complete Quest

bash
Copy
Edit
PUT /api/v7/quest/{questId}/complete
Response Body:

json
Copy
Edit
{
  "epTokensAwarded": 15,
  "meritcoinAwarded": 5,
  "bercDelta": 2.3,
  "gerpForecastImpact": {
    "waterStress": -0.12,
    "energyFlux": 0.05
  }
}
SLAService
Simulate SLA

bash
Copy
Edit
GET /api/v7/sla/{slaId}/simulate?durationHours=integer
Response Body:

json
Copy
Edit
{
  "projectedUsage": 12.4,
  "penalties": 3,
  "bercTrajectory": [78.4, 75.2, 72.6]
}
Adjust Quorum

bash
Copy
Edit
POST /api/v7/sla/{slaId}/adjustQuorum
Request Body:

json
Copy
Edit
{
  "proposedQuorum": 0.75,
  "reasonCode": "EMERGENCY",
  "initiatorId": "UUID"
}
Authorization: Requires HUOSRole.MODERATOR or above.
Response: 200 OK if successful, 403 Forbidden otherwise.

Testing & Quality Assurance
Unit Tests

Location: playnac-kernel/core/**/tests

Coverage: 89% (target ≥ 90%)

Key Test Suites:

QuorumPredictorServiceTest

MeritWeightedSeederTest

EarnedPathAdapterV2_3Test

Integration Tests

Location: playnac-kernel/adapters/earnedpath-v2-3/tests

Scenarios:

BulkTokenSync with 500 mock User‑GROUPs

Fallback to v2.1 on timeout

E2E Simulations

Location: playnac-kernel/simulation

Runs:

SOMT voting under high BERC volatility

Dust Storm Emergency with MRQS quest assignments

Security Audit

Auditor: Cybernite Security

Findings: Resolved low‑severity JWT rotation & input sanitization issues

Report: docs/security/Cybernite_Audit_v7.5.pdf

Configuration & Monitoring
Prometheus & Grafana
Prometheus Rules (docs/monitoring/playnac_prometheus_rules.yaml):

yaml
Copy
Edit
groups:
  - name: playnac-alerts
    rules:
      - alert: EarnedPathSyncError
        expr: earnedpath_sync_error_rate > 0.02
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "EarnedPath sync error rate exceeds 2%"
          description: "Check EarnedPathAdapterV2_3 connectivity"

      - alert: EventDispatchLatencyHigh
        expr: playnac_event_dispatch_latency > 0.2
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "Event dispatch latency > 200ms"
          description: "Possible node overload or network issues"
Grafana Dashboards (JSON exports in docs/monitoring/grafana_dashboards/):

SLA Performance Dashboard

BERC vs. EP Correlation Dashboard

DQAM Adjustment Frequency Dashboard

Contributing
Fork & Clone

bash
Copy
Edit
git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/PlayNAC-KERNEL.git
cd PlayNAC-KERNEL
Branching Strategy

Create feature branches off develop:

bash
Copy
Edit
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
Coding & Style Guidelines

Java code must follow Google Java Style (enforced by spotless-java).

Commit messages should follow Conventional Commits:

makefile
Copy
Edit
feat(core): add new DQAM threshold adjustment
fix(sla): correct oracle signature validation
docs: update README for v7.5 features
Writing Tests

Add unit tests under src/test/java corresponding to your module.

Run all tests locally before pushing:

bash
Copy
Edit
./gradlew test
Pull Request Workflow

Push your branch and open a PR targeting develop.

PR requirements:

At least one code review approval

Passing CI checks

No high‑severity security issues flagged

Documentation Updates

Update docs/ for any new features, API changes, or configuration steps.

Append to docs/releases/v7.x.md if the change constitutes a micro‑release.

License
This repository is licensed under the Apache 2.0 License. See LICENSE for details.

Acknowledgments
Lead Engineers (v7.5): Ananya Patel, Ricardo Morales, DeShawn Reed

Sociocratic Facilitator: Dr. Hélène DuBois

Security Audit: Cybernite Security (Jacob Lin)

EarnedPath Integration: Feng Zhao, Maria Oliveira

Documentation & Tutorials: Leila Hassan, Tenji Matsuda

Community Pilots: Nara‑Ti Council, Oasis Delta Hub

For detailed release notes, see docs/releases/v7.5.md. If you encounter issues, please open an issue or contact the PlayNAC core team via the SOMT portal.

Copy
Edit
