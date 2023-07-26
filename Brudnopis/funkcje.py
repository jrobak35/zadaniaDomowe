def drukuje():
    print("drukuje...")


def dodawanie(a, b = 0):
    suma = a + b
    return suma


print("A tutaj coś innego z programu głównego...")

for i in range(5):
    drukuje()

wyniki = []
wyniki.append(dodawanie(5, 5))
wyniki.append(dodawanie(22, 533))
wyniki.append(dodawanie(52223, 53333))
wyniki.append(dodawanie(52223))

print(wyniki)

# komunikat = "[Odmówił podania danych]"

# def pacjent(numer, imie = komunikat, nazwisko = komunikat):
#     print(f"Pacjent: nr = {numer}, imie = {imie}, nazwisko = {nazwisko}")
#
# pacjent(1)
# pacjent(2, "Tomasz")
# pacjent(3, nazwisko = "Kowalski")

komunikat = "[Odmówił podania danych]"
pacjenci = ["Tomasz", "Adam", "Robert", 'Inga']

def pacjent(numer, imie=komunikat, nazwisko=komunikat):
   return numer,imie,nazwisko


kolejka = []
for index,pc in enumerate(pacjenci):
    kolejka.append(pacjent(index+1,pc))

print(kolejka)

def parametry(*args):
    for x in range(len(args)):
        print(f"Parametry, które dotarły do funkcji: {args[x]}")

parametry()
parametry(23)
parametry(23, "Tomek")
parametry(23, "Tomek", [4, 5, 6])