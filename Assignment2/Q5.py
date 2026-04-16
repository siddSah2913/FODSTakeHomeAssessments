# Write a function that accepts a list of student names and returns the names sorted in reverse alphabetical order. dont use inbuilt function sorted() or sort() 

def sort_students_reverse(names):
    # Implementing bubble sort for reverse alphabetical order
    student_names = [name.strip() for name in names]
    n = len(student_names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_names[j] < student_names[j + 1]:
                student_names[j], student_names[j + 1] = student_names[j + 1], student_names[j]
    return student_names

#taking input from user
names = input("Enter student names separated by commas: ").split(",")

# Sorting names in reverse alphabetical order
sorted_names = sort_students_reverse(names)

# Displaying the sorted names
print("Student names in reverse alphabetical order:")
for name in sorted_names:
    print(name.capitalize())
