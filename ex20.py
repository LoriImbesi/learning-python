# Functions and Files
from sys import argv
# Argument variables
script, input_file = argv
# Functions
# This defines/creates the function "print_all". "f" is a variable - it's a file.
# It reads the file in the input_file variable.
def print_all(f):
    print(f.read())
# This defines/creates the function "rewind". "f" is a variable.
# It uses "seek" to set the current file position in the file stream. 
def rewind(f):
    f.seek(0)
# This defines the function "print_a_line". It has two parameters, line_count and "f".
# "f" is a variable.
# It creates the line count for each line read. Readline is a Python module.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Creating current_file as a variable. Assigned to it is "open". It will open input_file.
current_file = open(input_file)

# Message to print the whole file. Creates a new line.
print("First let's print the whole file:\n")

# Calling the function print_all which will read current_file.
print_all(current_file)

# Message
print("Now let's rewind, kind of like a tape.")

# Calling the function rewind which sets the position of current_file.
rewind(current_file)

# Message
print("Let's print three lines:")

# Assigning "1" to the variable current_line.
current_line = 1
# Calling the function print_a_line which has the parameters
# "current_line" and "current_file". The number 1 will be printed next
# to the first line of the current file.
print_a_line(current_line, current_file)

# Reassigning to the variable current_line. Causing it to increment by 1.
# Calling the function print_a_line which has the parameters
# "current_line" and "current_file". The number 2 will be printed next
# to the first line of the current file.
# You can change current_line assignment to:
# current_line += 1
current_line = current_line + 1
print_a_line(current_line, current_file)

# The variable current_line will again increment by 1.
# Calling the function print_a_line which has the parameters
# "current_line" and "current_file". The number 3 will be printed next
# to the first line of the current file.
# You can change current_line assignment to:
# current_line += 1
current_line = current_line + 1
print_a_line(current_line, current_file)