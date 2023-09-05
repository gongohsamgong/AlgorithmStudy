import sys

if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    words = []
    for _ in range(n):
        words.append(read().rstrip())
    words.sort(key=len)
    cnt = 0
    for i in range(n):
        _flag = True
        for j in range(i+1, n):
            if words[i] == words[j][0:len(words[i])]:
                _flag = False
                break
        if _flag:
            cnt += 1
    print(cnt)