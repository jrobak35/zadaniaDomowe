dozwoloneWaluty = ["PLN", "EUR", "USD"]
lista = []
lista.append("Slawek")
lista.append("Witek")
lista.append("Tomek")
lista.append("Kuba")
lista.append(2023)
# Nie możemy kilku elementów wrzucić naraz przez append, tak ręcznie. Ale możemy np. jakąs liste dorzucić gdzie jest kilka elementów
lista.append(dozwoloneWaluty)

lista.insert(0, "Piechol")

# lista.sort()
# nie sortujemy listy, która ma różne elementy wewnątrz
# w liscie można przechowywac wszystko, ale nie można sortowac listy z roznymi typami

print(lista)
#print(lista[6])
print(lista[6][2])
zmienna = lista[6][0:2]
print(zmienna)

#POP zawsze usuwa ostatni element

lista.pop()
print(lista)

lista.remove("Piechol")
print(lista)

lista.clear()
print(lista)

# Do listy można dodać inne listy inne typy danych i nawet krotki