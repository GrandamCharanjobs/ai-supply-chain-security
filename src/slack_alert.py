#!/usr/bin/env python3
import json
import sys
import os
from pathlib import Path

def send_slack_alert(risks):
    # Slack webhook format (replace with your webhook later)
    alert = {
        "text": "🚨 SUPPLY CHAIN ATTACK DETECTED!",
        "blocks": [{
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Repo:*\n{os.getenv('GITHUB_REPOSITORY', 'ai-supply-chain-security')}"},
                {"type": "mrkdwn", "text": f"*Threat:*\nMITRE T1195 - Supply Chain Compromise"}
            ]
        }]
    }
    
    for risk in risks[:3]:  # Top 3 risks
        alert["blocks"].append({
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*❌ {risk['package']}*"},
                {"type": "mrkdwn", "text": f"Risk: `{risk['risk_score']:.2f}`\n{risk['fix']}"}
            ]
        })
    
    print("📱 SLACK SOC ALERT SENT:")
    print(json.dumps(alert, indent=2))

if __name__ == "__main__":
    risks = json.loads(sys.argv[1])
    send_slack_alert(risks)
