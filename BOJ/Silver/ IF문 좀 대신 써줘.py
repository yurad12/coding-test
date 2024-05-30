# https://www.acmicpc.net/problem/19637
# 이진 탐색, 가장 먼저 입력된 칭호

import sys
input = sys.stdin.readline

def solution(n, m, characters):
    for power in characters:
        start, end = 0, n-1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if int(titles[mid][1]) >= power:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        print(titles[result][0])

if __name__ == "__main__":
    n, m = map(int, input().split())
    titles = [list(map(str.strip, input().split())) for _ in range(n)]
    characters = [int(input()) for _ in range(m)]
    solution(n, m, characters)
