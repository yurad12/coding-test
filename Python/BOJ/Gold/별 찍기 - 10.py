# https://www.acmicpc.net/problem/2447
'''
3 / 2 / 3
9 6 9 / 6 4 6 / 9 6 9
27 18 27 / 18 12 18 / 27 18 27 //
18 12 18  / 12 18 12  / 18 12 18 //
'''
import sys
input = sys.stdin.readline

N = int(input())

def get_pattern(n):
    if n == 3:
        return ["***", "* *", "***"]

    pattern = get_pattern(n//3)
    answer = []

    for p in pattern:
        answer.append(p * 3)
    for p in pattern:
        answer.append(p + " " * (n//3) + p)
    for p in pattern:
        answer.append(p * 3)
    
    return answer

answer = get_pattern(N)
print("\n".join(answer))