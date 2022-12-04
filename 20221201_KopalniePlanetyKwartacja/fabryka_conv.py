from datetime import time

# Funkcja zamieniająca wartość z systemu ósemkowego na system kwartański
# oct_value to wartość w systemie ósemkowym,
# divider to kwartański podzielnik do wyznaczania liter A, B, C, D,
# bits to długość ciągu bitowego w liczbie kwartańskiej
def to_kwart(oct_value, divider, bits):
    dec_value = int(oct_value, 8)
    d = dec_value // divider
    kwart_letter = chr(d + 65)      # Użycie tablicy ASCII do zamiany liczby na literę 
    reminder = bin(dec_value - d * divider)[2:]
    return kwart_letter + reminder.zfill(bits)

# Funkcja konwertująca czas z systemu ósemkowego na kwartański
def conv_time(octal_time):
    octal_time = octal_time.split(':')
    return to_kwart(octal_time[0], 24//4, 4) + ':' \
        + to_kwart(octal_time[1], 60//4, 4) + ':' \
        + to_kwart(octal_time[2], 60//4, 4)

# Funkcja konwertująca masę z systemu ósemkowego na kwartański
def conv_mass(octal_mass):
    return to_kwart(octal_mass, 1000//4, 8)


# Otwarcie pliku i wczytanie wszystkich linii z danymi do listy (bez znaków końca linii)
filename = 'fabryka.txt'

with open(filename) as file_object:
    lines = file_object.read().splitlines()

# Zamiana wartości ilości pomiarów z systemu ósemkowego na dziesiętny
count = int(lines[0], 8)
print(count)

# Otwarcie pliku do zapisu danych wyjściowych (skonwertowanych)
output_filename = 'converted_factory.txt'
with open(output_filename, 'w') as file_object:
    file_object.write(f"{bin(count)[2:]}\n")    # Zapisanie ilości pomiarów w systemie bin

    # Pętla główna
    for n in range(1, count + 1):
        data = lines[n].split()

        print("---------------------------")
        print(f"{data[0]} {data[1]}")

        measurement_time = conv_time(data[0])
        measurement_mass = conv_mass(data[1])
        out_str = f"{measurement_time} {measurement_mass}\n"

        print(out_str)
        file_object.write(out_str)
