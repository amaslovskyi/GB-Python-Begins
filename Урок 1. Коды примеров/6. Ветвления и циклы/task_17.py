
i = 0
while True:
    i += 1
    if i >= 10:
        # инструкция break при выполнении немедленно заканчивает выполнения цикла
        break
    if i % 2 == 0:
        # переходим к проверке условия цикла,
        # пропуская все операторы за инструкцией
        continue
    print(i)
    #i += 1

my_list = [1, 2, 3]
for el in my_list:
    print(el)
