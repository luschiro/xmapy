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
from xraymap import XrayMap # map Class

st.title("Resolution")

al_map = XrayMap("Al")
ax = al_map.xray_data_scaled
fig  = px.imshow(ax)

st.plotly_chart(fig)

# nl = list(range(0,al_map.dimensions[0]))

# nc = list(range(0,al_map.dimensions[1]))

# y_idx, x_idx = np.indices(ax.shape)   # rows (y), cols (x)
# df_pixels = pd.DataFrame({
#     "x": x_idx.ravel(),
#     "y": y_idx.ravel()
# })

# fig.add_trace(
#   go.Scatter(
#         x=df_pixels["x"],
#         y=df_pixels["y"],
#         mode="markers",
#         marker=dict(color="red", size=0.01)
#     )
# )

# fig.update_yaxes(autorange="reversed")
# event = st.plotly_chart(fig)
# st.write(event)


# st.write(selected_points)
