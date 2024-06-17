# https://www.acmicpc.net/problem/1138
'''
왼쪽에 큰 사람 수가 같으면, 인덱스가 앞에 오는 것 먼저
1. 순서대로 빈 자리에 채워넣는 방식
2. 아직 채워지지 않은 자리의 수가 왼쪽에 큰 사람 수와 같게 됨
'''

import sys
input = sys.stdin.readline

n = int(input())
records = list(map(int, input().split()))

answer = [0] * n
for i in range(n):
    count = 0
    for j in range(n):
        if records[i] == count and not answer[j]:
            answer[j] = i+1
            break
        elif not answer[j]:
            count += 1

print(*answer)
