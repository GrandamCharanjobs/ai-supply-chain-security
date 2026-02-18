#!/usr/bin/env python3
import json
import sys
import subprocess
from pathlib import Path

class SupplyChainAI:
    def __init__(self):
        self.known_threats = {
            "malicious-package": {"risk": 0.92, "cve": "CVE-2025-1234"},
            "crypto-miner-lib": {"risk": 0.87, "cve": "CVE-2025-5678"},
            "backdoor-utils": {"risk": 0.95, "cve": "CVE-2025-9999"}
        }
    
    def scan_package_json(self, path):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            
            risks = []
            for dep in data.get('dependencies', {}).keys():
                if dep in self.known_threats:
                    risks.append({
                        'package': dep,
                        'risk_score': self.known_threats[dep]['risk'],
                        'threat': 'MITRE T1195 - Supply Chain Compromise',
                        'fix': f'Remove {dep} (CVE: {self.known_threats[dep]["cve"]})',
                        'path': str(path)
                    })
            return risks
        except:
            return []
    
    def analyze(self):
        risks = []
        for pkg_path in Path('.').rglob('package.json'):
            risks.extend(self.scan_package_json(pkg_path))
        
        if risks:
            print("🚨 AI SUPPLY CHAIN RISKS DETECTED:")
            for risk in risks:
                print(f"  ❌ {risk['package']}: Risk {risk['risk_score']:.2f}")
                print(f"     {risk['threat']}")
                print(f"     Fix: {risk['fix']}")
            
            # Save risks for Slack
            print(f"::notice file=supply_chain_risks.json ::{json.dumps(risks)}")
            sys.exit(1)
        else:
            print("✅ No supply chain risks detected")
            sys.exit(0)

if __name__ == "__main__":
    SupplyChainAI().analyze()
