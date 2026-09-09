import pandas as pd


def count_null_records(df):

    return df.isnull().any(axis=1).sum()


def count_duplicate_records(df):

    return df.duplicated(
        subset=["EE_ID"]
    ).sum()


def count_negative_salary(df):

    return (
        df["Salary"] < 0
    ).sum()


def count_invalid_age(df):

    age_series = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )

    return age_series.isna().sum()