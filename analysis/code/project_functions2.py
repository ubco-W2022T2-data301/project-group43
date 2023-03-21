import pandas as pd

def load_and_process("https://raw.githubusercontent.com/ubco-W2022T2-data301/project-group43/main/data/raw/FT1000.csv?token=GHSAT0AAAAAAB5P32QCUNOPHFDLWIWCHGRGZA2FOXA"):
    df = (
        pd.read_csv("https://raw.githubusercontent.com/ubco-W2022T2-data301/project-group43/main/data/raw/FT1000.csv?token=GHSAT0AAAAAAB5P32QCUNOPHFDLWIWCHGRGZA2FOXA")
        .drop(columns=["Ranked2021", "Ranked2020"])
        .assign(
            **{
                "Change % in Employees": lambda x: (
                    (x["Employees2017"] - x["Employees2020"]) / x["Employees2017"]
                )
                * 100
            }
        )
    )

    sector_df = (
        df.groupby("Sector")
        .mean()
        .sort_values(by="Revenue2020", ascending=False)
        .round(2)
        .drop(columns=["Rank"])
    )

    return sector_df


