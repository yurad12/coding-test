# https://www.acmicpc.net/problem/13144
'''
1 2 3 4 5
1 -> {1} -> +1
2 -> {2}, {1,2} -> +2
3 -> {3}, {2,3}, {1,2,3} -> +3
=> end-start+1
'''

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = 0
window = set()
start = 0

for end in range(N):
    while numbers[end] in window:
        window.remove(numbers[start])
        start += 1

    window.add(numbers[end])
    answer += (end - start + 1)

print(answer)
