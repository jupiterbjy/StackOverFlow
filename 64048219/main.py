import pickle
from sys import modules
from os import listdir

main_script = modules['__main__']

for file in [path for path in listdir() if path.endswith('pk1')]:
    with open(file, "rb") as fp:
        setattr(main_script, fp.name.split('.')[0], pickle.load(fp))


print(a, b, c, d, e, sep='\n')
