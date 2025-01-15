# https://www.acmicpc.net/problem/1300
import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start, end = 1, k # N ** 2
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    # mid 이하의 숫자가 k개 이상인지 확인
    for i in range(1, N+1):
        total += min(mid // i, N)
    
    if total >= k:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)