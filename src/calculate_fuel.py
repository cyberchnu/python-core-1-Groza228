def calculate_fuel(distance):
    fuel_needed = distance * 10
    if fuel_needed < 0:
        return 100
    else:
        return fuel_needed
