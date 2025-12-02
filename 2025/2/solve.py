
from typing import List, Tuple
from functools import reduce

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def parse_input(path: str) -> List[Tuple[int, int]]:
    with open(path, 'r') as file:
        line = file.read()
    return [tuple(map(int, range.strip().split('-'))) for range in line.split(',')]

def find_repeating_sequences(id_ranges: List[Tuple[int, int]]) -> set[int]:
    invalid_ids : List[str] = []
    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            digits = str(id)
            # for idx, digit in enumerate(digits):
            digits_len = len(digits)
            if digits_len % 2 != 0 or digits_len == 1:
                continue
            part1 = digits[:digits_len//2]
            part2 = digits[digits_len//2:]
            if part1 == part2:
                invalid_ids.append(digits)

    print(sum(map(int, invalid_ids)))

def find_repeating_sequences2(id_ranges: List[Tuple[int, int]]) -> set[int]:
    invalid_ids : List[str] = []
    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            digits = str(id)
            digits_len = len(digits)
            all_factors = factors(digits_len)
            if digits_len == 1:
                continue
            for factor in all_factors:
                if factor == digits_len:
                    continue
                groups = []
                for i in range(0, digits_len, factor):
                    groups.append(digits[i:i + factor])
                if all_equal(groups):
                    invalid_ids.append(digits)
                    break

    print(sum(map(int, invalid_ids)))            

if __name__ == "__main__":
    input_path = '2025/2/input.txt'
    ranges = parse_input(input_path)
    find_repeating_sequences2(ranges)


    
    