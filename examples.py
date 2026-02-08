#!/usr/bin/env python3
"""
Example usage of the oo0-STATE Trinity System
Demonstrates Mind, Heart, and Conscience working together
"""

from trinity_integration import Trinity
import json


def example_basic_usage():
    """Basic Trinity usage example"""
    print("=" * 60)
    print("Example 1: Basic Trinity Usage")
    print("=" * 60)
    
    trinity = Trinity()
    
    # Process some input
    result = trinity.process("Calculate optimal path")
    print(f"\n✓ Processed input through Trinity")
    print(f"  Mind thought: {result['thought']['output']}")
    print(f"  Heart executed: {result['execution']['status']}")
    print(f"  Conscience judgment: {result['judgment']['ethical']}")
    print(f"  Entropy check: ΔS = {result['entropy_check']['delta_S']:.4f}")


def example_floor_checking():
    """Check all arifOS floors"""
    print("\n" + "=" * 60)
    print("Example 2: Floor Integrity Checks")
    print("=" * 60)
    
    trinity = Trinity()
    
    # Check critical floors
    critical_floors = ["F2", "F5", "F9", "F13"]
    print("\n✓ Checking critical floors:")
    for floor in critical_floors:
        status = trinity.check_floor(floor)
        print(f"  {floor} ({status['description']}): {status['integrity']}")


def example_multi_processing():
    """Process multiple inputs"""
    print("\n" + "=" * 60)
    print("Example 3: Multiple Operations")
    print("=" * 60)
    
    trinity = Trinity()
    
    inputs = [
        "Analyze system status",
        "Optimize resource usage",
        "Verify security protocols"
    ]
    
    print("\n✓ Processing multiple inputs:")
    for input_data in inputs:
        result = trinity.process(input_data)
        print(f"  - {input_data}: {result['execution']['status']}")


def example_trinity_audit():
    """Perform complete Trinity audit"""
    print("\n" + "=" * 60)
    print("Example 4: Trinity System Audit")
    print("=" * 60)
    
    trinity = Trinity()
    
    # Process some operations first
    trinity.process("Initialize audit sequence")
    trinity.process("Verify all components")
    
    # Perform audit
    audit = trinity.audit()
    print(f"\n✓ Audit Results:")
    print(f"  Mind Status: {audit['mind_status']}")
    print(f"  Heart Status: {audit['heart_status']}")
    print(f"  Conscience Status: {audit['conscience_status']}")
    print(f"  Floors Operational: {audit['floors_operational']}/13")
    print(f"  Anti-Hantu: {'Active' if audit['anti_hantu_active'] else 'Inactive'}")
    print(f"  Verdict: {audit['verdict']}")


def example_complete_status():
    """Get complete Trinity status"""
    print("\n" + "=" * 60)
    print("Example 5: Complete System Status")
    print("=" * 60)
    
    trinity = Trinity()
    
    status = trinity.get_status()
    print(f"\n✓ System Status:")
    print(f"  Mind: {status['mind']['status']}")
    print(f"  Heart: {status['heart']['status']} ({status['heart']['operations']} operations)")
    print(f"  Conscience: {status['conscience']['status']}")
    print(f"  Workspace: {status['workspace']}")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("oo0-STATE Trinity System - Usage Examples")
    print("DITEMPA BUKAN DIBERI")
    print("=" * 60 + "\n")
    
    example_basic_usage()
    example_floor_checking()
    example_multi_processing()
    example_trinity_audit()
    example_complete_status()
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("Check sovereign_data/workspace/ for detailed logs")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
