def print_kpis(df):

    print("\nKPI SUMMARY")

    print("-" * 40)

    print(
        f"Total Restaurants: {len(df)}"
    )

    print(
        f"Average Rating: {df['rate'].mean():.2f}"
    )

    print(
        f"Highest Votes: {df['votes'].max()}"
    )

    print(
        f"Restaurant Types: {df['listed_in(type)'].nunique()}"
    ) 