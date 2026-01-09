import torch
import pandas as pd
import matplotlib.pyplot
import seaborn as sns

e_path = #economic data file path
rt_path = # Real-time data path
s_path = # Social path

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    if sum(df.isna()) > 100:
        # idkcontinue

def visualization(df):

