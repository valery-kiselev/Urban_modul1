#1st program
my_dict = {'Иван': 2000, 'Мария': 2002}
print(my_dict)
print(my_dict['Иван'])
print(my_dict.get('Кирил'))
my_dict.update({'Евгений': 1997, 'Татьяна': 2001})
print(my_dict)

#2nd program
my_set = {5, 3, 2, 2, 3, 4, 'string1', 'string2', True}
print(my_set)
my_set.update({10, 'string3', False})
print(my_set)
my_set.discard('string3')
print(my_set)