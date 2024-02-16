import streamlit as st
import plotly.express as px
import pandas as pd
import datetime


def plot_snapshot(start: datetime, end: datetime, type: str):
    print(px.colors.qualitative.Vivid)
    df = pd.read_csv('jepx.df_actual.csv')
    data_tokyo = df.query(f"area.str.contains('Area.TOKYO|Area.HOKKAIDO') and frame_start_time > '{start}' and frame_start_time < '{end}'")
    if type == "line":
        return px.line(data_tokyo, x='frame_start_time', y='price', color='area', color_discrete_sequence=['rgb(0, 0, 255)', 'rgb(255, 0, 0)'])
    if type == "bar":
        return px.bar(data_tokyo, x='frame_start_time', y='price', color='area', barmode='group', color_discrete_sequence=['rgb(0, 0, 255)', 'rgb(255, 0, 0)'])


st.set_page_config(layout="wide")
st.subheader("グラフ表示")
col1, col2 = st.columns(2)
with col1:
    start = st.date_input(label="表示開始日", value=datetime.date(2024, 1, 1))
with col2:
    end = st.date_input(label="表示終了日", value=datetime.date(2024, 1, 5))
# 折れ線フラグ
st.plotly_chart(plot_snapshot(start=start, end=end, type="line"), use_container_width=True)
# バーグラフ
st.plotly_chart(plot_snapshot(start=start, end=end, type="bar"), use_container_width=True)