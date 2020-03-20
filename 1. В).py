'''
виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
'''
import numpy as np
from random import randint
a = [[randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)]]
b = [[randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)],
     [randint(-10,10), randint(-10,10), randint(-10,10)]] #генеруємо дві матриці 3*3 (як список)
a = np.array(a)
b = np.array(b) # перетворюємо списоки в масиви
c = a.dot(b) # функцією dot() множимо матриці матрицю
for i in range(len(c)):
    for j in range(len(c)):
      print(c[i][j], end=' ') #по елемнтено виводим матрицю
    print()