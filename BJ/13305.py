import sys


def solution(n, road_array, cost_array):
    total = 0
    _min = 1e9
    for i in range(n-1):
        if cost_array[i] <= _min:
            _min = cost_array[i]
        total += _min * road_array[i]
    return total


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    roads = list(map(int, read().split()))
    cost = list(map(int, read().split()))
    answer = solution(N, roads, cost)
    print(answer)
