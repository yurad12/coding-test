import heapq
n = int(input())
cards = []
for i in range(n):
    data = int(input())
    heapq.heappush(cards,data)
# print('>>>',cards)
result = 0
while len(cards) != 1:
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    temp = one + two
    heapq.heappush(cards,temp)
    result += temp
    # print(cards)
print(result)