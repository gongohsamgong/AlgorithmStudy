import sys


def solution(n, array):
    candidate = []
    array.sort()
    for weight in array:
        candidate.append(weight * n)
        n -= 1

    return max(candidate)


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read()) # 줄 개수
    ropes = [int(read()) for _ in range(N)] # 감당가능한 최대 중량
    ans = solution(N, ropes)
    print(ans)
