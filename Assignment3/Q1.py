'''This program reads a CSV file named "records.csv" and displays the contents of the specified fields: 
student_name, roll_no, program, year, and group. It uses the csv module to read the file and handles the case where the file is not found.'''

import csv
# To avoid FileNotFoundError when running the program from a different directory
import os

# Getting the folder path of current program file and joining it with records.csv
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, 'records.csv')

#Error handling for file not found
try:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        print(f"\n{'-'* 20}Student Record{'-'* 20}")
        for row in reader:
            print(f"Student Name: {row['student_name']}\n Roll No: {row['roll_no']}\n Program: {row['program']}\n Year: {row['year']}\n Group: {row['group']}\n")

except FileNotFoundError:
        print(f"Error: The file 'records.csv' was not found.")
