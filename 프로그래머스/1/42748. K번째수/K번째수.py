def solution(array, commands):
    answer = []
    
    for lst in commands:
        start = lst[0] - 1
        end = lst[1]
        idx = lst[2] - 1
        arr = array[start:end]
        arr.sort()
        answer.append(arr[idx])

    return answer