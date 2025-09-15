# تک رقمی
# ID : 3539
# https://quera.org/problemset/3539


def sum_digit(number):
    list_digit = [int(number[i]) for i in range(len(number))]
    new_number = sum(list_digit)

    if len(str(new_number)) > 1:
        return sum_digit(str(new_number))
    else: return new_number

number = input()

if len(number) > 1:
    print(sum_digit(number))
else: print(int(number))

