import sys
MOD = int(1e9)
d = [[0] * 10 for _ in range(101)]


def find(n):
    for i in range(1, 10):
        d[1][i] = 1
    for j in range(2, n+1):
        d[j][0] = d[j-1][1]
        for k in range(1, 10):
            if k == 9:
                d[j][k] = d[j-1][8]
            else:
                d[j][k] = d[j-1][k-1] + d[j-1][k+1]
    return sum(d[n]) % MOD
        

if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    print(find(n))