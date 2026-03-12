
while True:

    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть оператор (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if operator == '+':
        print("Результат:", num1 + num2)
    elif operator == '-':
        print("Результат:", num1 - num2)
    elif operator == '*':
        print("Результат:", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print("Результат:", num1 / num2)
        else:
            print("Помилка: Ділення на нуль!")
    else:
        print("Невідомий оператор!")

    user_choice = input("Бажаєте продовжити? (y/yes): ").lower()

    if user_choice != 'y' and user_choice != 'yes':
        print("Програма завершена.")
        break