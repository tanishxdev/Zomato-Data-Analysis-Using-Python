# Zomato Data Analysis Using Python

## Overview

This project performs Exploratory Data Analysis (EDA) on a Zomato restaurant dataset using Python. The objective is to understand customer preferences, restaurant trends, online ordering behavior, ratings, and pricing patterns through data cleaning, analysis, and visualization.

The project demonstrates data preprocessing, statistical analysis, and business insight generation using real-world restaurant data.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Project Structure

```text
Zomato-Data-Analysis-Using-Python
│
├── data
│   └── Zomato-data-.csv
│
├── images
│   ├── restaurant_types.png
│   ├── online_orders.png
│   ├── ratings_distribution.png
│   ├── cost_analysis.png
│   ├── boxplot.png
│   └── heatmap.png
│
├── src
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analysis.py
│   ├── kpi.py
│   └── main.py
│
├── reports
│   └── insights.txt
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset Features

The dataset contains information about restaurants including:

* Restaurant Name
* Votes
* Rating
* Online Order Availability
* Approximate Cost for Two People
* Restaurant Category
* Customer Engagement Metrics

---

## Analysis Performed

### Data Cleaning

* Converted ratings from string format to numerical format.
* Validated dataset structure.
* Checked for missing values.

### Exploratory Data Analysis

* Restaurant category analysis
* Customer voting analysis
* Rating distribution analysis
* Online vs offline order comparison
* Cost preference analysis
* Restaurant type and order mode relationship analysis

---

## Visualizations Generated

### Restaurant Types

Analyzes the distribution of restaurant categories.

### Online Orders

Compares restaurants accepting and not accepting online orders.

### Ratings Distribution

Shows how restaurant ratings are distributed.

### Cost Analysis

Identifies preferred spending ranges among customers.

### Ratings vs Order Mode

Compares ratings between online-order and offline-order restaurants.

### Heatmap Analysis

Shows the relationship between restaurant type and online ordering availability.

---

## Key Insights

* Dining restaurants are the most common restaurant category.
* Dining restaurants receive the highest customer engagement.
* Most restaurant ratings fall between 3.5 and 4.0.
* Restaurants supporting online orders generally receive higher ratings.
* Customers commonly prefer restaurants around the ₹300 price range.
* Cafes show stronger online ordering adoption compared to dining restaurants.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tanishxdev/Zomato-Data-Analysis-Using-Python.git
```

Move into the project directory:

```bash
cd Zomato-Data-Analysis-Using-Python
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
py src/main.py
```

---

## Sample Output

```text
==================================================
ZOMATO DATA ANALYSIS
==================================================

Dataset Loaded
Dataset Cleaned

Generating Visualizations...

All Graphs Generated Successfully
```

---

## Skills Demonstrated

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Insight Generation
* Python Programming
* Pandas Data Manipulation
* Statistical Analysis

---

## Future Improvements

* Interactive Streamlit Dashboard
* SQL-Based Analysis
* Power BI Dashboard
* Automated Reporting
* KPI Monitoring Dashboard
* Machine Learning-Based Restaurant Rating Prediction

---

## Author

Tanish Kumar

GitHub: https://github.com/tanishxdev
