# Reading and Writing Files
# Commands to remember:
# close: close the file
# read: reads the content of the file. You can assign the result to a var.
# readline: reads just one line of text
# truncate: empties the file *Beware*
# write('some string'): writes the string in quotes to the file
# seek(0): move the read/write location to the beginning of the file.
from sys import argv
# Command line arguments (argv = argument variable)
# When you see "filename" - you need to create a file
script, filename = argv

print(f"Were going to erase {filename}.")
# ctrl+c is the universal 'get me outta here' command
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# Target = open the file in "write" mode.
print("Opening the file...")
target = open(filename, 'w')
# Truncate the file = erase the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# Input prompts
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# Writing to the file, creating new lines
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Close the file - it's IMPORTANT TO DO THIS
print("And finally, we close it.")
target.close()
