import sys

pipe = sys.stdin.readline().rstrip()

stack = []
ans = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append(i)
    elif pipe[i] == ')':
        if pipe[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)