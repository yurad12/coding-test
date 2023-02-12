import sys

n, m = map(int, sys.stdin.readline().split())
money = list(int(sys.stdin.readline()) for _ in range(n))
d = [10001]*(m+1) # 최소 화폐 수
d[0] = 0

for i in range(n): # 2,3
    for j in range(money[i],m+1): # 2~15, 3~15
        # print('>>>',j,d[j])
        # print(j-money[i],d[j-money[i]]+1)
        d[j] = min(d[j],d[j-money[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])