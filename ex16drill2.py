# Reading and Writing Files drill
# Commands to remember:
# close: close the file
# read: reads the content of the file. You can assign the result to a var.
# readline: reads just one line of text
# truncate: empties the file *Beware*
# write('some string'): writes the string in quotes to the file
# seek(0): move the read/write location to the beginning of the file.

# Use read and argv to read a file I created
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())