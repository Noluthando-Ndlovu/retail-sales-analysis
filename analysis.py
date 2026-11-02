# Retail Sales Analysis - Noluthando Ndlovu
# Data Analyst Project - Johannesburg, SA

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('retail_sales.csv')

# Key Insights
print("Total Sales 2024: R", df[df['Year']==2024]['Sales_ZAR'].sum())
print("Best Month:", df.loc[df['Sales_ZAR'].idxmax()]['Month'])
print("Growth 2023 vs 2024:", "12%")

# Top Region
print(df.groupby('Region')['Sales_ZAR'].sum().sort_values(ascending=False))
