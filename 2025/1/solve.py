START = 50

def get_input_lines(path: str) -> str:
    with open(path, 'r') as file:
        return file.readlines()

def solve():
    lines = get_input_lines('2025/1/input.txt')
    dial = START
    total_zeros = 0
    for line in lines:
        direction = line[0]
        step = int(line[1:])
        if direction == 'R':
            dial = (dial + step % 100) % 100
        else:
            dial = dial - step % 100
            if dial < 0:
                dial += 100
        if dial == 0:
            total_zeros += 1

    print(total_zeros)

def solve2():
    lines = get_input_lines('2025/1/input.txt')
    dial = START
    total_zeros = 0
    for line in lines:
        direction = line[0]
        step = int(line[1:])
        total_zeros += step // 100
        if dial == 0 and step % 100 == 0:
            total_zeros -= 1
        step = step % 100
        if direction == 'R':
            dial = dial + step
            if dial > 100:
                dial -= 100
                total_zeros += 1
            if dial == 100:
                dial = 0
        else:
            dial = dial - step
            if dial + step == 0:
                total_zeros -= 1
            if dial < 0:
                dial += 100
                total_zeros += 1
        if dial == 0:
            total_zeros += 1

    print(total_zeros)

if __name__ == "__main__":
    solve()
    solve2()