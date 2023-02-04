n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]
f_num = []
print(num)

for i in range(n):
    f_num.append(min(num[i]))
result = max(f_num)
print(f_num)
print(result)