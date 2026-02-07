
lista = [1,2,3,4,5,7,6,8,9]

print(f"Przed usunieciem {lista}")

lista.pop()

print(f"Po usunieci {lista}")

lista.remove(1)
print(f"Po usunieci przez remove {lista}")

### Sortowanie
### print("Czesc Olga")

lista_2 = [1,2,4,3,9,8,7]
print(f"Przed sortowaniem {lista_2}")

lista_2.sort()
print(f"Po sortowaniu {lista_2}")

print(lista)

# Reverse
lista_2.reverse()
print(f"Po reverese {lista_2}")

lista_2 = [1,2,4,3,9,8,7]

small_list = lista_2[:5]


print(f" Typ danych po obcięciu: {type(small_list)}. \n Wartosci w nowej obcietej liscie {small_list}")


lista_owocow =  ["jablko","kawa","marchew","gruszka"]

for item in lista_owocow:
    print(item)
    
