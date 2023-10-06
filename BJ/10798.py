import sys


def alpha_solution(array):
    answer = ''
    for j in range(15):
        for i in range(5):
            if j < len(array[i]):
                answer += array[i][j]
    return answer


def solution(array):
    answer = ''
    length_array = []
    for i in range(5):
        length_array.append(len(array[i]))
    j = 0
    while sum(length_array) != 0:
        for i in range(5):
            if length_array[i] > 0:
                answer += array[i][j]
                length_array[i] -= 1
        j += 1
    return answer


if __name__ == "__main__":
    read = sys.stdin.readline
    arr = []
    for _ in range(5):
        arr.append(list(read().rstrip()))
    # ans = solution(arr)
    ans = alpha_solution(arr)
    print(ans)
