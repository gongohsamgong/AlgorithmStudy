import sys


def isPrime(a):
    if (a<2):
        return False
    for i in range(2, int(a**0.5) + 1):
        if (a % i) == 0:
            return False
    return True


def dfs(n, num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(n, temp)


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    dfs(n, 2)
    dfs(n, 3)
    dfs(n, 5)
    dfs(n, 7)
