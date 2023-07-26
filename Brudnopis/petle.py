jezyki = ["C", "Python", "Java"]
cyfry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Języki programowania")
#
# for x in range(len(jezyki)):
#     print(jezyki[x])

# for x in range(1, len(cyfry), 2):
#     print(f"Cyfry kolejno: {cyfry[x]}")

# Specjalną reprezentacją w pythonie jest gwiazdka.

# print(*cyfry)
# print(*cyfry, sep='-')

# for p in range(3):
#     for q in range(4):
#         if q == 2:
#             print(f"Pomijam q={q}")
#             continue
#     print(f'(p={p}, q={q})')


# for p in range(3):
#     for q in range(4):
#         if q == 2:
#             print(f"Pomijam q={q}")
#             break
#     print(f'(p={p}, q={q})')

# for p in range(len(jezyki)):
#     for q in range(len(cyfry)):
#         if q == 2:
#             print(f"Pomijam q={cyfry[q]}")
#             break
#     print(f'(p={p}, q={cyfry[q]})')

# while True:
#     print("Menu:")
#     print("1. policz")
#     print("2. wyjdz")
#     print("------")
#     wybor = input("Wybierz opcje:")
#     if wybor == "1":
#         print("Suma: ", 50 + 55)
#     elif wybor == "2":
#         break
#     else:
#         print("Nieznana opcja!")

# i = 97
# tmp = 0
# while i <= 100:
#     tmp = tmp + 1
#     i = i + 1
#
# print("Suma liczb od 1 do 99 wynik:", tmp, i)

# i = 11
# tmp = 0
# while i <= 100:
#     tmp = tmp + i
#     i = i + i
#
# print("Suma liczb od 1 do 99 wynik:", tmp)

count = 0
while True:
    count += 1
    print("To jest iteracja nr", count)
    if count >= 5:
        break