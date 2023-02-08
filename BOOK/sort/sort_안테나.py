# https://www.acmicpc.net/problem/18310
import sys
n = int(sys.stdin.readline())
house = map(int,sys.stdin.readline().split())
house = sorted(house)
center_idx = int( (len(house)-1)/2 )
print(house[center_idx])