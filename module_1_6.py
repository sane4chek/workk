my_dict = {'Алекса': 1999, 'Мария': 2000, 'Иван': 2001, 'Роман': 2002, 'Лейла': 2003}
print('Словарь:', my_dict)
print('Год рождения Марии:', my_dict['Мария'])
print('Год рождения Елены:', my_dict.get('Елена', 'нет такого ключа'))
my_dict.update({'Роберт': 1995, 'Салима': 2005})
removed_year = my_dict.pop('Салима')
print('Значение удалённого элемента \'Салима\':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
my_set.discard(3)
print('Изменённое множество:', my_set)
