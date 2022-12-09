# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.



from functools import reduce


list1 = [-1, 2, 3, 4, 5]
print(reduce(lambda x, y: x if x > y else y, list1))