def solution(s):
    result = []
    dic = {}
    
    for idx, char in enumerate(s):
        if char in dic:
            result.append(idx - dic[char])
            print(idx, dic[char])

        else:
            result.append(-1)
        dic[char] = idx
        # print(dic)
    return result