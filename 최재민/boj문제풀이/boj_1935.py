import sys

n = int(sys.stdin.readline().rstrip())
exp = sys.stdin.readline().rstrip()
num = []

for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

stack = []
for i in exp:

    if 'A' <= i <= 'Z' :		
        stack.append(num[ord(i)-ord('A')])
    else:
        second = stack.pop()
        first = stack.pop()
        if i == '+':
            stack.append(first+second)
        elif i == '-':
            stack.append(first-second)
        elif i == '*':
            stack.append(first*second)
        elif i == '/':
            stack.append(first/second)

print('%.2f' %stack[0])