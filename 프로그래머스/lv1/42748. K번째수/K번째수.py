def solution(array, commands):
    
    lst = []
    
    for i in range(len(commands)):
        a = commands[i][0] - 1
        b = commands[i][1]
        c = commands[i][2] - 1 
        

        new_lst = array[a:b]
        new_lst.sort()
        lst.append(new_lst[c])

    return lst

'''
1 5 2 6 3 7 4
1 2 3 4 5 6 7
0 1 2 3 4 5 6 


'''