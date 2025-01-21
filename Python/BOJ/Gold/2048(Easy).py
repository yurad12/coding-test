# https://www.acmicpc.net/problem/12100
import sys
input = sys.stdin.readline

N = int(input())
game_board = [list(map(int, input().split())) for _ in range(N)]

def up(board):
    for j in range(N):
        row = 0
        for i in range(1,N):
            if board[i][j]:
                value = board[i][j]
                board[i][j] = 0

                if not board[row][j]:
                    board[row][j] = value
                elif board[row][j] == value:
                    board[row][j] *= 2
                    row += 1
                else:
                    row += 1
                    board[row][j] = value
    
    return board

def down(board):
    for j in range(N):
        row = N-1
        for i in range(N-1,-1,-1):
            if board[i][j]:
                value = board[i][j]
                board[i][j] = 0

                if not board[row][j]:
                    board[row][j] = value
                elif board[row][j] == value:
                    board[row][j] *= 2
                    row -= 1
                else:
                    row -= 1
                    board[row][j] = value

    return board

def left(board):
    for i in range(N):
        col = 0
        for j in range(1, N):
            if board[i][j]:
                value = board[i][j]
                board[i][j] = 0

                if not board[i][col]:
                    board[i][col] = value
                elif board[i][col] == value:
                    board[i][col] *= 2
                    col += 1
                else:
                    col += 1
                    board[i][col] = value

    return board

def right(board):
    for i in range(N):
        col = N-1
        for j in range(N-1,-1,-1):
            if board[i][j]:
                value = board[i][j]
                board[i][j] = 0

                if not board[i][col]:
                    board[i][col] = value
                elif board[i][col] == value:
                    board[i][col] *= 2
                    col -= 1
                else:
                    col -= 1
                    board[i][col] = value

    return board

def get_max_block(board):
    return max(max(i) for i in board)

def dfs(board, count):
    global answer

    answer = max(answer, get_max_block(board))
    if count == 5:
        return

    for move in (up, down, left, right):
        new_board = [i[:] for i in board]
        new_board = move(new_board)

        if board != new_board:
            dfs(new_board, count+1)

answer = 0
dfs(game_board, 0)
print(answer)
