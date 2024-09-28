CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    while True:
        temperature = input("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if not temperature.isdigit():
            print("Invalid temperature. Please enter a numeric value.")
            continue

        if unit not in ("C", "F"):
            print("Invalid unit. Please enter 'C' or 'F'.")
            continue

        temperature = float(temperature)

        if unit == "C":
            converted_temperature = convert_to_fahrenheit(temperature)
            unit_label = "°C"
            converted_unit_label = "°F"
        else:
            converted_temperature = convert_to_celsius(temperature)
            unit_label = "°F"
            converted_unit_label = "°C"

        print(f"{temperature:.1f}{unit_label} is {converted_temperature:.2f}{converted_unit_label}")
        break


if __name__ == "__main__":
    main()
