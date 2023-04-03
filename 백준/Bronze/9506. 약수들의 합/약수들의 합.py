while True:
    n = int(input())
    lst = [n // i for i in range(1, n+1) if n % i == 0]
    lst.sort()
    lst = lst[:-1]

    if n == -1:
        break

    elif n == sum(lst):
        text = ''
        for i in range(len(lst)):
            lst[i] = str(lst[i])
        text = ' + '.join(lst)

        print("{} = {}".format(n, text))

    elif n != sum(lst):
        print("{} is NOT perfect.".format(n))