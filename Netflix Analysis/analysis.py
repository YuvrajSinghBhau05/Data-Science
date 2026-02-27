import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
df = pd.read_csv("netflix_titles.csv")

# Basic overview
print(df.shape)
print(df.head())
print(df.isnull().sum())

# Movies vs TV Shows
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.show()

# Top 10 countries
df['country'].value_counts().head(10).plot(kind='bar', color='red')
plt.title("Top 10 Countries on Netflix")
plt.show()

# Content added per year
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(kind='line')
plt.title("Content Added Per Year")
plt.show()