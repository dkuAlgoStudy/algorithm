import sys

n = sys.stdin.readline().rstrip()
cnt1 = 0
cnt2 = 0
answer1 = ""
answer2 = ""

for i in range(len(n)):   # 가장 큰
    if n[i] == "M":
        cnt1 += 1
    else:
        answer1 += str(5*10**cnt1)
        cnt1 = 0
if cnt1 != 0:
    answer1 += "1" * cnt1

if n[0] == "K":   # 가장 작은
    answer2 += "5"
else:
    answer2 += "1"

for i in range(1, len(n)):
    if n[i] == "K":
        answer2 += "5"
    else:
        if n[i-1] == "M":
            answer2 += "0"
        else:
            answer2 += "1"


print(answer1)
print(answer2)

