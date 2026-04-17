""" This program reads the CSV file "health_data.csv" using Pandas and plots the data using Matplotlib. It creates scatter plots for the following relationships: weight vs height, age vs weight, height vs age, gender vs height, gender vs weight. """

import pandas as pd
import matplotlib.pyplot as plt
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "health_data.csv")

# reading the CSV file
df = pd.read_csv(file_path)

# list of pairs of columns to plot
pairs = [
    ("weight", "height"),
    ("age", "weight"),
    ("height", "age"),
    ("gender", "height"),
    ("gender", "weight")
]

# Generate scatter plots using loop
for x, y in pairs:
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y}")
    plt.show()
