import plotly.express as px
import streamlit as st

from scanners.iam_scanner import scan_users
from scanners.bucket_scanner import scan_buckets

st.title("Cloud Security Dashboard")

iam_findings = scan_users()
bucket_findings = scan_buckets()

all_findings = iam_findings + bucket_findings

st.subheader("Security Findings")

for finding in all_findings:

    if finding["severity"] == "High":
        st.error(f"🔴 {finding['issue']}")

    elif finding["severity"] == "Medium":
        st.warning(f"🟡 {finding['issue']}")

    else:
        st.success(f"🟢 {finding['issue']}")

score = max(0, 100 - (len(all_findings) * 10))

st.subheader("Security Score")
st.metric("Score", score)