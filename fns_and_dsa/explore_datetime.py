from datetime import datetime, timedelta


def display_current_datetime():

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current Date and Time: {formatted_date}")


def calculate_future_date():

    days_to_add = input("Enter the number of days to add to the current date: ")

    while not days_to_add.isdigit():
        print("Invalid input. Please enter a positive integer.")
        days_to_add = input("Enter the number of days to add to the current date: ")

    days_to_add = int(days_to_add)

    current_date = datetime.now()

    future_date = current_date + timedelta(days=days_to_add)

    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future Date: {formatted_future_date}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
