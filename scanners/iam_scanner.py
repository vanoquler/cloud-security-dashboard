import json

def scan_users():

    with open("data/users.json", "r") as file:
        users = json.load(file)

    findings = []

    for user in users:

        if not user["mfa_enabled"]:
            findings.append({
                "issue": f"MFA disabled for {user['username']}",
                "severity": "High"
            })

        if user["role"] == "Administrator":
            findings.append({
                "issue": f"Admin privileges assigned to {user['username']}",
                "severity": "Medium"
            })

    return findings