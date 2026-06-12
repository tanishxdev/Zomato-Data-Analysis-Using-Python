# src/analysis.py

import matplotlib.pyplot as plt
import seaborn as sns


def restaurant_type_analysis(df):

    plt.figure(figsize=(8, 5))

    sns.countplot(
        x=df["listed_in(type)"]
    )

    plt.title("Restaurant Types")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "images/restaurant_types.png"
    )

    plt.close()


def online_order_analysis(df):

    plt.figure(figsize=(6, 4))

    sns.countplot(
        x=df["online_order"]
    )

    plt.title("Online Order Analysis")

    plt.tight_layout()

    plt.savefig(
        "images/online_orders.png"
    )

    plt.close()


def ratings_distribution(df):

    plt.figure(figsize=(6, 4))

    plt.hist(
        df["rate"],
        bins=5
    )

    plt.title(
        "Ratings Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        "images/ratings_distribution.png"
    )

    plt.close()


def cost_analysis(df):

    plt.figure(figsize=(10, 5))

    sns.countplot(
        x=df["approx_cost(for two people)"]
    )

    plt.title(
        "Cost For Two Analysis"
    )

    plt.tight_layout()

    plt.savefig(
        "images/cost_analysis.png"
    )

    plt.close()


def ratings_vs_order_mode(df):

    plt.figure(figsize=(6, 5))

    sns.boxplot(
        x="online_order",
        y="rate",
        data=df
    )

    plt.title(
        "Ratings vs Order Mode"
    )

    plt.tight_layout()

    plt.savefig(
        "images/boxplot.png"
    )

    plt.close()


def heatmap_analysis(df):

    pivot_table = df.pivot_table(
        index="listed_in(type)",
        columns="online_order",
        aggfunc="size",
        fill_value=0
    )

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        pivot_table,
        annot=True,
        cmap="YlGnBu",
        fmt="d"
    )

    plt.title(
        "Restaurant Type vs Online Order"
    )

    plt.tight_layout()

    plt.savefig(
        "images/heatmap.png"
    )

    plt.close()