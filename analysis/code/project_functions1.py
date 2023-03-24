import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    # Create a copy of the original DataFrame and drop the 'Rank' column
    df1 = df.copy().drop(['Rank'], axis=1)

# MC1: Filter the DataFrame to include only rows where 'Employees2017' is > 0
    df2 = df1[df1['Employees2017'] > 0]

# MC2: the DataFrame to include only rows where 'Employees2020' is > 2
    df3 = df2[df2['Employees2020'] > 2]

    #MC2: Convert the data types of several columns
    df4 = df3.astype({'Name': 'str',
                                'Ranked2021': 'category',
                                'Ranked2020': 'category',
                                'Country': 'category',
                                'Sector': 'category'})

    # MC3: 
    column_labels = {'Name': 'Name',
                     'Ranked2021': 'Ranked 2021?',
                     'Ranked2020': 'Ranked 2020?',
                     'Country': 'Country',
                     'Sector': 'Sector',
                     'CAGR': 'CAGR %',
                     'Revenue2020': '2020 Revenue ($)',
                     'Revenue2017': '2017 Revenue ($)',
                     'Employees2020': 'Employees in 2020',
                     'Employees2017': 'Employees in 2017',
                     'FoundingYear': 'FoundingYear'}

    df5 = df4.rename(columns=column_labels)

    return df5
