# %%
import pandas as pandas

def load_data_frame(path="../data/online-retail.xlsx"):
    try:
        print("Loading DataFrame...")
        dataframe = pandas.read_excel(path)
        print(f"DataFrame loaded with {dataframe.shape[0]} rows and {dataframe.shape[1]} columns.")
        return dataframe
    except FileNotFoundError:
        return "DataFrame not found"
    except Exception as e:
        return f"Error loading DataFrame: {e}"
