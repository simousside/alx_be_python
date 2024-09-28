from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")


# Part 2: Calculate a Future Date
def calculate_future_date():
    # Use a different input message
    try:
        days_to_add = int(input("Please input the number of days to add: "))

        # Get the current date
        current_date = datetime.now()

        # Calculate the future date by adding the specified number of days
        future_date = current_date + timedelta(days=days_to_add)

        # Format and print the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


# Run the functions
if __name__ == "__main__":
    display_current_datetime()  # Part 1
    calculate_future_date()  # Part 2