import sys


def dynamic(num, target, array):
    d = [10001] * (target + 1)
    for j in range(num):    # d[2], d[3] = 1, 1
        d[array[j]] = 1
    for k in range(array[num-1] + 1, target + 1):   # d[4]부터 target까지
        array_2 = []
        for h in range(num):
            array_2.append(d[k - array[h]])
        d[k] = min(array_2) + 1
    return d[target]


if __name__ == '__main__':
    read = sys.stdin.readline
    value = []
    n, m = map(int, read().split())
    for i in range(n):
        value.append(int(read()))
    res = dynamic(n, m, value)
    if res > 10000:
        print(-1)
    else:
        print(dynamic(n, m, value))
