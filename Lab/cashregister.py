def headache(money, price):
    bills = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    # bills = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

    change_amount = money - price
    change_received = 0
    new_bills = []
    newer_bills = []
    bills_3 = []
    calculation = []
    print(change_amount)

    for x in range(len(bills)):
        if change_received < change_amount:
            new_bills.append(bills[x])
            if new_bills[x] < change_amount or new_bills[x] == change_amount:
                newer_bills.append(new_bills[x])
            # print(new_bills)
            bill_sum = sum(new_bills)
            # print(bill_sum)
        else:
            print("Not enough money!")
            break

    print(newer_bills)

    for y in range(len(newer_bills)):
        if newer_bills[0] == change_amount:
            yy = newer_bills[0]
            calculation.append(yy)
            print(yy)
            print(f"Output: {yy}, Rp.{yy}")
            break
        yy = newer_bills[0] + newer_bills[y]
        calculation.append(yy)
        if yy == change_amount:
            print(yy)
            yyy = newer_bills[0], newer_bills[y]
            print(f"Output: {yyy}, Rp.{yy}")
            break

# I tried my best, but I've peaked for now.
# It only works with if it returns 1 or 2 values from bills

headache(100000, 75000)
print("*" * 80)
headache(100000, 50000)
print("*" * 80)
headache(100000, 45000)
print("*" * 80)
headache(200000, 50000)
print("*" * 80)
headache(20000, 9000)
print("*" * 80)           # This won't work, as it's output would be [5000, 2000, 200, 100]
headache(20000, 12700)






