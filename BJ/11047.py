import sys


def solution(array, target):
    cnt = 0
    while target != 0:
        temp = []
        for coin in array:
            if target // coin != 0:
                temp.append(target//coin)
        target -= min(temp) * array[temp.index(min(temp))]
        cnt += min(temp)
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    N, K = map(int, read().split())
    coins = [int(read()) for _ in range(N)]
    ans = solution(coins, K)
    print(ans)
