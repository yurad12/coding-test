# https://www.acmicpc.net/problem/17266
'''
가로등이 비춰주는 비춰주는 범위 찾기
1. 모든 곳 비출 수 있으면, end = mid-1 -> 이때가 최솟값
2. 모든 곳 비출 수 없으면, start = mid+1
'''

import sys
input = sys.stdin.readline

def solution(n, m, locations):

    def lights(height):
        prev = 0
        for i in range(m):
            if locations[i]-height <= prev:
                prev = locations[i] + height
            else:
                return False
        return n - prev < 1

    start, end = 1, n
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if lights(mid):
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    print(result)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    locations = list(map(int, input().split()))
    solution(n, m, locations)
