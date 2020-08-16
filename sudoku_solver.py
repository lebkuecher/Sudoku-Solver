import numpy as np

print("Enter values with no spaces, and use a 0 for blanks.")
print("Example: 530070000")
print('')

grid=[]

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid [i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    response = input("Do you have another? y/n: ")
    if response == 'n':
        print('Thank you for playing!')
        exit()
    else:
        grid=[]
        sudoku()

def enter_values():
    for row_value in range(9):
        row = list(map(int, input(f"Enter values for row {row_value + 1}: ")))
        grid.append(row)
        if row_value == 8:
            solve()
        else:
            continue

def sudoku():
    while True:
        try:
            enter_values()

        except ValueError:
            print('Please enter only numbers.')
            continue

sudoku()

