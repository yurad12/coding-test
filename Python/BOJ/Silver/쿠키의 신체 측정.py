import sys
input = sys.stdin.readline

n = int(input())
cookie = [list(input().strip()) for _ in range(n)]
print(cookie)

# find head
head = []
for i in range(n):
    for j in range(n):
        if cookie[i][j] == "*":
            head = [i,j]
            break
    if head: break

# find heart
heart = [head[0]+1,head[1]]
print("heart:", heart)

# find arms
left_arm = 0
right_arm = 0

for l in range(heart[1]):
    if cookie[heart[0]][l] == "*":
        left_arm += 1

for r in range(heart[1]+1,n):
    if cookie[heart[0]][r] == "*":
        right_arm += 1

# find waist
waist = 0
for w in range(heart[0]+1,n):
    if cookie[w][heart[1]] == "*":
        waist += 1

# find legs
left_leg = 0
right_leg = 0

for l in range(heart[0]+waist+1,n):
    if cookie[l][heart[1]-1] == "*":
        left_leg += 1

for r in range(heart[0]+waist+1,n):
    if cookie[r][heart[1]+1] == "*":
        right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)