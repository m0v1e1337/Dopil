def calculate_lived_days(year_of_birth):
    import datetime
    current_date = datetime.datetime.now()
    days_in_year = 365 if not current_date.year % 4 == 0 or (current_date.year % 100 == 0 and current_date.year % 400 != 0) else 366
    days_lived = (current_date.year - year_of_birth) * days_in_year
    return days_lived

year_of_birth = int(input("Введите год рождения: "))
lived_days = calculate_lived_days(year_of_birth)
print("Количество прожитых дней: ", lived_days)