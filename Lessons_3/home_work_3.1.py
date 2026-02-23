number_1 = int(input("1_st number:"))
number_2 = int(input("2_nd number:"))

actions = input("Write your actions:")
if actions == "+":
    answer = number_1 + number_2
    print(answer)
elif actions == "-":
    answer = number_1 - number_2
    print(answer)
elif actions == "/":
    if number_2 == 0:
        print("wrong!")
    else:
        answer = number_1 // number_2
        print(answer)
elif actions == "*":
    answer = number_1 * number_2
    print(answer)
else:
    print("Wrong!")
