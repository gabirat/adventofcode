from typing import List


def parse_input(path: str) -> List[List[int]]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return [list(map(int, line.strip())) for line in lines]

def calculate_optimal_joltage(battery_packs: List[List[int]]):
    results = []
    for pack in battery_packs:
        max_l = max(pack[:-1])
        max_idx = pack[:-1].index(max_l)
        max_r = max(pack[max_idx + 1:])
        results.append(max_l * 10 + max_r)
    sum_results = sum(results)
    print(f"Optimal joltage sum: {sum_results}")

if __name__ == "__main__":
    input_data = parse_input('2025/3/input.txt')
    calculate_optimal_joltage(input_data)

    
