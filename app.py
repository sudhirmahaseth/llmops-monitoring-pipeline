import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

# 1. Dashboard Layout Settings
st.set_page_config(
    page_title="LLMOps Enterprise Monitoring Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 LLMOps Infrastructure & Model Monitoring Dashboard")
st.subheader("Real-Time Prometheus & Grafana Metrics Simulation (AWS EKS)")
st.markdown("---")

# 2. Sidebar Settings & Architecture Info
st.sidebar.header("⚙️ Infrastructure Controls")
refresh_rate = st.sidebar.slider("Metrics Refresh Rate (seconds)", 1, 5, 2)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏢 Deployment Spec")
st.sidebar.code("""
Cluster: AWS EKS v1.28
Orchestrator: Kubernetes
Caching: Redis Cluster
Metrics: Prometheus
Visuals: Grafana / Streamlit
""")

# 3. Simulate Live Cluster Data Metrics
np.random.seed(int(time.time()))

# High-level Metrics Row
col1, col2, col3, col4 = st.columns(4)

# Data Generations
p95_latency = round(np.random.uniform(160, 195), 2)  # Simulating sub-200ms latency
token_saving = 30  # As per CV optimization
cost_reduced = "30%"
hallucination_rate = round(np.random.uniform(0.5, 2.4), 2)
semantic_drift = round(np.random.uniform(0.01, 0.08), 3)

with col1:
    st.metric(label="⏱️ P95 Response Latency", value=f"{p95_latency} ms", delta="-15ms (Optimal)")
with col2:
    st.metric(label="💰 Redis Token Cache Hit Rate", value=f"{token_saving}%", delta="+5% Efficiency")
with col3:
    st.metric(label="📉 Inference Cost Reduction", value=cost_reduced, delta="-30% AWS Budget")
with col4:
    st.metric(label="⚠️ Hallucination Index", value=f"{hallucination_rate}%", delta="-0.4% Drift")

st.markdown("---")

# 4. Graphs & Visualizations
col_left, col_right = st.columns(2)

# Generate Fake Time Series Data for Latency Trend
timestamps = pd.date_range(end=pd.Timestamp.now(), periods=20, freq='min')
latency_trend = np.random.uniform(150, 210, size=20)
# Ensure p95 behavior
latency_trend[12] = 205  # Slight bump

df_latency = pd.DataFrame({'Time': timestamps, 'p95 Latency (ms)': latency_trend})

with col_left:
    st.markdown("### 📈 Live Request Latency Trend (Target: < 200ms)")
    fig_lat = px.line(df_latency, x='Time', y='p95 Latency (ms)', markers=True, color_discrete_sequence=['#00CC96'])
    fig_lat.add_hline(y=200, line_dash="dash", line_color="red", annotation_text="SLA Breached (>200ms)")
    fig_lat.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_lat, use_container_width=True)

# Generate Fake Data for Token Optimization Split
with col_right:
    st.markdown("### 🗄️ Redis Semantic Cache Token Processing")
    labels = ['Cached Hits (Zero Cost)', 'Direct Model Inference API']
    values = [30, 70]
    fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, marker=dict(colors=['#636EFA', '#EF553B']))])
    fig_pie.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# 5. Simulated Kubernetes HPA (Horizontal Pod Autoscaler) Logging
st.markdown("### ⚓ Live Kubernetes Pod Cluster Event Logs (AWS EKS)")
log_container = st.container(border=True)

with log_container:
    current_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    st.code(f"""
[{current_time}] [INFO] [Prometheus] Scraping endpoint metrics from Triton Inference Server...
[{current_time}] [INFO] [Redis] Semantic cache lookup successful. Token savings actively logged.
[{current_time}] [SUCCESS] [Kubernetes-HPA] Current average CPU utilization at 72%. Active replica count maintained.
[{current_time}] [METRIC] [Model Monitor] Semantic Drift Factor: {semantic_drift} (Status: Safe).
[{current_time}] [SUCCESS] All systems operational. 99.9% target SLA uptime verified.
    """)

# Interactive Trigger Button to Simulate Live System Re-check
if st.button("🔄 Trigger Manual Prometheus Metric Scrape"):
    st.toast("Prometheus cluster metrics fetched successfully!", icon="✅")
              
