"""
OpenClaw - The Heart of the Trinity
Responsible for resource management, execution, and physical operations
"""

import os
import json
from datetime import datetime
from pathlib import Path


class OpenClaw:
    """
    OpenClaw: The Heart component of the Trinity
    Manages resources and executes operations
    """
    
    def __init__(self, workspace_path):
        self.workspace_path = Path(workspace_path)
        self.state = {
            "initialized": datetime.now().isoformat(),
            "status": "beating",
            "resources": {},
            "operations": 0
        }
        self.workspace_path.mkdir(parents=True, exist_ok=True)
        
    def execute(self, operation):
        """Execute an operation with the Heart's power"""
        execution = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "status": "executed",
            "result": f"Heart executed: {operation}"
        }
        self.state["operations"] += 1
        self._log_to_workspace("heart_executions", execution)
        return execution
    
    def grasp(self, resource):
        """Grasp and manage a resource"""
        resource_id = f"resource_{len(self.state['resources'])}"
        self.state["resources"][resource_id] = {
            "data": resource,
            "grasped_at": datetime.now().isoformat()
        }
        grasp_event = {
            "timestamp": datetime.now().isoformat(),
            "resource_id": resource_id,
            "resource": resource,
            "status": "grasped"
        }
        self._log_to_workspace("heart_grasps", grasp_event)
        return grasp_event
    
    def release(self, resource_id):
        """Release a grasped resource"""
        if resource_id in self.state["resources"]:
            resource = self.state["resources"].pop(resource_id)
            release_event = {
                "timestamp": datetime.now().isoformat(),
                "resource_id": resource_id,
                "status": "released"
            }
            self._log_to_workspace("heart_releases", release_event)
            return release_event
        return None
    
    def pulse(self):
        """Send a heartbeat pulse to the system"""
        pulse_event = {
            "timestamp": datetime.now().isoformat(),
            "beat": "thump",
            "operations_count": self.state["operations"],
            "resources_held": len(self.state["resources"])
        }
        self._log_to_workspace("heart_pulses", pulse_event)
        return pulse_event
    
    def _log_to_workspace(self, category, data):
        """Log data to sovereign workspace"""
        log_file = self.workspace_path / f"{category}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(data) + '\n')
    
    def get_state(self):
        """Return current state of OpenClaw"""
        return self.state
