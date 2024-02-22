import pandas as pd 
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


#----import data----
df = pd.read_csv(io = 'https://github.com/0929230515jimmy/Tigers/blob/main/AnalyticsQuestionnaireHitData.csv?raw=True')
#df = pd.read_csv("AnalyticsQuestionnaireHitData.csv")
df["HorzBreak"] = df["HorzBreak"].abs()

#----main page overall---
st.title(":bar_chart: Overall Performance")
pitch1 = st.selectbox(
    "Select the pitch call for the overall team",
    options = df["PitchCall"].unique(),
    index=2
)
df_all = df.query(
    "PitchCall == @pitch1"
)

df_all["BatterId"] = df_all["BatterId"].astype(str)

plot1 = px.scatter(
    df_all,
    x = "LaunchSpeed",
    y = "LaunchAngle",
    color = "BatterId",
    labels = {
        "LaunchSpeed": "Launch Speed",
        "LaunchAngle": "Launch Angle",
        "PitchType": "PitchType"
    },
        title = "Launch Speed vs Launch Anglel",
    width = 800,
    height = 800
)

plot1.update_xaxes(showgrid=True)
plot1.update_yaxes(showgrid=True)
plot1.update_traces(
        marker_size=12,
        selector=dict(mode='markers')
)
plot1.update_layout(title = dict(text = "Launch Speed vs Launch Angle", font=dict(size=18)))

st.plotly_chart(plot1)

#----main page for player---
st.title(":bar_chart: Player's Performance")

#----sidebar-----
pitch = st.selectbox(
    "Select the pitch call",
    options = df["PitchCall"].unique(),
    index=2
)

player = st.selectbox(
    "Select the Batter",
    options = df["BatterId"].unique()
)

df_selection = df.query(
    "PitchCall == @pitch and BatterId == @player"
)

#---graph1---
plot = px.scatter(
    df_selection,
    x = "LaunchSpeed",
    y = "LaunchAngle",
    color = "PitchType",
    labels = {
        "LaunchSpeed": "Launch Speed",
        "LaunchAngle": "Launch Angle",
        "PitchType": "PitchType"
    },
    width = 700,
    height = 700
)

plot.update_xaxes(showgrid=True, range = [0,110])
plot.update_yaxes(showgrid=True, range = [-70,80])
plot.update_traces(
        marker_size=20,
        selector=dict(mode='markers')
    )
plot.update_layout(title = dict(text = "Launch Speed vs Launch Angle", font=dict(size=24)))

#---graph2---
plot2 = px.scatter(
    df_selection, 
    x = "VerticalBreak",
    y = "HorzBreak",
    color = "ReleaseSpeed",
    labels = {
        "VerticalBreak": "Vertical Break",
        "HorzBreak": "Horizontal Break",
    },
    width = 700,
    height = 700,
)
plot2.update_xaxes(showgrid=True, range = [0,-5])
plot2.update_yaxes(showgrid=True, range = [0,1.5])
plot2.update_xaxes(autorange="reversed")
plot2.update_traces(
        marker_size=20,
        selector=dict(mode='markers')
    )
plot2.update_layout(title = dict(text = "Vertical Break vs Horizontal Break", font=dict(size=24)))

st.plotly_chart(plot)
st.plotly_chart(plot2)
