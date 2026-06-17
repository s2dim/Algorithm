def solution(s):
    cnt = 0
    for i in range(len(s)):
        state = True
        rotate = s[i:] + s[:i]
        stack = []
        
        for c in rotate:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack:
                    check = stack.pop()
                    if c == ")" and check != "(":
                        state = False
                        break
                    elif c == "]" and check != "[":
                        state = False
                        break
                    elif c == "}" and check != "{":
                        state = False
                        break
                else:
                    state = False
                    break

        if state and len(stack) == 0:
            cnt += 1

    return cnt