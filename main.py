size_of_board: int = 9

def print_board(arr: list[list[int]]) -> None:
    for i in range(size_of_board):
        for j in range(size_of_board):
            print(arr[i][j], end=" ")
        print()
        
def isSuitable(grid: list[list[int]], row: int, column: int, number: int) -> bool:
    for i in range(9):
        if grid[row][i] == number:
            return False
    for i in range(9):
        if grid[i][column] == number:
            return False
    
    start_row: int = row - row % 3
    start_column: int = column - column % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_column] == number:
                return False
    
    return True

def solve(grid: list[list[int]], row: int, column: int) -> bool:
    if (row == size_of_board - 1 and column == size_of_board):
        return True
    
    if column == size_of_board:
        row += 1
        column = 0
        
    if grid[row][column] > 0:
        return solve(grid, row, column + 1)
    for number in range(1, size_of_board + 1, 1):
        if isSuitable(grid, row, column, number):
            grid[row][column] = number
            if solve(grid, row, column + 1):
                return True
        grid[row][column] = 0
    return False

def main() -> None:
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    grid: list[list[int]] = [
        [0, 0, 4, 6, 7, 2, 0, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 9, 6],
        [0, 6, 3, 0, 4, 0, 0, 0, 8],
        [3, 8, 2, 1, 0, 0, 9, 6, 0],
        [4, 7, 5, 0, 0, 0, 1, 0, 0],
        [9, 1, 0, 2, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 9],
        [0, 0, 1, 0, 0, 0, 7, 4, 3],
        [2, 0, 0, 0, 6, 3, 8, 0, 1]
        ]
    
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 2, 3],
        [0, 0, 0, 0, 0, 0, 7, 5, 0],
        [0, 5, 0, 4, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 6, 7, 0, 0, 2],
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 0, 2, 0, 0, 0, 4, 0],
        [0, 4, 0, 1, 0, 0, 0, 0, 5],
        [8, 0, 0, 0, 0, 5, 6, 0, 0]
    ]

    if (solve(grid, 0, 0)):
        print_board(grid)
    else:
        print("no solution  exists ")
        
if __name__ == "__main__":
    main()