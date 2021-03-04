#EX1
# while True:
#     userInput = input("Insert data: ")
#     if userInput == "telacad":
#         print("End of program")
#         break

#EX2
# while True:
#     value = input("Insert values")
#     suma = 0
#     if value.isnumeric():
#         newValue = int(value)
#         if newValue > 2:
#             for i in range(1, newValue+1):
#                 suma = i
#                 suma += suma
#             print(suma)
#             break
#         else:
#             print("Please insert a valid value ")
#     else:
#         print("Insert numerical values")

#EX3
# seq = ["telacad", "over 13 years of experience", "in", "teaching", "online courses"]
#
# while True:
#     newInput = input("Insert value: ")
#     if newInput == "telacad":
#        print(" ".join(seq))
#        break
#     else:
#         print("Insert new value")

#EX4
#
# x = 4 + 5j
# while x:
#     if isinstance(x, int):
#         x = x + 3
#         print(x)
#         break
#     elif isinstance(x, float):
#         x = x // 2
#         print(x)
#         break
#     elif isinstance(x, complex):
#         print("Numarul complex "+ str(complex(x))+ "\n" + "Valoare modul " + str(abs(x)))
#         break
#     else:
#         print("Insert numeric value")

#EX5
#
# while True:
#     value = input("Insert value ")
#     try:
#         value = float(value)
#         valInteger = int(value)
#         if value > 10 :
#             print("{}{}".format(value, " is greater than 10 " ) + "\n"
#                   "{}{}".format(valInteger, " is greater than 10"))
#         elif 5 <= value <= 10:
#             print("{}{}".format(value, " is between 5 and 10") + "\n"
#                   "{}{}".format(valInteger, " is greater than 10"))
#         elif value < 5:
#             print("{}{}".format(value, " is below 5") + "\n"
#                   "{}{}".format(valInteger, " is greater than 10"))
#         else:
#             print("Error")
#         break
#     except :
#         print("Insert numerical value")

#EX6
#
# value = input("Insert value: ")
#
# try:
#     value = int(value)
#     if value % 2 == 0:
#         print(str(value) + " is even")
#     else:
#         print(str(value) + " is odd")
# except:
#     print("Invalid input, please insert numerical")

#EX7
#
# value = input("Insert value: ")
#
# if value.isnumeric():
#     value = int(value)
#     if value > 1 and value != 2:
#         for i in range(2, value):
#             if value % i == 0:
#                 print(value, "is not prime")
#                 break
#             else:
#                 print(value, "is prime")
#                 break
#     else:
#         print("2 is prime")
# else:
#     print("Only numbers > 1 can be prime")

#EX8
#
# count = 0
# term = 0
# increment = 1
#
# while count < 5:
#     print(term)
#     temp = term + increment
#     term = increment
#     increment = temp
#     count += 1
#
# for i in range(5):
#     print(term)
#     temp = term + increment
#     term = increment
#     increment = temp


