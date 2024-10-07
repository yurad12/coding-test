# https://school.programmers.co.kr/learn/courses/30/lessons/17686#

# sol1
def solution(files):
    files_dict = {}
    for file in files:
        head, number, tail = '', 0, ''
        idx = -1
        for i in range(len(file)):
            if not head and file[i].isdigit():
                head = file[:i].upper()
                idx = i
            if head and not file[i].isdigit():
                number = int(file[idx:i])
                tail = file[i:].upper()
                break
            if i == len(file)-1:
                number = int(file[idx:])
        files_dict[file] = [head, number, tail]
        
    sorted_files = sorted(files_dict.items(), key = lambda x: (x[1][0], x[1][1]))
    answer = [file[0] for file in sorted_files]
    
    return answer
    
# sol2
import re

def solution(files):
    p = re.compile('([a-zA-Z-. ]+)(\d{1,5})(.*)')
    files_dict = {}
    
    for file in files:
        head, number, tail = p.match(file).groups()
        files_dict[file] = [head, int(number)]
        
    sorted_files = sorted(files_dict.items(), key = lambda x: (x[1][0].upper(), x[1][1]))
    answer = [f[0] for f in sorted_files]
    
    return answer