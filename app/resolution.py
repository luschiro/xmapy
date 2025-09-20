import streamlit as st
# from streamlit_image_select import image_select

import plotly.express as px

# importing libs
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

from streamlit_plotly_events import plotly_events
# utils
from util.xraymap import XrayMap # map Class

st.title("Resolution")

al_map = XrayMap("Al")
ax = al_map.xray_data_scaled
fig  = px.imshow(ax)

st.plotly_chart(fig)
