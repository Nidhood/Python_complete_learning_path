import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# First we import the data:
bike_h_df = pd.read_csv('bike+sharing+dataset/hour.csv')
bike_d_df = pd.read_csv('bike+sharing+dataset/day.csv')

# What time of year should I make sure I have the most bikes available?
# We select the usefully fields for the answer:
# ->