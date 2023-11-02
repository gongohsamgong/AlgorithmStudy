T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    original = list(map(int, input().rstrip()))
    length = len(original)
    new = [0] * length
    cnt = 0
    for i in range(length):
        if new[i] != original[i]:
            for j in range(i, length):
                new[j] = original[i]
            cnt += 1
    print("#%d %d" % (test_case, cnt))
