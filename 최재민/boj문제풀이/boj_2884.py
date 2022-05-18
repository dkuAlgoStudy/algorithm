a,b=map(int,input().split())

if a==0 and b<45:
    print(23,(60-45+b))
else:
    H=int((((a*60)+b)-45)/60)
    M=int((((a*60)+b)-45)%60)
    print(H, M)
