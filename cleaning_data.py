import pandas as pd
import numpy as np
import re
from rapidfuzz import fuzz

def load_csv(path):
    return pd.read_csv(path)

def clean_pattern_column(df, column, pattern):
    df = df.copy()
    df[column] = df[column].replace(pattern, np.nan, regex=True)
    return df