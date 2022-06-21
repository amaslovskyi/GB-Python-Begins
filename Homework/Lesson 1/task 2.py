'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в
формате чч:мм:сс. Используйте форматирование строк.
'''
time = int(input("Input time in seconds: "))  # время в секундах
time_minuts = time / 60  # в минутах
time_hours = time_minuts / 60  # в часах
print(f"Your time is {time_hours:.2f}:{time_minuts:.2f}:{time} ")  # выводим все на экран