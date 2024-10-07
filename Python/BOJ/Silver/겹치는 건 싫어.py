# https://www.acmicpc.net/problem/20922
'''
투 포인터 이용: left, right
1. k개수 넘으면 l+1
2. 현재 최대 길이 구하기, r+1
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

l, r = 0, 1
counts = defaultdict(int)
counts[numbers[l]] += 1
answer = 0
while r < n:
    counts[numbers[r]] += 1

    # k개 넘는 경우
    while counts[numbers[r]] > k:
        counts[numbers[l]] -= 1
        l += 1
    
    answer = max(answer, r-l+1)
    r += 1

print(answer)
