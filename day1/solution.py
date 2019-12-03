def parse_input():
    inputs = []

    with open('input.txt') as f:
        for line in f:
            num = int(line)
            inputs.append(num)

    return inputs


def calculate_consumption_basic(mass):
    return int(mass/3) - 2


def calculate_consumption_realistic(mass):
    total_fuel = 0
    fuel_needed = mass

    while True:
        fuel_needed = int(fuel_needed/3) - 2

        if fuel_needed <= 0:
            break

        total_fuel = total_fuel + fuel_needed

    return total_fuel


def sum_fuel(module_masses, consumption_function):
    total_fuel = 0

    for mass in module_masses: 
        total_fuel = total_fuel + consumption_function(mass)

    return total_fuel


if __name__ == '__main__':
    module_masses = parse_input()

    total_fuel_basic = sum_fuel(module_masses, calculate_consumption_basic)
    total_fuel_realistic = sum_fuel(module_masses, calculate_consumption_realistic)

    print(total_fuel_basic)
    print(total_fuel_realistic)
