'''
Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

'''
print('Введите число: ')

number = int(input())

result = [i for i in range(1, number) if number % i == 0]

print(result)
for i in range(len(result)):
    for j in range(2, (result[i])):
        if result[i] % j == 0:
            result[i] = 0

print(result)


