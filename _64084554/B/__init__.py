try:
    from _64084554.A import a

    print("IDE import")
except ImportError:
    from os import getcwd
    from sys import path

    path.append(getcwd() + "/..")
    from _64084554.A import a
    print("without IDE")

print(a)
