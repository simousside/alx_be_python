# Prompt the user for their current age and validate input
current_age = input("How old are you? ")

# Keep asking for input until a valid integer is entered
while not current_age.isdigit():
    print("Please enter a valid integer.")
    current_age = input("How old are you? ")

# Convert the valid input to an integer
current_age = int(current_age)

# Calculate age in 2050
age_in_2050 = current_age + 27

# Print the result
print(f"In 2050, you will be {age_in_2050} years old.")