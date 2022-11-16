import sys

d = [0] * 100


def dynamic(n, arr):
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, n):
        d[i] = max(d[i-2] + arr[i], d[i-1])
    return d[n-1]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    array = list(map(int, input().split()))
    print(dynamic(n, array))