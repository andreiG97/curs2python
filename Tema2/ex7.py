value = input("Insert value: ")

if value.isnumeric():
    value = int(value)
    if value > 1 and value != 2 and value != 0:
        for i in range(2, value):
            if value % i == 0:
                print(value, "is not prime")
                break
            else:
                print(value, "is prime")
                break
    elif value == 2:
        print("2 is prime")
    else:
        print("Can't insert 0")
else:
    print("Only numbers > 1 can be prime")
