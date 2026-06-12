# src/clean_data.py

def handle_rate(value):
    """
    Convert:
    4.1/5 -> 4.1
    """

    value = str(value).split('/')

    return float(value[0])


def clean_dataset(df):
    """
    Data cleaning and preprocessing
    """

    df["rate"] = df["rate"].apply(handle_rate)

    return df