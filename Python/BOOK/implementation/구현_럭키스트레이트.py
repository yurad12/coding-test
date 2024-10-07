score = input()
length = int(len(score)/2)
left = list(map(int,score[:length]))
right = list(map(int,score[length:]))
l_sum = 0; r_sum = 0

for i in range(length):
    l_sum += left[i]
    r_sum += right[i]
#print(l_sum, r_sum)

if l_sum == r_sum:
    print('LUCKY')
else:
    print('READY')