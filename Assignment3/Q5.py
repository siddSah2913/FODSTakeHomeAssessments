""" This program defines a class called Learner with attributes such as roll_no, full_name, address, enrollment_year, program, 
and group. It then creates an object of the class, takes input for all attributes from the user, and displays the details. """

class Learner:
    def __init__(self):
        self.roll_no = None
        self.full_name = None
        self.address = None
        self.enrollment_year = None
        self.program = None
        self.group = None

    # Method to take input
    def input_details(self):
        self.roll_no = input("Enter roll number: ")
        self.full_name = input("Enter full name: ")
        self.address = input("Enter address: ")
        self.enrollment_year = input("Enter enrollment year: ")
        self.program = input("Enter program: ")
        self.group = input("Enter group: ")

    # Method to display details
    def display_details(self):
        print(f"\n{'-'*20}Learner Details{'-'*20}")
        print(f"Roll Number: {self.roll_no.strip()}")
        print(f"Full Name: {self.full_name.strip().capitalize()}")
        print(f"Address: {self.address.strip()}")
        print(f"Enrollment Year: {self.enrollment_year.strip()}")
        print(f"Program: {self.program.strip()}")
        print(f"Group: {self.group.strip()}")

#Creating an object of the Learner class
learner1 = Learner()

#Taking input for all attributes from the user
learner1.input_details()

#Displaying the details of learner1
learner1.display_details()