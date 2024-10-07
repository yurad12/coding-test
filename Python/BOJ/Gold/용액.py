# https://www.acmicpc.net/problem/2467

n = int(input())
sol = list(map(int, input().split()))

start, end = 0, n-1
result = [2000000000,0,0]

while start < end:
    if abs(sol[start] + sol[end]) < result[0]:
        result[0] = abs(sol[start] + sol[end])
        result[1], result[2] = sol[start], sol[end]

    if sol[start] + sol[end] < 0:
        start += 1
    else:
        end -= 1

print(result[1],result[2])

'''
4
-1 0 2 3
'''