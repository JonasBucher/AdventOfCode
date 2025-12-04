def parse_input(raw: str) -> list[list[int]]:
    sequences = raw.strip().splitlines()
    return [[int(c) for c in s] for s in sequences]


def solve_part1(data: list[list[int]]) -> int:
    sum_of_joltages = 0

    for digits in data:
        leading_digit = max(digits[:-1])
        leading_digit_index = digits.index(leading_digit)
        trailing_digit = max(digits[leading_digit_index + 1:])
        
        sum_of_joltages += leading_digit * 10 + trailing_digit

    return sum_of_joltages


def solve_part2(data: list[list[int]], number_of_digits: int = 12) -> int:
    sum_of_joltages = 0

    for digits in data:
        min_index = 0
        
        for i in range(number_of_digits - 1, 0, -1):
            max_value = max(digits[min_index:-i])
            sum_of_joltages += max_value * (10 ** i)
            min_index = digits.index(max_value, min_index, -i) + 1

        sum_of_joltages += max(digits[min_index:])

    return sum_of_joltages