# اعداد فیثاغورثی
# ID : 280
# https://quera.org/problemset/280


x = int(input())
y = int(input())
z = int(input())

if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (z**2 + y**2 == x**2):
    print('YES')
else:
    print('NO')