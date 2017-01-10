
keys_list = [1, 2, 3, 4, 5, 6]
values_list = ['Paul', 'Oxana', 'Angelina', 'Katerine', 'Maxime', 'asdasd', 2123, 12]
result_dict = {
}


def dict_from_keys(keys, values):
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))


print(dict_from_keys(keys_list, values_list))
