import torch
import pandas as pd
import matplotlib.pyplot
import seaborn as sns

e_path = ''# Economic data file path
rt_path = '/fishhealth_norway_rt.csv'# Real-time data path
s_path = ''# Social path

def load_data(path1, path2, path3):
    social_data = pd.read_csv(path1)
    economic_data = pd.read_csv(path2)
    rt_data = pd.read_csv(path3)
    return social_data, economic_data, rt_data

def clean_rt_data(df):
    # Data Cleaning for Social Data
    if df == social_data:
        blablabal
    # Data Cleaning for Economic Data
    if df == economic_data:
        blabla
    # Data Cleaning for Real-Time Data
    if df == rt_data:
        for item in df['Status']:
            if item == 'Påvist':
                str.replace('Detected')
            elif item == 'Mistanke':
                str.replace('Suspected')
            else:
                None
    
    # Dropping NAs    !!!! DOUBLE CHECK IF NECESSARY!!!!
    if sum(df.isna()) > 100:
        # idkcontinue
    cleaned_data = df.dropna()
    return cleaned_data

def visualization(df):
    graphs = [plot for x, y in df] # obv not correct but we'll figure out what exactly we may want to plot
    return graphs
