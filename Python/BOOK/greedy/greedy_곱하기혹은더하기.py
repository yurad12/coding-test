n = input()
n_list = list(map(int,n))
print(n_list)
temp = n_list[0]

for i in range(1,len(n_list)):
    if (temp+n_list[i]) >= (temp*n_list[i]):
        temp += n_list[i]
    else:
        temp *= n_list[i]
print(temp)