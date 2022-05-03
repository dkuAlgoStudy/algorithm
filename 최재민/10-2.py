import sys

n, m = map(int,input().split())
parent = [0]*(n+1)
for i in range(m):
    parent[i]=i

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]


def union_parent(parent, b, c):
    b=find_parent(parent, b)
    c=find_parent(parent, c)
    if b<c:
        parent[c] = b
    else:
        parent[b] = c


for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    if a==0:
        union_parent(parent,b,c)
    elif a==1:
        if find_parent(parent,b) == find_parent(parent,c):
            print("YES")
        if find_parent(parent, b) != find_parent(parent, c):
            print("NO")

