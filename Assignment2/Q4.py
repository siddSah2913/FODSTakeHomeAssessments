""" Write a function that takes a list of numbers as input and returns a dictionary showing how many times each number occurs in the list. 
Test this function with at least three different lists. """

def count_occur(numbers):
    dict = {}
    for n in numbers:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

# Testing the function with three different lists
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 8]
list2 = [50, 60, 70, 80, 90, 50, 60]
list3 = [100, 300, 500, 700, 500, 300, 900]

# Showing the results
print("List 1:", list1)
for number, count in count_occur(list1).items():
    print(f"{number} occurs {count} times")

print("\nList 2:", list2)
for number, count in count_occur(list2).items():
    print(f"{number} occurs {count} times")

print("\nList 3:", list3)
for number, count in count_occur(list3).items():
    print(f"{number} occurs {count} times")
