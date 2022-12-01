# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def f(n):
    lst = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        lst.append(n)
    return lst
print(f(int(input(f'Задайте натуральное число N: '))))