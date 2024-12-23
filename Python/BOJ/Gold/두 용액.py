# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))

solution.sort()

min_value = float('inf')
idx1, idx2 = 0, 0

for i in range(N-1):
    start, end = i+1, N-1

    while start <= end:
        mid = (start + end) // 2
        value = solution[i] + solution[mid]

        if abs(value) < min_value:
            min_value, idx1, idx2 = abs(value), i, mid
        
        if value < 0:
            start = mid + 1
        else:
            end = mid - 1

print(solution[idx1], solution[idx2])
