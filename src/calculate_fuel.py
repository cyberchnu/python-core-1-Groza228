def calculate_fuel(distance):
    fuel_needed = distance * 10
    if fuel_needed < 0:
        print(100)
    else:
        return fuel_needed


distance = float(input("Enter distance in kilometers: "))
print(calculate_fuel(distance))
