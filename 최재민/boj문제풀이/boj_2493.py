import sys

input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = [0]*n

for i in enumerate(tower):
    while stack and tower[stack[-1]] < i[1]:
        stack.pop()
    if stack:
        answer[i[0]] = stack[-1] + 1
    stack.append(i[0])

print(' '.join(list(map(str,answer))))