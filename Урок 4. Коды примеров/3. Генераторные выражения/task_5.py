"""Генераторы списков и словарей"""

# обычный цикл
my_list = [2, 4, 6]
print(f"Исходный список: {my_list}")  # -> Исходный список: [2, 4, 6]
new_list = []
for el in my_list:
    new_list.append(el + 10)
print(f"Новый список: {new_list}")  # -> Новый список: [12, 14, 16]

# генераторное выражение
my_list = [2, 4, 6]
new_list = [el+10 for el in my_list]
print(f"Исходный список: {my_list}")  # -> Исходный список: [2, 4, 6]
print(f"Новый список: {new_list}")  # -> Новый список: [12, 14, 16]
