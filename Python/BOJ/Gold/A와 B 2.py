# https://www.acmicpc.net/problem/12919
'''
1. 시작 B -> 마지막에 B추가+뒤집기
2. 마지막 A -> 마지막에 A추가

BABA
BAABAAAAAB -> BAAAAABAA

AB -> ABB BBA
ABB
'''

import sys
input = sys.stdin.readline

s = input().strip()
t = list(input().strip())
result = 0
print("t:", t)

def dfs(t):
    global result
    if s == ''.join(t):
        result = 1
        return
    if not t:
        return
    if t[-1] == 'A':
        temp = t.pop()
        dfs(t)
        t.append(temp)
    if t[0] == 'B':
        t.reverse()
        temp = t.pop()
        dfs(t)
        t.append(temp)
        t.reverse()

dfs(t)
print(result)