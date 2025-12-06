from typing import List, Tuple


def parse_input(path: str) -> List[Tuple[int, int, int, int, str]]:
    out = []
    def self_split(string: str) -> List[str]:
        return string.strip().split()
    with open(path, 'r') as file:
        lines = list(map(self_split, file.readlines()))
        for i in range(len(lines[0])):
            tmp = [0, 0, 0, 0, lines[4][i]]
            for j in range(4):
                tmp[j] = int(lines[j][i])
            out.append(tmp)
    return out

if __name__ == "__main__":
    equations = parse_input('2025/6/input.txt')
    total = 0
    for equation in equations:
        a, b, c, d, op = equation
        if op == '+':
            total += a + b + c + d
        elif op == '-':
            total += a - b - c - d
        elif op == '*':
            total += a * b * c * d
        elif op == '/':
            if b != 0 and c != 0 and d != 0:
                total += a / b / c / d
    print(total)

            