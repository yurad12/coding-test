# https://www.acmicpc.net/problem/2230
# 차이가 M이상이 되는 지점은 그 뒤를 살펴볼 필요가 없으니까 start += 1
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

answer = float('inf') # 0 ≤ M ≤ 2,000,000,000
end = 0
for start in range(N):
    while end < N and A[end] - A[start] < M:
        end += 1
    if end == N:
        break
    answer = min(answer, A[end] - A[start])
    
print(answer)