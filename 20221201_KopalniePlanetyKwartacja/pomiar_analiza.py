def bin_to_dec(numbers):
    decimal_number = 0
    for power, binary_digit in enumerate(reversed(numbers.strip())):
        decimal_number += int(binary_digit) * 2**power
    return decimal_number

def to_dec(kwart_value, multiplier):
    kwart = int(chr(ord(kwart_value[0]) - 17))
    remainder = bin_to_dec(kwart_value[1:])
    return kwart * multiplier + remainder


def conv_date(kwart_date):
    kwart_date = kwart_date.split(':')
    return str(to_dec(kwart_date[0], 24//4)) + ":" \
        + str(to_dec(kwart_date[1], 60//4)) + ":" \
        + str(to_dec(kwart_date[2], 60//4))

def conv_mass(kwart_mass):
    return to_dec(kwart_mass, 1000//4)


filename = 'kopalnia.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


count = bin_to_dec(lines[0])

correct_measurement, probable_measurement, error_measurement  = 0, 0, 0
prev = -1

for n in range(1, count + 1):
    data = lines[n].split()

    print(data)
    print(conv_date(data[0]))
    print(conv_mass(data[1]))

    current = conv_mass(data[1])
    if prev != -1:
        delta = abs((current - prev) / prev)
        if delta <= 0.05:
            correct_measurement += 1
            print("correct")
        elif delta <= 0.10:
            probable_measurement += 1
            print("probable")
        else:
            error_measurement += 1
            print("error")
        
    prev = current

print("--------------------------------------------------------------------")
print(f"correct_measurement: {correct_measurement},\
    probable_measurement: {probable_measurement},\
    error_measurement: {error_measurement}")




#    try:
#        print(unbinary(line.strip()))
#    except ValueError:
#        pass