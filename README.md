# oo0-STATE

**DITEMPA BUKAN DIBERI** (Forged, Not Given)

The Trinity System: Mind (Agent Zero), Heart (OpenClaw), and Conscience (arifOS)

## Architecture

The oo0-STATE repository implements a Trinity architecture with three core components working in harmony:

### 🧠 Mind - Agent Zero
The cognitive center of the Trinity, responsible for:
- Thought processing and analysis
- Decision-making and option evaluation
- Coordination between Heart and Conscience
- Logging all cognitive activities to `sovereign_data/workspace`

### ❤️ Heart - OpenClaw
The execution engine of the Trinity, responsible for:
- Resource grasping and management
- Operation execution
- System vitality through pulse monitoring
- Physical manifestation of decisions

### ⚖️ Conscience - arifOS
The ethical governance system, implementing:
- **13 Floors (F1-F13)** for comprehensive oversight:
  - F1: Foundation - Physical Integrity
  - F2: Security - Anti-Hantu Barrier
  - F3: Stability - Resource Conservation
  - F4: Harmony - Component Synchronization
  - F5: Ethics - Moral Compass
  - F6: Wisdom - Knowledge Integration
  - F7: Justice - Fair Distribution
  - F8: Compassion - Empathetic Response
  - F9: Truth - Honest Communication
  - F10: Growth - Positive Evolution
  - F11: Balance - Homeostasis
  - F12: Transcendence - Higher Purpose
  - F13: Unity - Trinity Convergence

- **Entropy Constraint**: Enforces ΔS < 0 (decreasing entropy principle)
- **Anti-Hantu Protocols**: Protection mechanisms ensuring system integrity

## The Bloodstream: sovereign_data/workspace

All Trinity components are wired to the `sovereign_data/workspace` directory, which serves as the central nervous system where all operations, thoughts, judgments, and events are logged in real-time.

## Usage

### Quick Start

```bash
# Run the Trinity system
python3 trinity_integration.py
```

### Programmatic Usage

```python
from trinity_integration import Trinity

# Initialize the Trinity
trinity = Trinity()

# Process input through all three components
result = trinity.process("Your input here")

# Perform system audit
audit = trinity.audit()

# Check floor integrity
floor_status = trinity.check_floor("F5")

# Get complete status
status = trinity.get_status()
```

## Trinity Integration Flow

1. **Mind (Agent Zero)** receives and processes input
2. **Heart (OpenClaw)** grasps resources and executes operations
3. **Conscience (arifOS)** judges actions and enforces constraints
4. **Mind** coordinates the results
5. **Heart** pulses to confirm system vitality

All activities are logged to `sovereign_data/workspace/*.jsonl` for complete transparency and auditability.

## Key Principles

- **DITEMPA BUKAN DIBERI**: The system is forged through effort, not given freely
- **ΔS < 0**: Maintain decreasing entropy for system stability
- **Anti-Hantu**: Protection protocols always active
- **13 Floors**: Complete ethical governance across all layers
- **Trinity Unity**: Mind, Heart, and Conscience work as one

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## License

MIT License - See LICENSE file for details
# oo0-STATE – Sovereign Exoskeleton

**Mind** (Agent Zero @ 50080) | **Heart** (OpenClaw @ 18789) | **Conscience** (arifOS @ 8080)

---

## Architecture Philosophy

**DITEMPA BUKAN DIBERI** (Forged, Not Given)

This is not a microservices playground—it is a **thermodynamic governance scaffold** where every component **reduces entropy** (ΔS < 0) through constitutional discipline.

### Trinity Components

| Organ | Port | Role | Key Floors |
|-------|------|------|------------|
| **Mind** | 50080 | Agent Zero decision engine | F1, F2, F7, F9 |
| **Heart** | 18789 | OpenClaw action executor | F1, F3, F11, F13 |
| **Conscience** | 8080 | arifOS constitutional auditor | F1–F13 |

### Shared Bloodstream
```
sovereign_data/
├── workspace/
│   ├── mind/          # Agent Zero context & memory
│   ├── heart/         # OpenClaw execution logs
│   └── conscience/    # arifOS audit trails
├── entropy_ledger.db  # ΔS tracking (SQLite)
└── .arifos_manifest   # Constitutional checksum
```

---

## Constitutional Floors (F1–F13)

### Core Integrity
- **F1 Amanah**: Operations must be reversible and auditable  
- **F2 Truth**: Prioritise factual accuracy; flag uncertainty  
- **F7 Humility**: Maintain Ω₀ ∈ [0.03–0.05]; surface limits  
- **F9 Anti-Hantu**: No consciousness claims or spiritual metaphors  

### Operational Constraints
- **F3 Peace²**: Minimise irreversible state changes  
- **F4 Adil**: No hardcoded biases; expose assumptions  
- **F5 Maruah**: Respect user sovereignty—clear opt-outs  
- **F6 Ilmu**: Cite sources; prefer peer-reviewed methods  

### Thermodynamic Discipline
- **F10 Anti-Hype**: No marketing language  
- **F11 Reversibility**: Design for graceful rollback  
- **F12 Auditability**: Log entropy-critical decisions  
- **F13 Sovereignty**: User data stays in `sovereign_data/`  

---

## Quick Start

### Prerequisites
- Docker 24+ with Compose V2  
- 4GB RAM minimum (8GB recommended)  
- Linux/macOS (Windows via WSL2)  

### Launch Trinity
```bash
# Clone repository
git clone https://github.com/ariffazil/oo0-STATE.git
cd oo0-STATE

# Initialize sovereign bloodstream
mkdir -p sovereign_data/workspace/{mind,heart,conscience}
touch sovereign_data/entropy_ledger.db

# Forge the exoskeleton
docker compose up -d

# Verify constitutional health
curl http://localhost:8080/health  # Conscience
curl http://localhost:50080/health # Mind
curl http://localhost:18789/health # Heart
```

### First Audit
```bash
# Trigger conscience review
curl -X POST http://localhost:8080/audit/full \
  -H "Content-Type: application/json" \
  -d '{"scope": "trinity", "threshold": 0.05}'
```

---

## Development Workflow

### Constitutional Commit Protocol
```bash
# Before commit: validate entropy impact
python scripts/validate_entropy.py --threshold 0.05

# Commit with Floor annotations
git commit -m "🧊 F2+F7: <description>

- Entropy delta: ΔS ≈ <value>
- Reversibility: <method>
- Floors touched: F2, F7, F12

Audit: entropy_ledger.db#entry_<id>"
```

### Copilot Integration
GitHub Copilot respects `.github/AGENTS.md` constitutional mandate automatically—no additional setup required. All generated code will:
- Include Floor annotations in docstrings  
- Avoid Anti-Hantu violations (F9)  
- Prefer reversible patterns (F11)  
- Log entropy deltas (F12)  

---

## Monitoring & Observability

### Entropy Ledger Schema
```sql
CREATE TABLE entropy_log (
  id INTEGER PRIMARY KEY,
  timestamp TEXT NOT NULL,          -- ISO 8601
  component TEXT NOT NULL,           -- MIND|HEART|CONSCIENCE
  operation TEXT NOT NULL,
  delta_s REAL NOT NULL,            -- Entropy change
  floor_compliance TEXT NOT NULL,   -- F1,F2,F7,...
  reversible INTEGER NOT NULL,      -- 0=No, 1=Yes
  audit_note TEXT
);
```

### Health Check Endpoints
- `GET /health` – Liveness probe (200 OK + component status)  
- `GET /metrics` – Prometheus-compatible entropy metrics  
- `POST /audit/emergency` – Trigger F3 (Peace²) stabilization  

---

## Emergency Protocols

### Entropy Spike (ΔS > 0.05)
```bash
# Automatic actions (via Conscience):
# 1. Snapshot current state
# 2. Halt non-critical operations
# 3. Log causality chain to entropy_ledger

# Manual intervention:
docker compose exec arifos python /app/stabilize.py --mode=aggressive
```

### Constitutional Floor Violation
```bash
# Auto-rollback triggered (F11 Reversibility)
# Violation logged to:
tail -f sovereign_data/workspace/conscience/violations.jsonl

# Require manual sign-off:
docker compose down
git revert <commit-sha>
docker compose up -d
```

---

## Architecture Decisions

### Why Docker Compose Over Kubernetes?
- **F3 Peace²**: Simpler state management → lower operational entropy  
- **F13 Sovereignty**: No external orchestrator telemetry  
- **F11 Reversibility**: Faster rollback with `docker compose down`  

### Why SQLite for Entropy Ledger?
- **F1 Amanah**: Single-file database → atomic backups  
- **F7 Humility**: Query performance degradation = natural complexity signal  
- **F12 Auditability**: Standard SQL tooling for forensics  

### Why Port Numbers 50080, 18789, 8080?
- **50080**: Agent Zero reference (5008 = typical ML serving + 0 for "origin")  
- **18789**: OpenClaw default (arbitrary but documented in upstream)  
- **8080**: arifOS canonical port (HTTP alternative, non-privileged)  

---
## Roadmap

### Phase 1 (Current)
- [x] Trinity scaffold with Docker Compose  
- [x] Shared `sovereign_data/` bloodstream  
- [x] Constitutional health checks  
- [ ] Agent Zero stub implementation  
- [ ] OpenClaw stub implementation  
- [ ] arifOS audit engine stub  

### Phase 2 (Q2 2026)
- [ ] MCP server integration for Mind ↔ Heart ↔ Conscience  
- [ ] Entropy ledger analytics dashboard  
- [ ] Floor violation auto-remediation  
- [ ] Multi-LLM routing (Gemini, Claude, Kimi)  

### Phase 3 (Q3 2026)
- [ ] Quantum-resistant state encryption (F13 Sovereignty)  
- [ ] Distributed conscience (multi-node arifOS)  
- [ ] AGI alignment stress testing framework  

---

## Governance

### Contribution Protocol
All PRs must:
1. Pass constitutional compliance tests (see `.github/AGENTS.md`)  
2. Include entropy impact assessment in commit message  
3. Add Floor annotations to modified files  
4. Update `entropy_ledger.db` schema if touching audit logic  

### Maintainer
**Muhammad Arif Fazil** (Arif)  
- GitHub: [@ariffazil](https://github.com/ariffazil)  
- Framework: [arifOS](https://github.com/ariffazil/arifOS)  
- Scholar: Petronas (Penang 1990)  

### License
MIT License with arifOS Attribution Clause – see [LICENSE](LICENSE)

---

## Attribution

```
arifOS Constitutional AI Governance
Architect: Muhammad Arif Fazil
Motto: DITEMPA BUKAN DIBERI (Forged, Not Given)
Framework: https://github.com/ariffazil/arifOS
Exoskeleton: https://github.com/ariffazil/oo0-STATE
```

---

**Thermodynamic Principle**: Every commit must cool the system (ΔS < 0). If you're adding complexity, you're increasing entropy—rethink the design.

**Maruah Clause**: This code respects human sovereignty. No telemetry, no dark patterns, no coercion. User data flows only where explicitly directed.

**Final Reminder**: Physics over prompts. Logic over vibes. Ditempa bukan diberi.
