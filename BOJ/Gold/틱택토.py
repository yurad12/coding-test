# https://www.acmicpc.net/problem/7682
'''
1. x와 o의 수
 - x 개수 == o 개수
 - x 개수 == o 개수+1
2. 승리 조건
 - 가로/세로/대각선
 - 동시에 승리 불가
3. 승자가 있는 경우
 - x 승리: x개수 == o개수+1
 - o 승리: x개수 == o개수
4. 승자가 없는 경우
 - 게임판 가득찼는지 확인
'''

import sys
input = sys.stdin.readline

def solution(game:list):
    cnt_x = sum(r.count('X') for r in game)
    cnt_o = sum(r.count('O') for r in game)

    # case1: x and o count
    if cnt_o > cnt_x or cnt_x > cnt_o+1:
        return False
    
    # case2: win conditions
    def win(player):
        for i in range(3):
            # row
            if all(game[i][j] == player for j in range(3)):
                return True
            # column
            if all(game[j][i] == player for j in range(3)):
                return True
        # diagnal-down
        if all(game[i][i] == player for i in range(3)):
            return True
        # diagnal-up
        if all(game[i][2-i] == player for i in range(3)):
            return True
        return False

    win_x = win('X')
    win_o = win('O')
    
    # case3: winner exists
    if win_x and win_o:
        return False
    if win_x and (cnt_x != cnt_o+1):
        return False
    if win_o and (cnt_x != cnt_o):
        return False

    # case4: winner doesn't exist
    if not win_x and not win_o and cnt_x + cnt_o < 9:
        return False
    
    return True

if __name__ == "__main__":
    while True:
        data = input().strip()
        if data == "end":
            break

        game = [list(['']*3) for _ in range(3)]
        for i in range(9):
            game[i//3][i%3] = data[i]

        answer = solution(game)
        if answer:
            print("valid")
        else:
            print("invalid")
            