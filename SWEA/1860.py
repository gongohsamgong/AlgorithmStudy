"""
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    consumer = list(map(int, input().split()))
    consumer.sort()
    fish_bread, check = 0, True
    if consumer[0] == 0:
        check = False
    for time in range(1, consumer[-1] + 1):
        if time % M == 0:
            fish_bread += K
        if time in consumer:
            if fish_bread <= 0:
                check = False
                break
            else:
                fish_bread -= 1
    print("#%d" % test_case, end=' ')
    if check:
        print("Possible")
    else:
        print("Impossible")
"""

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    consumer = list(map(int, input().split()))
    consumer.sort()
    answer = "Possible"
    for i in range(N):
        bread_number = (consumer[i] // M) * K - (i+1)
        if bread_number < 0:
            answer = "Impossible"
    print("#{} {}".format(test_case, answer))
