import sys
from collections import Counter


def solution(n, m, weight):
    result = 0
    for i in range(1, m+1):
        n -= weight[i]
        result += weight[i] * n
    return result


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split()) # N: 볼링공의 개수, M: 공의 최대 무게
    array = list(map(int, read().split()))
    weight = Counter(array)
    ans = solution(N, M, weight)
    print(ans)
