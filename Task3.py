# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8
n=float(input('Введите число N= '))
while n<=0:
    n=float(input('Некорректное значение! Введите число N= '))
my_list=[]
for i in range(int(n)):
    if (2**i)<=n:
        my_list.append(2**i)
print (f'Все целые степени двойки, не превосходящие числа N={n}: {my_list}')
