import pickle

for i, n in enumerate('abcde'):
    with open(f"{n}.pk1", "wb") as fp:
        pickle.dump([*iter(range(i))], fp)

