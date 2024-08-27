def print_grid(grid: list[list[int]]) -> None:
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
        
def find_empty_location(grid: list[list[int]], position: list[int]) -> bool:
    for row in range(9):
        for column in range(9):
            if (grid[row][column] == 0):
                position[0] = row
                position[1] = column
                return True
    return False

def used_in_row(grid: list[list[int]], row: int, number: int) -> bool:
    for i in range(9):
        if (grid[row][i] == number):
            return True
    return False

def used_in_column(grid: list[list[int]], column: int, number: int) -> bool:
    for i in range(9):
        if (grid[i][column] == number):
            return True
    return False

def used_in_box(grid: list[list[int]], row: int, column: int, number: int) -> bool:
    for i in range(3):
        for j in range(3):
            if (grid[i + row][j + column] == number):
                return True
    return False

def is_safe(grid: list[list[int]], row: int, column: int, number: int) -> bool:
    return (not used_in_row(grid, row, number) and
           (not used_in_column(grid, column, number) and
           (not used_in_box(grid, row - row % 3,
                            column - column % 3, number))))
    
def solve(grid: list[list[int]]) -> bool:
    position: list[int] = [0, 0]
    
    if (not find_empty_location(grid, position)):
        return True
    
    row: int = position[0]
    column: int = position[1]
    
    for number in range(1, 10):
        if (is_safe(grid, row, column, number)):
            grid[row][column] = number
            if solve(grid):
                return True
            grid[row][column] = 0
    return False

def main() -> None:
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
    
    if solve(grid):
        print_grid(grid)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()