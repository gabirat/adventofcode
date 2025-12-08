from typing import List

def parse_input(path: str) -> List[List[str]]:
    with open(path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]
    
def calculate_splits(board: List[List[str]]):
    splits = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.' and board[i-1][j] == 'S':
                 board[i][j] = '|'
            elif board[i][j] == '.' and board[i-1][j] == '|':
                board[i][j] = '|'
            elif board[i][j] == '^' and board[i-1][j] == '|':
                board[i][j-1] = '|'
                board[i][j+1] = '|'
                splits += 1
    print(splits)

if __name__ == "__main__":
    board = parse_input("2025/7/input.txt")
    calculate_splits(board)