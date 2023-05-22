import sys


def adjacent(x, n):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def dfs(x, n):
    global count

    if x == n:
        count += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x, n):
                dfs(x+1, n)


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    row = [0] * N
    start, count = 0, 0
    dfs(start, N)
    print(count)
