def isprime():
    user_input = int(input("Enter a number: "))

    for i in range(2, user_input):
        if (user_input % i) == 0:
            return False
    return True


print(isprime())
