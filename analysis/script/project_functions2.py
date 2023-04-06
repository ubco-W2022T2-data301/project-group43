import pandas as pd

def load_and_process("https://raw.githubusercontent.com/ubco-W2022T2-data301/project-group43/main/data/raw/FT1000.csv?token=GHSAT0AAAAAAB5P32QDKJMYINKJ4EJC4F4YZBPKSGA"):
    df = (pd.read_csv("https://raw.githubusercontent.com/ubco-W2022T2-data301/project-group43/main/data/raw/FT1000.csv?token=GHSAT0AAAAAAB5P32QDKJMYINKJ4EJC4F4YZBPKSGA")
      .drop(columns=['Ranked2021', 'Ranked2020'])
      .dropna()
      .query("Employees2017 != 0 and Employees2020 >= 3")
      .assign(**{'Change % in Employees': lambda x: ((x['Employees2017'] - x['Employees2020']) / x['Employees2017']) * 100}))


    return df


