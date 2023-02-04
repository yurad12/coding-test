def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    food_dict = {}
    for i in range(len(food_times)):
        food_dict[i+1] = food_times[i]
    food_dict = list(sorted(food_dict.items(), key=lambda x: x[1]))
    current = 0
    previous = 0
    length = len(food_times)
    
    while current + ((food_dict[0][1] - previous) * length) <= k:
        now = food_dict.pop(0)[1]
        current = current + ((now-previous)*length)
        length -= 1
        previous = now
    
    food_dict.sort()
    answer = food_dict[(k-current)][0]
    print(answer)

    return answer

solution([3,1,2],5)
solution([3,1,2,5,1,3],7)