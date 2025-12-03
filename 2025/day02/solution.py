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

def iter_pairs(data):
    for start, end in data:
        for number in range(start, end + 1):
            number_str = str(number)
            yield number_str, len(number_str) / 2

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))

def all_equal(values):
    return all(x == values[0] for x in values)