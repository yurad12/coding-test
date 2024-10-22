# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(set(X))
compressed = {sorted_X[i]: i for i in range(len(sorted_X))}

answer = []
for x in X:
    answer.append(compressed[x])
print(*answer)

# from bisect import bisect_left
# answer = [bisect_left(sorted_X, x) for x in X]
# print(*answer)