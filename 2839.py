import sys
d = [5001] * 5001


def dynamic(a):
    d = [5001] * 5001
    d[3] = 1
    d[5] = 1
    for i in range(6, a+1):
        d[i] = min(d[i-3], d[i-5]) + 1
    return d[a]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    res = dynamic(n)
    if res > 5000:
        res = -1
    print(res)