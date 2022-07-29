'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''

print('Введите размерность списка')

length  = int(input())

arr = [int(input()) for i in range(length) ]
result = []

print(arr)

for i in range(len(arr)):
    if arr[i] != arr[i-1]:
        result.append(arr[i])

print(result)