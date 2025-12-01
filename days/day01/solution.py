def parse_input(raw: str):
    items = []
    for line in raw.splitlines():
        d, amt_str = line[0], line[1:]
        direction = -1 if d.upper() == "L" else 1

        items.append({"direction": direction, "amount": int(amt_str)})
    return items


def solve_part1(data):
    return _run_moves(data, visit_each_step=False)


def solve_part2(data):
    return _run_moves(data, visit_each_step=True)

def _run_moves(data, visit_each_step: bool):
    number_of_positions = 100
    start_position = 50
    position_visited = [0] * number_of_positions

    current_position = start_position
    for move in data:
        direction = move["direction"]
        amount = move["amount"]
        for _ in range(amount):
            current_position = (current_position + direction) % number_of_positions
            if visit_each_step:
                position_visited[current_position] += 1
        if not visit_each_step:
            position_visited[current_position] += 1
        print(f"Moved {direction * amount} to position {current_position}")
    return position_visited[0]
