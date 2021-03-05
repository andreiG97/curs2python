while True:
    value = input("Insert values")
    suma = 0
    if value.isnumeric():
        newValue = int(value)
        if newValue > 2:
            for i in range(1, newValue+1):
                suma = i
                suma += suma
            print(suma)
            break
        else:
            print("Please insert a valid value ")
    else:
        print("Insert numerical values")
