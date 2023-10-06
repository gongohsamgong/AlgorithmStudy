import sys


def solution(n, m, array):
    result = ''
    hamming_dist = 0
    for i in range(m):
        count = [0, 0, 0, 0]    # A, C, G, T 개수
        for j in range(n):
            if array[j][i] == 'A':
                count[0] += 1
            elif array[j][i] == 'C':
                count[1] += 1
            elif array[j][i] == 'G':
                count[2] += 1
            elif array[j][i] == 'T':
                count[3] += 1
        idx = count.index(max(count))
        if idx == 0:
            result += 'A'
        elif idx == 1:
            result += 'C'
        elif idx == 2:
            result += 'G'
        else:
            result += 'T'
        hamming_dist += n - max(count)
    return result, hamming_dist


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    dna_array = []
    for _ in range(N):
        dna_array.append(list(read().rstrip()))
    dna, distance = solution(N, M, dna_array)
    print("%s\n%d" % (dna, distance))
