""" This program reads the CSV file "health_data.csv" using Pandas and adds 2 new columns: BMI and Health_Status. It populates these columns using the conditions:
    BMI = Weight / Height
    Health_Status is based on BMI values:
    BMI < 18.5 : Underweight
    18.5 ≤ BMI ≤ 24.9 : Healthy range
    25 ≤ BMI ≤ 29.9 : Overweight risk
    30 ≤ BMI ≤ 34.9 : High risk of diabetes/heart disease
    BMI ≥ 40 : Critical health condition
 """

import pandas as pd
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "health_data.csv")

# reading the CSV file
df = pd.read_csv(file_path)

# adding BMI column
df["BMI"] = df["weight"] / df["height"]

# adding Health_Status column
def health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy range"
    elif 25 <= bmi <= 29.9:
        return "Overweight risk"
    elif 30 <= bmi <= 34.9:
        return "High risk of diabetes/heart disease"
    else:
        return "Critical health condition"

df["Health_Status"] = df["BMI"].apply(health_status)

# printing the DataFrame
print(df)