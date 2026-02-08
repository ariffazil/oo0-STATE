# Quick Start Guide - oo0-STATE Trinity System

## Installation

No installation needed! The system uses only Python standard library.

Requirements:
- Python 3.6 or higher

## Quick Start

### 1. Run the Main Trinity System

```bash
python3 trinity_integration.py
```

This will:
- Initialize Mind (Agent Zero)
- Initialize Heart (OpenClaw)
- Initialize Conscience (arifOS)
- Activate Anti-Hantu protocols
- Initialize all 13 floors
- Run basic tests

### 2. Run Examples

```bash
python3 examples.py
```

This demonstrates:
- Basic Trinity usage
- Floor integrity checking
- Multiple operations
- System audits
- Status reporting

## Basic Usage in Code

```python
from trinity_integration import Trinity

# Initialize the Trinity
trinity = Trinity()

# Process input through all components
result = trinity.process("Your operation here")

# Check the results
print(f"Mind thought: {result['thought']['output']}")
print(f"Heart executed: {result['execution']['status']}")
print(f"Conscience judged: {result['judgment']['ethical']}")
print(f"Entropy delta: {result['entropy_check']['delta_S']}")
```

## Common Operations

### Check Floor Status

```python
# Check a specific floor (F1-F13)
status = trinity.check_floor("F5")  # Ethics floor
print(f"{status['description']}: {status['integrity']}")
```

### Perform System Audit

```python
# Get complete Trinity audit
audit = trinity.audit()
print(f"Floors operational: {audit['floors_operational']}/13")
print(f"Verdict: {audit['verdict']}")
```

### Get System Status

```python
# Get current status of all components
status = trinity.get_status()
print(f"Mind: {status['mind']['status']}")
print(f"Heart: {status['heart']['status']}")
print(f"Conscience: {status['conscience']['status']}")
```

### Access Individual Components

```python
# Use Mind (Agent Zero) directly
thought = trinity.mind.think("Analyze this")
decision = trinity.mind.decide(["option1", "option2"])

# Use Heart (OpenClaw) directly
execution = trinity.heart.execute("Some operation")
pulse = trinity.heart.pulse()

# Use Conscience (arifOS) directly
judgment = trinity.conscience.judge("Some action")
entropy = trinity.conscience.enforce_entropy_constraint(data)
anti_hantu = trinity.conscience.activate_anti_hantu()
```

## Understanding the Logs

All operations are logged to `sovereign_data/workspace/*.jsonl` files:

### View Mind Activity
```bash
cat sovereign_data/workspace/mind_thoughts.jsonl
cat sovereign_data/workspace/mind_decisions.jsonl
cat sovereign_data/workspace/mind_coordination.jsonl
```

### View Heart Activity
```bash
cat sovereign_data/workspace/heart_executions.jsonl
cat sovereign_data/workspace/heart_grasps.jsonl
cat sovereign_data/workspace/heart_pulses.jsonl
```

### View Conscience Activity
```bash
cat sovereign_data/workspace/conscience_judgments.jsonl
cat sovereign_data/workspace/entropy_enforcements.jsonl
cat sovereign_data/workspace/anti_hantu_activations.jsonl
cat sovereign_data/workspace/floor_integrity_checks.jsonl
cat sovereign_data/workspace/trinity_audits.jsonl
```

## The 13 Floors

Quick reference for arifOS floors:

- **F1**: Foundation - Physical Integrity
- **F2**: Security - Anti-Hantu Barrier
- **F3**: Stability - Resource Conservation
- **F4**: Harmony - Component Synchronization
- **F5**: Ethics - Moral Compass
- **F6**: Wisdom - Knowledge Integration
- **F7**: Justice - Fair Distribution
- **F8**: Compassion - Empathetic Response
- **F9**: Truth - Honest Communication
- **F10**: Growth - Positive Evolution
- **F11**: Balance - Homeostasis
- **F12**: Transcendence - Higher Purpose
- **F13**: Unity - Trinity Convergence

## Key Principles

1. **ΔS < 0**: Operations should decrease or maintain entropy
2. **Anti-Hantu**: Protection protocols always active
3. **13 Floors**: Complete ethical governance
4. **DITEMPA BUKAN DIBERI**: Forged through effort, not given
5. **Trinity Unity**: Mind, Heart, Conscience work as one

## Troubleshooting

### Issue: Import errors
**Solution**: Ensure you're running from the repository root directory

### Issue: Permission denied on workspace
**Solution**: Check write permissions on `sovereign_data/workspace/`

### Issue: Entropy constraint always violated
**Solution**: This is informational - the system tracks but doesn't block operations

## Advanced Usage

See [ARCHITECTURE.md](ARCHITECTURE.md) for:
- Detailed component documentation
- Extension points
- Design principles
- Advanced integration patterns

## Philosophy

**DITEMPA BUKAN DIBERI** - "Forged, Not Given"

The Trinity system embodies the principle that true understanding and mastery come through active creation and engagement, not passive consumption. Each component must be understood, maintained, and evolved through conscious effort.

## Next Steps

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) for deep dive
2. Explore the source code in `trinity/` directory
3. Run and modify `examples.py` to experiment
4. Check logs in `sovereign_data/workspace/` to understand operations
5. Extend the system with your own components

---

For questions and issues, refer to the repository README and documentation.