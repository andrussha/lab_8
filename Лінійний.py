'''
Лінійний пошук
'''
from random import randint
a = [randint(-10,10) for i in range(10)] # генеруємо список
x = int(input('Введіть шукане число: ')) # користувач вводить шукане число
n = len(a) # присвоюємо змінній значення довжини списка
b = 0 # кількість перевірок
for i in range(len(a)):
    b += 1 # при кожній ітерації кількість перевірок збільшується на 1
    if a[i] == x:
        print('Елемент знайдено. Індекс:',b-1)
        print('Виконано перевірок:',b) # якщо є збіг, то перевірка закінчується і виводиться на екран кількість перевірок
        print(a)
        break
    elif b == n:
        print('Елементів немає')
        print('Виконано перевірок:', b) # якщо кількість перевірок дорівнює довжині списка, то збігів немає
        print(a)
        break