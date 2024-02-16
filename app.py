import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv('jepx.df_actual.csv')
data_tokyo = df.query(
        "area.str.contains('Area.TOKYO|Area.HOKKAIDO') and frame_start_time > '2024-01-01' and frame_start_time < '2024-01-06'"
    )
fig1 = px.bar(data_tokyo, x='frame_start_time', y='price', color='area', barmode='group', color_discrete_sequence=px.colors.qualitative.Vivid)
fig2 = px.line(data_tokyo, x='frame_start_time', y='price', color='area', color_discrete_sequence=px.colors.qualitative.Vivid)

# Plot!
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
