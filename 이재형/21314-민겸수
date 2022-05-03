def MaxMk(arr):
    arrLength = len(arr)
    Mnum = 0
    ans = []
    for i in range(arrLength):
        if arr[i] == 'M':
            Mnum += 1
            if i == arrLength - 1:
                for i in range(Mnum):
                    ans.append(1)
        else:
            ans.append(5)
            for i in range(Mnum):
                ans.append(0)
            Mnum = 0
    
    return ans

def MinMk(arr):
    arrLength = len(arr)
    Mnum = 0
    ans = []
    for i in range(arrLength):
        if arr[i] == 'M':
            Mnum += 1
            if i == arrLength - 1:
                ans.append(10**(Mnum - 1))
        else:
            if Mnum > 0:
                ans.append(10**(Mnum - 1))
            ans.append(5)
            Mnum = 0

    return ans

if __name__ == "__main__":
    arr = list(input())
    arrMax = MaxMk(arr)
    arrSmall = MinMk(arr)

    print(''.join(map(str,arrMax)))
    print(''.join(map(str,arrSmall)))
