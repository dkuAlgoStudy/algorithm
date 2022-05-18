from itertools import combinations
import sys

answer =[] 
temp = []  
stack = []  
pair = []   #짝이 맞는 괄호
bracket = sys.stdin.readline().rstrip()

for i in enumerate(bracket):
    if i[1] == '(':
        stack.append(i)
    elif i[1] == ')':
        pair.append([stack.pop()[0], i[0]])

combi = []
for i in range(1,len(pair)+1):
    for j in combinations(pair,i):
        combi.append(j)
for i in combi:
    temp = list(bracket)
    for j in i:
        for k in j:
            temp[k] = ' '
    answer.append((''.join(temp).replace(' ',"")))

answer = set(answer)
answer = sorted(list(answer))
for i in answer:
    print(str(i))