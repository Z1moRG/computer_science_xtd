import random

def NWD(a, b, n = 0):
    if b != 0:
        n += 1
        return(NWD(b, a % b, n))
    return a

# Zasada budowy trójkąta, przeciwprostokątna jest najdłuższym bokiem trójkąta
# Nie możemy więc od przyprostokątnej odejmować przeciwprostokątnej by wyznaczyć
# Długość drugiej przyprostokątnej (jest to pozbawione jakiegokolwiek sensu)

def szukaj_wszystkich_trojek(x, y):
    answers = [[0 for z in range(2)] for w in range(2)]
    if y > x:
        x, y = y, x
    
    # a = b
    a = (x ** 2 - y ** 2) ** 0.5
    if a % 1 == 0:
        answers[0] = [int(a), y, x]
    else:
        answers[0] = [0]
    c = (x ** 2 + y ** 2) ** 0.5
    if c % 1 == 0:
        answers[1] = [x, y, int(c)]
    else:
        answers[1] = [0]
    
    return answers

def szukaj_pierwotnych_trojek(x, y):
    any_possible = szukaj_wszystkich_trojek(x, y)
    nwd = NWD(x, y)
    x //= nwd
    y //= nwd
    pierwotne = szukaj_wszystkich_trojek(x, y)
    return any_possible, pierwotne


#x, y = random.randint(1, 1000), random.randint(1, 1000)
x = 10
y = 6

print(szukaj_pierwotnych_trojek(x, y))