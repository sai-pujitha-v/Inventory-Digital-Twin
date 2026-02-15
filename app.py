import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

st.set_page_config(page_title="TwinLogix 3D", layout="wide", page_icon="📦")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stMetric { background-color: #1e293b; border-radius: 8px; padding: 15px; border: 1px solid #334155; }
    </style>
    """, unsafe_allow_html=True)

if 'twin_data' not in st.session_state:
    data = {
        'Item': [f'SKU-{100+i}' for i in range(50)],
        'X': np.random.randint(0, 10, 50),
        'Y': np.random.randint(0, 20, 50),
        'Z': np.random.randint(0, 5, 50),
        'Stock': np.random.randint(10, 500, 50)
    }
    st.session_state.twin_data = pd.DataFrame(data)

st.title("📦 TwinLogix | Warehouse Digital Twin")
st.write("Real-time Spatial Inventory Monitoring & 3D Mapping")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Warehouse Capacity", "82%", delta="2.1%")
m2.metric("Active SKUs", len(st.session_state.twin_data))
m3.metric("Pick Efficiency", "94.5%")
m4.metric("Sync Status", "LIVE")

col_map, col_list = st.columns([2, 1])

with col_map:
    st.subheader("3D Warehouse Spatial View")
    fig = go.Figure(data=[go.Scatter3d(
        x=st.session_state.twin_data['X'],
        y=st.session_state.twin_data['Y'],
        z=st.session_state.twin_data['Z'],
        mode='markers',
        marker=dict(
            size=st.session_state.twin_data['Stock']/20,
            color=st.session_state.twin_data['Stock'],
            colorscale='Viridis',
            opacity=0.8
        ),
        text=st.session_state.twin_data['Item']
    )])
    fig.update_layout(template="plotly_dark", margin=dict(l=0, r=0, b=0, t=0), 
                      scene=dict(xaxis_title='Aisle', yaxis_title='Row', zaxis_title='Level'))
    st.plotly_chart(fig, use_container_width=True)

with col_list:
    st.subheader("Inventory Telemetry")
    search = st.text_input("Search SKU:")
    df_disp = st.session_state.twin_data
    if search:
        df_disp = df_disp[df_disp['Item'].str.contains(search)]
    st.dataframe(df_disp[['Item', 'Stock']], height=400)

for i in range(100):
    idx = np.random.randint(0, 50)
    st.session_state.twin_data.at[idx, 'Stock'] += np.random.randint(-5, 6)
    time.sleep(5)
    st.rerun()
