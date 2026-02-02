import torch
import pandas as pd
import matplotlib.pyplot
import seaborn as sns

e_path = '/Cost.csv'# Economic data file path
rt_path = '/checklist-cat.csv'# Real-time data path
s_path = ''# Social path

# Can be used to connect to a database if one of our sources ends up being postgresSQL
# import pandas as pd conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd)) sql = "select count(*) from table;" dat = pd.read_sql_query(sql, conn) conn = None

def load_data(path1, path2, path3):
    """ Loads all data source files (code subject to change)"""
    social_data = pd.read_csv(path1)
    economic_data = pd.read_csv(path2)
    rt_data = pd.read_csv(path3)
    return social_data, economic_data, rt_data

def clean_data(social, economic, real_time):
    """Translation and filtering for all source datasets"""
    # Data Cleaning for Social Data
    social[''] = social['']
    # Data Cleaning for Economic Data
    economic[''] = pd.to_numeric(economic[''])
    # Data Cleaning for Real-Time Data
    real_time[['year'], ['occurenceCount']] = pd.to_numeric(real_time[['year'], ['occurrenceCount']])
    real_time = real_time[real_time['year'] >= 1960]

    
    # Dropping NAs    !!!! DOUBLE CHECK IF NECESSARY!!!!
    cols_to_drop = df.columns[df.isna().sum() > 1000000]
    df = df.drop(columns=cols_to_drop)


        # idkcontinue
    cleaned_data = df.dropna()
    return cleaned_data

def visualization(df):
    """ Plots, graphs, etc to display how data correlates, helpful for inferences"""
    graphs = [plot for x, y in df] # obv not correct but we'll figure out what exactly we may want to plot
    return graphs
