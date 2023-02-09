import sys

n = int(sys.stdin.readline())
values = list(map(int,sys.stdin.readline().split()))

start = 0
end = n-1
result = -1
while start <= end:
    mid = (start + end) // 2
    if values[mid] == mid:
        result = mid
        break
    elif values[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

print(result)