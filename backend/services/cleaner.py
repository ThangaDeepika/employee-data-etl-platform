import pandas as pd


def clean_dataframe(df):

    df["EE_name"] = (
        df["EE_name"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    df["Location"] = (
        df["Location"]
        .astype(str)
        .str.strip()
    )

    return df


def remove_duplicates(df):

    return df.drop_duplicates(
        subset=["EE_ID"]
    )


def remove_negative_salary(df):

    return df[
        df["Salary"] >= 0
    ]


def remove_invalid_age(df):

    df["Age"] = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )

    return df.dropna(
        subset=["Age"]
    )


def remove_null_values(df):

    return df.dropna()