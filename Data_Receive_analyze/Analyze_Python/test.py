import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Read data from a csv

#z_data = pd.dataframe(r'C:\Users\abc47\Desktop\VLP\RotateVLP\Data_Receive_analyze\Data\2019_8_23\csv_arranged\data_15_1.csv')
z_data=np.array([[0,1,2],[0,1,2],[0,1,2]])
fig = go.Figure(data=[go.Surface(z=z_data)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=1000, height=1000,
                  margin=dict(l=65, r=50, b=65, t=90))

#fig.write_image(file='fig1.png',format="png", width=600, height=350, scale=10)
fig.write_html('first_figure.html', auto_open=True)