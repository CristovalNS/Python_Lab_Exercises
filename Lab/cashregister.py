def cash_register(price, cash):
    # price, cash = eval(input("Enter the price and amount of cash [Ex: 10_000, 20_000]:"))
    bills = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    x = cash - price
    print(x)
    if cash > price:
        print("You can pay")
        if x != 0:
            new_x = x - bills[0]

            print(f"Here is your change: {new_x}")
    else:
        print("Sorry! You don't have enough money!")


cash_register(75_000, 100_000)
# print(cash_register())