import sys


def solution(people):
    people.sort()
    count = 0
    result = 0
    for rate in people:
        count += 1  # 한 그룹에 있는 인원 수
        if count >= rate:  # 1 2 2 3 3 3 4
            result += 1 # 그룹 개수
            count = 0
    return result
    

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    adventurer = list(map(int, read().split()))
    ans = solution(adventurer)
    print(ans)
    