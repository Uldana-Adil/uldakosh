#Задача 1.1
a = 0
while a < 10:
    print(a)
    a = a+1
print('Цикл окончен')

#Задача 1.2
for x in range(10):
    print(x)
print('Цикл окончен')

#Задача 3
import random
random_number = random.randint(0, 125)
print(random_number)


#Задача 4.1
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)

#Задача 4.2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
 
#Задача 4.3
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')

#Задача 4.4
n = int(input())
sum1 = n
sum2 = 0
for i in range(1, n):
    sum1 += i
    sum2 += int(input())
print("Потеряно:", sum1 - sum2)


