# https://www.acmicpc.net/problem/5052
import sys
input = sys.stdin.readline

# sol1: trie 알고리즘 이용o
def solution(n, phoneNumbers):
    trie = {}
    for number in phoneNumbers:
        node = trie
        for i in number:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['$'] = True

    for number in phoneNumbers:
        node = trie
        length = len(number)
        for i in range(length):
            if '$' in node and i <= length-1:
                return "NO"
            node = node[number[i]]

    return "YES"

# sol2: trie 알고리즘 이용x
def solution2(n, phoneNumbers):
    phoneNumbers.sort()

    for i in range(n-1):
        length = len(phoneNumbers[i])
        if phoneNumbers[i] in phoneNumbers[i+1][:length]:
            return "NO"
    
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        phoneNumbers = [input().strip() for _ in range(n)]
        answer = solution(n, phoneNumbers)
        print(answer)

        # print(solution2(n, phoneNumbers))