from typing import Tuple


def parse_database(path: str) -> Tuple[list, list]:
    with open(path, 'r') as file:
        id_ranges, ids = file.read().split('\n\n')
    id_ranges = [tuple(map(int, line.split('-'))) for line in id_ranges.splitlines()]
    ids = [int(line) for line in ids.splitlines()]
    return id_ranges, ids

def count_fresh_ids(id_ranges: list, ids: list) -> int:
    count = 0
    for id in ids:
        for id_range in id_ranges:
            if id >= id_range[0] and id <= id_range[1]:
                count += 1
                break
    print(count)

if __name__ == "__main__":
    id_ranges, ids = parse_database('2025/5/input.txt')
    count_fresh_ids(id_ranges=id_ranges, ids=ids)
    