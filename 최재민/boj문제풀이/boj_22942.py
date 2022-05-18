import sys
input = sys.stdin.readline

flag = True
stack = []
data = []
n = int(input())
for i in range(n):
    x, r = map(int,input().split())
    data.append([x-r,x,0])
    data.append([x+r,x,1])

data.sort()

for circle in data:
    if circle[2] == 0:
        stack.append(circle)
    else:
        if stack[-1][1] == circle[1]:
            stack.pop()
        else:
            print("NO")
            flag = False
            break
if flag:
    print("YES")

