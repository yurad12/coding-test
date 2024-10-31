# https://www.acmicpc.net/problem/22862
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

i = 0
count = 0 # 현재 윈도우에 담긴 홀수 개수
answer = 0

for j in range(N):
    if S[j] % 2 != 0:
        count += 1
    
    while count > K:
        if S[i] % 2 != 0:
            count -= 1
        i += 1
    
    now = j - i - count + 1
    answer = max(answer, now)

print(answer)