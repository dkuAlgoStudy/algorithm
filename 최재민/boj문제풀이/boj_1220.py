cnt=int(input())

for _ in range(cnt):
    a,b=input().split()
    for i in b:
        print(i*int(a),end="")
    print(" ")
