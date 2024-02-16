def calculate_fuel(distance):
    fuel = distance * 10
    if fuel < 0:
        return 100
    else:
        return fuel
