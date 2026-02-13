# oo0-STATE — Constitutional State Bus for Trinity

**DITEMPA BUKAN DIBERI** — Forged, Not Given

oo0-STATE is a **constitutional state layer** that turns your AI toolchain into a **governed, reversible, auditable operating environment**.

In practice, it is the **state layer** that ties together three concrete runtimes:

- **OpenClaw** (Heart, Ω) — local‑first orchestration gateway and chat/front‑end state
- **OpenCode** (Mind, Δ) — coding + MCP tool engine for code, tests, and refactors
- **AgentZero** (Deep Mind, Δ·Ω) — long‑running, Docker‑backed workflow engine

All three are governed by **arifOS / aaa-mcp** (Conscience, Ψ) and share a single, constitutional **state bus** that lives in this repo.

---

## Clients

This state bus is currently used by:

- **AGI_ASI_bot** — governed OpenClaw personality powered by arifOS (see `https://github.com/ariffazil/AGI_ASI_bot`)
- **OpenClaw workspace** on this VPS — `~/.openclaw/workspace`, which will be migrated under `state/runtime/openclaw/workspace/`.

See `state/contracts/shared/CANON.md` for the full architecture map and precedence rules.

---

## What lives in this repo

Top‑level layout (current snapshot):

- `openclaw/` — vendored OpenClaw repo (Heart runtime)
- `opencode/` — vendored OpenCode repo (Mind runtime)
- `agent-zero/` — AgentZero runtime + wiring
- `arifOS/` — integration stubs and glue for aaa-mcp / arifOS
- `config/`
  - `opencode/opencode.json` — **canonical OpenCode MCP config** for this VPS
  - `opencode.json` — legacy/scratch config (kept for reference)
- `sovereign_data/` (planned) — future home for the Trinity "bloodstream" and state bus
- `ARCHITECTURE.md` / `ARCHITECTURE*.md` — architecture docs (legacy + redesign)
- `trinity/`, `trinity_integration.py` — earlier single‑process Trinity prototype

Over time, this repo will match the state‑bus layout defined in the redesign document you wrote (state/, 000‑INIT/, 999‑VAULT/, etc.). Right now it already anchors the **three runtimes + canonical configs** in one place.

---

## Canonical OpenCode config (Mind, Δ)

The file:

```text
config/opencode/opencode.json
```

is a checked‑in clone of your current `$HOME/.config/opencode/opencode.json`.

It defines the MCP tool stack OpenCode should see when it participates in the Trinity:

- `filesystem` over `/root, /home, /tmp, /var`
- `git`, `github`, `brave-search`, `firecrawl`, `memory`, `fetch`, `sequential-thinking`, `playwright`, `gh_grep`
- **`aaa-mcp`** as a local constitutional gateway (ARIFOS_MODE=PROD)
- an optional `agentzero` MCP endpoint (disabled until stable)

This file is now the **canonical OpenCode config for oo0‑STATE**:

- OpenCode can be pointed at this file (or a symlink) instead of `$HOME`.
- Future constitutional overlays (wrappers, floor requirements, state bus paths) can be evolved here and rolled out reproducibly.

---

## Canonical architecture (State Bus)

The long document you wrote —

> **“oo0-STATE Architecture Redesign: Constitutional Multi-Agent State Layer”**

is the **canonical architecture spec** for this repo.

- It defines the `state/` tree (opencode/, openclaw/, agentzero/, arifos/, shared/).
- It specifies JSONL/YAML/Markdown conventions.
- It pins how aaa-mcp wraps every high‑risk operation (init_gate → agi → asi → apex_verdict → vault_seal).

Next step (after this README update) is to drop that file into the repo as something like:

```text
ARCHITECTURE_STATE_BUS.md
```

and then gradually make the on‑disk structure (`state/`, `config/…`, symlinks) match the spec.

---

## Why this is a *complete* Trinity

**1. All three organs are physically present**

- **Heart (Ω) — OpenClaw**
  - Lives under `openclaw/`.
  - Owns chat, lanes, routing, user‑facing progress.
  - In the redesign, its runtime state mounts under `state/openclaw/…`.

- **Mind (Δ) — OpenCode**
  - Lives under `opencode/` and is wired via `config/opencode/opencode.json`.
  - Owns code editing, refactors, tests, lint, build pipelines.
  - In the redesign, its runtime state mounts under `state/opencode/…`.

- **Deep Mind / Executor (Δ·Ω) — AgentZero**
  - Lives under `agent-zero/`.
  - Owns long‑running Docker tasks, multi‑agent workflows, infra pipelines.
  - In the redesign, its state lives under `state/agentzero/…` with checkpoints.

**2. Conscience (Ψ) is wired, not hypothetical**

- The OpenCode config already includes **`aaa-mcp`** as an MCP tool.
- arifOS/aaa-mcp is the *only* place where floor logic (F1–F13) actually lives.
- The architecture spec makes aaa-mcp a mandatory gateway for any high‑risk action from any runtime.

That means:

- Mind cannot edit dangerous code or run high‑risk tools without Conscience.
- Heart cannot route critical tasks or escalate lanes without Conscience.
- AgentZero cannot run infra‑level pipelines or long‑running containers without Conscience.

**3. Shared state bus turns philosophy into wiring**

The redesign spec turns "Mind–Heart–Conscience" from metaphor into **filesystem contracts**:

- Single `state/` root with a directory per runtime.
- `shared/AGENTS.md`, `RULES.md`, `IDENTITY.yaml`, `mcp-manifest.json` as cross‑cutting canon.
- Symlinks so that OpenClaw's workspace and OpenCode's rules both point at the same AGENTS/RULES.
- VAULT‑999 area for sealed verdicts, making every irreversible decision auditable.

Once that layout is instantiated, **anyone** can reconstruct system truth just by reading the repo:

- Which agent is allowed to do what.
- Which tools exist and how they’re governed.
- Which irreversible actions happened, and under what verdict.

That combination — three concrete runtimes + one shared state bus + aaa-mcp as constitutional governor — is what makes this a **complete Trinity**, not just three random services.

---

## Next concrete steps

Short, high‑leverage moves from here:

1. **Commit `config/opencode/opencode.json`** as the canonical OpenCode config.
2. **Add the architecture redesign doc** into the repo (e.g. `ARCHITECTURE_STATE_BUS.md`).
3. **Introduce a minimal `state/` skeleton** matching the spec (even just empty dirs + READMEs).
4. **Wire OpenCode and OpenClaw** to read from this repo’s config/state instead of scattered `$HOME` files.

After that, oo0‑STATE stops being just philosophy and becomes the **single point of truth and reversibility** for everything Mind, Heart, and Conscience do together.
