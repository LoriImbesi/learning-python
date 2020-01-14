# Assigning "10" to the variable "types_of_people"
types_of_people = 10
# Assigning a string with a variable inside to the variable "x"
x = f"There are {types_of_people} types of people."

# Assigning the string "binary" to the variable "binary"
binary = "binary"
# Assigning the string "don't" to the variable "do_not"
do_not = "don't"
# Assigning a formatted string, with two variables inside, to the variable "y"
y = f"Those who know {binary} and those who {do_not}."

# Print the variables "x" and "y" - you don't need curly braces
# because the variables are not inside a string.
print(x)
print(y)

# Print the formatted string, "I said:" and print the variable "x"
print(f"I said: {x}")
# Print the formatted string, "I also said:" and print the variable "y"
print(f"I also said: {y}")

# Assign the boolean value "False" to the variable "hilarious"
hilarious = False

# Assigning the string "Isn't that joke so funny" with an empty variable inside
# to "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the value of the variable "joke_evaluation" and attach the formatted
# value of the variable "hilarious"
print(joke_evaluation.format(hilarious))

# Assigning strings to the variables "w" and "e"
w = "This is the left side of..."
e = "a string with a right side."

# Print the concatenated strings w and e
print(w + e)