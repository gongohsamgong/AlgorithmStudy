import sys


def hansu(number):
    lst = str(number)
    if len(lst) == 1:
        return True
    standard = int(lst[1]) - int(lst[0])
    for i in range(len(lst) - 1):
        if int(lst[i+1]) - int(lst[i]) != standard:
            return False
    return True


if __name__ == '__main__':
    read = sys.stdin.readline
    cnt = 0
    n = int(read())
    for i in range(1, n+1):
        if hansu(i):
            cnt += 1
        else:
            continue
    print(cnt)