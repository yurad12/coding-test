## solution 1
import sys
n = int(sys.stdin.readline())
d = [0]*n
d[0] = 1
n1, n2, n3 = 2, 3, 5
i1 = i2 = i3 = 0

for l in range(1,n):
    d[l] = min(n1,n2,n3)
    if d[l] == n1:
        i1 += 1
        n1 = d[i1] * 2
    if d[l] == n2:
        i2 += 1
        n2 = d[i2] * 3
    if d[l] == n3:
        i3 += 1
        n3 = d[i3] * 5
print(d[n-1])

## solution 2
import sys
import heapq

n = int(sys.stdin.readline())

d = []
heapq.heappush(d,1)
n1, n2, n3 = 2, 3, 5

for i in range(1,n):
    heapq.heappush(d,n1*i)
    heapq.heappush(d,n2*i)
    heapq.heappush(d,n3*i)

d = list(set(d))
print(d)
print(d[n-1])