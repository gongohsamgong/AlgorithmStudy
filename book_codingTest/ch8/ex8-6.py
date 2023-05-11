import sys


def solution(n, array):
    d = [0] * 100
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[n-1] = max(d[n-2], d[n-3] + array[n-1])
    return d[n-1]


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    foods = list(map(int, read().split()))
    ans = solution(N, foods)
    print(ans)
