wiek = 20

# Forma pełna:
if wiek >= 18:
    status = "pełnoletni"
else:
    status = "niepełnoletni"

# Forma skrócona (ternary):
status = "pełnoletni" if wiek >= 18 else "niepełnoletni"

print(status)

# Więcej przykładów:
liczba = 7
typ = "parzysta" if liczba % 2 == 0 else "nieparzysta"

print(typ)
