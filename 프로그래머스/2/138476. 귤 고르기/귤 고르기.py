from collections import Counter
def solution(k, tangerine):
    cnt = Counter(tangerine)
    cnt = sorted(cnt.items(), key=lambda x:-x[1])
    
    idx = 0
    ans = 0
    while k > 0:
        k -= cnt[idx][1]
        ans += 1
        if k == 0:
            break

        idx += 1
    return ans