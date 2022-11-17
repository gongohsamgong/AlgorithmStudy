import sys


def dynamic(n):
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]


if __name__ == '__main__':
    read = sys.stdin.readline
    lst = []
    t = int(read())
    for i in range(t):
        lst.append(int(read()))
    for i in range(t):
        print(dynamic(lst[i]))
