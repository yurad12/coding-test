# https://www.acmicpc.net/problem/1654

k, n = map(int,input().split())
lines = [int(input()) for _ in range(k)]
start = 1 #
end = max(lines)

result = 0
while start <= end:
    if n == 1:
        result = lines[0]
        break
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += (line//mid)
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)