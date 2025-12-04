def parse_input(path: str) -> list:
    with open(path, 'r') as file:
        return file.readlines()
    
def is_accessible(grid: list, x: int, y: int) -> int:
    adj_rolls = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if x + dx < 0 or x + dx >= len(grid[0]):
                continue
            if y + dy < 0 or y + dy >= len(grid):
                continue
            if grid[y + dy][x + dx] == '@':
                adj_rolls += 1

    return adj_rolls < 4

if __name__ == "__main__":
    grid = parse_input('2025/4/input.txt')
    total_rolls = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                if is_accessible(grid, x, y):
                    total_rolls += 1
    print(total_rolls)