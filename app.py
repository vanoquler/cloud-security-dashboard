import streamlit as st
import plotly.express as px

from scanners.iam_scanner import scan_users
from scanners.bucket_scanner import scan_buckets

# Sidebar
st.sidebar.title("Cloud Security Dashboard")
st.sidebar.success("Version 2.0")

# Main Title
st.title("Cloud Security Dashboard")

# Run Scans
iam_findings = scan_users()
bucket_findings = scan_buckets()

all_findings = iam_findings + bucket_findings

# Risk Counts
high_count = sum(
    1 for f in all_findings
    if f["severity"] == "High"
)

medium_count = sum(
    1 for f in all_findings
    if f["severity"] == "Medium"
)

low_count = sum(
    1 for f in all_findings
    if f["severity"] == "Low"
)

# Security Score
score = max(
    0,
    100 - (
        high_count * 15 +
        medium_count * 10 +
        low_count * 5
    )
)

# Dashboard Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Security Score", score)

with col2:
    st.metric("Total Findings", len(all_findings))

with col3:
    st.metric("High Risks", high_count)

# Risk Distribution Chart
risk_data = {
    "Risk": ["High", "Medium", "Low"],
    "Count": [high_count, medium_count, low_count]
}

fig = px.pie(
    names=risk_data["Risk"],
    values=risk_data["Count"],
    title="Risk Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Findings Section
st.subheader("Security Findings")

for finding in all_findings:

    if finding["severity"] == "High":
        st.error(f"🔴 {finding['issue']}")

    elif finding["severity"] == "Medium":
        st.warning(f"🟡 {finding['issue']}")

    else:
        st.success(f"🟢 {finding['issue']}")

# Recommendations
st.subheader("Recommendations")

recommendations = set()

for finding in all_findings:

    if "MFA" in finding["issue"]:
        recommendations.add(
            "Enable MFA for all users."
        )

    if "public" in finding["issue"]:
        recommendations.add(
            "Disable public bucket access."
        )

    if "encrypted" in finding["issue"]:
        recommendations.add(
            "Enable bucket encryption."
        )

for recommendation in recommendations:
    st.info(recommendation)

# Footer
st.markdown("---")
st.caption("Cloud Security Dashboard v2.0")