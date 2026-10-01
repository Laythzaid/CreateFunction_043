import math

# Temperature converter
def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        return value * 9 / 5 + 32      # Celsius to Fahreheit
    elif unit == 'F':
        return (value - 32) * 5 / 9    # Fahrenheit to Celsius
    else:
        raise ValueError("Unit must be 'C' or 'F'")

# Circle area using lambda 
circle_area = lambda r: math.pi * r ** 2


# Test
if __name__ == "__main__":
    print(convert_temperature(100, 'C'))   # 212.0
    print(convert_temperature(212, 'F'))   # 100.0
    print(circle_area(7))                  # 153.93804002589985
    print(round(circle_area(7), 2))        # 153.94