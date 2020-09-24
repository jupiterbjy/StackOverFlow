from ast import literal_eval


lines = ['foo True 8 9.2', 'bar False 17 -3.1']

for line in lines:
    for word in line.split():
        try:
            eval_ed = literal_eval(word)
        except ValueError:
            eval_ed = word  # it's a string, EAFP at it's finest
        print(type(eval_ed), eval_ed)
