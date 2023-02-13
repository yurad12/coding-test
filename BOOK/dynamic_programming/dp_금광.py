import sys

answer = []
case = int(sys.stdin.readline())
while case != 0:
    n, m = map(int, sys.stdin.readline().split())
    temp = list(map(int,sys.stdin.readline().split()))
    gold = [[]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            gold[i].append(temp[i*m+j])

    value = 0
    for c in range(n): # 뒤에 사용할 값
        if gold[c][0] > value:
            value = gold[c][0]
            x, y = c, 0
    # print('>>>',x,y)
    # print(gold)

    dx = [1,0,-1] # 행
    dy = [1,1,1] # 열
    for _ in range(m-1):
        value = 0
        for i in range(3): # 최댓값,인덱스 찾기
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= n or ty <0 or ty >= m:
                continue 
            if gold[tx][ty] > value:
                value = gold[tx][ty]
                gold[tx][ty] += gold[x][y]
                nx, ny = tx, ty
        x, y = nx, ny
    answer.append(gold[x][y])
    print(gold)
    case -= 1

for ans in answer:
    print(ans)

# solution 2
# 점화식: dp[i][j] = array[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
# result = max(dp[i][m-1])