import sys
n, k = map(int,sys.stdin.readline().split())
array = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
a  = sorted(array[0])
b = sorted(array[1], reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]
print(sum(a))