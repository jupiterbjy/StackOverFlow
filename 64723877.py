from pprint import pprint


source = [list(range(n, n + 4)) for n in range(4)]
pprint(source, width=41)


def pad_frame_once(src_: list, pad) -> list:
    output = [[pad, *line, pad] for line in src_]
    return [[pad] * len(output[0]), *output, [pad] * len(output[0])]


def pad_grid(src_, padding_size: int, pad=0):
    reference = src_
    for _ in range(padding_size):
        reference = pad_frame_once(reference, pad)

    return reference


pprint(pad_frame_once(source, pad=0))
pprint(pad_grid(source, 3))
