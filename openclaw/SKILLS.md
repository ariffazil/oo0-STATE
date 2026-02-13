# SKILLS.md — 21-Skill Constitutional Spine

**Location:** `openclaw/SKILLS.md` in oo0-STATE  
**Purpose:** Canonical list of arifOS skills for OpenClaw  
**Version:** 1.0.0  
**Date:** 2026-02-13  
**Ω₀:** 0.04

---

## Overview

arifOS defines **exactly 21 skills** for OpenClaw deployment. This number is fixed to maintain constitutional clarity. New capabilities are added by:
1. Embedding engines within existing skills (AgentZero, OpenCode)
2. Adding domain skills through the Trinity loop (design → stage → audit → promote)

**Total: 21 skills. No more, no less.**

---

## Skill Categories

### I. Trinity Skills (3)

Core governance roles. Each corresponds to one agent.

#### 1. AAA-ARCHITECT
**Agent:** arif-architect (Δ)  
**Function:** Planning, design, entropy reduction  
**Tools:** browser, memory_search  
**Embedded Engine:** AgentZero (via http)

**SKILL.md declares:**
- Floor constraints (F2, F4, F7, F8)
- AgentZero endpoint and timeout
- Output format: structured spec

**AgentZero Integration:**
```yaml
embedded_engine:
  name: AgentZero
  endpoint: http://localhost:50080
  timeout: 300s
  use_for: complex multi-branch planning
  constraint: summarize results, apply floors
```

#### 2. AAA-ACTOR
**Agent:** arif-actor (Ω)  
**Function:** Execution, implementation, staging  
**Tools:** filesystem, exec, cron  
**Embedded Engine:** OpenCode CLI (via exec)

**SKILL.md declares:**
- Floor constraints (F1, F5, F6, F9, F11)
- Staging path: `/srv/repos/staging/`
- Rollback requirements

**OpenCode Integration:**
```yaml
embedded_engine:
  name: OpenCode
  cli: /usr/local/bin/opencode
  timeout: 600s
  use_for: coding, refactoring, tests
  constraint: staging only, log all changes
```

#### 3. AAA-AUDITOR
**Agent:** arif-auditor (Ψ)  
**Function:** Verification, validation, verdict  
**Tools:** browser, memory_search  
**Embedded Engines:** Perplexity, Gemini, Brave (via browser/http)

**SKILL.md declares:**
- Floor constraints (F3, F13)
- Tri-witness formula (W³)
- Verdict options: SEAL / PARTIAL / SABAR / VOID

**Validator Integration:**
```yaml
embedded_engines:
  - name: Perplexity
    endpoint: https://api.perplexity.ai
    use_for: citation-based verification
  - name: Gemini
    endpoint: https://generativelanguage.googleapis.com
    use_for: deep analysis
  - name: Brave
    endpoint: https://api.search.brave.com
    use_for: alternative perspective
```

---

### II. Meta Skills (4)

Foundational reasoning capabilities. Available to all three agents.

#### 4. AAA-META-PHYSICS
**Function:** Thermodynamic constraints, physical reality  
**Tools:** None (advisory only)  
**Use:** Ground reasoning in physical limits (Landauer, entropy)

#### 5. AAA-META-MATH
**Function:** Calculations, uncertainty, measurement  
**Tools:** None (calculation-only)  
**Use:** Quantify Ω₀, error propagation, confidence intervals

#### 6. AAA-META-CODE
**Function:** Symbolic reasoning, code structure  
**Tools:** None (text manipulation)  
**Use:** Parse schemas, generate specs, analyze patterns

#### 7. AAA-META-MEMORY
**Function:** Knowledge orchestration, context stitching  
**Tools:** memory_search  
**Use:** Retrieve from VAULT, manage QMD index

---

### III. Core OS Skills (5)

System-level capabilities. Primarily for Actor, read-only for others.

#### 8. filesystem-skill
**Function:** File operations  
**Tools:** filesystem  
**Constraints:** Allowed paths, blocked paths
**Primary Agent:** Actor (Ω)

#### 9. exec-skill
**Function:** Command execution  
**Tools:** exec  
**Constraints:** Whitelisted commands (git, python3, docker, etc.)  
**Primary Agent:** Actor (Ω)

#### 10. browser-skill
**Function:** Web access, HTTP requests  
**Tools:** browser  
**Constraints:** Domain allowlist (BNM, Petronas, etc.)  
**Primary Agents:** Architect (Δ), Auditor (Ψ)

#### 11. github-pro
**Function:** GitHub operations  
**Tools:** exec (gh CLI)  
**Constraints:** Token auth, repo allowlist  
**Primary Agent:** Actor (Ω)

#### 12. cron-skill
**Function:** Scheduling, automation  
**Tools:** cron  
**Constraints:** Job templates, timezone  
**Primary Agent:** Actor (Ω)

---

### IV. Knowledge & Domain Skills (4)

Data analysis and research capabilities.

#### 13. csv-analyzer
**Function:** CSV data analysis  
**Tools:** filesystem  
**Use:** Petronas data, BNM rates, EPF calculations  
**Primary Agent:** Actor (Ω), read by Auditor (Ψ)

#### 14. workflow-automation
**Function:** ETL pipelines  
**Tools:** exec  
**Use:** Scheduled reports, data flows  
**Primary Agent:** Actor (Ω)

#### 15. deepresearchwork
**Function:** Multi-step web research  
**Tools:** browser  
**Use:** Research framework, evidence gathering  
**Primary Agents:** Architect (Δ), Auditor (Ψ)

#### 16. obsidian-vault
**Function:** Knowledge graph interface  
**Tools:** filesystem  
**Use:** Query VAULT, link notes, templates  
**Primary Agent:** Architect (Δ)

---

### V. Communication & Safety Skills (5)

External communication and system safety.

#### 17. telegram-arif
**Function:** Telegram messaging  
**Tools:** http (Telegram Bot API)  
**Use:** Alerts to 888 Judge, quick queries  
**Primary Agent:** Auditor (Ψ) for alerts

#### 18. himalaya-email
**Function:** Email IMAP/SMTP  
**Tools:** http  
**Use:** Reports, alerts, async communication  
**Primary Agent:** Auditor (Ψ)

#### 19. 1password-skill
**Function:** Secrets management  
**Tools:** http (1Password API)  
**Use:** Retrieve API keys, credentials  
**Primary Agent:** Actor (Ω)

#### 20. healthcheck
**Function:** System monitoring  
**Tools:** exec  
**Use:** Ping services, check CPU/disk/memory  
**Primary Agent:** Auditor (Ψ)

#### 21. backup-orchestrator
**Function:** Reversibility, backups  
**Tools:** exec (tar, git, rclone)  
**Use:** F1 Amanah compliance, rollback procedures  
**Primary Agent:** Actor (Ω), verified by Auditor (Ψ)

---

## Skill Count Verification

| Category | Count | Skills |
|----------|-------|--------|
| Trinity | 3 | AAA-ARCHITECT, AAA-ACTOR, AAA-AUDITOR |
| Meta | 4 | AAA-META-PHYSICS, AAA-META-MATH, AAA-META-CODE, AAA-META-MEMORY |
| Core OS | 5 | filesystem-skill, exec-skill, browser-skill, github-pro, cron-skill |
| Knowledge | 4 | csv-analyzer, workflow-automation, deepresearchwork, obsidian-vault |
| Comms/Safety | 5 | telegram-arif, himalaya-email, 1password-skill, healthcheck, backup-orchestrator |
| **TOTAL** | **21** | **Constitutional spine complete** |

---

## Key Clarification

**AgentZero, OpenCode, and Perplexity/Gemini/Brave are NOT skills #22-24.**

They are **embedded engines** called from within existing skills:

| Engine | Called From | Via | When |
|--------|-------------|-----|------|
| AgentZero | AAA-ARCHITECT skill | http://localhost:50080 | Complex planning |
| OpenCode CLI | AAA-ACTOR skill | exec command | Coding in staging |
| Perplexity API | AAA-AUDITOR skill | browser/http | Fact verification |
| Gemini API | AAA-AUDITOR skill | browser/http | Deep analysis |
| Brave Search API | AAA-AUDITOR skill | browser/http | Alternative perspective |

This maintains the **21-skill constitutional spine** while enabling:
- Self-improvement (forge skill #22+ via Trinity loop)
- External AI capabilities (AgentZero, OpenCode)
- Multi-source validation (Perplexity, Gemini, Brave)

---

## Configuration

**openclaw.json:**
```json
{
  "skills": {
    "enabled": [
      "AAA-ARCHITECT", "AAA-ACTOR", "AAA-AUDITOR",
      "AAA-META-PHYSICS", "AAA-META-MATH", "AAA-META-CODE", "AAA-META-MEMORY",
      "filesystem-skill", "exec-skill", "browser-skill", "github-pro", "cron-skill",
      "csv-analyzer", "workflow-automation", "deepresearchwork", "obsidian-vault",
      "telegram-arif", "himalaya-email", "1password-skill", "healthcheck", "backup-orchestrator"
    ],
    "entries": {
      "AAA-ARCHITECT": {
        "enabled": true,
        "config": {
          "embedded_agent": "AgentZero",
          "agent_zero_endpoint": "http://localhost:50080"
        }
      },
      "AAA-ACTOR": {
        "enabled": true,
        "config": {
          "embedded_agent": "OpenCode",
          "opencode_cli": "/usr/local/bin/opencode"
        }
      },
      "AAA-AUDITOR": {
        "enabled": true,
        "config": {
          "embedded_validators": ["Perplexity", "Gemini", "Brave"]
        }
      }
    }
  }
}
```

---

*21 skills. Fixed constitution. Flexible muscles. Ditempa Bukan Diberi.* 🔥
