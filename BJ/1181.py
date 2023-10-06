import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    words = [read().rstrip() for _ in range(N)]
    distinct_words = list(set(words))
    distinct_words.sort(key=lambda x: (len(x), x))
    for i in range(len(distinct_words)):
        print(distinct_words[i])
