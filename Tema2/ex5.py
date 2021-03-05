while True:
    value = input("Insert value ")
    try:
        value = float(value)
        valInteger = int(value)
        if value > 10 :
            print("{}{}".format(value, " is greater than 10 " ) + "\n"
                  "{}{}".format(valInteger, " is greater than 10"))
        elif 5 <= value <= 10:
            print("{}{}".format(value, " is between 5 and 10") + "\n"
                  "{}{}".format(valInteger, " is greater than 10"))
        elif value < 5:
            print("{}{}".format(value, " is below 5") + "\n"
                  "{}{}".format(valInteger, " is greater than 10"))
        else:
            print("Error")
        break
    except :
        print("Insert numerical value")
