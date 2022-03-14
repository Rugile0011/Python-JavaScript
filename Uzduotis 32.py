import numpy as np
import random

a_list = np.arange(1, 10)
print(a_list)

zero_list = np.ones(10) * 0
print(zero_list)

one_list = np.ones(10) * 1
print(one_list)

four_list = np.ones(10) * 4
print(four_list)

even_zero_hundred = np.arange(0, 100, 2)
print(even_zero_hundred)

matrix = np.arange(1, 26).reshape((5, 5))
print(matrix)

number = matrix[2, 1]
print(number)

line = matrix[4:, :]
print(line)

submatrix_1 = matrix[0:3, 0:3]
print(submatrix_1)

submatrix_2 = matrix[1:4, 1:5]
print(submatrix_2)

# submatrix_3 = matrix[0:2, 3:3]
# print(submatrix_3) ????

random_matrix = np.random.rand(20)
print(random_matrix)

max = random_matrix.max()
index_max = random_matrix.argmax()
print(max)
print(index_max)

min = random_matrix.min()
index_min = random_matrix.argmin()
print(min)
print(index_min)

type = matrix.dtype
print(type)
