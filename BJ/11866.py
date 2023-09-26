import sys
from collections import deque


def solution(n, k, deq):
    result = []
    while len(deq) != 0:
        for _ in range(k-1):
            deq.append(deq.popleft())
        result.append(str(deq.popleft()))
    return result


if __name__ == "__main__":
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num = [i for i in range(1, N+1)]
    deq = deque(num)
    answer = solution(N, K, deq)
    print('<' + ', '.join(answer) + '>')


