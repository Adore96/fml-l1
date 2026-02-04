#%%
import pandas as pandas

def load_data_frame(path="../data/online-retail.xlsx"):
    try:
        return pandas.read_excel(path)
    except FileNotFoundError:
        return "DataFrame not found"