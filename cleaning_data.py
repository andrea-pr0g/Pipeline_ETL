import pandas as pd
import numpy as np
import re
from rapidfuzz import fuzz

# This function is used to load a csv file and return a pandas dataframe
def load_csv(path):
    return pd.read_csv(path)

# This function is used to replace values that match a specific pattern with NA values in a specific column
def clean_pattern_column(df, column: str, pattern):
    df = df.copy()
    df[column] = df[column].replace(pattern, np.nan, regex=True)
    return df

# This function is used to delete rows with NA values in a specific column
def delete_na(df, column: str):
    df = df.copy()
    df.dropna(subset=[column], inplace=True)
    return df