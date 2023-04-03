while True:
    try:
        a, b = map(int, input().split())
        if b % a == 0 and b // a >= 1:
            print("factor")
        elif a // b > 0 and a % b == 0:
            print("multiple")
        else:
            print("neither")

    except ZeroDivisionError:
        break