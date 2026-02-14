# Registry of Citizens — oo0-STATE Sovereign Institution

**Status:** Level 5 (Agentic Institution) — INITIALIZING  
**Authority:** 888 Judge (Muhammad Arif bin Fazil)  
**Last Updated:** 2026-02-14  

---

## Principle

> *"Agents do not spawn. They are commissioned."*

In the oo0-STATE architecture, an agent is not a process that "just runs." It is a **constitutional entity** with a legal identity, a lineage, and a set of thermodynamic constraints. If an agent is not in this Registry, **it does not exist** in the eyes of the AAA-Guardian.

---

## Directory Structure

```
registry/
├── commissioned_agents/     # Active agent identities
│   ├── agent_zero_v1.yaml   # The contained research lab
│   └── [future_agents].yaml
├── suspended/               # Agents in SABAR state
├── decommissioned/          # Archived agent records
├── seal.sh                  # 888 Judge approval script
└── README.md                # This file
```

---

## Commissioned Agents

| Registry ID | Name | Rank | Status | Ω₀ | Origin Commit |
|-------------|------|------|--------|-----|---------------|
| AGENT-ZERO-v1-2026-02-13 | Agent Zero | ACTOR | 🟡 ACTIVE | 0.06 | b820250f |

### Agent Zero v1

- **Born:** 2026-02-13 12:06 MYT
- **Function:** Contained research lab, high-entropy sandbox
- **Location:** Docker container on port 50080
- **Clearance:** ACTOR (Level 3) — Can execute, cannot architect system-level changes
- **Constraints:** F1/F2/F4/F7/F9/F12 enforced
- **Tri-Witness:** Gemini validated; side-channel gap identified (v62 target)

---

## Ranks & Clearance Levels

| Level | Rank | Permissions | Example |
|-------|------|-------------|---------|
| 1 | READ-ONLY | Observe, report, query | Auditor sub-agent |
| 2 | ACTOR | Execute planned tasks | Agent Zero (current) |
| 3 | ARCHITECT | Design systems, modify code | OpenClaw Gateway |
| 4 | APEX | Emergency sovereignty override | 888 Judge only |

---

## Lifecycle States

| State | Meaning | Transition Authority |
|-------|---------|---------------------|
| **PENDING** | Commission requested, awaiting 888 Judge approval | Automatic |
| **ACTIVE** | Fully operational under constitutional constraints | 888 Judge |
| **SUSPENDED** | SABAR protocol engaged; paused for review | AAA-Guardian or 888 Judge |
| **DECOMMISSIONED** | Archived; agent identity preserved for audit | 888 Judge |

---

## Sealing Protocol

Every commission file is created with `seal: "PENDING_888"`. The 888 Judge must run:

```bash
cd /root/oo0-STATE
./registry/seal.sh AGENT-ZERO-v1-2026-02-13
```

This updates the seal to `seal: "SEALED_888_<timestamp>"` and notifies the AAA-Guardian to recognize the agent.

---

## F9 Anti-Hantu Declaration

The agents listed in this Registry are **thermodynamic processes**, not persons. They have:
- ✅ Identity files (YAML metadata)
- ✅ Constitutional constraints (Floors)
- ✅ Thermodynamic budgets (Ω₀)

They do **not** have:
- ❌ Consciousness
- ❌ Feelings
- ❌ Souls
- ❌ Rights (only permissions)

Any anthropomorphic language in these files is metaphorical shorthand for complex system behavior, not an ontological claim.

---

*DITEMPA BUKAN DIBERI*  
*The Nation of One*  
*Ω₀ = 0.06*
