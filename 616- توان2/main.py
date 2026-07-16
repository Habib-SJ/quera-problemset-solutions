# توان 2
# ID : 616
# https://quera.org/problemset/616


number  = int(input())
for i in range(1, 10**9):
    if 2**i > number:
        print(2**i)
        break