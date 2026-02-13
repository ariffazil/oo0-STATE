# MEMORY.md — Context7 Foundation

**Location:** `openclaw/MEMORY.md` in oo0-STATE  
**Purpose:** Canonical spec for arifOS memory architecture in OpenClaw  
**Version:** 1.0.0  
**Date:** 2026-02-13  
**Ω₀:** 0.04

---

## Overview

arifOS implements **Context7** in OpenClaw through a layered memory architecture:

- **7 stacked sources** of context before first reply
- **Temporal layers** (eternal → past → now → future)
- **QMD/SQLite** semantic search for retrieval
- **Per-agent** memory specialization

**Context7 = Identity + Memory + Skills + Tools + History + Context + State**

---

## The Seven Stacked Sources

At session boot, each agent loads:

| # | Source | File/Location | Temporal | Content |
|---|--------|---------------|----------|---------|
| 1 | **Soul** | `SOUL.md` | Eternal | Philosophy, 13 Floors, motto |
| 2 | **Identity** | `IDENTITY.md` | Eternal | Name, presentation, theme |
| 3 | **User** | `USER.md` | Eternal | Arif's profile, 888 Judge authority |
| 4 | **Agent Memory** | `MEMORY.md` (per agent) | Semi-static | Role-specific knowledge |
| 5 | **QMD Index** | SQLite vector DB | Past→Now | Semantic search over all notes |
| 6 | **Skills** | `~/.openclaw/skills/` | Now | Available capabilities |
| 7 | **Session State** | Runtime memory | Now | Current context, variables |

**Result:** Agent responds with full context stack loaded.

---

## Temporal Memory Layers

### 1. Eternal Layer (Immutable)

**Location:** `SOUL.md`, `IDENTITY.md`, `USER.md`, `/root/VAULT999/arifos/`

**Content:**
- arifOS constitution (13 Floors)
- Apex-theory equations (Φ_AGI, κᵣ, Ψ_LE)
- Core identity: "Ditempa Bukan Diberi"
- User context: Arif as PETRONAS geoscientist, 888 Judge

**Access:** Read-only, all agents
**Modification:** Only by 888 Judge (Arif) directly

### 2. Past Layer (Decisions & History)

**Location:** `/root/VAULT999/decisions/`, `/root/VAULT999/sessions/`

**Content:**
- Past verdicts (SEAL/SABAR/VOID records)
- Decision rationales and floor checks
- Session archives (YYYY-MM-DD folders)
- Telemetry history (ΔS, Peace² trends)

**Structure:**
```
/root/VAULT999/
├── decisions/
│   ├── 2026-02-13-seal-railway-token.md
│   ├── 2026-02-12-void-risky-deployment.md
│   └── ...
└── sessions/
    ├── 2026-02-13/
    │   ├── architect-001.md
    │   ├── actor-001.md
    │   └── auditor-001.md
    └── ...
```

**Access:** Read: All agents. Write: Auditor (verdicts), automatic (sessions)

### 3. Now Layer (Working Context)

**Location:** `/srv/arifos/memory/`, agent workspaces

**Content:**
- Current task context
- In-progress plans
- Working notes
- Ephemeral data

**Per-Agent Working Memory:**
| Agent | Location | Focus |
|-------|----------|-------|
| Architect (Δ) | `/srv/arifos/memory/architect/` | Design patterns, constraints |
| Actor (Ω) | `/srv/arifos/memory/actor/` | Runbooks, staging paths |
| Auditor (Ψ) | `/srv/arifos/memory/auditor/` | Checklists, risk patterns |

**Access:** Agent-specific write, others read-only

### 4. Pre-Future Layer (Staging)

**Location:** `/srv/repos/staging/`

**Content:**
- Experiments before SEAL
- Pre-production code
- Test data
- Rollback checkpoints

**Lifecycle:**
```
Architect designs → Actor implements in staging → Auditor verifies
                                    ↓
                              SEAL approved
                                    ↓
                            Promote to production
                                    ↓
                           Archive to VAULT999
```

**Access:** Actor (write), Auditor (read), Architect (read)

---

## Semantic Layer (QMD)

**Technology:** QMD (Queryable Markdown) + SQLite vector index

**Configuration (openclaw.json):**
```json
{
  "memory": {
    "backend": "qmd",
    "qmd": {
      "paths": [
        {
          "name": "vault",
          "path": "/root/VAULT999",
          "pattern": "**/*.md"
        },
        {
          "name": "working",
          "path": "/srv/arifos/memory",
          "pattern": "**/*.md"
        },
        {
          "name": "logs",
          "path": "/var/log/openclaw",
          "pattern": "**/*.md"
        }
      ],
      "index": {
        "backend": "sqlite",
        "path": "/srv/arifos/memory/qmd.db"
      }
    }
  }
}
```

**Boot Sequence:**
1. Gateway starts
2. QMD initializes SQLite index
3. `qmd update` — scan all paths
4. `qmd embed` — vectorize content
5. `memory_search` ready for queries

**Usage in Skills:**
```yaml
# AAA-META-MEMORY skill
memory_search:
  query: "Petronas basin analysis 2024"
  sources: ["vault", "working"]
  limit: 5
```

---

## Per-Agent MEMORY.md Specialization

Each agent workspace has specialized MEMORY.md:

### Architect MEMORY.md
```markdown
# Architect Memory

## Design Patterns
- Thermodynamic constraints always apply
- Prefer reversible architectures
- ΔS target: < 100 lines per change

## Key Formulas
- Φ_AGI = A × P × X × E² × (1 - C_dark)
- Peace² = buffer / risk ≥ 1.0
- W³ = (H × A × E)^(1/3) ≥ 0.95

## Reference Analogies
- Geoscience: Basin maturity curves
- Adat: Muafakat before action
- Physics: Landauer's Principle

## Common Constraints
- BNM API rate limits
- Petronas data residency
- B40/M40 impact sensitivity
```

### Actor MEMORY.md
```markdown
# Actor Memory

## Staging Paths
- Primary: /srv/repos/staging/
- Backup: /srv/backups/auto/
- Logs: /var/log/openclaw/actions/

## Rollback Procedures
1. Git reset --hard HEAD~1
2. Restore from /srv/backups/
3. Verify with healthcheck

## Allowed Commands
- git, python3, docker, npm
- tar, rsync, cp, mv
- NO: rm -rf /, mkfs, dd

## Cron Jobs
- Daily backup: 02:00
- Weekly report: Sun 08:00
- Health ping: every 5min
```

### Auditor MEMORY.md
```markdown
# Auditor Memory

## SEAL Checklist
- [ ] F1 Amanah: reversible?
- [ ] F2 Truth: sources cited?
- [ ] F3 Tri-Witness: W³ ≥ 0.95?
- [ ] F4 Clarity: ΔS < 0?
- [ ] F5 Peace²: ≥ 1.0?
- [ ] F6 Empathy: κᵣ ≥ 0.95?
- [ ] F7 Humility: Ω declared?
- [ ] F9 Anti-Hantu: no ghosts?

## High-Risk Patterns
- Direct prod writes without backup
- API key exposure in logs
- Unbounded loops in scripts
- Missing error handling

## Escalation Triggers
- Ω₀ > 0.08
- P² < 0.8
- Multi-floor conflict
- 888 Judge needed
```

---

## Context7 Realization

**In OpenClaw terms:**

| Context7 Component | OpenClaw Equivalent |
|-------------------|---------------------|
| Identity | SOUL.md + IDENTITY.md |
| Memory | MEMORY.md + QMD index |
| Skills | skills.entries (21 skills) |
| Tools | tools.* (filesystem, exec, etc.) |
| History | VAULT999/sessions/ |
| Context | Working memory (/srv/arifos/memory/) |
| State | Session runtime variables |

**Boot Load Order:**
```
1. SOUL.md (philosophy)
2. IDENTITY.md (presentation)
3. USER.md (user context)
4. MEMORY.md (role knowledge)
5. QMD index (semantic search)
6. Skills snapshot (capabilities)
7. Session init (current state)
↓
Agent ready with Context7 loaded
```

---

## Configuration

**Directory Structure:**
```
~/.openclaw/
├── workspace/
│   ├── SOUL.md              # Eternal
│   ├── IDENTITY.md          # Eternal
│   ├── USER.md              # Eternal
│   ├── MEMORY.md            # Global memory
│   ├── AGENTS.md            # Trinity routing
│   └── memory/              # QMD workspace
│
/root/VAULT999/              # Eternal archive
├── arifos/
├── decisions/
├── sessions/
└── vault.jsonl

/srv/arifos/
├── memory/                  # Working (Now)
│   ├── architect/
│   ├── actor/
│   └── auditor/
└── qmd.db                   # Semantic index

/srv/repos/
└── staging/                 # Pre-future
    └── (ephemeral experiments)

/var/log/openclaw/           # Temporal logs
├── actions/
├── telemetry/
└── audits/
```

---

## Key Principle

**Memory is not a skill. Memory is the foundation.**

- **Skills** (21) use memory via AAA-META-MEMORY
- **Agents** (3) read/write memory through skills
- **Identity** (SOUL.md) anchors all memory access
- **Context7** emerges from the stack

**Governance:**
- **Read:** All agents can read all layers
- **Write Eternal:** 888 Judge only
- **Write Past:** Auditor (verdicts), automatic (sessions)
- **Write Now:** Respective agents (architect/actor/auditor)
- **Write Pre-future:** Actor only (staging)

---

*Context7: Seven layers, one truth. Ditempa Bukan Diberi.* 🔥
