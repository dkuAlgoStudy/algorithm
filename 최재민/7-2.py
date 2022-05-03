
def search(array,num,first,end):
    while first <= end:
        mid = (first+end)//2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            end = mid-1
        else:
            first = mid+1
    return 0

N = int(input())
list1=list(map(int,input().split()))
list1.sort()

M=int(input())
list2=list(map(int,input().split()))

for i in list2:
    result=search(list1, i, 0, N-1)
    if result != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')