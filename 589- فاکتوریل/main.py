# فاکتوریل
# ID : 589
# https://quera.org/problemset/589

x = int(input())
fact = x
for i in range(x-1, 1, -1):
    fact= i*fact
print(fact)