x = 4 + 5j
while x:
    if isinstance(x, int):
        x = x + 3
        print(x)
        break
    elif isinstance(x, float):
        x = x // 2
        print(x)
        break
    elif isinstance(x, complex):
        print("Numarul complex "+ str(complex(x))+ "\n" + "Valoare modul " + str(abs(x)))
        break
    else:
        print("Insert numeric value")
