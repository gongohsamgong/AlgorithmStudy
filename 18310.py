import sys


def calculate(num, array):
    array.sort()
    return array[(num - 1) // 2]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))
    print(calculate(n, arr))