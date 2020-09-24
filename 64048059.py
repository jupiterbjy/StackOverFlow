from itertools import product


source = [1.1, 1.3, 2.1, 2.2, 2.3]
separated = [str(n).split(".") for n in source]

integers, decimals = map(set, zip(*separated))
products = [float(f"{i}.{d}") for i, d in product(integers, decimals)]

print(*(set(products) ^ set(source)))
