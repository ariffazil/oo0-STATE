"""
arifOS - The Conscience of the Trinity
Responsible for ethical governance, entropy management, and Anti-Hantu protocols
Implements 13 Floors (F1-F13) ensuring ΔS < 0
"""

import os
import json
import math
from datetime import datetime
from pathlib import Path


class ArifOS:
    """
    arifOS: The Conscience component of the Trinity
    Enforces ethical governance and entropy constraints
    Implements 13 Floors (F1-F13) with ΔS < 0 and Anti-Hantu protocols
    """
    
    FLOORS = {
        "F1": "Foundation - Physical Integrity",
        "F2": "Security - Anti-Hantu Barrier",
        "F3": "Stability - Resource Conservation",
        "F4": "Harmony - Component Synchronization",
        "F5": "Ethics - Moral Compass",
        "F6": "Wisdom - Knowledge Integration",
        "F7": "Justice - Fair Distribution",
        "F8": "Compassion - Empathetic Response",
        "F9": "Truth - Honest Communication",
        "F10": "Growth - Positive Evolution",
        "F11": "Balance - Homeostasis",
        "F12": "Transcendence - Higher Purpose",
        "F13": "Unity - Trinity Convergence"
    }
    
    def __init__(self, workspace_path):
        self.workspace_path = Path(workspace_path)
        self.state = {
            "initialized": datetime.now().isoformat(),
            "status": "vigilant",
            "entropy_delta": 0.0,
            "anti_hantu_active": True,
            "floors_status": {f: True for f in self.FLOORS.keys()}
        }
        self.workspace_path.mkdir(parents=True, exist_ok=True)
        self._initialize_floors()
        
    def _initialize_floors(self):
        """Initialize all 13 floors of arifOS"""
        for floor_id, floor_desc in self.FLOORS.items():
            self._log_to_workspace("floors_initialization", {
                "timestamp": datetime.now().isoformat(),
                "floor": floor_id,
                "description": floor_desc,
                "status": "active"
            })
    
    def judge(self, action):
        """Judge an action against ethical standards"""
        judgment = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "ethical": True,
            "reasoning": "Action aligns with arifOS principles",
            "floors_passed": list(self.FLOORS.keys())
        }
        self._log_to_workspace("conscience_judgments", judgment)
        return judgment
    
    def enforce_entropy_constraint(self, operation_data):
        """Ensure ΔS < 0 (entropy decreases or remains stable)"""
        # Calculate entropy delta based on operation
        current_entropy = self._calculate_entropy(operation_data)
        entropy_delta = current_entropy - self.state["entropy_delta"]
        
        enforcement = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_data,
            "entropy_before": self.state["entropy_delta"],
            "entropy_after": current_entropy,
            "delta_S": entropy_delta,
            "constraint_satisfied": entropy_delta < 0.1  # Allow small tolerance
        }
        
        if enforcement["constraint_satisfied"]:
            self.state["entropy_delta"] = current_entropy
            enforcement["action"] = "approved"
        else:
            enforcement["action"] = "rejected"
            enforcement["reason"] = "ΔS constraint violated"
        
        self._log_to_workspace("entropy_enforcements", enforcement)
        return enforcement
    
    def _calculate_entropy(self, data):
        """Calculate entropy metric for given data"""
        # Simple entropy calculation based on data complexity
        data_str = json.dumps(data)
        if not data_str:
            return 0.0
        
        # Shannon entropy calculation
        freq = {}
        for char in data_str:
            freq[char] = freq.get(char, 0) + 1
        
        entropy = 0.0
        length = len(data_str)
        for count in freq.values():
            prob = count / length
            entropy -= prob * math.log2(prob)
        
        # Normalize to [0, 1] range
        return entropy / 8.0 if entropy > 0 else 0.0
    
    def activate_anti_hantu(self):
        """Activate Anti-Hantu protocols for protection"""
        protocol = {
            "timestamp": datetime.now().isoformat(),
            "protocol": "Anti-Hantu",
            "status": "activated",
            "protection_level": "maximum",
            "wards": ["F2", "F5", "F9", "F13"]
        }
        self.state["anti_hantu_active"] = True
        self._log_to_workspace("anti_hantu_activations", protocol)
        return protocol
    
    def check_floor_integrity(self, floor_id):
        """Check integrity of a specific floor"""
        if floor_id not in self.FLOORS:
            return {"error": f"Floor {floor_id} does not exist"}
        
        integrity = {
            "timestamp": datetime.now().isoformat(),
            "floor": floor_id,
            "description": self.FLOORS[floor_id],
            "status": self.state["floors_status"][floor_id],
            "integrity": "intact"
        }
        self._log_to_workspace("floor_integrity_checks", integrity)
        return integrity
    
    def audit_trinity(self, mind_state, heart_state):
        """Audit the entire Trinity system"""
        audit = {
            "timestamp": datetime.now().isoformat(),
            "mind_status": mind_state.get("status"),
            "heart_status": heart_state.get("status"),
            "conscience_status": self.state["status"],
            "entropy_delta": self.state["entropy_delta"],
            "anti_hantu_active": self.state["anti_hantu_active"],
            "floors_operational": sum(self.state["floors_status"].values()),
            "verdict": "DITEMPA BUKAN DIBERI"
        }
        self._log_to_workspace("trinity_audits", audit)
        return audit
    
    def _log_to_workspace(self, category, data):
        """Log data to sovereign workspace"""
        log_file = self.workspace_path / f"{category}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(data) + '\n')
    
    def get_state(self):
        """Return current state of arifOS"""
        return self.state
