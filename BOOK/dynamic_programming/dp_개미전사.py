import sys

n = int(sys.stdin.readline().rstrip())
warehouse = list(map(int,sys.stdin.readline().split()))
d = [0] * n

# answer
d[0] = warehouse[0]
d[1] = max(warehouse[0],warehouse[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+warehouse[i])
print(d[-1])

# # my solution
# for i in range(n):
#     d[i] = warehouse[i]
#     if i > 1:
#         d[i] += max(d[:i-1])
# print(d)

# print(max(d))