# اطلاعات کوه نوردی
# ID : 211018
# https://quera.org/problemset/211018

n = int(input())

lists = list(map(int, input().split()))


cnt = lists.count(1)
       
if cnt % 2 != 0 :
    print(1)
elif lists.count(2) % 2 == 0:
    print(0)
else:
    print(2)
    
