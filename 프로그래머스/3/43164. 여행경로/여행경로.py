from collections import defaultdict
def solution(tickets):
    # 따라적기
    
    t_dict = defaultdict(list)
    
    for s, e in tickets:
        t_dict[s].append(e)
        
    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse = True)
        
    print("!!", t_dict)
    
    answer = []
    
    stack = ['ICN']
    
    while stack:
        now = stack[-1]
        
        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(t_dict[now].pop())
            
    return answer[::-1]
