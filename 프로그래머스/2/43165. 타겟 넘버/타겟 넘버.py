def Plus(a, b):
    return a + b

def Minus(a, b):
    return a - b

def solution(numbers, target):
    
    if sum(numbers) == target:
        return 1
    
    cnt = 0
    stack = [numbers[0], -numbers[0]]
    
    for i in range(1, len(numbers)):
        
        temp = []
        
        while stack:
            a = stack.pop()
            
            p = Plus(a, numbers[i])
            m = Minus(a, numbers[i])
            
            # 스택에 담기
            temp.append(p)
            temp.append(m)

        stack = temp
    answer = stack.count(target)
    return answer

'''

값이 됐는데 남은 숫자가 더 있음 -> 탈출


'''