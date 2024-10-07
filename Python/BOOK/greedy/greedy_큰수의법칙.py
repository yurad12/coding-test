# # 모범 답안
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort(reverse=True)

# first = data[0]
# second = data[1]
# # 5 8 3: 3+1+3+1
# count = (m // (k+1)) * k
# count += m % (k+1)

# result = 0
# result += count * first
# result += (m-count)*second

# print(result)

'''
5 8 3
2 4 5 4 6
'''

# 내가 푼 답
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
#print(num)
num.sort(reverse=True)
#print(num)
sum = 0
cnt = 0

while(True):
    if m == 0:
        break
    if cnt != k:
        sum += num[0]
        m -= 1
        cnt += 1
    else:
        sum += num[1]
        m -= 1
        cnt = 0
print(sum)
