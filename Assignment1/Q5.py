'''5.	Write a program to input the marks of 6 subjects. Calculate total, average, percentage, and grade according to the rules below: Marks [2*5]
o	Distinction: 85% or above
o	First Division: 70% and above
o	Second Division: 55% and above
o	Third Division: 45% and above
o	Fail: Below 45%
'''

print("\n-----Calculate total, average, percentage, and grade-----")
# Taking input for marks of 6 subjects
marks = []
for i in range(1, 7):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculating total, average, and percentage
total = sum(marks)
average = total / 6
percentage = (total / 600) * 100  # Assuming each subject has a maximum of 100 marks

# Determining the grade
if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Displaying the results
print(f"\nTotal marks: {total}")
print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")