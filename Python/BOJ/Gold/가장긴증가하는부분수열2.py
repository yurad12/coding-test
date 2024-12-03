# https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def binary_search(dp, num):
    start, end = 0, len(dp)-1

    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

dp = []
for a in A:
    idx = binary_search(dp, a)

    if idx >= len(dp):
        dp.append(a)
    else:
        dp[idx] = a

print(len(dp))