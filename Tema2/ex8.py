count = 0
term = 0
increment = 1

while count < 5:
    print(term)
    temp = term + increment
    term = increment
    increment = temp
    count += 1

# for i in range(5):
#     print(term)
#     temp = term + increment
#     term = increment
#     increment = temp
