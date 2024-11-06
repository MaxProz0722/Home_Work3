def print_params(*params, a = 1, b = 'строка', c = True):
    print(*params, a, b, c)


print_params()
print_params(a = 2, b = 3, c = 5)
print_params(b = 25)
print_params(c = [1,2,3])

value_list = ['@', 2, float]
value_dict = {'a': True, 'b': 2, 'c': 'yo'}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = ['yes', False]
print_params(*values_list_2, 42)