from itertools import product

extensions = 'abc'

for filename in product(extensions, repeat=2):
    with open(f"{filename[0]}.{filename[1]}", "w") as fp:
        fp.close()

