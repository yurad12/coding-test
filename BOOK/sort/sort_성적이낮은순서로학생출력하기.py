import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    data = sys.stdin.readline().split()
    array.append([data[0],int(data[1])])
score = [[] for _ in range(101)]

for i in range(n):
    score[array[i][1]].append(array[i][0])

for i in score:
    for j in range(len(i)): 
        print(i[j], end = ' ')