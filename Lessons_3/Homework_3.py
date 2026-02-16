#----1. Квадрат числа.

number = int(input("Введіть число:"))
x = number ** 2
print("квадрат числа:", x)

#----2. “Середнє трьох чисел”

x = float(input("Введіть число x :"))
y = float(input("Введіть число y :"))
z = float(input("Введіть число z :"))
average = (x + y + z) / 3
print("середнє число:", average)

#----3. “Перетворення хвилин у години”

time_in_minutes = int(input("Ваш час у хвилинах:"))
hours = time_in_minutes // 60
minutes = time_in_minutes % 60
print("У вас:", hours,":",minutes)

#----4. “Розрахунок знижки”

money = float(input("Початкова ціна:"))
discount = float(input("Знижка:"))
total = money - ((discount * money)/100)
print("Ціна зі знижкою:", total)

#----5. “Остання цифра числа”

number = int(input("Число:"))
last_number = number % 10
print("Останнє число:", last_number)

#----6. “Периметр прямокутника”

length = float(input("Довжина:"))
width = float(input("Ширина:"))
perimeter = (length + width) * 2
print("Периметр:", perimeter)

