import random

n = int(input('Введите размер массива : '))

a = []
a.append(random.randint(1,n))
for i in range(1,n):
    a.append(random.randint(1,20))
print(a)
x = int(input('Введите какое число надо найти : '))


for i in range(1,n):
    if a[i] == x:
        y = i

print(a[y-1])