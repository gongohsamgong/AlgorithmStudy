import sys


if __name__ =="__main__":
    read = sys.stdin.readline
    N = int(read())
    array = []
    for _ in range(N):
        array.append(int(read()))
    array.sort()
    for i in range(N):
        print(array[i])
