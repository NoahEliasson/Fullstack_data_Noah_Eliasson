import streamlit as st 
import pandas as pd 
from pathlib import Path

def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "cleaned_yh.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df



def layout():
    df = read_data()

    st.markdown("# YH dashboard")
    st.dataframe(df)


if __name__ == "__main__":
    layout()