from datetime import time, datetime, date

# Funkcja zamieniająca liczbę w systemie binarnym na liczbę w systemie dziesiętnym.
# Normalnie można użyć int(binary_str, 2)
def bin_to_dec(numbers):
    decimal_number = 0
    for power, binary_digit in enumerate(reversed(numbers.strip())):
        decimal_number += int(binary_digit) * 2**power
    return decimal_number

# Funkcja, zamieniająca wartość kwartańską na dziesiętną.
# Multiplier dla godzin wynosi 24 // 4, dla minut i sekund 60 // 4, dla ton 1000 // 4.
# Wynika to z zapisu A, B, C, D w systemie kwartańskim.
def to_dec(kwart_value, multiplier):
    kwart = ord(kwart_value[0]) - 65        # Urzycie tablic ASCII to zamiany litery na liczbę
    remainder = bin_to_dec(kwart_value[1:])
    return kwart * multiplier + remainder

# Funkcja zamieniająca czas kwartański na czas ziemski :)
# Funkcja zwraca wartość typu datetime.time
def conv_time(kwart_time):
    kwart_time = kwart_time.split(':')
    return time( \
        hour = to_dec(kwart_time[0], 24//4), \
        minute = to_dec(kwart_time[1], 60//4), \
        second = to_dec(kwart_time[2], 60//4))

# Funkcja zamieniająca masę kwartańską na masę ziemską (tonę) :)
def conv_mass(kwart_mass):
    return to_dec(kwart_mass, 1000//4)


# Otwarcie pliku i wczytanie wszystkich linii z danymi do listy
filename = 'kopalnia.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# Konwersja z bin na dec ilości rekordów
count = bin_to_dec(lines[0])

# Słownik kategorii pomiarów (zad 1.1)
measurement = {
    "correct": 0,
    "probable": 0,
    "error": 0
}

# Inicjalizacja zminnej, która zapamiętuje poprzednią wartość masy (zad 1.2)
prev_mass = None

# Słownik zapamiętujący długość trwania i ilość kolejnych poprawnych odczytów (zad 1.2)
continuous_period = {
    'begin_time': time(0, 0, 0),
    'end_time': time(0, 0, 0),
    'counter': 0, 
}

# Słownik zawierający wynik, czyli najdłuższy okres i największą ilość poprawnych odczytów (zad 1.2)
longest_period = {
    'period': time(0, 0, 0),
    'counter': 0,
}

# Pętla główna
for n in range(1, count + 1):
    data = lines[n].split()

    print("---------------------------------")
    print(f"{data[0]}\t{data[1]}")

    measurement_time = conv_time(data[0])
    current_mass = conv_mass(data[1])
    print(f"{measurement_time}\t\t{current_mass}")

    # Flaga błędu pomiaru ustawana na False
    measurement_error = False
    if prev_mass:
        delta = abs((current_mass - prev_mass) / prev_mass)     # Wyliczenie różnicy pomiaru
        # Sprawdzenie do jakiego przedziału należy pomiar (zad 1.1)
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
                # Flaga błędu pomiaru ustawiona na True
                measurement_error = True
                print("error")
            # Wyznaczenie najdluższego okresu i ilości pomiarów właściwych (zad 1.2)
            if longest_period['counter'] <= continuous_period['counter']:
                # Aby obliczyć różnicę czasu należy time skonwertować do datetime
                longest_period['period'] = str( \
                    datetime.combine(date.today(), continuous_period['end_time']) - \
                    datetime.combine(date.today(), continuous_period['begin_time']))
                longest_period['counter'] = continuous_period['counter']
                continuous_period['counter'] = 0

    # Zapamiętanie wartości masy z poprzedniej iteracji jeśli nie była błędna
    # Tylko jeśli flaga błędu measurement_error jest równa False (zad 1.1 pkt 3)
    # W przypadku błędu pomiaru nie zmieniamy wartości prev_mass
    prev_mass = current_mass if measurement_error == False else prev_mass

print("=================================")

for key, value in measurement.items():
    print(f"{key} measurement\t{value}")

for key, value in longest_period.items():
    print(f"{key}\t\t\t{value}")
