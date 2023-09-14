import sys


def solution(n, cards_array, dictionary):
    for i in range(n):
        if cards_array[i] in dictionary:
            dictionary[cards_array[i]] += 1
    return dictionary


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    cards = list(map(int, read().split()))
    M = int(read())
    guess_array = list(map(int, read().split()))
    guess_dict = {key: 0 for key in guess_array}
    answer = solution(N, cards, guess_dict)
    for i in range(M):
        print(answer[guess_array[i]], end=' ')
