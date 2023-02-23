# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()

def search(array,target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for target in b:
    print(search(a,target))