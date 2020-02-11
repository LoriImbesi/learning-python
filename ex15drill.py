# Reading Files

# Imports the argv module. argv is the "argument variable". This variable
# holds the arguments you pass to the Python script when you run it. Sys is a package
# from which we get argv.
from sys import argv
# This line "unpacks" argv so that, rather than holding all the arguments, it gets
# assigned to variables you can work with, ex: script, filename. It means "take 
# whatever is in argv, unpack it, and assign it to all of these variables on
# the left in order" on the command line. This line is using argv to get a filename.
script, filename = argv

# Uses the "open" function to open the file. The filename variable is passed
# into the open function.
txt = open(filename)

# Prints a message and tells you the name of the file. print() to return
# the filename parameter
print(f"Here's your file {filename}:")

# This is where the magic happens! Here we call a function on txt named read. What we get 
# back from open is a file, and it also has commands you can give it. You can give
# a file a command by using the . (dot or period), the name of the command and paramters,
# just like with open and input. The difference is that txt.read() says, "Hey, txt!
# Do your read command with no parameters!"
print(txt.read())
txt.close()

# Print a message that prompts you to type the file name again.
print ("Type the filename again:")
# The input function allows for user input at the prompt. The input is saved to a var.
file_again = input("> ")

# This line uses the "open" command to open the file again. The input from the user
# that was saved to the file_again var is being passed to the open function
# then saved to a var.
txt_again = open(file_again)

# This line calls the read function on txt_again with no parameters. So we open
# the file txt_again and can read it. read() method on the var will print the
# file to the screen again.
print(txt_again.read())
txt_again.close()