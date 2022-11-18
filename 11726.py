import sys

MOD = 10007


def dynamic(a):
    d = [0] * 1001
    d[1] = 1
    d[2] = 2
    for i in range(3, a+1):
        d[i] = d[i-1] + d[i-2]  # 개수가 아니라 방법이기 때문에 +1 각자 안해줌
    return d[a]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    print(dynamic(n) % MOD)