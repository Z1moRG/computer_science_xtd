import random

N = 5
A = [0] * N
for i in range(N):
    A[i] = [random.randint(0,1)] * N
print(A)

def losuj(A, N):
    for i in range(N):
        for j in range(N):
            A[i][j] = random.randint(0, 1)
    print(A)

    if random.randint(1, 10)%2 == 1:
        idol = random.randint(1, 10)%N
        print(idol)
        for i in range(N):
            A[i][idol] = 1
        print(A)
        for j in range(N):
            A[idol][j] = 0
    return A

print(losuj(A, N))

