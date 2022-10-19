def supply_drop(m, n):
    # if m % 2 == 0 and n % 2 == 0:   # m and n are even
    #     amount = (m * n) // 4
    # elif m % 2 == 0 and n % 2 != 0:     # m is even while n is odd
    #     amount = (m * n) // 4 + m//2
    # elif m % 2 != 0 and n % 2 == 0:     # m is odd while n is even
    #     amount = (m * n) // 4 + n//2
    # elif m % 2 != 0 and n % 2 != 0:     # m and n are odd
    #     amount = ((m * n) // 4) + n//2 + m//2 + 1

    amount = int((m - (m // 2)) * (n - (n // 2)))   # found this formula so i used this instead ;-;
    return amount


# m is rows while n is columns
print(supply_drop(2, 2))
print(supply_drop(9, 9))
print(supply_drop(10, 1))
print(supply_drop(6, 4))


