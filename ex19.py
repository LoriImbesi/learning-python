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

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# The variables amount_of_cheese and amount_of_crackers are
# assigned the values 10 and 50. 
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Assigning arguments to the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Math! So the value of amount_of_cheese, the first argument,
# is 30 and the value of the second argument is 11. 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Variables and math! Whoa! Value of argument + plus a number = new value
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

