# A simple time conversion program

# User input
time_input = int(input("Enter the number of seconds: "))

# Calculations
time_input = time_input % (24 * 3600)
hour = time_input // 3600

time_input %= 3600
minutes = time_input // 60

time_input %= 60
seconds = time_input

# Output
print(f"Hours:Minutes:Seconds -> {hour}:{minutes}:{seconds}")

