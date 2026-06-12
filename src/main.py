from load_data import load_dataset
from clean_data import clean_dataset
from kpi import print_kpis

from analysis import (
    restaurant_type_analysis,
    online_order_analysis,
    ratings_distribution,
    cost_analysis,
    ratings_vs_order_mode,
    heatmap_analysis
)


def main():

    print("=" * 50)
    print("ZOMATO DATA ANALYSIS")
    print("=" * 50)

    print("\nLoading Dataset...")

    df = load_dataset(
        "data/Zomato-data-.csv"
    )

    print("Dataset Loaded")

    print("\nCleaning Dataset...")

    df = clean_dataset(df)

    print("Dataset Cleaned")

    # KPI Summary
    print_kpis(df)

    print("\nGenerating Visualizations...")

    restaurant_type_analysis(df)

    online_order_analysis(df)

    ratings_distribution(df)

    cost_analysis(df)

    ratings_vs_order_mode(df)

    heatmap_analysis(df)

    print("\nAll Graphs Generated Successfully")

    print("\nCheck images folder")


if __name__ == "__main__":
    main()