# https://www.acmicpc.net/problem/1205

# solution1
n, score, p = map(int, input().split())
if not n:
    print(1)
else:
    ranking = list(map(int, input().split()))
    result, count = 1, 0
    for i in range(n):
        if ranking[i] > score:
            result += 1
        elif ranking[i] == score:
            count += 1
        else:
            break
    if count + result > p:
        print(-1)
    else:
        print(result)

# solution2
n, score, p = map(int, input().split())
if not 0:
    print(1)
else:
    ranking = list(map(int, input().split()))
    ranking.append(score)
    ranking.sort(reverse=True)

    if ranking.count(score) + ranking.index(score) > p:
        print(-1)
    else:
        print(ranking.index(score)+1)
