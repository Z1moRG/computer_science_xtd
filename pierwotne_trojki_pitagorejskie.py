def NWD(a, b, n = 0):
    if b != 0:
        n += 1
        return(NWD(b, a % b, n))
    return a

# Zasada budowy trójkąta, przeciwprostokątna jest najdłuższym bokiem trójkąta
# Nie możemy więc od przyprostokątnej odejmować przeciwprostokątnej by wyznaczyć
# Długość drugiej przyprostokątnej (jest to pozbawione jakiegokolwiek sensu)

def szukaj_wszystkich_trojek(x, y):
    if y > x:
        x, y = y, x

    a = (x ** 2 - y ** 2) ** 0.5
    if a == int(a) and a != 0:
        if a < y:
            return f"{int(a)}, {y}, {x}"
        else:
            return f"{y}, {int(a)}, {x}"
    c = (x ** 2 + y ** 2) ** 0.5
    if c == int(c) and c != 0:
        return f"{y}, {x}, {int(c)}"
    return 0
  
def szukaj_pierwotnych_trojek(x, y):
    any_possible = szukaj_wszystkich_trojek(x, y)
    nwd = NWD(x, y)
    x //= nwd
    y //= nwd
    pierwotne = szukaj_wszystkich_trojek(x, y)
    
    if any_possible:
        return [any_possible, pierwotne]

answers = []
for i in range(1, 1000):
    for j in range(i, 1000):
        try:
            answer = szukaj_pierwotnych_trojek(i, j)
            if answer not in answers:
                print(answer[0])
                print(f"{answer[1]} PIERWOTNE\n------------------")
                answers.append(answer)
        except TypeError:
            continue
