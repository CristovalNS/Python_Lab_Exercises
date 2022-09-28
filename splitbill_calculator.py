# Split Bill Calculator

# User input
bill = float(input("Enter the amount of bill: "))
people = float(input("Enter the amount of people: "))
tips = float(input("Enter the amount of tips (%): "))

# Output
print("=" * 40)

person_tip = (bill * (tips/100) / people)
print(f"Tip amount per person: ${person_tip}")

total_tip = ((bill / people) + person_tip)
print(f"Total amount per person: ${total_tip}")
