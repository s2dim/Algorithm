def solution(food_times, k):
    total = sum(food_times)
    if k >= total:
        return -1

    n = len(food_times)

    # 2) (먹는시간, 원래 인덱스)로 정렬해 층 단위로 처리
    foods = sorted((t, i + 1) for i, t in enumerate(food_times))

    prev = 0        # 직전 층 높이
    remain = n      # 남은 음식 개수
    i = 0           # foods에서 진행 포인터

    # 3) 층을 한 번에 벗기며 k를 크게 줄이기
    while i < n:
        t, _ = foods[i]
        delta = t - prev          # 이번 층 두께
        if delta > 0:
            cost = delta * remain # 이번 층을 모두 벗기는 데 드는 시간
            if k >= cost:
                k -= cost
                prev = t
            else:
                # 4) 층을 다 못 벗기면, 남은 음식들만 대상으로 다음 음식 선택
                #    남은 음식들을 '원래 인덱스' 오름차순으로 정렬한 뒤
                #    k % remain 번째를 선택
                leftovers = sorted(idx for tt, idx in foods[i:])
                return leftovers[k % remain]

        # 5) 현재 층(t)에서 끝난 음식들 제거(남은 개수 갱신)
        while i < n and foods[i][0] == t:
            i += 1
            remain -= 1

    return -1