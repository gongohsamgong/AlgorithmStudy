import sys


if __name__ == '__main__':
    read = sys.stdin.readline   # 속도 개선을 위해 sys 사용   ex) 50-20+20-40+15
    a = read().split('-')   # 값이 최소가 되기 위해서는 무조건 - 기준으로 괄호를 묶으면 됨. 따라서 - 기준으로 분리   ex) a = ['50', '20+20', '40+15']
    num = []
    for i in a:
        cnt = 0
        s = i.split('+')    # ex) i = ['50']    i = ['20', '20']    i = ['40', '15']
        for j in s:
            cnt += int(j)   # ex) cnt = 50      cnt = 40        cnt = 55
        num.append(cnt) # ex) append(50), append(40), append(55)
    n = num[0]  # ex) 50
    for i in range(1, len(num)):
        n -= num[i] # ex) 50 - 40 - 55  for문 돌아가며 차례로 진행
    print(n)
