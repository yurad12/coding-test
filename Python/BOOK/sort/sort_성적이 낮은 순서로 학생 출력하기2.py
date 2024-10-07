import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    data = sys.stdin.readline().split()
    array.append((data[0],int(data[1])))
sorted(array,key = lambda x:x[1])

for i in array:
    print(i[0], end=' ')