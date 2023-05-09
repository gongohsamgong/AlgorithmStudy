import sys


def solution(n, m, a, b):
    count = 0
    b.sort()
    for i in range(n):
        if a[i] > max(b):
            count += m
            continue
        for j in range(m):
            if a[i] > b[j]:
                count += 1
            else:
                break
    return count


if __name__ == "__main__":
    read = sys.stdin.readline
    answers = []
    T = int(read())
    for _ in range(T):
        N, M = map(int, read().split())
        A_size = list(map(int, read().split()))
        B_size = list(map(int, read().split()))
        answers.append(solution(N, M, A_size, B_size))
    for answer in answers:
        print(answer)
