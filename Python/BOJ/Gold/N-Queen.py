# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

n = int(input())
chess = [0] * n # 행: 배열 인덱스, 열: 배열 값
result = 0

def bt(q):
    global result
    if q == n:
        result += 1
        return
    
    for i in range(n): # 모든 후보 탐색
        chess[q] = i # [q,i]에 후보 추가
        if place(q): # 가능 다음 후보 탐색
            bt(q+1)

def place(q):
    for i in range(q):
        if (chess[i] == chess[q]) or (abs(i-q) == abs(chess[i]-chess[q])): # 기울기 이용: x,y 변화량 동일
            return False
    return True

bt(0)
print(result)