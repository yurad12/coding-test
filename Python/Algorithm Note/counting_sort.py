# 계수정렬, O(N+K), 해당 숫자가 몇 번 등장하는지 기록

arr = [0,1,2,3,4,0,2,3,2]
count = [0] * (max(arr)+1)
for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
print()
