import json

def scan_users():

    with open("data/users.json", "r") as file:
        users = json.load(file)

    findings = []

    for user in users:

        if not user["mfa_enabled"]:
            findings.append(
                f"MFA disabled for {user['username']}"
            )

        if user["role"] == "Administrator":
            findings.append(
                f"Admin privileges assigned to {user['username']}"
            )

    return findings