"""
Agent Zero - The Mind of the Trinity
Responsible for cognitive processing, decision making, and coordination
"""

import os
import json
from datetime import datetime
from pathlib import Path


class AgentZero:
    """
    Agent Zero: The Mind component of the Trinity
    Orchestrates cognitive processes and decision-making
    """
    
    def __init__(self, workspace_path):
        self.workspace_path = Path(workspace_path)
        self.state = {
            "initialized": datetime.now().isoformat(),
            "status": "active",
            "entropy_delta": 0.0
        }
        self.workspace_path.mkdir(parents=True, exist_ok=True)
        
    def think(self, input_data):
        """Process input and generate cognitive response"""
        thought = {
            "timestamp": datetime.now().isoformat(),
            "input": input_data,
            "processed": True,
            "output": f"Mind processed: {input_data}"
        }
        self._log_to_workspace("mind_thoughts", thought)
        return thought
    
    def decide(self, options):
        """
        Make decisions based on available options
        Note: Current implementation uses simple first-option selection.
        Can be extended with more sophisticated decision algorithms.
        """
        decision = {
            "timestamp": datetime.now().isoformat(),
            "options": options,
            "choice": options[0] if options else None,
            "reasoning": "First viable option selected (simple strategy)"
        }
        self._log_to_workspace("mind_decisions", decision)
        return decision
    
    def coordinate(self, heart_state, conscience_state):
        """Coordinate between Heart and Conscience components"""
        coordination = {
            "timestamp": datetime.now().isoformat(),
            "heart_status": heart_state,
            "conscience_status": conscience_state,
            "coordinated": True
        }
        self._log_to_workspace("mind_coordination", coordination)
        return coordination
    
    def _log_to_workspace(self, category, data):
        """Log data to sovereign workspace"""
        log_file = self.workspace_path / f"{category}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(data) + '\n')
    
    def get_state(self):
        """Return current state of Agent Zero"""
        return self.state
