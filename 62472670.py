
# just converting data
raw_data = '''
0      1      1
1      1      2
2      1      3
3      2      4
4      2      5
5      2      6
6      2      7
7      2      8
8      2      9
9      3     10
10     3     11
11     3     12'''.lstrip().split('\n')

data = [list(map(int, row.split())) for row in raw_data]
# ---------------------------


def tablePrint(lst: list):
    print('   my_cls  val')
    for row in lst:
        print(''.join([str(i).ljust(6) for i in row]))


def gen_filtered(lst: list):
    last = 0
    for row in lst:
        if row[1] == last:
            continue

        last = row[1]
        yield row[1]

