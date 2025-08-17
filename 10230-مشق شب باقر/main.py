# مشق شب باقر
# ID : 10230
# https://quera.org/problemset/10230


x, y, z = input().split()

if x == '0' or y == '0' or z == '0' or int(x)+int(y)+int(z) != 180:
    print('No')
elif int(x)+int(y)+int(z) == 180:
    print('Yes') 
    

