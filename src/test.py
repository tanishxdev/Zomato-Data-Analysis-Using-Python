from load_data import load_dataset
from clean_data import clean_dataset

df = load_dataset(
    "data/Zomato-data-.csv"
)

print("Before Cleaning:")
print(df["rate"].head())

df = clean_dataset(df)

print("\nAfter Cleaning:")
print(df["rate"].head())

print("\nDatatype:")
print(df["rate"].dtype)