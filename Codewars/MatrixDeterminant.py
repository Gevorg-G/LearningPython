# Write a function that accepts a square matrix (n x n 2D array) and returns the determinant of the matrix.
# Note the alternation of signs.
# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)


# Более правильное, но читерское решение
import numpy as np

def determinant(matrix):
    array = np.array(matrix)
    return np.linalg.det(array)

print(determinant ([[2,5,3], [1,-2,-1], [1, 3, 4]]))

# # Менее правильное, но самостоятельное решение
# # Функция для уменьшения размерности массива
# def sub_determinant(matrix, i):
#     sub_matrix = []
#     # Ходим по массиву
#     for j in range(1,len(matrix)):
#         # Берём все элемент до i и элементы после i
#         sub_matrix.append(matrix[j][:i] + matrix[j][i+1:])
#     return sub_matrix
    
# def determinant(matrix):
#     # Если размерность матрицы нулевая — возвращаем ноль
#     if len(matrix) == 0:
#         return 0
#     # Если размерность матрицы 1 — возвращаем единственное число
#     elif len(matrix) == 1:
#         return matrix[0][0]
#     # Если размерность матрицы 2 — считаем определетель
#     elif len(matrix) == 2:
#         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#     else:
#         det = 0
#         # Ходим по массиву
#         for i in range(0,len(matrix)):
#             # Смотрим на чётность и нечётность i (волшебство побитового "и": https://wiki.python.org/moin/BitwiseOperators) 
#             # Плюс в дело вступает рекурсия — мы будем уменьшать размерность массива, пока она не станет 2*2
#             if 1 == i & 1:
#                 det = det - matrix[0][i] * determinant(sub_determinant(matrix,i))
#             else:
#                 det = det + matrix[0][i] * determinant(sub_determinant(matrix,i))
#         return det