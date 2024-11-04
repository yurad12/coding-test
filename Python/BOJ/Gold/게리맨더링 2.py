# https://www.acmicpc.net/problem/17779
import sys
input = sys.stdin.readline

N = int(input())
A = [[0] * (N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

def split(x, y, d1, d2):
    count = [0] * 6
    #1
    j = y + 1
    for i in range(x+d1):
        if i >= x:
            j -= 1
        count[1] += sum(A[i][1:j])

    #2
    j = y + 1
    for i in range(x+d2+1):
        if x < i:
            j += 1
        count[2] += sum(A[i][j:])
    
    #3
    j = y - d1 - 1
    for i in range(x+d1, N+1):
        if i <= x + d1 + d2:
            j += 1
        count[3] += sum(A[i][1:j])

    #4
    j = y + d2
    for i in range(x+d2+1, N+1):
        count[4] += sum(A[i][j:])
        if i <= x + d2 + d1:
            j -= 1

    count[5] = total - sum(count)
    return max(count[1:]) - min(count[1:])

answer = float('inf')
total = sum(map(sum, A))
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 <= N and 1 <= y - d1 and y + d2 <= N:
                    answer = min(answer, split(x, y, d1, d2))

print(answer)


'''
# https://www.acmicpc.net/problem/17779
import sys
input = sys.stdin.readline

N = int(input())
A = [[0] * (N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

def split(x, y, d1, d2):
    city = [[0] *  (N+1) for _ in range(N+1)]

    count = [0] * 6
    #1
    j = y + 1
    for i in range(x+d1):
        if i >= x:
            j -= 1
        for k in range(1, j):
            count[1] += A[i][k]
            city[i][k] = 1
        # count[1] += sum(A[i][:j])

    #2
    j = y + 1
    for i in range(x+d2+1):
        if x < i:
            j += 1
        # count[2] += sum(A[i][j:])
        for k in range(j, N+1):
            count[2] += A[i][k]
            city[i][k] = 2
    
    #3
    j = y - d1 - 1
    for i in range(x+d1, N+1):
        if i <= x + d1 + d2:
            j += 1
        # count[3] += sum(A[i][:j])
        for k in range(1, j):
            count[3] += A[i][k]
            city[i][k] = 3

    #4
    j = y + d2
    for i in range(x+d2+1, N+1):
        # count[4] += sum(A[i][j:])
        for k in range(j, N+1):
            count[4] += A[i][k]
            city[i][k] = 4
        if i <= x + d2 + d1:
            j -= 1

    if x == 3 and y == 3 and d1 == 1 and d2 == 1:
        for c in city:
            print(c)

    count[5] = total - sum(count)

    return max(count[1:]) - min(count[1:])

'''