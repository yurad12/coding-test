import sys
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
array = sorted(array, reverse = True)
for i in array:
    print(i,end = ' ')