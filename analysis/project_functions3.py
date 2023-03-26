import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(path):
    df = pd.read_csv(path)
    # We first look for delimeters by running the following code:

    delimiters = [',', ';', '\t', '|']

    for delimiter in delimiters:
        try:
            df = pd.read_csv(pd.compat.StringIO(df.to_csv(index=False)), delimiter=delimiter)
            print(f"Delimiter found: '{delimiter}'")
            break
        except:
            pass

    # No Delimeters found.

    # MC 1 - Dropping Rank as redundant and I am now looking to delete all blank values in the data:
    df_new = (df.copy().drop(['Rank','Ranked2021','Ranked2020','Country', 'FoundingYear'], axis=1).dropna(axis=0).dropna(axis=1)) 

    # We can confirm that are no empty values in the data.

    # Dropping companies that had no CAGR over the given period of time
    df_new = df_new[df['CAGR'] > 0]

    # Renaming Rows
    column_labels = {'Name':'Name',
                 'Sector':'Sector',
                 'CAGR':'CAGR %',
                 'Revenue2020':'2020 Revenue ($)',
                 'Revenue2017':'2017 Revenue ($)',
                 'Employees2020':'Employees in 2020',
                 'Employees2017':'Employees in 2017',
                 }
    df_new.rename(columns= column_labels, inplace=True)


    # I sorted the data by the sector to better answer my questions:

    df_new = df_new.groupby("Sector").mean()

    ## I added the row Change % in Revenue to see the increase or decrease in revenue in percentage over the period of time.

    df_new['Change % in Revenue'] = ((df_new['2020 Revenue ($)'] - df_new['2017 Revenue ($)']) / df_new['2017 Revenue ($)']) * 100

    df_new = df_new.sort_values(by='CAGR %', ascending=False)
    df_new
    