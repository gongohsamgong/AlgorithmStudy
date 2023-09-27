import sys


def solution(n, array):
    array.sort(reverse=True)
    days = []
    for i in range(n):
        day = array[i] + (i + 1)
        days.append(day)
    return max(days) + 1


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    growth_days = list(map(int, read().split()))
    answer = solution(N, growth_days)
    print(answer)
