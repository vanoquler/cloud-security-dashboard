# Cloud Security Dashboard

A Python-based Cloud Security Dashboard built with Streamlit that helps identify security risks in cloud environments through IAM and storage security analysis.

## Features

### Version 2 Features

* IAM Security Auditing
* Storage Bucket Security Analysis
* Severity-Based Findings (High, Medium, Low)
* Security Score Calculation
* Risk Distribution Visualization
* Security Recommendations Engine
* Interactive Dashboard UI

## Tech Stack

* Python
* Streamlit
* Plotly
* JSON
* Git & GitHub

## Project Structure

```text
cloud-security-dashboard/
│
├── app.py
├── data/
│   ├── users.json
│   └── buckets.json
│
├── scanners/
│   ├── iam_scanner.py
│   ├── bucket_scanner.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/vanoquler/cloud-security-dashboard.git
cd cloud-security-dashboard

pip install -r requirements.txt

streamlit run app.py
```

## Current Capabilities

* Detects disabled MFA accounts
* Detects privileged administrator accounts
* Detects public storage buckets
* Detects unencrypted storage buckets
* Calculates a security score
* Categorizes findings by severity
* Generates security recommendations

## Future Improvements

### Version 3

* JSON File Upload Scanner
* Dynamic Risk Analysis
* User-Supplied Cloud Configuration Scanning

### Version 4

* PDF Report Generation
* Historical Security Trends
* Advanced Visualizations

### Version 5

* AWS Integration
* Azure Integration
* GCP Integration
* AI Security Recommendations

## Author

**Vansh Sharma**

Cloud Security & AI Enthusiast

