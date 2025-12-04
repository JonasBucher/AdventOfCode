import numpy as np

LOOK_DISTANCE = 1
MAX_ALLOWED_NEIGHBORS = 3

def parse_input(raw: str) -> np.ndarray:
    rows = raw.strip().splitlines()
    data = [[c == '@' for c in row] for row in rows]
    return np.array(data)


def solve_part1(data: np.ndarray) -> int:
    cnt = 0
    padded = pad_data(data, LOOK_DISTANCE)

    for x in range(LOOK_DISTANCE, len(padded) - LOOK_DISTANCE):
        for y in range(LOOK_DISTANCE, len(padded[0]) - LOOK_DISTANCE):
            cnt += check_can_move(padded, x, y)

    return cnt


def solve_part2(data: np.ndarray) -> int:
    cnt = 0
    padded = pad_data(data, LOOK_DISTANCE)

    while True:
        to_remove = np.zeros_like(padded)

        for x in range(LOOK_DISTANCE, len(padded) - LOOK_DISTANCE):
            for y in range(LOOK_DISTANCE, len(padded[0]) - LOOK_DISTANCE):
                if check_can_move(padded, x, y):
                    to_remove[x][y] = True

        if not to_remove.any():
            break

        padded[to_remove] = False
        cnt += to_remove.sum()

    return cnt
    

def check_can_move(data: np.ndarray, x: int, y: int) -> bool:
    if not data[x][y]:
        return False
    
    cnt_neighbors = data[x-LOOK_DISTANCE:x+LOOK_DISTANCE+1, y-LOOK_DISTANCE:y+LOOK_DISTANCE+1].sum() - 1
    return cnt_neighbors <= MAX_ALLOWED_NEIGHBORS


def pad_data(data: np.ndarray, pad_width: int) -> np.ndarray:
    return np.pad(data, pad_width, mode='constant', constant_values=False)