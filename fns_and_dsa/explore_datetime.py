from datetime import datetime, timedelta


def display_current_datetime():

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")


def calculate_future_date():

    try:
        days_to_add = int(input("How many days would you like to add?: "))

        current_date = datetime.now()

        future_date = current_date + timedelta(days=days_to_add)

        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date: {formatted_future_date}")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()


