'''
У матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
'''
import numpy as np
from random import randint
c = [[randint(-10,10), randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10), randint(-10,10)]]
    #генеруємо матрицю 4*4, всі елементи якої дорівнюють від -10 до 10
a = np.array(c) #перетворюємо список в масив
for i in range(len(a)):
    for j in range(len(a)): #перебираємо по елемнтно масив і всі від'ємні значення замінюємо на 0
        if a[i][j]<0:
            a[i][j] = 0
        print(a[i][j], end=' ') #по елемнетно виводим масив, щоб він мав вигляд матриці
    print()
