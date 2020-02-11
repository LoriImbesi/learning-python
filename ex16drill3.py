# Reading and Writing Files
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
# Writing the lines to the file in fewer than 6 lines
 target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# or this:
lines = (line1, line2, line3)
target.write('\n'.join(lines))

# or you could do: 
lines =(line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')

# or this:
line = '{}\n{}\n{}n'.format(line1, line2, line3)
target.write(line)

# First example uses 6 lines
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# Close the file - it's IMPORTANT TO DO THIS
print("And finally, we close it.")
target.close()
