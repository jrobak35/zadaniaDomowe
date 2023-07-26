# imie = "Kuba"
# rok = 2023

imie = input("podaj imie: ")
rok = input("podaj rok: ")

# print(type(imie))
# print(type(rok))
# print(type(imie), type(rok))

print("Podane imie to: " + imie)
print("Podany wiek to: " + rok)

if int(rok) == 1988:
    print("Zajebiście!")

# if rok < 2020:
#     print("Dopiero co był 2020 i pandemia. Lata lecą!")
# elif rok >= 2020 and rok <= 2023:
#     print("Trafiony zatopiony!")
#     if imie != "Tomek":
#         print("No witam!")
# else:
#     print("Na szczęście cofamy się w czasie")