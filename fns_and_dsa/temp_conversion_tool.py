
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def temperature_conversion_tool():

    temp_input = input("Enter the temperature (e.g., 32 or 100): ")

    if temp_input.replace('.', '', 1).isdigit():
        temperature = float(temp_input)
    else:
        print("Invalid temperature. Please enter a numeric value.")
        return

    temp_unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? Enter C or F: ").strip().upper()

    if temp_unit == "F":

        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
    elif temp_unit == "C":

        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    temperature_conversion_tool()
