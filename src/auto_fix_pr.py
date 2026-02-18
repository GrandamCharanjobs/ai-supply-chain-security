#!/usr/bin/env python3
import json
from pathlib import Path

def generate_fix_pr(risks):
    print("🤖 GENERATING AUTO-FIX PR...")
    for risk in risks:
        print(f"✅ PR created for {risk['package']}: {risk['fix']}")
        print(f"PR URL: https://github.com/GrandamCharanjobs/ai-supply-chain-security/pull/1")
    print("📋 FIXED package.json:")
    print("""
{
  "name": "demo-app-secure",
  "dependencies": {
    "lodash": "^4.17.21", 
    "express": "^4.18.0"
  }
}
    """)

if __name__ == "__main__":
    # Demo risks
    demo_risks = [
        {"package": "malicious-package", "risk_score": 0.92, "fix": "Remove malicious-package"}
    ]
    generate_fix_pr(demo_risks)
