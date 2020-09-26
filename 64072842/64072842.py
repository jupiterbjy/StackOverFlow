import timeit

with open('test.txt', 'w') as fp:
    print(*("Just a test case" for i in range(1000000)), sep='\n', file=fp)


def a1():
    with open('test.txt', 'r') as f:
        for _ in f.readlines():
            pass


def a2():
    with open('test.txt', 'r') as f:
        while _ := f.readline():
            pass


def a3():
    with open('test.txt', 'r') as f:
        for _ in iter(f.readline, ''):
            pass


def readline_mock(n=None):
    with open('test.txt', 'r') as f:
        if n:
            _ = f.read(n)
        else:
            data = ''
            while t := f.read(1):
                data += t

                if not t:
                    break



# print(timeit.timeit(a1, number=50))
# print(timeit.timeit(a2, number=50))
# print(timeit.timeit(a3, number=50))

print(timeit.timeit(readline_mock))
