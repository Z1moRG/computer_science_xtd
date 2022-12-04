from datetime import time

def to_kwart(oct_value, divider, bits):
    dec_value = int(oct_value, 8)
    d = dec_value // divider
    kwart_letter = chr(d + 65)
    reminder = bin(dec_value - d * divider)[2:]
    return kwart_letter + reminder.zfill(bits)

def conv_time(octal_time):
    octal_time = octal_time.split(':')
    return to_kwart(octal_time[0], 24//4, 4) + ':' \
        + to_kwart(octal_time[1], 60//4, 4) + ':' \
        + to_kwart(octal_time[2], 60//4, 4)

def conv_mass(octal_mass):
    return to_kwart(octal_mass, 1000//4, 8)


filename = 'fabryka.txt'

with open(filename) as file_object:
    lines = file_object.read().splitlines()

print(lines)

count = int(lines[0], 8)
print(count)

output_filename = 'converted_factory.txt'
with open(output_filename, 'w') as file_object:
    file_object.write(f"{bin(count)[2:]}\n")

    for n in range(1, count + 1):
        data = lines[n].split()

        print("---------------------------")
        print(f"{data[0]} {data[1]}")

        measurement_time = conv_time(data[0])
        measurement_mass = conv_mass(data[1])
        out_str = f"{measurement_time} {measurement_mass}\n"

        print(out_str)
        file_object.write(out_str)
