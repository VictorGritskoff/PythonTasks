# Напишите функцию, которая проверяет, является ли матрица симметричной
def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Testing the function
matrix1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matrix2 = [[1, 2], [2, 1]]
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(is_symmetric(matrix1)) # Output: True
print(is_symmetric(matrix2)) # Output: True
print(is_symmetric(matrix3)) # Output: False