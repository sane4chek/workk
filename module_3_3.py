def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = (123, "body", False)
dictionary = {'a': 1, 'b': 'body', 'c': False}
dictionary = {'a': 1, 'b': 'body', 'c': False}

print_params(*values_list)
print_params(**dictionary)


values_list_2 = (500.123, "monkey")

print_params(*values_list_2, 42)
