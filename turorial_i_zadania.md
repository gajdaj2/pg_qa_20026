# 🐍 Python - Tutorial od Podstaw

## Spis treści
1. [Zmienne i typy danych](#1-zmienne-i-typy-danych)
2. [Instrukcje warunkowe](#2-instrukcje-warunkowe)
3. [Pętle](#3-pętle)
4. [Funkcje](#4-funkcje)
5. [Programowanie obiektowe](#5-programowanie-obiektowe)
6. [Zadania praktyczne](#6-zadania-praktyczne)

---

## 1. Zmienne i typy danych

### Tworzenie zmiennych

W Pythonie nie musisz deklarować typu zmiennej - Python automatycznie rozpoznaje typ na podstawie przypisanej wartości.

```python
# Tworzenie zmiennych
imie = "Jan"
wiek = 25
wzrost = 1.75
czy_student = True
```

### Podstawowe typy danych

#### 1.1 Liczby (int, float)

```python
# Liczby całkowite (int)
liczba_calkowita = 42
wiek = 25

# Liczby zmiennoprzecinkowe (float)
temperatura = 36.6
pi = 3.14159

# Operacje matematyczne
suma = 10 + 5           # 15
roznica = 10 - 5        # 5
iloczyn = 10 * 5        # 50
iloraz = 10 / 5         # 2.0 (zawsze zwraca float)
iloraz_calkowity = 10 // 3  # 3
reszta = 10 % 3         # 1
potega = 2 ** 3         # 8
```

#### 1.2 Teksty (str)

```python
# Tworzenie stringów
tekst1 = "Hello World"
tekst2 = 'Python jest super'
tekst3 = """Tekst 
wieloliniowy"""

# Operacje na stringach
polaczenie = "Hello" + " " + "World"  # Konkatenacja
powtorzenie = "Ha" * 3                # "HaHaHa"
dlugosc = len("Python")               # 6

# Formatowanie stringów
imie = "Anna"
wiek = 30
print(f"Cześć, mam na imię {imie} i mam {wiek} lat")
print("Cześć, mam na imię {} i mam {} lat".format(imie, wiek))

# Metody stringów
tekst = "python programming"
print(tekst.upper())        # "PYTHON PROGRAMMING"
print(tekst.capitalize())   # "Python programming"
print(tekst.replace("python", "Java"))  # "Java programming"
print(tekst.split())        # ['python', 'programming']
```

#### 1.3 Wartości logiczne (bool)

```python
czy_prawda = True
czy_falsz = False

# Operatory logiczne
wynik1 = True and False  # False
wynik2 = True or False   # True
wynik3 = not True        # False

# Porównania zwracają bool
print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 3)   # True
```

#### 1.4 Listy (list)

```python
# Tworzenie list
owoce = ["jabłko", "banan", "pomarańcza"]
liczby = [1, 2, 3, 4, 5]
mieszana = [1, "tekst", True, 3.14]

# Dostęp do elementów (indeksowanie od 0)
pierwszy = owoce[0]      # "jabłko"
ostatni = owoce[-1]      # "pomarańcza"

# Operacje na listach
owoce.append("gruszka")              # Dodaj na końcu
owoce.insert(1, "truskawka")         # Wstaw na pozycji 1
owoce.remove("banan")                # Usuń element
usuniety = owoce.pop()               # Usuń i zwróć ostatni
dlugosc = len(owoce)                 # Długość listy

# Slicing (wycinki)
liczby = [0, 1, 2, 3, 4, 5]
fragment = liczby[1:4]    # [1, 2, 3]
od_poczatku = liczby[:3]  # [0, 1, 2]
do_konca = liczby[3:]     # [3, 4, 5]
co_drugi = liczby[::2]    # [0, 2, 4]
```

## 2. Instrukcje warunkowe

### Podstawowa składnia if-elif-else

```python
wiek = 18

if wiek < 18:
    print("Jesteś niepełnoletni")
elif wiek == 18:
    print("Właśnie skończyłeś 18 lat!")
else:
    print("Jesteś pełnoletni")
```

### Operatory porównania

```python
a = 10
b = 5

print(a == b)  # Równe: False
print(a != b)  # Różne: True
print(a > b)   # Większe: True
print(a < b)   # Mniejsze: False
print(a >= b)  # Większe lub równe: True
print(a <= b)  # Mniejsze lub równe: False
```

### Operatory logiczne

```python
wiek = 25
ma_prawo_jazdy = True

# AND - oba warunki muszą być prawdziwe
if wiek >= 18 and ma_prawo_jazdy:
    print("Możesz prowadzić samochód")

# OR - przynajmniej jeden warunek musi być prawdziwy
jest_weekend = False
jest_urlop = True

if jest_weekend or jest_urlop:
    print("Możesz odpocząć")

# NOT - negacja warunku
jest_deszcz = False

if not jest_deszcz:
    print("Możesz iść na spacer")
```

### Operator warunkowy (ternary)

```python
wiek = 20
status = "pełnoletni" if wiek >= 18 else "niepełnoletni"
print(status)  # "pełnoletni"
```

### Sprawdzanie obecności elementu

```python
owoce = ["jabłko", "banan", "pomarańcza"]

if "banan" in owoce:
    print("Mamy banany!")

if "gruszka" not in owoce:
    print("Nie mamy gruszek")
```

### Warunki zagnieżdżone

```python
ocena = 85

if ocena >= 50:
    if ocena >= 90:
        print("Celujący")
    elif ocena >= 75:
        print("Bardzo dobry")
    else:
        print("Dobry")
else:
    print("Niedostateczny")
```

---

## 3. Pętle

### 3.1 Pętla for

#### Iteracja po sekwencjach

```python
# Iteracja po liście
owoce = ["jabłko", "banan", "pomarańcza"]
for owoc in owoce:
    print(owoc)

# Iteracja po stringu
for litera in "Python":
    print(litera)

# Iteracja po słowniku
osoba = {"imie": "Jan", "wiek": 30, "miasto": "Gdańsk"}

# Tylko klucze
for klucz in osoba:
    print(klucz)

# Klucze i wartości
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")
```

#### Funkcja range()

```python
# range(stop) - od 0 do stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - od start do stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step) - z krokiem
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Odliczanie w dół
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

```

### 3.2 Pętla while

```python
# Podstawowa pętla while
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1

# While z warunkiem
haslo = ""
while haslo != "python":
    haslo = input("Podaj hasło: ")
    if haslo != "python":
        print("Błędne hasło, spróbuj ponownie")
print("Dostęp przyznany!")
```


---

## 4. Funkcje

### 4.1 Definiowanie funkcji

```python
# Podstawowa funkcja
def powitanie():
    print("Witaj w Pythonie!")

# Wywołanie funkcji
powitanie()
```

### 4.2 Parametry i argumenty

```python
# Funkcja z parametrami
def powitaj_osobe(imie, wiek):
    print(f"Cześć {imie}, masz {wiek} lat")

powitaj_osobe("Anna", 25)

# Argumenty domyślne
def przedstaw_sie(imie, miasto="Warszawa"):
    print(f"Jestem {imie} z {miasto}")

przedstaw_sie("Jan")              # Używa domyślnej wartości
przedstaw_sie("Anna", "Gdańsk")   # Nadpisuje domyślną wartość

# Argumenty nazwane
przedstaw_sie(miasto="Kraków", imie="Piotr")
```

### 4.3 Zwracanie wartości

```python
# Funkcja zwracająca wartość
def dodaj(a, b):
    return a + b

wynik = dodaj(5, 3)
print(wynik)  # 8

# Zwracanie wielu wartości (krotka)
def statystyki(liczby):
    minimum = min(liczby)
    maksimum = max(liczby)
    srednia = sum(liczby) / len(liczby)
    return minimum, maksimum, srednia

min_val, max_val, avg = statystyki([1, 2, 3, 4, 5])
print(f"Min: {min_val}, Max: {max_val}, Średnia: {avg}")
```



### 4.4 Zakres zmiennych (scope)

```python
# Zmienna globalna
zmienna_globalna = "globalny"

def funkcja():
    # Zmienna lokalna
    zmienna_lokalna = "lokalny"
    print(zmienna_globalna)  # Dostęp do globalnej
    print(zmienna_lokalna)

funkcja()
# print(zmienna_lokalna)  # Błąd! Zmienna lokalna

# Modyfikacja zmiennej globalnej
licznik = 0

def zwieksz():
    global licznik
    licznik += 1

zwieksz()
print(licznik)  # 1
```

### 4.5 Dokumentacja funkcji (docstring)

```python
def oblicz_pole_prostokata(dlugosc, szerokosc):
    """
    Oblicza pole prostokąta.
    
    Args:
        dlugosc (float): Długość prostokąta
        szerokosc (float): Szerokość prostokąta
    
    Returns:
        float: Pole prostokąta
    
    Examples:
        >>> oblicz_pole_prostokata(5, 3)
        15
    """
    return dlugosc * szerokosc

# Wyświetlenie dokumentacji
print(oblicz_pole_prostokata.__doc__)
help(oblicz_pole_prostokata)
```

---

## 5. Programowanie obiektowe

### 5.1 Podstawy klas

```python
# Definicja klasy
class Osoba:
    # Metoda inicjalizująca (konstruktor)
    def __init__(self, imie, wiek):
        self.imie = imie  # Atrybut instancji
        self.wiek = wiek
    
    # Metoda instancji
    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} i mam {self.wiek} lat")
    
    def obchodzi_urodziny(self):
        self.wiek += 1
        print(f"Hurra! Mam teraz {self.wiek} lat")

# Tworzenie obiektów (instancji)
osoba1 = Osoba("Anna", 25)
osoba2 = Osoba("Jan", 30)

# Wywołanie metod
osoba1.przedstaw_sie()  # Cześć, jestem Anna i mam 25 lat
osoba1.obchodzi_urodziny()  # Hurra! Mam teraz 26 lat

# Dostęp do atrybutów
print(osoba2.imie)  # Jan
osoba2.wiek = 31    # Modyfikacja atrybutu
```

### 5.2 Atrybuty klasowe

```python
class Pracownik:
    # Atrybut klasowy (wspólny dla wszystkich instancji)
    firma = "Moja Firma Sp. z o.o."
    liczba_pracownikow = 0
    
    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1
    
    def wyswietl_info(self):
        print(f"{self.imie} - {self.stanowisko} w {Pracownik.firma}")
    
    @classmethod
    def zmien_nazwe_firmy(cls, nowa_nazwa):
        cls.firma = nowa_nazwa
    
    @staticmethod
    def czy_dzien_roboczy(dzien):
        return dzien not in ["sobota", "niedziela"]

# Użycie
pracownik1 = Pracownik("Anna", "Programista")
pracownik2 = Pracownik("Jan", "Tester")

print(Pracownik.liczba_pracownikow)  # 2
pracownik1.wyswietl_info()

# Metoda klasowa
Pracownik.zmien_nazwe_firmy("Nowa Firma")
pracownik2.wyswietl_info()

# Metoda statyczna
print(Pracownik.czy_dzien_roboczy("poniedziałek"))  # True
```

### 5.3 Dziedziczenie

```python
# Klasa bazowa (nadklasa)
class Zwierze:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    
    def wydaj_dzwiek(self):
        print("Jakiś dźwięk")
    
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} i mam {self.wiek} lat")

# Klasy pochodne (podklasy)
class Pies(Zwierze):
    def __init__(self, imie, wiek, rasa):
        super().__init__(imie, wiek)  # Wywołanie konstruktora klasy bazowej
        self.rasa = rasa
    
    # Nadpisanie metody (override)
    def wydaj_dzwiek(self):
        print("Hau hau!")
    
    # Nowa metoda specyficzna dla psa
    def aport(self):
        print(f"{self.imie} przynosi piłkę")

class Kot(Zwierze):
    def wydaj_dzwiek(self):
        print("Miau!")
    
    def mruczenie(self):
        print(f"{self.imie} mruczy")

# Użycie
pies = Pies("Burek", 3, "Owczarek")
kot = Kot("Mruczek", 2)

pies.przedstaw_sie()  # Dziedziczona metoda
pies.wydaj_dzwiek()   # Nadpisana metoda
pies.aport()          # Metoda specyficzna

kot.wydaj_dzwiek()
kot.mruczenie()
```

### 5.4 Enkapsulacja

```python
class KontoBankowe:
    def __init__(self, wlasciciel, saldo_poczatkowe=0):
        self.wlasciciel = wlasciciel
        self.__saldo = saldo_poczatkowe  # Atrybut prywatny (__)
    
    # Getter
    def pobierz_saldo(self):
        return self.__saldo
    
    # Setter z walidacją
    def wplac(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            print(f"Wpłacono {kwota} zł")
        else:
            print("Kwota musi być dodatnia")
    
    def wyplac(self, kwota):
        if kwota > 0:
            if kwota <= self.__saldo:
                self.__saldo -= kwota
                print(f"Wypłacono {kwota} zł")
            else:
                print("Niewystarczające środki")
        else:
            print("Kwota musi być dodatnia")

# Użycie
konto = KontoBankowe("Jan Kowalski", 1000)
konto.wplac(500)
print(konto.pobierz_saldo())  # 1500
konto.wyplac(200)
# print(konto.__saldo)  # Błąd! Atrybut prywatny
```

### 5.5 Property - eleganckie gettery i settery

```python
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, wartosc):
        if wartosc < -273.15:
            raise ValueError("Temperatura nie może być niższa niż -273.15°C")
        self._celsius = wartosc
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, wartosc):
        self.celsius = (wartosc - 32) * 5/9

# Użycie
temp = Temperatura(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 86
print(temp.celsius)      # 30.0

# temp.celsius = -300  # ValueError
```

## Wskazówki 
- Używajcie `input()` do pobierania danych od użytkownika
- Pamiętajcir o konwersji typów: `int()` dla liczb całkowitych, `float()` dla dziesiętnych
- Używajcie `print()` do wyświetlania wyników
- Sprawdzaj działanie programu krok po kroku (debuger)


## Zadanie 1 - Powitanie
Napisz program, który poprosi użytkownika o imię, a następnie wyświetli spersonalizowane powitanie.

**Przykład:**
```
Jak masz na imię? Jan
Witaj, Jan! Miło Cię poznać!
```

---
## Zadanie 2 - Sprawdzanie parzystości
Napisz funkcję, która przyjmuje liczbę całkowitą i zwraca informację, czy jest ona parzysta czy nieparzysta.

**Przykład:**
```python
sprawdz_parzystosc(4)  # "Liczba 4 jest parzysta"
sprawdz_parzystosc(7)  # "Liczba 7 jest nieparzysta"
```
---

## Zadanie 3 - Suma liczb z listy
Napisz funkcję, która przyjmuje listę liczb i zwraca ich sumę (bez używania wbudowanej funkcji `sum()`).

**Przykład:**
```python
suma_listy([1, 2, 3, 4, 5])  # Wynik: 15
suma_listy([10, 20, 30])     # Wynik: 60
```
---

## Zadanie 4 - Zliczanie samogłosek
Stwórz program, który policzy ile samogłosek (a, e, i, o, u, y) znajduje się w podanym przez użytkownika tekście.

**Przykład:**
```
Podaj tekst: Programowanie w Pythonie
Liczba samogłosek: 10
```
---

## Zadanie 5 - Zgadywanka liczb
Stwórz grę, w której komputer losuje liczbę od 1 do 100, a użytkownik próbuje ją odgadnąć. Po każdej próbie program powinien informować, czy podana liczba jest za duża, za mała, czy prawidłowa.

**Przykład:**
```
Zgadnij liczbę od 1 do 100: 50
Za mało!
Zgadnij liczbę od 1 do 100: 75
Za dużo!
Zgadnij liczbę od 1 do 100: 63
Gratulacje! Odgadłeś za 3 próby!
```
---

## Zadanie 6 - Proste działania matematyczne
Stwórz zmienne `a = 10` i `b = 5`. Wyświetl wyniki następujących operacji:
- Dodawanie
- Odejmowanie
- Mnożenie
- Dzielenie

---

## Zadanie 7 - Wiek w sekundach
Poproś użytkownika o podanie wieku w latach i oblicz, ile to sekund (zakładając rok = 365 dni).

**Przykład:**
```
Ile masz lat? 25
Masz około 788400000 sekund!
```
---

## Zadanie 8 - Pole prostokąta
Napisz program, który poprosi o długość i szerokość prostokąta, a następnie obliczy i wyświetli jego pole.

**Przykład:**
```
Podaj długość: 5
Podaj szerokość: 3
Pole prostokąta wynosi: 15
```

---


## Zadanie 9 - Większa liczba
Poproś użytkownika o podanie dwóch liczb i wyświetl, która z nich jest większa.

**Przykład:**
```
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 20
Większa liczba to: 20
```
---

## Zadanie 10 - Długość imienia
Poproś użytkownika o imię i wyświetl, ile ma ono znaków.

**Przykład:**
```
Jak masz na imię? Kuba
Twoje imię ma 4 litery.
```

---

