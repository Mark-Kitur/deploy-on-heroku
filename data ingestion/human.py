
import logging
import subprocess
import os
import yaml
import datetime
import gc
import re
import pandas as pd


# read file
def read_file(filepath):
    with open (filepath, 'r') as file:
        return yaml.safe_load(file)
            
# Converts string data to numerical  and stores it to dictionary
def convert_string_interger(df):
    # dictionary to store data
    column_identifier={}
    
    for column in df.columns:
        if df[column].dtype == object:
            # Extract unique strings from the colun
            unique_strings = df[column].unique()
            # crrate dictionary mapping
            string_identifier = {string: i for i, string in enumerate(unique_strings)}
            
            # store mapping to the dictionary
            column_identifier [column] =string_identifier
            
            # mapp to dataframe
            df[column] =df[column].apply(lambda x: string_identifier.get(x,float('nan')))
            
    return df
def filedata(df):
    keys = ['columns', 'rows']
    N_values = [df.columns.tolist(), df.to_dict(orient='records')]
    dicto = dict(zip(keys, N_values))
    return dicto

