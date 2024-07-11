immutable_var = (1, 2.5, 'Пять', True)
print(immutable_var)
# immutable_var[0] = 3 Высвечивается ошибка "TypeError: 'tuple' object does not support item assignment" - элемент изменить нельзя
mutable_list = [1, 2.5, 'Пять', True]
print(mutable_list)
mutable_list[0] = 3
print(mutable_list)