'''
Виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем)
'''
import numpy as np
from random import randint
import copy
a = [[randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)]]
        #генеруємо матрицю 3*3 (як список)
c = np.array(a) # перетворюємо список в масив
c_copy = copy.deepcopy(c) #створюємо глибоку копію матриці
for i in range(len(c)):
    for j in range(len(c)):
        for i in range(len(c_copy)):
            for j in range(len(c_copy)):
                c[i][j], c[j][i] = c_copy[j][i], c_copy[i][j]
                '''
                замінюємо елемент матриці з індексами j та i выдповыдним елеменом з
                копії цієї матриці
                '''
for i in range(len(c)):
    for j in range(len(c)):
        print(c[i][j],end=' ')
    print()