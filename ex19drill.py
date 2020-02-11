# Functions and Variables
# def = define; def indicates you're creating the function
# named cheese_and_crackers. This function has two arguments:
# cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # The first two print statements print the value of the args. 
    # The values 20 and 30 respectively. 
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

def strawberries_and_chocolate(number_of_strawberries, chocolate_bars):
    print(f"You have {number_of_strawberries} strawberries!")
    print(f"You have {chocolate_bars} chocolate bars!")
    print("My favorite combination! \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Giving the function the numbers directly:")
strawberries_and_chocolate(20, 15)

# The variables amount_of_cheese and amount_of_crackers are
# assigned the values 10 and 50. 
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Assigning arguments to the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Here we use variables from our script:")
number_of_strawberries = 25
chocolate_bars = 18

strawberries_and_chocolate(number_of_strawberries, chocolate_bars)

# Math! So the value of amount_of_cheese, the first argument,
# is 30 and the value of the second argument is 11. 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("Here we do math on the inside:")
strawberries_and_chocolate(5 + 15, 12 + 6)

# Variables and math! Whoa! Value of argument + plus a number = new value
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Here we combine the two, variables and math:")
strawberries_and_chocolate(number_of_strawberries + 10, chocolate_bars + 2)


