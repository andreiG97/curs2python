value = input("Insert value: ")

try:
    value = int(value)
    if value % 2 == 0:
        print(str(value) + " is even")
    else:
        print(str(value) + " is odd")
except:
    print("Invalid input, please insert numerical")
