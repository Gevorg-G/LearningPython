# Умножает друг на друга 2 матрицы

# Инициализируем и заполняем матрицу
def fillMatrix (rows, colums):
    matrix = [[0 for i in range(colums)] for j in range(rows)]

    for i in range(rows):
        for j in range(colums):
            print ("Введите элемент [", i, "][", j, "]: ", sep=''),
            matrix[i][j]= int(input())
    return matrix

# Строки и столбцы в первой матрице
firstMatrixRows = int(input("Введите число сторок в матрице 1: "))
firstMatrixColumns = int(input("Введите число столбцов в матрице 1: "))


# Строки и столбцы во второй матрице
secondMatrixRows = int(input("Введите число сторок в матрице 2: "))
secondMatrixColumns = int(input("Введите число столбцов в матрице 2: "))


# Инициализируем матрицы
# firstMatrix = [[0 for x in range(firstMatrixRows)] for y in range(firstMatrixColumns)]


# Проверяем на согласованность: https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86
if firstMatrixColumns == secondMatrixRows:
    finalMatrix = [[0 for i in range(secondMatrixColumns)] for j in range(firstMatrixRows)]
    print ("Матрицы согласованы\n")

else:
    print ("Матрицы не согласованы\n")
    quit()


firstMatrix = fillMatrix(firstMatrixRows, firstMatrixColumns)
secondMatrix = fillMatrix(secondMatrixRows, secondMatrixColumns)


for i in range(firstMatrixRows):
    for j in range(secondMatrixColumns):
        for k in range(firstMatrixColumns):
            finalMatrix[i][j] = finalMatrix[i][j] + firstMatrix[i][k] * secondMatrix[k][j]
        print (finalMatrix[i][j])