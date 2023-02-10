# https://www.acmicpc.net/problem/2110
import sys

n, c = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
house.sort()

min_gap = 1
max_gap = house[-1]-house[0]

result = 0
while min_gap <= max_gap:
    mid = (max_gap + min_gap)//2
    temp = house[0]
    count = 1
    for i in range(1,n): #공유기 설치할 수 있는 집 수 세기
        if house[i]-temp >= mid:
            count += 1 # install router
            temp = house[i]
    if count >= c:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid - 1

print(result)