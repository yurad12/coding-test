# https://www.acmicpc.net/problem/24337
'''
1보다 크거나 같은 정수
- 1에서 a까지 증가
- N-b+1에서 N까지 감소

1 2 3 4 1
N: 5, a: 4, b: 2
10 1 3
3 1 1 1 1 1 1 1 2 1
10 8 1
1 1 1 2 3 4 5 6 7 8
'''

import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

towers = [1] * a
for i in range(1, a):
    towers[i] = i + 1

towers[a-1] = max(a, b)

for i in range(b-1, 0, -1):
    towers.append(i)

answer = [towers[0]]
for i in range(N-len(towers)):
    answer.append(1)

if a + b > N + 1:
    print(-1)
else:
    answer += towers[1:]
    print(*answer)
