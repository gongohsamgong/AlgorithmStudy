import sys


def count(n, array, target):
    cnt = 0
    for i in range(n):
        if target == array[i]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    array = list(map(int, read().split()))
    target = int(read())
    print(count(n, array, target))