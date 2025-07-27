
import sys

a = input().split('-')

ans = 0
state = False

def Sum(i, state):
    sumsum = 0
    cal = a[i].split('+')
    temp = list(map(int, cal))
    tem_sum = sum(temp)

    if state:
        sumsum -= tem_sum
    else:
        sumsum += tem_sum

    return sumsum

for i in range(len(a)):
    if i == 0:
        ans += sum(map(int, a[0].split('+')))
        state = True
    elif '+' not in a[i]:
        ans -= int(a[i])
        state = True

    else:
        ans += Sum(i, state)

print(ans)


