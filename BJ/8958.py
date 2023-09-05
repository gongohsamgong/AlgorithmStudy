n = int(input())

for i in range(n):
    lst = list(input())
    scr = [0] * len(lst)
    for j in range(len(lst)):
        if j>0 and lst[j] == 'O' and lst[j-1] == 'O':
            scr[j] = scr[j-1] + 1
        elif lst[j] == 'O':
            scr[j] = 1  
        else:
            scr[j] = 0
    print(sum(scr))