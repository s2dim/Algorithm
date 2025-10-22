def solution(arr):
    temp = -1
    ans = []
    for i in arr:
        if temp == i:
            continue
        else:
            ans.append(i)
            temp = i

    return ans