# This is function called "formatter". It is assigned four {} which will turn
# the formatter variable into four strings.
formatter = "{} {} {} {}"

# Take the formatter string defined on line 3 and call its format function.
# Pass the four arguments, 1, 2, 3, 4 to it.
# The result of calling format on formatter is a new string that has
# the {} replaced with the four variables. Print will print these out. 
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I am",
    "not afraid,",
    "Toad said",
    "to Frog."
))