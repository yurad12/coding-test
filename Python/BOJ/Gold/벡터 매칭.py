# https://www.acmicpc.net/problem/1007
import sys
input = sys.stdin.readline
from itertools import combinations
import math

T = int(input())
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    
    total_x = sum(p[0] for p in points)
    total_y = sum(p[1] for p in points)

    answer = float('inf')
    count = N // 2

    for comb in combinations(points, count):
        sum_x = sum(p[0] for p in comb)
        sum_y = sum(p[1] for p in comb)
        # 선택된 점의 반대 방향 벡터
        vector_x = total_x - 2 * sum_x
        vector_y = total_y - 2 * sum_y

        length = math.sqrt(vector_x ** 2 + vector_y ** 2)
        answer = min(answer, length)

    print(f"{answer:.6f}")
