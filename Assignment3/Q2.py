'''This program takes user details as input and appends them to the existing file "records.csv". 
The fields taken as input are: student_name, roll_no, program, year, and group.'''

import csv
# To avoid FileNotFoundError when running the program from a different directory
import os

# Getting the folder path of current program file and joining it with records.csv
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, 'records.csv')

print(f"\n{'-'* 20}Enter Students Details to append{'-'* 20}")
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

# Error handling for file not found while appending details
try:
    with open(file_path, mode='a', newline='') as file:
        append_details = csv.writer(file)
        append_details.writerow([student_name, roll_no, program, year, group])
    print("\nUser details have been successfully appended to records.csv!")

except FileNotFoundError:
    print("Error: The file 'records.csv' was not found.")
