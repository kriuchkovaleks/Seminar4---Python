'''
Вычислить число c заданной точностью d

Пример:

- при d = 3, π = 3.141
'''
import math




print('Введите точность: ')

d = int(input())

count =0 
pi_d = 0
while count < d:
    
    pi_d = pi_d + (1/16**(count))*(((4)/((8)*(count) + (1))) - ((2)/((8)*(count) + (4))) - ((1)/((8)*(count) + (5))) - ((1)/((8)*(count) + (6))))
    print(pi_d)
    count +=1
  
print(round(pi_d, d))


