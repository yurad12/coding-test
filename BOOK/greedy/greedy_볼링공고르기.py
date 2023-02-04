n, m = map(int,input().split())
weight = list(map(int, input().split()))
combination = []

for i in range(n):
    if i == n-1:
        break
    for j in range(i+1,n):
        if weight[i] != weight[j]:
            combination.append([weight[i],weight[j]])
        else:
            pass
print(len(combination))