""" This program reads from one file and copies the content into another file. The input and output file names are 
entered by the user. It uses try/except to handle exceptions, displaying an error message if the input file does not exist, 
and also if the output file already exists. """

# To avoid FileNotFoundError when running the program from a different directory
import os

input_fileName = input("Enter the name of the input file: ")
output_fileName = input("Enter the name of the output file: ")

# Obtaining folder path of this program file  and joining it with the input and output file names to get the full paths
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path_input = os.path.join(folder_path, input_fileName)
file_path_output = os.path.join(folder_path, output_fileName)

try:
    # Reading the content of the input file
    with open(file_path_input, 'r') as input_file:
        content = input_file.read()
        
    # Writing the content to the output file using 'x' exclusive creation mode to avoid overwriting an existing file
    with open(file_path_output, 'x') as output_file:
        output_file.write(content)
        
    print("File copied successfully.")

# Error handling for FileNotFoundError if the input file does not exist
except FileNotFoundError:
    print(f"\nError: The file '{input_fileName}' does not exist.")

# Error handling for FileExistsError as 'x' mode raises error if the file already exists
except FileExistsError:
    print(f"\nError: The file '{output_fileName}' already exists. Please choose a different name for the output file.")