import random

def losuj(numbers):
    x = random.randint(1, 10)
    for i in range(10):
        y = random.randint(1, 10)
        if y%2 == 0:
            numbers.append(x)
        else:
            numbers.append(y)


def find_leader(numbers):
    numbers = sorted(numbers)
    counter = 0
    candidate = numbers[len(numbers) // 2] 
    for i in range(0, len(numbers) - 1):
        if numbers[i] == candidate:
            counter += 1
    if counter > len(numbers) // 2:
        return candidate
    else:
        return -1

numbers = []
losuj(numbers)

print(numbers)
print(find_leader(numbers))