from datetime import time, datetime, date

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
    return time(hour=to_dec(kwart_time[0], 24//4), \
        minute=to_dec(kwart_time[1], 60//4), \
        second=to_dec(kwart_time[2], 60//4))

def conv_mass(kwart_mass):
    return to_dec(kwart_mass, 1000//4)


filename = 'kopalnia.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


count = bin_to_dec(lines[0])

correct_measurement, probable_measurement, error_measurement  = 0, 0, 0
prev_mass = -1


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

    print("-----------------------------")
    print(data)

    measurement_time = conv_time(data[0])
    print(measurement_time)
    print(conv_mass(data[1]))

    current_mass = conv_mass(data[1])
    if prev_mass != -1:
        delta = abs((current_mass - prev_mass) / prev_mass)
        if delta <= 0.05:
            correct_measurement += 1
            if continuous_period['counter'] == 0:
                continuous_period['begin_time'] = measurement_time
            continuous_period['end_time'] = measurement_time
            continuous_period['counter'] += 1
            print("correct")
        else:
            if delta <= 0.10:
                probable_measurement += 1
                print("probable")
            else:
                error_measurement += 1
                print("error")
            if longest_period['counter'] <= continuous_period['counter']:
                longest_period['period'] = str( \
                    datetime.combine(date.today(), continuous_period['end_time']) - \
                    datetime.combine(date.today(), continuous_period['begin_time']))
                longest_period['counter'] = continuous_period['counter']
                continuous_period['counter'] = 0


    prev_mass = current_mass

print("--------------------------------------------------------------------")
print(f"correct_measurement: {correct_measurement},\
    probable_measurement: {probable_measurement},\
    error_measurement: {error_measurement}")


for key, value in longest_period.items():
    print(f"{key} = {value}")




#    try:
#        print(unbinary(line.strip()))
#    except ValueError:
#        pass