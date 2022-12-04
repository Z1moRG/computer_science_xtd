from datetime import time, datetime, date

# Funkcja zamieniająca liczbę w systemie binarnym na liczbę w systemie dziesiętnym.
# Normalnie można użyć int(binary_str, 2)
def bin_to_dec(numbers):
    decimal_number = 0
    for power, binary_digit in enumerate(reversed(numbers.strip())):
        decimal_number += int(binary_digit) * 2**power
    return decimal_number

def to_dec(kwart_value, multiplier):
    kwart = ord(kwart_value[0]) - 65
    remainder = bin_to_dec(kwart_value[1:])
    return kwart * multiplier + remainder

def conv_time(kwart_time):
    kwart_time = kwart_time.split(':')
    return time( \
        hour = to_dec(kwart_time[0], 24//4), \
        minute = to_dec(kwart_time[1], 60//4), \
        second = to_dec(kwart_time[2], 60//4))

def conv_mass(kwart_mass):
    return to_dec(kwart_mass, 1000//4)


filename = 'kopalnia.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


count = bin_to_dec(lines[0])

prev_mass = None

measurement = {
    "correct": 0,
    "probable": 0,
    "error": 0
}

continuous_period = {
    'begin_time': time(0, 0, 0),
    'end_time': time(0, 0, 0),
    'counter': 0, 
}

longest_period = {
    'period': time(0, 0, 0),
    'counter': 0,
}


for n in range(1, count + 1):
    data = lines[n].split()

    print("---------------------------------")
    print(f"{data[0]}\t{data[1]}")

    measurement_time = conv_time(data[0])
    current_mass = conv_mass(data[1])
    print(f"{measurement_time}\t\t{current_mass}")

    if prev_mass:
        delta = abs((current_mass - prev_mass) / prev_mass)
        if delta <= 0.05:
            measurement['correct'] += 1
            if continuous_period['counter'] == 0:
                continuous_period['begin_time'] = measurement_time
            continuous_period['end_time'] = measurement_time
            continuous_period['counter'] += 1
            print("correct")
        else:
            if delta <= 0.10:
                measurement['probable'] += 1
                print("probable")
            else:
                measurement['error'] += 1
                print("error")
            if longest_period['counter'] <= continuous_period['counter']:
                longest_period['period'] = str( \
                    datetime.combine(date.today(), continuous_period['end_time']) - \
                    datetime.combine(date.today(), continuous_period['begin_time']))
                longest_period['counter'] = continuous_period['counter']
                continuous_period['counter'] = 0

    prev_mass = current_mass

print("=================================")

for key, value in measurement.items():
    print(f"{key} measurement\t{value}")

for key, value in longest_period.items():
    print(f"{key}\t\t\t{value}")
