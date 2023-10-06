import sys


def solution(n, array):
    ans = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(n):
            if cnt == array[i] and ans[j] == 0:
                ans[j] = i + 1
                break
            elif ans[j] == 0:
                cnt += 1
    return ans


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    arr = list(map(int, read().split()))    # 2 1 1 0
    answer = solution(n, arr)
    for i in range(n):
        print(answer[i], end =' ')
