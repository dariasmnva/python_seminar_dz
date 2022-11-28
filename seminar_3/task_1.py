# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.



lst = list(map(int, input("Введите числа через пробел:\n").split()))
print('Список: ')
print(lst)
list_length = len(lst)
sumOfElements = 0
i = 1
while i < list_length:
    sumOfElements = sumOfElements + lst[i]
    i = i + 2

print(f'Сумма элементов списка, стоящих на нечетной позиции: {sumOfElements}')












