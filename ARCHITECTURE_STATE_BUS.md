# oo0-STATE Architecture Redesign: Constitutional Multi-Agent State Layer

## 0. Snapshot

### 0.1 Core Truth Statement

The oo0-STATE repository at https://github.com/ariffazil/oo0-STATE serves as the foundational state layer for a multi-agent, multi-runtime governance system that must harmonize four distinct computational entities: **OpenCode** (primary coding/IDE agent with MCP tools), **OpenClaw** (local-first orchestration gateway), **AgentZero** (multi-agent long-running workflow engine), and **aaa-mcp/arifOS** (constitutional governor already operational as an MCP server). The current repository structure reveals a significant gap between aspirational architecture and operational reality—while the repository describes itself as unifying "Mind (Agent Zero), Heart (OpenClaw), and Conscience (arifOS)"  [(Source)](about:blank) , direct inspection shows minimal implementation: a flat directory structure with basic documentation, placeholder code, and no systematic state management infrastructure. The fundamental truth is that oo0-STATE currently functions more as a conceptual commitment than as an active state coordination layer, requiring substantial architectural investment to bridge the gap between governance philosophy and enforceable, auditable, reversible state operations.

### 0.2 Tri-Witness Validation

The tri-witness framework (AGI mind Δ, ASI heart Ω, APEX verdict Ψ) demands three independent validation perspectives for every architectural decision. **AGI mind (Δ)** assesses analytical correctness: the current structure shows conventional software organization without specialized state-layer abstractions, suggesting that AgentZero's planning capabilities would encounter friction when persisting or retrieving structured state. The information-theoretic efficiency of state access—how quickly any observer can reconstruct complete system state—is unacceptably low due to fragmented, implicit conventions. **ASI heart (Ω)** evaluates systemic harmony and stakeholder protection: OpenClaw's local-first philosophy ("Files beat abstractions")  [(LinkedIn)](https://www.linkedin.com/pulse/inside-openclaw-how-ai-agent-actually-works-under-hood-ajith-raghavan-eqahc)  creates tension with centralized governance needs, and the absence of explicit memory cooling bands (L0-L5) risks unbounded growth of sensitive user data without privacy-preserving archival. The empathy-architecture gap is substantial—components cannot reliably infer each other's state, leading to defensive coding and redundant validation. **APEX verdict (Ψ)** demands constitutional fidelity and final authority: while arifOS's aaa-mcp is operational with live health endpoint  [(Libraries.io)](https://libraries.io/pypi/arifos) , its integration into oo0-STATE's state flow is unspecified. The 13 constitutional floors (F1-F13) have no visible embodiment in repository structure, meaning governance enforcement cannot be systematically verified or audited. The conditional verdict is **SEAL/PARTIAL pending architectural remediation**—the conceptual foundation is sound, but implementation requires comprehensive restructuring.

### 0.3 Thermodynamic Efficiency Principle

Every architectural decision must demonstrate **thermodynamic efficiency**: reducing entropy (disorder, uncertainty, irreversibility) while maintaining or increasing system capability. This principle manifests concretely in five design constraints: **append-only formats** (JSONL) prevent state corruption from in-place edits and enable streaming audit; **symlink-based single sources of truth** eliminate configuration drift without copy synchronization overhead; **directory-per-runtime ownership** creates explicit interfaces that reduce cross-component coupling entropy; **constitutional governance overlays** prevent expensive error-correction by catching violations at earliest possible stage; and **content-addressed storage** for sealed records enables deduplication and integrity verification. The 8.7ms constitutional reflex target  [(PyPI)](https://pypi.org/project/arifos/47.1.0/) —while explicitly theoretical—establishes performance expectations: governance overhead must be bounded and predictable, not unbounded friction. The 4× computational cost versus ungoverned operation is accepted trade-off for safety guarantees. For oo0-STATE specifically, thermodynamic efficiency requires that state primitives be **self-describing** (format version in each record), operations be **idempotent** (same input produces same output), and transitions be **reversible** (F1 Amanah) or explicitly marked irreversible with cryptographic justification.

---

## 1. Recon: Current State Assessment

### 1.1 Repository Structure Mapping

#### 1.1.1 Top-Level Directory Tree

Based on direct repository inspection  [(Source)](about:blank) , the current oo0-STATE structure is:

```
oo0-STATE/
├── 000-STATE/           # Directory with numeric prefix, purpose unclear
│   └── hello.py         # Single Python example file
├── LICENSE              # Standard open-source license
└── README.md            # Project documentation: "Mind, Heart, Conscience"
```

This structure is **extremely minimal**—four items total, with no evidence of operational state management infrastructure. The `000-STATE` directory naming suggests arifOS stage nomenclature (000 = INIT) but contains only a basic "Hello World" script without state primitives. No dedicated directories exist for OpenCode, OpenClaw, AgentZero, or arifOS configuration. No `state/`, `config/`, `logs/`, or `shared/` directories are present. The repository's self-description as "state layer" is **aspirational rather than descriptive**—the physical structure does not embody the architectural intent.

**Critical uncertainty (F7 Humility):** The `visit` tool did not successfully retrieve complete directory listings. The structure above represents confirmed elements; additional files or directories may exist unobserved. This reconnaissance gap itself indicates architectural risk—if system state cannot be fully observed, it cannot be fully governed.

#### 1.1.2 Component Directory Purposes

| Directory | Observed Contents | Inferred Purpose | Confidence |
|-----------|-------------------|------------------|------------|
| `000-STATE/` | `hello.py` | Nominal state root, uninitialized | Low—name implies structure, content contradicts |
| `LICENSE` | Standard OSS license | Legal compliance | High |
| `README.md` | Conceptual description | Human orientation | High |

No component-specific directories are observed. The "Mind, Heart, Conscience" framing from README.md  [(Source)](about:blank)  suggests intended organization—AgentZero/Mind for reasoning, OpenClaw/Heart for orchestration, arifOS/Conscience for governance—but this tripartition has **no physical embodiment** in directory structure.

#### 1.1.3 Existing State Primitives Inventory

| Primitive | Expected Location | Observed? | Evidence |
|-----------|-------------------|-----------|----------|
| JSONL logs | `*/logs/` or `*.jsonl` | **No** | No log files in directory listing |
| YAML configs | `config/` or `*.yaml` | **No** | No config directory or YAML files |
| Markdown contracts | `AGENTS.md`, `*.md` | **Partial** | README.md only, no AGENTS.md observed |
| MCP server registry | `mcp.json` or `aaa_mcp/` | **No** | No MCP configuration visible |
| VAULT-999 seals | `vault/` or `VAULT*/` | **No** | No cryptographic storage visible |
| Agent definitions | `agents/` or `AGENTS.md` | **No** | No agent configuration visible |
| Session state | `sessions/` or `memory/` | **No** | No runtime state directories |

The state primitive inventory is **effectively empty**. A repository claiming to be "state layer" for multi-agent governance has no observable state primitives. This represents **foundational architectural debt**—the system cannot be audited, debugged, or recovered without explicit, versioned, schema-defined state representations.

### 1.2 Component State Audit

#### 1.2.1 OpenCode Current Configuration

**No OpenCode-specific configuration is present in oo0-STATE.** The term "OpenCode" appears only in the task description, not in retrieved sources. This creates critical knowledge gap: OpenCode's actual configuration format, MCP server expectations, and file loading conventions are **entirely unspecified** in available evidence.

Inferred requirements from general MCP patterns  [(PyPI)](https://pypi.org/project/arifos/49.0.1/) : OpenCode would expect `opencode.json` or similar with MCP server registry, agent definitions, and permission models. The absence of such configuration in oo0-STATE means OpenCode integration, if attempted, would use **default configurations without constitutional awareness**—a severe governance gap.

#### 1.2.2 OpenClaw Current State Files

**No OpenClaw-specific state is present in oo0-STATE.** However, OpenClaw's architecture is well-documented externally  [(LinkedIn)](https://www.linkedin.com/pulse/inside-openclaw-how-ai-agent-actually-works-under-hood-ajith-raghavan-eqahc) , revealing patterns that oo0-STATE should accommodate:

| OpenClaw Primitive | Standard Location | Format | Relevance to oo0-STATE |
|-------------------|-------------------|--------|------------------------|
| Workspace root | `~/.openclaw/workspace/` or `~/clawd/` | Directory | Should be symlinked to `state/openclaw/` |
| AGENTS.md | `workspace/AGENTS.md` | Markdown | Should be unified in `state/shared/` |
| SOUL.md | `workspace/SOUL.md` | Markdown | Runtime-specific, OpenClaw-owned |
| TOOLS.md | `workspace/TOOLS.md` | Markdown | Should reference unified tool registry |
| IDENTITY.md | `workspace/IDENTITY.md` | Markdown | Should reference unified identity |
| USER.md | `workspace/USER.md` | Markdown | User-specific, privacy-sensitive |
| HEARTBEAT.md | `workspace/HEARTBEAT.md` | Markdown | Operational, OpenClaw-owned |
| MEMORY.md | `workspace/MEMORY.md` | Markdown | Long-term memory, curated |
| Daily memory | `workspace/memory/YYYY-MM-DD.md` | Markdown | Ephemeral, rolling window |
| Session logs | `.openclaw/agents/<id>/sessions/*.jsonl` | JSONL | Audit trail, should mirror to `state/openclaw/logs/` |
| Heartbeat state | `workspace/memory/heartbeat-state.json` | JSON | Ephemeral health tracking |

OpenClaw's "file-first" philosophy  [(LinkedIn)](https://www.linkedin.com/pulse/inside-openclaw-how-ai-agent-actually-works-under-hood-ajith-raghavan-eqahc) —"Files beat abstractions," "Explainability beats cleverness"—aligns thermodynamically with oo0-STATE goals. However, current oo0-STATE provides **no integration point** for this philosophy—no directory to symlink, no contract to share.

#### 1.2.3 AgentZero Current Integration

**No AgentZero-specific state is present in oo0-STATE.** AgentZero's documented capabilities  [(Github)](https://github.com/agent0ai/agent-zero)  include: polyglot code generation, task decomposition, microservice development, legacy modernization, and performance optimization. The framework emphasizes "AI-assisted software development" with "repeatable, auditable, and architecture-first delivery"  [(Github)](https://github.com/msitarzewski/AGENT-ZERO) .

Critical distinction: **AGENT-ZERO** (repository  [(Github)](https://github.com/msitarzewski/AGENT-ZERO) ) provides patterns and documentation—specifically the canonical `AGENTS.md` guide—while "AgentZero" in the task description appears to refer to a **runtime engine** with MCP support. The relationship between these is **unverified**. The MCP changelog reference in the task was not retrieved in sources; AgentZero's "MCP client and MCP server mode" capabilities are **speculative** (marked "Estimate Only" per F2).

AgentZero's Docker-centric architecture  [(Github)](https://github.com/agent0ai/agent-zero)  implies state externalization challenge: container filesystems, volume mounts, and runtime-generated tools exist outside standard file system observation. oo0-STATE must define **explicit synchronization contract** for this state to be governable.

#### 1.2.4 arifOS/aaa-mcp Current Deployment

**arifOS/aaa-mcp is production-verified**, with multiple confirmation channels  [(Libraries.io)](https://libraries.io/pypi/arifos) :

| Verification Method | Evidence | Confidence |
|---------------------|----------|------------|
| PyPI package | `arifos` 53.2.9 published | High |
| MCP Registry | `io.github.ariffazil/aaa-mcp` | High |
| Health endpoint | `aaamcp.arif-fazil.com/health` | High |
| Live documentation | `arifos.arif-fazil.com` | High |
| GitHub repository | 1,856+ commits, 25+ releases | High |

The 25 MCP servers mapped to constitutional floors  [(PyPI)](https://pypi.org/project/arifos/49.0.1/)  provide concrete integration points. Verified server-floor mappings include:

| MCP Server | Floors Enforced | Heat Sink |
|------------|---------------|-----------|
| `filesystem` | F1 (Amanah), F11 (Sovereignty) | Reversibility via checkpoint |
| `http_client` | F2 (Truth), F12 (Defense) | Truth verification + injection defense |
| `sequential_thinking` | F4 (Clarity), F7 (Humility) | Clear reasoning + uncertainty |
| `websearch` | F2 (Truth), F3 (Consensus) | Tri-witness verification |
| `postgres` | F1 (Amanah), F5 (Peace²), F11 (Sovereignty) | Transactional safety + non-escalation + authority |

The "20 more servers" mentioned in documentation  [(PyPI)](https://pypi.org/project/arifos/49.0.2/)  are **not fully enumerated in retrieved sources**—this coverage gap represents implementation risk.

**Critical integration gap:** While aaa-mcp is operational, its **connection to oo0-STATE is unspecified**. No `AAA-MCP/` directory content was retrieved; no `unified_mcp_spec.json` version was confirmed; VAULT-999 sealing is referenced but **not implemented** in observable structure.

### 1.3 Naming Pattern Analysis

#### 1.3.1 000-STATE Convention Usage

The `000-STATE` naming follows arifOS metabolic pipeline staging  [(PyPI)](https://pypi.org/project/arifos/49.0.1/) :

| Stage | Range | Organ | Function |
|-------|-------|-------|----------|
| INIT | 000 | — | Load constitutional context + VAULT memory |
| AGI | 111-333 | Δ (Mind) | Search, think, reason |
| ASI | 444-666 | Ω (Heart) | Align, empathy, bridge |
| APEX | 777-999 | Ψ (Verdict) | Reflect, judge, proof, vault |

The `000` prefix signals **initialization and constitutional loading**—appropriate for state layer root. However, the pattern is **not extended**: no `111-AGI/`, `444-ASI/`, `777-APEX/`, or `999-VAULT/` directories exist to complete the pipeline visualization. The `oo0` variant in "oo0-STATE" may indicate "object-oriented zero-state" or visual symmetry with "ooo" (three organs), but this interpretation is **unverified**.

The missed opportunity: stage-organized directories would make state lifecycle **visually apparent** from filesystem organization, simplifying debugging and audit. Current partial implementation creates confusion—`000-STATE` appears first but contains mixed-stage data.

#### 1.3.2 AAA-MCP File Locations

The `AAA-MCP` naming convention (triple-A for priority, MCP for Model Context Protocol) suggests **highest-priority governance interface**. Expected locations based on arifOS patterns  [(Github)](https://github.com/ariffazil/arifOS) :

| Expected Path | Purpose | Verification Status |
|-------------|---------|---------------------|
| `AAA-MCP/` or `aaa_mcp/` | MCP server implementation | **Not observed** in oo0-STATE |
| `aaa_mcp/v46/unified_mcp_spec.json` | Canonical 25-server mapping | Referenced  [(PyPI)](https://pypi.org/project/arifos/49.0.2/) , not retrieved |
| `aaa_mcp/v*/` | Versioned specifications | Inferred, not verified |
| `mcp/` (root) | Runtime server implementations | Inferred, not verified |

The version drift risk is substantial: if `v46` is referenced but not present, future specification updates may conflict with existing configurations.

#### 1.3.3 AGENTS.md Presence and Structure

**No `AGENTS.md` is observed in oo0-STATE.** This absence is **critical** because `AGENTS.md` serves as the primary contract between human intent and agent behavior across the emerging ecosystem  [(Github)](https://github.com/msitarzewski/AGENT-ZERO) . Three competing patterns exist:

| Source | `AGENTS.md` Purpose | Structure |
|--------|---------------------|-----------|
| AGENT-ZERO  [(Github)](https://github.com/msitarzewski/AGENT-ZERO)  | Human-AI collaboration contract | Single canonical guide for "repeatable, auditable, architecture-first delivery" |
| OpenClaw  [(LinkedIn)](https://www.linkedin.com/pulse/inside-openclaw-how-ai-agent-actually-works-under-hood-ajith-raghavan-eqahc)  | Runtime bootstrap context | AGENTS/SOUL/TOOLS/IDENTITY/USER/HEARTBEAT/BOOTSTRAP/MEMORY sections |
| arifOS multi-agent  [(PyPI)](https://pypi.org/project/arifos/47.1.0/)  | Governance workflow definition | ARCHITECT → ENGINEER → AUDITOR → VALIDATOR pipeline |

These patterns **serve different purposes and are not directly compatible**. oo0-STATE's `AGENTS.md` (when created) must integrate all three: human-readable contract, runtime bootstrap context, and governance workflow definition. This design tension requires explicit architectural resolution.

### 1.4 Boundary Issues and Duplication

#### 1.4.1 State Ownership Conflicts

Without observable state, **potential conflicts must be inferred** from component capability overlaps:

| Capability | OpenClaw Claim | AgentZero Claim | Conflict Severity |
|------------|--------------|-----------------|-------------------|
| Long-term memory | `memory.ts` → 76KB manager  [(Hosted Personal AI Assistant | Complete Data Control (formerly Moltbot, Clawdbot))](https://openclaw-ai.online/architecture/)  | "Context Awareness: Maintains understanding of your entire project structure"  [(Agent Zero)](https://www.agent-zero.ai/p/use-cases/development/)  | **High**—duplicate memory systems create synchronization risk |
| Session persistence | JSONL `session-manager.ts`  [(Hosted Personal AI Assistant | Complete Data Control (formerly Moltbot, Clawdbot))](https://openclaw-ai.online/architecture/)  | Implicit in "long-running workflow engine" | **Medium**—overlapping persistence concerns |
| Task decomposition | Skills system  [(wordpress.com)](https://atalupadhyay.wordpress.com/2026/02/08/openclaw-build-your-ai-agent-army-in-60-minutes/)  | "break down complex tasks into manageable steps"  [(Agent Zero)](https://www.agent-zero.ai/p/use-cases/development/)  | **High**—competing orchestration claims |
| Docker execution | Not documented | "Long-running Docker tasks" (task description) | **Low**—complementary, but boundary unclear |

The "Mind/Heart/Conscience" framing suggests functional separation—AgentZero/Mind for reasoning, OpenClaw/Heart for orchestration, arifOS/Conscience for governance—but **operational boundaries** (who writes which state files) remain undefined.

#### 1.4.2 Configuration Redundancy

**Expected redundancy** (not yet observed, but architecturally likely): MCP server definitions repeated across OpenCode, OpenClaw, and AgentZero contexts without shared base. The `filesystem` MCP server, for example, requires identical path allowances and F1/F11 floor enforcement across all runtimes—without shared configuration, **manual synchronization creates drift risk**.

The symlink-based single source of truth pattern (Section 6.2) eliminates this redundancy, but requires **each component to support symlink-following in configuration loading**—capability unverified for OpenCode and AgentZero.

#### 1.4.3 Governance Gaps

**Critical governance gaps** where state transitions lack constitutional validation:

| Gap Location | Risk | Mitigation Required |
|--------------|------|---------------------|
| AgentZero long-running workflows | **Severe**—Docker tasks, multi-agent planning, infrastructure experiments without aaa-mcp integration | Mandatory `init_gate` → `apex_verdict` pipeline before any container execution |
| OpenCode bash execution | **High**—`rm -rf`, database modifications, network reconfiguration without governance | Explicit risk classification with mandatory pipeline for high-risk commands |
| OpenClaw skill activation | **Medium**—skill invocation may trigger ungoverned tool chains | Skill manifest with declared floor requirements |
| Cross-runtime state sync | **Critical**—state propagation without cryptographic verification | Merkle-tree verification for all cross-boundary transfers |

The "fast-path" for low-risk operations is **not formally defined**—subjective risk assessment varies by operator, creating inconsistency.

---

## 2. Target Architecture: The State Bus Design

### 2.1 Centralized State Layer Structure

#### 2.1.1 Proposed Directory Hierarchy

The target architecture transforms oo0-STATE from conceptual description to **operational state bus** with explicit constitutional governance overlay:

```
oo0-STATE/
├── README.md                    # Human orientation with architecture diagram
├── LICENSE                      # AGPL-3.0 (arifOS compatibility)
├── .gitignore                   # Exclude: secrets/, *.sqlite, logs/raw/
│
├── 000-INIT/                    # Constitutional loading (renamed from 000-STATE)
│   └── README.md                # Stage purpose and transition rules
│
├── 111-333-AGI/                 # Mind layer: analytical validation (future)
├── 444-666-ASI/                 # Heart layer: care-centered validation (future)
├── 777-888-APEX/                # Authority layer: final judgment (future)
│
├── 999-VAULT/                   # Cryptographically sealed records
│   └── README.md                # Mount point documentation
│
├── state/                       # THE STATE BUS—single source of truth
│   ├── README.md                # State layer contract and navigation
│   │
│   ├── opencode/                # OpenCode runtime state
│   │   ├── README.md            # Ownership and lifetime policies
│   │   ├── config/              # Symlinked from ../../config/opencode/
│   │   ├── runs/                # Ephemeral: active editing sessions (YAML)
│   │   ├── checkpoints/         # Ephemeral: pre-refactor snapshots
│   │   ├── logs/                # Append-only: tool execution (JSONL)
│   │   └── agents/              # Persistent: agent definitions (YAML)
│   │
│   ├── openclaw/                # OpenClaw runtime state
│   │   ├── README.md            # Ownership and lifetime policies
│   │   ├── workspace/           # Mirrored from ~/.openclaw/workspace/
│   │   │   ├── AGENTS.md -> ../../shared/AGENTS.md  # Symlink
│   │   │   ├── SOUL.md          # Personality (OpenClaw-owned)
│   │   │   ├── TOOLS.md         # Tool notes (OpenClaw-owned)
│   │   │   ├── IDENTITY.md -> ../../shared/IDENTITY.md  # Symlink
│   │   │   ├── USER.md          # User profile (privacy-sensitive)
│   │   │   ├── HEARTBEAT.md     # Operational checklist
│   │   │   ├── MEMORY.md        # Curated long-term memory
│   │   │   └── memory/          # Daily append-only logs (Markdown)
│   │   ├── sessions/            # JSONL: chat history, lane queues
│   │   ├── lanes/               # YAML: task routing state
│   │   └── logs/                # JSONL: gateway operations
│   │
│   ├── agentzero/               # AgentZero runtime state
│   │   ├── README.md            # Ownership and lifetime policies
│   │   ├── config/              # Symlinked from ../../config/agentzero/
│   │   ├── pipelines/           # Ephemeral: active workflow runs
│   │   ├── docker/              # Ephemeral: container state snapshots
│   │   ├── logs/                # JSONL: execution traces
│   │   ├── agents/              # Persistent: multi-agent configs (YAML)
│   │   └── plugins/             # Persistent: plugin state
│   │
│   ├── arifos/                  # Constitutional governance state
│   │   ├── README.md            # VAULT-999 access and verification
│   │   ├── constitutional/      # F1-F13 floor definitions (Markdown)
│   │   ├── mcp/                 # aaa-mcp server implementation
│   │   ├── gates/               # YAML: active governance gates
│   │   ├── verdicts/            # JSONL: SEAL/SABAR/PARTIAL/VOID/888_HOLD
│   │   ├── ledger/              # JSONL: append-only audit chain
│   │   └── vault/               # SEALED: cryptographic records
│   │
│   └── shared/                  # CROSS-CUTTING CONTRACTS
│       ├── AGENTS.md            # Unified agent behavior (canonical)
│       ├── RULES.md             # Global constitutional interpretation
│       ├── IDENTITY.yaml        # System identity schema
│       ├── mcp-manifest.json    # Canonical 25-server registry reference
│       └── schemas/             # JSON Schema for all state types
│
├── config/                      # CONFIGURATION SOURCE OF TRUTH
│   ├── README.md                # Configuration architecture
│   ├── opencode/                # Merged into opencode runtime
│   │   ├── core.json            # Immutable defaults
│   │   ├── mcp.json             # Server registry
│   │   └── rules/               # Repo-specific governance rules
│   ├── openclaw/                # Referenced by openclaw bootstrap
│   │   ├── gateway.yaml         # WebSocket, network, token settings
│   │   ├── skills.yaml          # Skill loading configuration
│   │   └── heartbeat.yaml       # Wake scheduling, rate limits
│   ├── agentzero/               # Loaded by agentzero runtime
│   │   ├── runtime.yaml         # Docker, resource, concurrency limits
│   │   ├── pipelines/           # Reusable pipeline definitions
│   │   └── agents/              # Agent role specifications
│   └── arifos/                  # Constitutional enforcement parameters
│       ├── floors.yaml          # F1-F13 thresholds, overrides
│       ├── mcp-gateway.yaml     # aaa-mcp server configuration
│       └── vault-policy.yaml    # Sealing, retention, cooling bands
│
├── scripts/                     # OPERATIONAL AUTOMATION
│   ├── init-state.sh            # Idempotent state directory creation
│   ├── verify-symlinks.sh       # Configuration integrity check
│   ├── migrate-stage.sh         # 000→111→444→777→999 transitions
│   └── archive-ephemeral.sh     # Entropy reduction: compress old state
│
└── docs/                        # ARCHITECTURE DOCUMENTATION
    ├── ADR-001-state-bus.md     # Architecture Decision Record
    ├── data-flow.md             # Text-described architecture diagrams
    └── OPERATIONS.md            # Runbook for common tasks
```

**Thermodynamic efficiency rationale:** Each `README.md` at directory roots makes ownership and policies **self-describing**, reducing cognitive load. The `state/` → `config/` symlink pattern ensures runtime components read from "owned" locations while content is **centrally versioned**. The numerical stage directories (000, 111-333, 444-666, 777-888, 999) create **explicit pipeline visualization**—state transitions are physically apparent. The `.gitignore` at `state/` root with explicit inclusions (rather than exclusions) prevents accidental commits of ephemeral data.

... (truncated for brevity)
