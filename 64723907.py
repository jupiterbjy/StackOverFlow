chess = [
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 6, 1, 2, 1],
]

def validate_position(board, pos: str) -> (int, int):
    try:
        x, y = map(int, pos.split())  # Fail-fast
    except ValueError as err:
        raise ValueError(f"Not enough / Too many values, expected 2!") from err

    # put some rule check here.
    if (0 <= x < len(board)) and (0 <= y < len(board[0])):
        return board[x][y], x, y

    raise ValueError(f"Position {(x, y)} is outside of board!")


def piece_position(board):
    inp = input("Enter coordinates (x y): ")  # Expecting 1 10 format
    try:
        return validate_position(board, inp)
    except ValueError as err:
        print(err)
        return piece_position(board)


print(f"Selected: {piece_position(chess)}")
