import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    dots = []
    for _ in range(N):
        dots.append(list(map(int, read().split())))
    result = sorted(dots)
    for x, y in result:
        print("%d %d" % (x, y))
