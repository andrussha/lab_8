'''
Виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем)
'''
import numpy as np
from random import randint
c = [[randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)]] #генеруємо матрицю 3*3 (як список)
a = np.array(c) # перетворюємо список в масив
a = a.transpose() # функцією transpose() транспонуємо матрицю
for i in range(len(a)):
    for j in range(len(a)):
      print(a[i][j], end=' ') #по елемнтено виводим матрицю
    print()