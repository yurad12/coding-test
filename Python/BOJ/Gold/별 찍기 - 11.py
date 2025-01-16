# https://www.acmicpc.net/problem/2448
import sys
input = sys.stdin.readline

N = int(input())

def get_pattern(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    pattern = get_pattern(n//2)
    answer = []

    for p in pattern:
        answer.append(' ' * (n//2) + p + ' ' * (n//2))
    for p in pattern:
        answer.append(p + ' ' + p)

    return answer

answer = get_pattern(N)
print("\n".join(answer))

'''
머리 + 몸통 * 2
'''