import datetime

# Функция для определения дня недели
def weekday_of_birthdate(day, month, year):
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    birth_date = datetime.datetime(year, month, day)
    return week_days[birth_date.weekday()]

# Функция для определения високосного года
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Функция для определения возраста пользователя
def calculate_age(year):
    current_year = datetime.datetime.now().year
    return current_year - year

# Запрос данных у пользователя
day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

# Вывод информации о дне недели, високосном годе и возрасте пользователя
print("\nДень недели вашего рождения: ", weekday_of_birthdate(day, month, year))
if is_leap_year(year):
    print("Этот год был високосный.")
else:
    print("Этот год не был високосным.")
print("Вам сейчас", calculate_age(year), "лет.")

# Вывод даты рождения пользователя в формате звёздочек
print("\nДата вашего рождения в формате звёздочек:")
print(f"** {day:02d} ** {month:02d} ** {year:04d} **")

