x = 4 + 9j

if isinstance(x, int):
    x = x + 3
    print(x)

elif isinstance(x, float):
    x = x // 2
    print(x)

elif isinstance(x, complex):
    print("Numarul complex "+ str(complex(x))+ "\n" + "Valoare modul " + str(abs(x)))

else:
    print("Insert numeric value")

