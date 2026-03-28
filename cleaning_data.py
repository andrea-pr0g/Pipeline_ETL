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

# This function is used to replace values that match a specific pattern with "unknown" in a specific column
def correct_int(df, column: str):
    df = df.copy()
    df[column] = df[column].str.replace(r"\d+[,.]\d+", "unknown", regex=True)
    df[column] = df[column].str.replace(r"-\d+[,.]?[\d+]?", "unknown", regex=True)
    return df

# This function is used to replace values that match a specific pattern with "unknown" in a specific column
def correct_float(df, column):
    df = df.copy()
    df[column] = df[column].str.replace(r"(\b\d+),(\d{1,2}\b)", r"\1.\2", regex=True)
    return df

# This function converts the data type of a specific column to a new data type
def convert_type(df, column: str, new_type):
    df = df.copy()
    df[column] = df[column].astype(new_type)
    return df

# This function is used to replace values that match a specific pattern with a new value in a specific column
def convert_pattern_column(df, column: str, pattern, new_value):
    df = df.copy()
    df[column] = df[column].replace(pattern, new_value, regex=True)
    return df

# This function is used to replace values that match a specific pattern with the mean value of the column in a specific column
def mean_column(df, column: str, pattern):
    df = df.copy()
    df1 = df.copy()
    df1[column] = df1[column].replace(pattern, np.nan, regex=True)
    mean_value = df1[column].astype(float).mean()
    mean_value = mean_value.astype(str)
    df[column] = df[column].replace(pattern, mean_value, regex=True)
    return df

# This function is used to convert a specific column to a datetime data type with a specific format
def convert_time(df, column: str, time_format):
    df = df.copy()
    df[column] = pd.to_datetime(df[column], format=time_format)
    return df

# This function is used to replace values that do not match a specific email pattern with "unknown" in a specific column
def correct_email(df, column: str):
    df = df.copy()
    email = r"^(?![a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
    df[column] = df[column].str.replace(email, "unknown", regex=True)
    df[column] = df[column].str.replace(r"\bunknown\w*", "unknown", regex=True)
    return df