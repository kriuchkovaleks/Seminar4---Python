'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

import random

print('Задайье степень многочлена')

arr = []

k = int(input())

for i in range(k, -1, -1):
    if i !=0:
        member = f'{str(random.randint(0, 10))}*x^{i}'
        arr.append(member)
    elif i == 0:
        member = str(random.randint(0, 101))
        arr.append(member)

polinomial = '+'.join(arr)

print(f'{polinomial}=0')