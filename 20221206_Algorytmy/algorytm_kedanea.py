import timeit
import random
from math import inf

def slow_the_largest_subsequence_sum(numbers):
    total_max = -inf
    for i in range(len(numbers)):
        local_max = 0
        for k in range(i, len(numbers)):
            local_max += numbers[k]
            total_max = max(total_max, local_max)

    return total_max        

def fast_the_largest_subsequence_sum(numbers):
    local_max = total_max = numbers[0]
    for x in numbers[1:]:
        local_max = max(x, local_max + x)
        total_max = max(total_max, local_max)

    return total_max


numbers = []

for num in range(10000):
    numbers.append(random.randint(-100, 100))

def execute_slow():
    slow_the_largest_subsequence_sum(numbers)

def execute_fast():
    fast_the_largest_subsequence_sum(numbers)

print(f"slow computed: {slow_the_largest_subsequence_sum(numbers)}")
print(f"fast computed: {fast_the_largest_subsequence_sum(numbers)}")

# czas wykonania dla 10 wywołan funkcji bruteforce
print(f"t1: {timeit.timeit(stmt=execute_slow, number=10):.4f}s")

# czas wykonania dla 10 wywołań funkcji optymalnej
print(f"t2: {timeit.timeit(stmt=execute_fast, number=10):.4f}s")
