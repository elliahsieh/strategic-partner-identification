# Data Visualization Libraries
import plotly.express as px            # For simple and interactive plots
import plotly.graph_objects as go       # For customizable and advanced visualizations
import plotly.figure_factory as ff      # For complex and specialized visualizations
import plotly.subplots as make_subplots # For creating subplots in Plotly
import matplotlib.pyplot as plt         # Traditional 2D plotting
import seaborn as sns                   # Statistical graphics built on top of Matplotlib

# Display plots directly in Jupyter Notebook (if using a notebook)
%matplotlib inline 

# Data Processing Libraries
import numpy as np
import pandas as pd

# Exploratory Data Analysis (EDA) Supporting Library
# Ensure 'ydata-profiling' is installed in the environment (use requirements.txt or environment.yml)
from ydata_profiling import ProfileReport

# Load Dataset
# Provide the file path for the dataset
file_path = 'your_dataset.csv'
df = pd.read_csv(file_path)

# Quick overview of the data
print("First 5 rows of the dataset:")
display(df.head())

print("\nDataset shape:", df.shape)

print("\nDataset info:")
df.info()

# Generate EDA Report
print("\nGenerating Profile Report...")
report = ProfileReport(df)
report.to_notebook_iframe()  # Display the report in Jupyter Notebook

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isna().sum())

# Check for unique values in each column
print("\nNumber of unique values per column:")
print(df.nunique())
