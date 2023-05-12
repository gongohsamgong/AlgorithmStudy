import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    array = []
    N = int(read())
    for _ in range(N):
        array.append(int(read()))
    array.sort(reverse=True)
    for i in range(N):
        print(array[i], end=' ')