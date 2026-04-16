""" Write a function key_value(sentence) that takes a sentence as input and 
returns a dictionary showing how many times each character (excluding spaces) occurs. """

def key_value(sentence):
    frequency_dict = {}
    for char in sentence:
        if char != " ":  # Exclude spaces
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict

# Taking input from the user
sentence = input("Enter a sentence: ")

# Calling the function and displaying the result
result = key_value(sentence)
for char, count in result.items():
    print(f"'{char}' occurs {count} times.")

