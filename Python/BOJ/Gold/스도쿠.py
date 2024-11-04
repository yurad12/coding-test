# https://www.acmicpc.net/problem/2239
import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().strip())) for _ in range(9)]

def place(r, c, num):
    if inRow(r, num) and inCol(c, num) and inBox(r, c, num):
        return True
    return False

def inRow(r, num):
    if num in sudoku[r]:
        return False
    return True

def inCol(c, num):
    for r in range(9):
        if sudoku[r][c] == num:
            return False
    return True

def inBox(r, c, num):
    r2 = r // 3 * 3
    c2 = c // 3 * 3
    for i in range(r2, r2+3):
        for j in range(c2, c2+3):
            if sudoku[i][j] == num:
                return False
    return True

def find_position():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def fill():
    position = find_position()
    if position is None:
        return True
    
    x, y = position[0], position[1]
    for num in range(1, 10):
        if place(x, y, num):
            sudoku[x][y] = num

            if fill():
                return True
            sudoku[x][y] = 0
    
    return False

fill()
for i in sudoku:
    print(''.join(map(str,i)))


