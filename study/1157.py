import sys
from collections import Counter


def solution(word):
    countWord = Counter(word)
    common = countWord.most_common()
    if len(common) > 1:
        candidates = common[0:2]
        if candidates[0][1] == candidates[1][1]:
            return '?'
        else:
            return candidates[0][0].upper()
    else:
        return common[0][0].upper()


if __name__ == '__main__':
    read = sys.stdin.readline
    word = read().rstrip().lower()
    ans = solution(word)
    print(ans)
