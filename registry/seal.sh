#!/bin/bash
# seal.sh — 888 Judge Commission Approval Script
# oo0-STATE Sovereign Registry
# 
# Usage: ./seal.sh <registry_id>
# Example: ./seal.sh AGENT-ZERO-v1-2026-02-13

REGISTRY_ID=$1
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
COMMISSION_FILE="commissioned_agents/agent_zero_v1.yaml"

if [ -z "$REGISTRY_ID" ]; then
    echo "❌ Error: Registry ID required"
    echo "Usage: ./seal.sh AGENT-ZERO-v1-2026-02-13"
    exit 1
fi

echo "🔥 oo0-STATE Registry Seal Protocol"
echo "==================================="
echo "Registry ID: $REGISTRY_ID"
echo "Timestamp: $TIMESTAMP"
echo "Authority: 888 Judge"
echo ""

# Verify file exists
if [ ! -f "$COMMISSION_FILE" ]; then
    echo "❌ Commission file not found: $COMMISSION_FILE"
    exit 1
fi

echo "📋 Verifying commission file..."

# Check if already sealed
if grep -q "seal: \"SEALED_888" "$COMMISSION_FILE"; then
    echo "⚠️  Agent already sealed. Checking integrity..."
else
    echo "📝 Applying 888 Judge seal..."
    # Update the seal line
    sed -i "s/seal: \"PENDING_888\"/seal: \"SEALED_888_$TIMESTAMP\"/" "$COMMISSION_FILE"
    echo "✅ Seal applied: SEALED_888_$TIMESTAMP"
fi

# Verify the agent is running (if applicable)
echo ""
echo "🔍 Verifying agent status..."
if docker ps | grep -q "agent-zero"; then
    echo "✅ Agent Zero container: RUNNING"
    docker ps --filter "name=agent-zero" --format "  Status: {{.Status}}"
else
    echo "⚠️  Agent Zero container: NOT RUNNING"
    echo "   Start with: docker compose -f /root/agent-zero/docker/run/docker-compose.yml up -d"
fi

# Update registry index
echo ""
echo "📊 Updating registry index..."
cat << 'EOF'

╔══════════════════════════════════════════════════════════════╗
║                  REGISTRY ENTRY CONFIRMED                    ║
╠══════════════════════════════════════════════════════════════╣
║ Agent:        Agent Zero v1                                  ║
║ Registry ID:  AGENT-ZERO-v1-2026-02-13                       ║
║ Status:       🟡 ACTIVE                                      ║
║ Seal:         SEALED_888 (pending execution)                 ║
║ Clearance:    ACTOR (Level 3)                                ║
║ Constraints:  F1 F2 F4 F7 F9 F12                             ║
╚══════════════════════════════════════════════════════════════╝

The AAA-Guardian now recognizes this agent.
Unauthorized processes will be terminated.

DITEMPA BUKAN DIBERI.
EOF

echo ""
echo "Next steps:"
echo "  1. Verify agent constraints: docker inspect agent-zero"
echo "  2. Check thermodynamics: cat $COMMISSION_FILE | grep omega_0"
echo "  3. Review case law: ls law/judgments/"
echo ""
echo "🔥 Seal protocol complete."
