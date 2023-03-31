def solution(numbers):
    lst = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum_num = numbers[i] + numbers[j]
                lst.append(sum_num)

    lst = list(set(lst))
    lst.sort()


    return lst