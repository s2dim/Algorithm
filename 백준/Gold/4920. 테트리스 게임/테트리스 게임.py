import sys

# 누운 막대기
def stick():
    max_ = -int(1e9)
    for x in range(n):
        for y in range(n-3):
            max_ = max(max_, arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x][y+3])
 
    return max_

def stick_sleep():
    max_ = -int(1e9)
    for x in range(n-3):
        for y in range(n):
            max_ = max(max_, arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y]) 
    return max_

def thunder1():
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-2):

            max_ = max(max_, arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2])
            
    return max_

def thunder2():
    max_ = -int(1e9)
    for x in range(n-2):
        for y in range(n-1):

            max_ = max(max_, arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y] + arr[x+2][y])
    return max_

def gioek():
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-2):
            max_ = max(max_, arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2])

    return max_

def gioek2(): 
    max_ = -int(1e9)
    for x in range(n-2):
        for y in range(n-1):
            max_ = max(max_, arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1] + arr[x+2][y])

    return max_


def gioek3(): #  ㄴ
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-2):
            max_ = max(max_, arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2])

    return max_


def gioek4(): # ┌
    max_ = -int(1e9)
    for x in range(n-2):
        for y in range(n-1):
            max_ = max(max_, arr[x][y] + arr[x][y+1] + arr[x+1][y] + arr[x+2][y])

    return max_


def t1(): # ㅜ
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-2):

            max_ = max(max_, arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1])

    return max_


def t2(): # ㅗ
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-2):
            max_ = max(max_, arr[x][y+1] + arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2])
    return max_


def t3(): # ㅓ
    max_ = -int(1e9)
    for x in range(n-2):
        for y in range(n-1):
            max_ = max(max_, arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1] + arr[x+1][y])

    return max_


def t4(): # ㅏ
    max_ = -int(1e9)
    for x in range(n-2):
        for y in range(n-1):
            max_ = max(max_, arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1])
    return max_


def box():
    max_ = -int(1e9)
    for x in range(n-1):
        for y in range(n-1):
            max_ = max(max_, arr[x][y] + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1])

    return max_



idx = 0
while True:
    n = int(input())
    if n == 0:
        break

    idx += 1
    arr = []
    for i in range(n):
        lst = list(map(int, sys.stdin.readline().split()))
        arr.append(lst)
    answer = max(stick(), stick_sleep(), thunder1(), thunder2(), gioek(), gioek2(), gioek3(), gioek4(),
                 t1(), t2(), t3(), t4(), box())
    print(f"{idx}. {answer}")


