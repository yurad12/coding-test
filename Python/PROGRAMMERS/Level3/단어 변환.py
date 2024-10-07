'''
문제: https://school.programmers.co.kr/learn/courses/30/lessons/43163

1. target이 words에 있는지 확인하기 ->  없으면 return 0
2. bfs로 단어 탐색하면서 변환할 수 있는 단어인지 확인하기
3. 변환할 수 있는 단어이면, (단어,현재 count)를 큐에 넣기
4. bfs 과정에서 단어가 target이랑 같아지면 return count
'''

from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0
    
    def is_possible(begin, target):
        count = 0
        for i in range(len(begin)):
            if begin[i] == target[i]:
                count += 1
        if count == len(begin)-1:
            return True
        return False
    
    q = deque([(begin,0)])
    while q:
        now, count = q.popleft()
        if now == target:
            return count
        for word in words:
            if is_possible(now, word):
                q.append((word,count+1))
                