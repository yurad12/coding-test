n = int(input())
result = [list(input()) for _ in range(n)]
print('input:',result)

for i in range(n):
    before = ''
    score = 0
    add = 0
    for j in range(len(result[i])):
        if (result[i][j] == 'O') & (result[i][j]!=before):
            score += 1
            before = result[i][j]
            add = 0
        elif (result[i][j] == 'O') & (result[i][j]==before):
            add += 1
            score = score + 1 + add
            before = result[i][j]
        else:
            before = result[i][j]
            add = 0
    print(score)