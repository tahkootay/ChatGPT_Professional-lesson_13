import datetime
import random

def generate_random_time_stamps(num_time_stamps, date):
    time_stamps = []
    for _ in range(num_time_stamps):
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        microseconds = random.randint(0, 999999)
        time_stamp = datetime.datetime(date.year, date.month, date.day, hours, minutes, seconds, microseconds)
        time_stamps.append(time_stamp.isoformat())
    return time_stamps

# Используем сегодняшнюю дату для генерации временных отметок
today = datetime.date.today()

# Генерируем список из 50 временных отметок
time_stamps = generate_random_time_stamps(100, today)
# Проверяем результат, напечатав некоторые отметки из списка
#for ts in time_stamps:  # Выводим первые три для примера
print(time_stamps)