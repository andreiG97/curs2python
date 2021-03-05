seq = ["telacad", "over 10 years of experience", "in", "teaching", "online courses"]

while True:
    newInput = input("Insert value: ")
    if newInput == "telacad":
       print(" ".join(seq))
       break
    else:
        print("Insert new value")