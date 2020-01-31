import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog


data={'x' : pd.DataFrame(np.arange(10).reshape(5,-1)),
      'y' : pd.DataFrame(np.arange(10).reshape(5,-1))}
z=pd.Panel(data).to_frame()
z['x']


