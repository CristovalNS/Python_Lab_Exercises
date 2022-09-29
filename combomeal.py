# Combo Meal Price Calculator
# This program has a function which takes in three integers denoting
# the selling price of a burger, soda, and combo meal; and returns an integer
# denoting the fixed profit.

def profit(burger, soda, combo):
    # Return the fixed profit.
    fixed_price = (burger + soda) - combo
    print("The fixed price is $", fixed_price, sep="")
    return


# User input
burger = int(input("Enter burger selling price: "))
soda = int(input("Enter burger selling price: "))
combo = int(input("Enter burger selling price: "))

# Output
profit(burger, soda, combo)








