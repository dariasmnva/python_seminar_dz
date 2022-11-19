# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = True
y = False
z = True

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = True
y = True
z = True

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = True
y = True
z = False

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = False
y = False
z = False

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = False
y = True
z = False

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = False
y = False
z = True

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = True
y = False
z = False

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')

x = False
y = True
z = True

f1 = not(x or y or z)
f2 = not x and not y and not z
print(f'{f1} {f2}')