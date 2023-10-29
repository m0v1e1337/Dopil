def calculate_lived_days(year_of_birth):
    import datetime
    current_date = datetime.datetime.now()
    days_in_year = 365 if not current_date.year % 4 == 0 or (current_date.year % 100 == 0 and current_date.year % 400 != 0) else 366
    days_lived = (current_date.year - year_of_birth) * days_in_year
    return days_lived

year_of_birth = int(input("Введите год рождения: "))
lived_days = calculate_lived_days(year_of_birth)
print("Количество прожитых дней: ", lived_days)






def count_substrings(substring, string):
    count = string.count(substring)
    return count

substring = input("Введите подстроку: ")
string = input("Введите строку: ")
substrings_count = count_substrings(substring, string)
print("Количество встреченных подстрок: ", substrings_count)








import math

def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def calculate_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Нет действительных корней"

def calculate_probability_joint(events):
    probability = 1
    for event in events:
        probability = probability * event
    return probability

def calculate_probability_not_joint(event1, event2):
    probability_not_joint = 1 - event1 - event2
    return probability_not_joint

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = calculator.calculate_discriminant(a, b, c)
print("Дискриминант: ", discriminant)

if discriminant > 0:
    root1, root2 = calculator.calculate_roots(a, b, c)
    print("Корни уравнения: ", root1, root2)
elif discriminant == 0:
    root = calculator.calculate_roots(a, b, c)
    print("Корень уравнения: ", root)
else:
    print("Нет действительных корней")

event1 = float(input("Введите вероятность события 1: "))
event2 = float(input("Введите вероятность события 2: "))

joint_probability = calculator.calculate_probability_joint([event1, event2])
print("Вероятность совместных событий: ", joint_probability)

not_joint_probability = calculator.calculate_probability_not_joint(event1, event2)
print("Вероятность несовместных событий: ", not_joint_probability)
