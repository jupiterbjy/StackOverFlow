import re
import timeit


def parse_rgb_gen(filename="source.txt"):

    with open(filename) as fp:
        for line in fp:
            yield "\t".join(line.split())

def wrapped():
    for item in parse_rgb_gen():
        repr(item)


def parse_re_gen(filename):
    regex = re.compile(r"[ \t]*(\d+)[ \t]*(\d+)[ \t]*(\d+)[ \t]*(.*)")

    with open(filename) as f:  # "r" = "rt" and already default, no need to specify.
        for line in f:
            try:
                yield regex.match(line).groups()
            except AttributeError:  # first line falls here. " ! $Xorg:~~~ "
                pass

def wrapped_re():
    gen_instance = parse_re_gen('source.txt')

    for record in gen_instance:
        # print(record)
        print(repr("\t".join(record)))

# res1 = f"without re: {timeit.timeit(parse_rgb_gen, number=100):.4}"
# res2 = f"without re: {timeit.timeit(red_green_blue, number=100):.4}"

wrapped_re()
