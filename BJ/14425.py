import sys


def solution(n_array, m_array):
    cnt = 0
    for i in range(len(m_array)):
        if m_array[i] in n_array:
            cnt += 1
    return cnt


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    N_array, M_array = set(), []
    for _ in range(N):
        N_array.add(read().rstrip())
    for _ in range(M):
        M_array.append(read().rstrip())
    answer = solution(N_array, M_array)
    print(answer)
