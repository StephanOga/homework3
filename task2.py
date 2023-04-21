from  random import randint

n = int(input('Введите размер массива : '))
a = [randint(1,11) for i in range(n)]
print(a)
x = int(input('Введите какое число надо найти : '))
min_diff = abs(x-a[0])
closest = a[0]

for i in a:
    diff = abs(x-i)
    if diff < min_diff:
        min_diff = diff
        closest = i

print("Ближайший элемет к числу", x , "в массиве",a,"равен" , closest )