# جدول ضرب گنده
# ID : 3409
# https://quera.org/problemset/3409


n = int(input())

for i in range(n):
    for j in range(1, n+1):
        print((i+1) * j, end = ' ')
    print()