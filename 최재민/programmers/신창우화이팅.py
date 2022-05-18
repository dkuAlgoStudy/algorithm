def paperCuttings(textlength, starting, ending):
    answer = 0
    length = len(starting)
    overlap = [[] for _ in range(length)]
    for i in range(length):
        overlap[i].append(starting[i])
        overlap[i].append(ending[i])
    if length > 1:
        overlap = list(set(map(tuple, overlap)))
    else:
        return 0
    overlap = sorted(overlap)
    length = len(overlap)
    for i in range(length):
        left = i+1
        right = length-1
        target = overlap[i][1]
        while left <= right:
            mid = (left+right)//2
            if 0 < mid < length-1:
                if overlap[mid][0] < target < overlap[mid+1][0]:
                    answer += length - mid-1
                    break
                elif overlap[mid-1][0] <= target < overlap[mid][0]:
                    answer += length - mid
                    break
                elif overlap[mid][0] > target:
                    right = mid - 1

                else:
                    left = mid + 1
            elif mid == length-1:
                if overlap[mid][0] > target:
                    answer += 1
                    break
                else:
                    break
            elif mid == 0:
                answer += length - 2
                break

    return answer

print(paperCuttings(15,[3,1,2,8,8],[5,3,7,10,10]))