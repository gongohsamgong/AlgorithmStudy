n = int(input())
score = [0] * 79

for i in range(n):
    lst = list(input())
    scr = [0] * len(lst)
    for j in range(len(lst)):
        if lst[j] == 'O':
            scr[j] = 1
            if j > 0 and lst[j-1] == 'O':
                scr[j] = scr[j-1] + 1
        else:
            scr[j] = 0
    score[i] = sum(scr)

for i in range(n):
    print(score[i])