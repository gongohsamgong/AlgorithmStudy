n = int(input())
lst = []
score = []

for i in range(n):
    lst = list(input())
    a = 1
    scr = 0
    for j in range(len(lst) - 1):
        if lst[j] == 'O':
            scr += a
            if lst[j+1] == 'O':
                if a != 1:
                    scr -= a
                a += 1
                scr += a
            else:
                a = 1
    print(scr)