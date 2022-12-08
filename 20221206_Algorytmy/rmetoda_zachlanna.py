import random

N = 8
NOMINALY = [200, 100, 50, 20, 10, 5, 2, 1]

def wydaj_reszte(kwota, N, NOMINALY):
    reszta = []
    for i in range(N):
        reszta.insert(i, kwota // NOMINALY[i]) 
        kwota=kwota%NOMINALY[i]
    return reszta

kwota = random.randint(450, 10000)
print(f"--- {kwota}")

reszta = wydaj_reszte(kwota, N, NOMINALY)
for i in range(N):
    if reszta[i]>0:
        print(f"{NOMINALY[i]}:\t{reszta[i]}")