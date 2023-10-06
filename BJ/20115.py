import sys


def solution(n, array):
    array.sort(reverse=True)
    total = array[0]
    for i in range(1, n):
        total += array[i] / 2
    return total


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    energy_drink = list(map(int, read().split()))
    answer = solution(N, energy_drink)
    print(answer)
