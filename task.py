from random import randint

a = int (input("Ввведите длинну массива "))
b = int (input("Ввведите число которое надо найти "))
array = []
count = 0
for i in range(a):
    array.append(randint(0,9))
print(array)
print("Число " , b,"содержится в массиве" , array.count(b), "раз")
