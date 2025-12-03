from typing import Iterator
from collections import Counter
from math import gcd
from functools import reduce

def parse_input(raw: str):
    pairs = raw.strip().split(",")
    return [(int(pair.split("-")[0]), int(pair.split("-")[1])) for pair in pairs]

def solve_part1(data):
    sum = 0
    
    for number_str, half_length in iter_pairs(data):
        if half_length.is_integer() and number_str[:int(half_length)] == number_str[int(half_length):]:
            sum += int(number_str)

    return sum

def solve_part2(data):
    sum = 0
    
    for number_str, half_length in iter_pairs(data):
        for i in range(int(half_length), 0, -1):
            chunk_str = chunkstring(number_str, i)
            if len(chunk_str) >= 2 and all_equal(chunk_str):
                sum += int(number_str)
                break

    return sum

def iter_pairs(data: list[tuple[int, int]]) -> Iterator[tuple[str, float]]:
    for start, end in data:
        for number in range(start, end + 1):
            number_str = str(number)
            if has_valid_digit_frequencies(number_str): # Only consider numbers with valid digit frequencies for more efficiency
                yield number_str, len(number_str) / 2

def has_valid_digit_frequencies(number_str: str) -> bool:
    # counts = list(Counter(number_str).values())
    counts = count_digit_frequencies(number_str) # More efficient than Counter for this use case
    
    if 1 in counts:
        return False
    
    if len(counts) == 1:
        return True
    
    return gcd(counts) > 1

def count_digit_frequencies(number_str: str) -> list[int]:
    freq = [0] * 10
    for character in number_str:
        freq[int(character)] += 1
    return freq

def gcd(numbers: list[int]) -> int:
    ggt = numbers[0]
    for number in numbers[1:]:
        ggt = gcd_two_numbers(ggt, number)
        if ggt == 1:
            return 1
    return ggt

def gcd_two_numbers(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def chunkstring(number_str: str, length: int) -> list[str]:
    return list(number_str[0+i:length+i] for i in range(0, len(number_str), length))

def all_equal(values: list[str]) -> bool:
    return all(x == values[0] for x in values)
