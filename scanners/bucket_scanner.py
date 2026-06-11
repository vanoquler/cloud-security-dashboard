import json

def scan_buckets():

    with open("data/buckets.json", "r") as file:
        buckets = json.load(file)

    findings = []

    for bucket in buckets:

        if bucket["public"]:
            findings.append(
                f"Bucket {bucket['name']} is public"
            )

        if not bucket["encrypted"]:
            findings.append(
                f"Bucket {bucket['name']} is not encrypted"
            )

    return findings