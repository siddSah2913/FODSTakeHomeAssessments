""" This program is a basic library management system that allows users to borrow, return, and search for books. 
It uses OOP concepts to create necessary classes and applies OOP features (like encapsulation/inheritance if applicable). 
For storing book details, it uses file handling along with exception handling. """

import csv
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "library.csv")


# creating a class for book (encapsulation)
class Book:
    def __init__(self, book_id, title, author, genre, status):
        self.__book_id = book_id
        self.__title = title.strip().title()
        self.__author = author.strip().title()
        self.__genre = genre.strip().title()
        self.__status = status.strip().capitalize()

    def to_list(self):
        return [self.__book_id, self.__title, self.__author, self.__genre, self.__status]


# creating a class to manage books in library
class Library:
    def __init__(self, file_path):
        self.file_path = file_path

    # method to add book
    def add_book(self):
        book_list = []

        while True:
            try:
                book_id = int(input("Enter Book ID: ").strip())
                # check if book id already exists
                if book_id in [book.book_id for book in book_list]:
                    print("Book ID already exists!")
                    break
                else:
                    title = input("Enter Title: ")
                    author = input("Enter Author: ")
                    genre = input("Enter Genre: ")
                    status = input("Enter Status (Available/Borrowed): ")

                    new_book = Book(book_id, title, author, genre, status)
                    book_list.append(new_book)

                choice = input("Add another book? (y/n): ").strip().lower()
                if choice != 'y':
                    break

            except ValueError:
                print("Invalid input! Please enter correct data.\n")

        try:
            file_exists = os.path.exists(self.file_path)

            with open(self.file_path, "a", newline="") as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(["Book ID", "Title", "Author", "Genre", "Status"])

                for b in book_list:
                    writer.writerow(b.to_list())

            print("\nData saved successfully!")

        except Exception as e:
            print("Error writing file:", e)
    
    # method to display book
    def display_books(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) == 0:
            print("Library is empty! Please add books first.")
            return

        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)

                print("\n--- Book Records ---")
                for row in reader:
                    print("\t".join(row))

        except FileNotFoundError:
            print("File storing book records not found! Please add books first.")
        except Exception as e:
            print("Error reading file:", e)

    # method to search book
    def search_book(self):
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)

                search_term = input("Enter Book ID or Title: ").strip().lower()
                found = False

                for row in reader:
                    if search_term in [col.lower() for col in row]:
                        print("\t".join(row))
                        found = True
                        break

                if not found:
                    print("Book not found!")

        except FileNotFoundError:
            print("File storing book records not found! Please add books first.")
        except Exception as e:
            print("Error reading file:", e)

    # method to borrow book
    def borrow_book(self):
        try:
            with open(self.file_path, "r") as file:
                rows = list(csv.reader(file))

            book_id = input("Enter Book ID: ").strip()
            found = False

            for row in rows:
                if row[0] == book_id:
                    found = True
                    if row[4] == "Available":
                        row[4] = "Borrowed"
                        print("Book borrowed successfully!")
                    else:
                        print("Book already borrowed!")
                    break

            if not found:
                print("Book not found!")

            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        except FileNotFoundError:
            print("File storing book records not found! Please add books first.")
        except Exception as e:
            print("Error:", e)

    # method to return book
    def return_book(self):
        try:
            with open(self.file_path, "r") as file:
                rows = list(csv.reader(file))

            book_id = input("Enter Book ID: ").strip()
            found = False

            for row in rows:
                if row[0] == book_id:
                    found = True
                    if row[4] == "Borrowed":
                        row[4] = "Available"
                        print("Book returned successfully!")
                    else:
                        print("Book already available!")
                    break

            if not found:
                print("Book not found!")

            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        except FileNotFoundError:
            print("File not found! Please add books first.")
        except Exception as e:
            print("Error:", e)


# Main Program
library = Library(file_path)

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        library.search_book()
    elif choice == '4':
        library.borrow_book()
    elif choice == '5':
        library.return_book()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")