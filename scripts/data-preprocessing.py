# Import visualization libraries

import plotly.express as px # simple and interactive plots
import plotly.graph_objects as go # customizable and advanced visualizations
import plotly.figure_factory as ff # complex and specialized visualizations
import plotly.subplots as make_subplots # function to make subplots in Plotly, make arranging multiple plots together available

import matplotlib.pyplot as plt # traditional 2D plotting
%matplotlib inline
# display plots directly in Jupyter notebook
import seaborn as sns # attractive statistical graphics (built on top of Matplotlib)


# Import data processing libraries

import numpy as np
import pandas as pd


# Import EDA supporting library

!pip install ydata-profiling
from ydata_profiling import ProfileReport


# Import dataset

df = pd.read_csv('')


df.head()


df.shape


df.info()


report = ProfileReport(df)
report


# Check missing values

df.isna().sum()


# Check unique values

df.nunique()


