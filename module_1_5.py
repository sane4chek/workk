immutable_var = 43, 'beautiful', 9.12, False # для кортежа скобки не обязательно
print(immutable_var)

immutable_var2 ='привет', # Если нужно создать кортеж с одним элементом, то запятую обязательно надо ставить
print(type( immutable_var2))

#В отличие от списков, кортежи неизменяемы. Однако если элемент сам по себе является изменяемым типом данных (например, списком), его вложенные элементы менять уже можно.


#my_typle = 'b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l',    Изменять элементы кортежа нельзя. Это значит, что удалять их тоже нельзя.
#del my_typle[3] - TypeError: 'tuple' object doesn't support item deletion (появится ошибка)


mutable_list = ["яблоко", 23, True]
mutable_list[1] = 1000
mutable_list[2] = False
mutable_list. append("банан")
mutable_list. extend('персик')
print(mutable_list)




