global  FAHRENHEIT_TO_CELSIUS_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

global  CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def conversion_to_celsius(fahrenheit):
    temperature_in_celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature_in_celcius

def conversion_to_fahrenheit(celcius):
    temperature_in_fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature_in_fahrenheit

if type(temperature) is int:
    if unit == 'C':
        converted_temp = conversion_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = conversion_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")
