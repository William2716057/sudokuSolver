square = [
    [0, 8, 4, 0, 0, 2, 0, 3, 0],
    [2, 0, 7, 8, 3, 1, 0, 0, 9],
    [0, 1, 0, 5, 0, 0, 0, 2, 7],
    [0, 7, 8, 0, 1, 0, 9, 0, 2],
    [0, 0, 9, 7, 6, 0, 0, 8, 5],
    [5, 0, 1, 9, 0, 0, 3, 0, 0],
    [0, 3, 0, 1, 0, 7, 4, 0, 6],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [7, 0, 0, 3, 9, 0, 0, 0, 0]
]

def checkNums(mat, row, col, num):
    # Check if num exists in row
    if num in mat[row]:
        return False

    # Check if num exists in column
    if any(mat[x][col] == num for x in range(9)):
        return False

    # Check if num exists in each square
    startRow, startCol = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if mat[startRow + i][startCol + j] == num:
                return False

    return True

def solve(grid, row=0, col=0):

    if row == 8 and col == 9:
        return True

    # Move to next row if column exceeds 8
    if col == 9:
        row += 1
        col = 0

    # If cell already filled, move to next
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if checkNums(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 0 

    return False

if __name__ == "__main__":
    if solve(square):
        for row in square:
            print(" ".join(map(str, row)))
    else:
        print("No solution")