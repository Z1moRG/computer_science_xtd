import random, numpy

def losuj(N):
    A = [0] * N
    for i in range(N):
        A[i] = [0] * N
    for i in range(N):
        for j in range(N):
            A[i][j] = random.randint(0, 1)

    if random.randint(1, 10)%2 == 1:
        idol = random.randint(1, 10)%N
        for i in range(N):
            A[i][idol] = 1
        for j in range(N):
            A[idol][j] = 0
    return A

def losuj_numpy(N):
    A = numpy.random.randint(0, 2, size=(N, N))
    idol = random.randint(0, N-1)
    A[0:N, idol:idol+1] = numpy.ones((N, 1))
    A[idol] = numpy.zeros((1, N))
    return A

def wypisz(A):
    print(A)
    for a, i in enumerate(A):
        print(i)
        for b, j in enumerate(i):
            if a != b:
                print(f"{j} = {A[a][b]}")
                

#print(losuj(5))
A = losuj_numpy(5)
wypisz(A)