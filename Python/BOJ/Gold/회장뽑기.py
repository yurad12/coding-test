# https://www.acmicpc.net/problem/2660
import sys
input = sys.stdin.readline

n = int(input())
scores = [[int(1e9)] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            scores[i][j] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    scores[a][b] = 1
    scores[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            scores[a][b] = min(scores[a][b], scores[a][k] + scores[k][b])


min_score = min([max(i[1:]) for i in scores])
answer = []
for i in range(1, n+1):
    score = max(scores[i][1:])
    if min_score == score:
        answer.append(i)


print(min_score, len(answer))
print(*answer)