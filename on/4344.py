c = int(input())
final = []

for i in range(c):
    lst = list(map(int, input().split()))
    total = 0
    cnt = 0
    for j in range(lst[0]):
        total += lst[j+1]
        avg = total / lst[0]
    for k in range(lst[0]):
        if lst[k+1] > avg:
            cnt += 1
        ans = cnt / lst[0] * 100
    final.append("%.3f" %ans + "%")

for i in range(c):
    print(final[i])