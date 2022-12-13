a = None
b = 8
c = 10

def szukaj_trojki(a, b, c):
    if not a:
        a =(c ** 2 - b ** 2) ** 0.5
        if a % 1 == 0:
            return f"a: {int(a)}, b: {b}, c: {c}"
    elif not b:
        b = (c ** 2 - a ** 2) ** 0.5
        if b % 1 == 0:
            return f"a: {a}, b: {int(b)}, c: {c}"
    elif not c:
        c =(a ** 2 + b ** 2) ** 0.5
        if c % 1 == 0:
            return f"a: {a}, b: {b}, c: {int(c)}"
    return 0

print(szukaj_trojki(a, b, c))



