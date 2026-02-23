number_1 = int(input("1_st number:"))
number_2 = int(input("2_nd number:"))

print("+_print_1:")
print("-_print_2:")
print("/_print_3:")
print("*_print_4:")

actions = input("Write your actions:")
if actions == "1":
    answer = number_1 + number_2
    print(answer)
elif actions == "2":
    answer = number_1 - number_2
    print(answer)
elif actions == "3":
    if number_2 == 0:
        print("wrong!")
    else:
        answer = number_1 // number_2
        print(answer)
elif actions == "4":
    answer = number_1 * number_2
    print(answer)
else:
    print("Wrong!")
