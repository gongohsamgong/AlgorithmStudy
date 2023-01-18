from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = len(q1) * 2
    tot1 = sum(q1)
    tot2 = sum(q2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = q1.popleft()
            q2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1
        elif tot1 < tot2:
            target = q2.popleft()
            q1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
