import random
zbior = set()
# dozwolone_waluty = ('PLN', 'EUR', 'USD')
# waluta = input("Podaj walute: ")
#
# if waluta in dozwolone_waluty:
#     print("Poprawna waluta")
# else:
#     print(f"Nieznany kod waluty, podano {waluta}.")

# for i in dozwolone_waluty:
#     print(i)

# totolotek = {12,25,33,41,12,33}
# print(totolotek)

def dodaj_liczby(liczba):
    zbior.add(liczba)
    print(zbior)

# dodaj_liczby(random.randint(1,10))
# dodaj_liczby(random.randint(1,10))
# dodaj_liczby(random.randint(1,10))
# dodaj_liczby(random.randint(1,10))
# dodaj_liczby(random.randint(1,10))

for i in range(5):
    dodaj_liczby(random.randint(1,10))

nowa_lista = list(zbior)
nowa_lista.sort()
print(nowa_lista)