""" This program defines a Staff class with attributes such as emp_id, full_name, address, phone_number, 
marital_status, dependents, and salary. It creates instances of the class for multiple staff members and 
writes their data to a CSV file called "staff.csv". The program also allows the user to view the list of staff 
and their details. The program also includes error handling using try/except blocks. """

import csv
import os

# To avoid FileNotFoundError when running the program from a different directory
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "staff.csv")

# creating a class for staff (encapsulation)
class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary

    def to_list(self):
        return [self.emp_id, self.full_name, self.address,
                self.phone_number, self.marital_status,
                self.dependents, self.salary]

# method to add staff
def add_staff():
    staff_list = []

    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            full_name = input("Enter Full Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            marital_status = input("Enter Marital Status: ")
            dependents = int(input("Enter Number of Dependents: "))
            salary = float(input("Enter Salary: "))

            new_staff = Staff(emp_id, full_name, address, phone_number,
                          marital_status, dependents, salary)
            staff_list.append(new_staff)

            # Asking user if they want to add another staff
            print("Do you want to add another staff? (y/n): ")
            choice = input()
            if choice.lower() != 'y':
                break

        except ValueError:
            print("Invalid input! Please enter correct data types.\n")

    # method to write to csv
    try:
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)

            if not os.path.exists(file_path):
                writer.writerow(["ID", "Name", "Address", "Phone",
                                 "Marital Status", "Dependents", "Salary"])

            for s in staff_list:
                writer.writerow(s.to_list())

        print("\nData saved successfully!")
    
    # error handling for any error
    except Exception as e:
        print("Error writing file:", e)

# method to display staff
def display_staff():
    # if the file exits but empty
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        print("File is empty! Please add staff first.")
        return
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)

            print("\n--- Staff Records ---")
            for row in reader:
                print("\t".join(row))

    except FileNotFoundError:
        print("File not found! Please add staff first.")
    except Exception as e:
        print("Error reading file:", e)


# main program
while True:
    print("\n1. Add Staff")
    print("2. Display Staff")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_staff()
    elif choice == '2':
        display_staff()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")