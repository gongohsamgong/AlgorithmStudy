import sys


def solution(n, array):
    visit = [0] * 1001
    assignments.sort(key=lambda x: x[1], reverse=True)
    result = 0
    for day, value in assignments:
        i = day
        while visit[i]:
            i -= 1
        if i == 0:
            continue
        else:
            visit[i] = 1
            result += value
    return result


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    assignments = [list(map(int, read().split())) for _ in range(N)]
    ans = solution(N, assignments)
    print(ans)
