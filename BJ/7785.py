import sys


def solution(dict):
    answer = []
    for key in dict.keys():
        if dict[key] == 'enter':
            answer.append(key)
    return sorted(answer, reverse=True)


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    entry_log = {}
    for i in range(n):
        name, entrance = read().split()
        if entrance == 'leave':
            del entry_log[name]
        else:
            entry_log[name] = entrance
    names = solution(entry_log)
    for name in names:
        print(name)
