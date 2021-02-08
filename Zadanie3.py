def str_to_dict(s):
    return {i + 1: c for i, c in enumerate(s)}


my_string = "Тест"
print(str_to_dict(my_string))
