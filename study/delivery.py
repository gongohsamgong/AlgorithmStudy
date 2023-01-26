def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    need_deli = 0
    need_pick = 0

    for i in range(n):
        need_deli += deliveries[i]
        need_pick += pickups[i]

        while need_deli > 0 or need_pick > 0:
            need_deli -= cap
            need_pick -= cap
            answer += (n - i) * 2

    return answer
