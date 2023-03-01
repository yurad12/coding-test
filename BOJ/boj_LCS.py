# https://www.acmicpc.net/problem/9251

one = input()
two = input()
l1, l2 = len(one), len(two)

d = [[0]*(l2+1) for _ in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if one[i-1] == two[j-1]:
            d[i][j] = d[i-1][j-1] +1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[l1][l2])