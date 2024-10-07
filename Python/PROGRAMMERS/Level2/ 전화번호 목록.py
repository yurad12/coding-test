'''
https://school.programmers.co.kr/learn/courses/30/lessons/42577

1. node에 trie를 얕은 복사해놓는다.
2. node를 변경하면 trie도 변경된다. 그래서 node에 임시로 저장한 값은 실제로 trie에도 저장되는 것이다.
3. 문자열이 끝났음을 확인하기 위해 ‘$’를 추가한다.
4. 탐색하면서 ‘$’로 끝날 때, 자기자신이 아닌 경우에는 다른 문자열이 접두사로 사용된 것임을 찾는다.
'''

def solution(phone_book):
    # trie 트리 만들기
    trie = {}
    for phone in phone_book:
        node = trie
        for char in phone:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True
    
    # 찾기
    for phone in phone_book:
        node = trie
        length = len(phone)
        for i in range(length):
            if '$' in node and i <= length-1:
                return False
            node = node[phone[i]]
    return True