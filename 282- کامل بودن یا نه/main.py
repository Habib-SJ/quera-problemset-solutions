# کامل بودن یا نبودن
# ID : 282
# https://quera.org/problemset/282

number = int(input())
res = 0
for i in range(1, number):
    if number % i == 0:
        res += i
        
if number == res:
    print('YES')
else:
    print('NO')