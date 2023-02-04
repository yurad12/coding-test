import math

m, n = map(int, input().split())
# 가능한 범위가 1,000,000까지니까 가능한 범위까지로 배열 크기 지정해주기
array = [True for i in range(n+1)]
array[1] = False
# for i in range(2):
#     if i < 2:
#         array[i] = False
print(array)


for i in range(2, int(math.sqrt(n))+1):
    if array[i]==True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(m,n+1):
    if array[i]:
        print(i)
