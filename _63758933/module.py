
_generate_list = {name: arg for name, arg in zip('abcde', range(5))}

for name, arg in _generate_list.items():
    globals()[name] = lambda: print(arg)

