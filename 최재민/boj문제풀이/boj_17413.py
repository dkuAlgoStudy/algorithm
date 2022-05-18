import sys

s = sys.stdin.readline().rstrip()

temp = ""
tag = False
answer = ""

for i in s:
    if not tag:
        if i == "<":
            temp += i
            tag = True
        elif i == " ":
            temp += i
            answer += temp
            temp = ""
        else:
            temp = i + temp
    else:
        temp += i
        if i == ">":
            tag = False
            answer += temp
            temp = ""

print(answer+temp)

