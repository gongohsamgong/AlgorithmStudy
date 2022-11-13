import sys


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    lst = list(map(int, read().rstrip()))
    sum = 0
    for i in range(n):
        sum += lst[i]
    print(sum)