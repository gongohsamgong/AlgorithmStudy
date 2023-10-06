import sys


def find(n, x, arr):
    res = []
    for i in range(n):
        if arr[i] < x:
            res.append(arr[i])
    return res


if __name__ == '__main__':
    read = sys.stdin.readline
    n, x = map(int, read().split())
    arr = list(map(int, read().split()))
    result = find(n, x, arr)
    for i in range(len(result)):
        print(result[i], end = ' ')