# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    # 2*2 블록 찾기
    def find_blocks_to_remove(m, n, board):
        remove_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if not board[i][j]:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove_set.add((i,j))
                    remove_set.add((i,j+1))
                    remove_set.add((i+1,j))
                    remove_set.add((i+1,j+1))
        return remove_set
    
    # 2*2 블록 지우기
    def remove_blocks(board, remove_set):
        for i, j in remove_set:
            board[i][j] = ''
    
    # 블록 떨어뜨려서 빈 공간 채우기
    def drop_blocks(m, n, board):
        for j in range(n):
            row = m-1
            for i in range(m-1,-1,-1):
                if board[i][j]:
                    board[row][j] = board[i][j]
                    if row != i:
                        board[i][j] = ''
                    row -= 1
    
    board = [list(b) for b in board]
    while True:
        remove_set = find_blocks_to_remove(m, n, board)
        if not remove_set:
            break
        remove_blocks(board, remove_set)
        drop_blocks(m, n, board)
        
    answer = sum(b.count('') for b in board)
    
    return answer