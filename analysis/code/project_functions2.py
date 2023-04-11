import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


def load_and_process(url):
    df_new = (pd.read_csv("../data/raw/FT1000.csv")
      .drop(columns=['Ranked2021', 'Ranked2020'])
      .dropna()
      .query("Employees2017.between(10, 250) and Employees2020.between(10, 250)")
      .assign(**{'Change % in Employees': lambda x: ((x['Employees2020'] - x['Employees2017']) / x['Employees2020']) * 100}))

    sector_df = (df.groupby("Sector").mean()
                 .sort_values(by='Revenue2020', ascending=False)
                 .round(2)
                 .drop(columns=['Rank']))

    return df_new


